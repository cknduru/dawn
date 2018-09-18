import subprocess

def install_crontab():
    print('installing crontab..')
    subprocess.check_output(['./install_crontab.sh', 'testarg'])
    print('installed crontab')

# setup function calls
install_crontab()