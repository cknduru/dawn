# Embedded file name: event_manager.py
import logger
import datetime
import importlib

registered_triggers = {}

# register_trigger('24:17:45', testfunc)
def register_trigger(trigger_time, trigger_function):
    registered_triggers[trigger_time] = trigger_function
    logger.write('registered trigger @ {}'.format(registered_triggers[trigger_time]))
# unregister_trigger('24:17:45')
def unregister_trigger(trigger_time):
    del registered_triggers[trigger_time]
    logger.write('unregistered trigger @ {}'.format(trigger_time))

def should_trigger():
    now = datetime.datetime.now()
    current_minute = now.minute
    current_hour = now.hour
    current_day = now.day

    # todo: improve error handling
    try:
        assembled_string = '{}:{}:{}'.format(now.day, now.hour, now.minute)
        print(assembled_string)
        t_func = registered_triggers[assembled_string]
        t_func()
        unregister_trigger(assembled_string)
    except KeyError:
        pass

def read_event_file():
    conf_file_path = '/home/pi/Desktop/dawn/config/events.conf'

    with open(conf_file_path) as cfp:  
        line = cfp.readline()

        while line:
            if 'recurring' in line:
                event_type, event_time, event_file, event_class = line.split()

                print('event_type = {} event_time = {} event_file = {} event_class = {}'.format(event_type, event_time, event_file, event_class))

                mod = importlib.import_module(event_file)
                mod.run()
        
            line = cfp.readline()

        print("{}".format(line.strip()))


read_event_file()