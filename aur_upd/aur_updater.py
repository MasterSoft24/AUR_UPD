import os
import subprocess

import requests
import json

class aur_updater():


    def __init__(self):
        pass

    def get_aur_packages(self):

        list = str(subprocess.run(['pacman', '-Qm'], stdout=subprocess.PIPE).stdout, 'utf-8').split('\n')
        return list

    def clone_package(self, name):

        r =subprocess.run(['git', 'clone', 'https://aur@aur.archlinux.org/'+name+'.git'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return r.returncode

    def build_package(self, name):
        os.chdir(name)
        r = subprocess.run('makepkg', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.chdir('..')
        return r.returncode

    def get_package_current_version(self, name):

        r = json.loads(requests.get('https://aur.archlinux.org/rpc/?v=5&type=info&arg[]='+name).text)

        # print(r)
        if r['resultcount'] != 0:
            return r['results'][0]['Version']
        else:
            return None

    def install_package(self, name, passw):

        os.chdir(name)
        r = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
        pkg = str(subprocess.run(['grep','pkg.tar.xz'], stdin=r.stdout, stdout=subprocess.PIPE).stdout, 'utf-8').strip()

        command = 'pacman --noconfirm -U ./'+pkg

        p = subprocess.call('echo {} | sudo -S {}'.format(passw, command), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        os.system('rm -rf ../'+name)


