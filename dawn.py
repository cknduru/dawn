import weather
import time
import subprocess
import threading

SLEEP_INTERVAL = 15 # run every minute
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
    trigger_h = '20'
    trigger_m = '29'
    h, m = format_current_time(format24=True)
    
    if h == trigger_h and m == trigger_m and trigger_m != last_trigger_m:
        print('Trigger')
        last_trigger_m = m # update last trigger minute
        return True
    else:
        print(' no trigger {} {}'.format(h, m))
    

def speak(text):
    cmd = '/home/pi/bin/speak.sh \"{}\"'.format(text)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

def main():
    weather.update_weather()

    h, m = format_current_time()

    greeting = """Good morning. The time is {} {} and it is time to wake up. 
The weather is {} so im sure it will be a lovely day""".format(h,
                                                               m,
                                                               weather.last_weather)
    if should_trigger():
        speak(greeting)
        print(greeting)
    
    threading.Timer(SLEEP_INTERVAL, main).start()

print('Dawn launched')
main()
