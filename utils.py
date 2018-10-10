import time

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

def speak(text):
    cmd = '/home/pi/bin/speak.sh \"{}\"'.format(text)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    proc.wait()

def play_song(song_path):
    cmd = 'omxplayer {} --vol -1500'.format(song_path)
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)