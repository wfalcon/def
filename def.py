  
#!/usr/bin/env python3

import os
import platform
import socket
import subprocess


def get_ver_os():
    '''
    возвращает версию ОС, кол-во процессоров, имя и ip
    '''
    if os.name == "nt":
        os_data = (platform.system() + ' ' + platform.version() + ' ' +
                   platform.win32_edition() + '\n' + str(os.cpu_count()) + ' processors')

        iface = ('PC name: ' + socket.gethostname() + ', ' +
                 'IP address: ' + socket.gethostbyname(socket.gethostname()))
        return os_data + '\n' + iface


def get_ip(domen):
    '''
    возвращает список Ip для домена
    '''
    a = socket.gethostbyname_ex(domen)
    str = []
    for i in a:
        if i:
            if type(i) != list:
                str.append(i)
            else:
                for a in i:
                    str.append(a)
    return str


def test_ping(ipAddr, timeout=100, count=2):
    '''
    Send a ping packet to the specified host, using the system ping command.
    Accepts ipAddr as string for the ping destination.
    Accepts timeout in ms for the ping timeout.
    Returns True if ping succeeds otherwise Returns False.
        Ping succeeds if it returns 0 and the output includes b'TTL='
    '''
    if platform.system().lower() == 'windows':
        numFlag = '-n'
    else:
        numFlag = '-c'
    completedPing = subprocess.run(['ping', numFlag, str(count), '-w', str(timeout), ipAddr],
                                   stdout=subprocess.PIPE,    # Capture standard out
                                   stderr=subprocess.STDOUT)  # Capture standard error
    # print(completedPing.stdout)
    return (completedPing.returncode == 0) and (b'TTL=' in completedPing.stdout)


if __name__ == "__main__":

   
    list_domen = ['google.com', 'mail.ru', 'ya.ru', 'ok.ru']

    for l in list_domen:
        for k in (get_ip(l)):
            print(k, test_ping(k))