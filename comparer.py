from os import mkdir, chdir, getcwd, path
import os.path

pas = 'Backup_hifuzion'

cam = path.join(path.expanduser('~'), 'Desktop')
chdir(cam)

if os.path.isdir(pas):
    print(F'A pasta "{pas}" já existe em Desktop!')

else:
    mkdir(pas)
    cam2 = cam + '\\' + pas
    chdir(cam2)
    print(getcwd)