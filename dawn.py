import weather
import time
import subprocess

def speak(text):
    cmd = '/home/pi/bin/speak.sh \"{}\"'.format(text)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

weather.update_weather()

t = time.strftime("%I:%M:%S")
t_hr = t.split(':')[0]
t_min = t.split(':')[1]

if t_hr[0] == '0':
    t_hr = t_hr[1:]

if t_min[0] == '0':
    t_min = t_min[1:]

greeting = """Good morning. The time is {} {} and it is time to wake up. 
The weather is {} so im sure it will be a lovely day""".format(t_hr,
                                                               t_min,
                                                               weather.last_weather)
print greeting
speak(greeting)
