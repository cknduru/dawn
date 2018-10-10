import weather
import subprocess
import threading
import logger
import event_manager
import utils

def main():
    weather.update_weather()

    h, m = utils.format_current_time()

    # split this up to make pronounciation more fluent?
    greeting = """Good morning. The time is {} {} and it is time to wake up.
The weather is {} so im sure it will be a lovely day. I have prepared a song to start the day. Remember to book
christmas holiday and that you have visitors at six o clock""".format(h,
                                                               m,
                                                               weather.last_weather)

    if event_manager.should_trigger():
        utils.speak(greeting)

        utils.play_song('/home/pi/Desktop/dawn/music/fr.mp3')

if __name__ == "__main__":
    main()