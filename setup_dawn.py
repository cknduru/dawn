import subprocess
import logger
import os

def install_crontab():
    logger.write('installing crontab..')
    subprocess.check_output(['./install_crontab.sh', 'testarg'])
    logger.write('installed crontab')

def create_directory(dir_name):
    try:
        os.makedirs(dir_name)
    except OSError:
        pass


# setup function calls
create_directory('log')
install_crontab()