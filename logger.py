from time import gmtime, strftime

def write(msg):
    # open log file in append mode so it is created if it does not exist
    f = open("/home/pi/Desktop/dawn/log/log.txt", "a")
    log_str = '{} - {}\n'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), msg)
    f.write(log_str)
