import weather
import time
import subprocess
import threading
import logger


SLEEP_INTERVAL = 55 # run every 55 seconds
last_trigger_m = 0 # last trigger minute to eliminate multiple triggers within SLEEP_INTERVAL

# strip time of leading zeros, if any
def format_current_time(format24=False):
    if(format24):
        t = time.strftime("%H:%M:%S")
    else:
        t = time.strftime("%I:%M:%S")

    t_hr = t.split(':')[0]
    t_min = t.split(':')[1]

    if t_hr[0] == '0':
        t_hr = t_hr[1:]

    if t_min[0] == '0':
        t_min = t_min[1:]

    return t_hr, t_min

def should_trigger():
    global last_trigger_m
    trigger_h = '7'
    trigger_m = '30'
    h, m = format_current_time(format24=True)
    
    if h == trigger_h and m == trigger_m and trigger_m != last_trigger_m:
        logger.write('trigger')
        last_trigger_m = m # update last trigger minute
        return True
    else:
        return False    

def speak(text):
    cmd = '/home/pi/bin/speak.sh \"{}\"'.format(text)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    proc.wait()

def main():
    weather.update_weather()

    h, m = format_current_time()

    # split this up to make pronounciation more fluent?
    greeting = """Good morning. The time is {} {} and it is time to wake up.
The weather is {} so im sure it will be a lovely day. I have prepared a song to start the day. Remember to book
christmas holiday and that you have visitors at six o clock""".format(h,
                                                               m,
                                                               weather.last_weather)

    if should_trigger():
        speak(greeting)

        cmd = 'omxplayer music/fr.mp3 --vol -1500'
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

if __name__ == "__main__":
    logger.write('dawn launched')
    main()