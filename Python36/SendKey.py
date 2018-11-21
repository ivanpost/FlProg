#!python3
# -*- coding: utf-8 -*-
import time
import telnetlib
import sys

hostname = str(input('Введите имя хоста или ip: '))

if hostname == '':
    hostname = '192.168.31.12' # Переменная ip адрес
    print('Имя хоста установлено: ' + hostname)

try:
    tn = telnetlib.Telnet(hostname, 23, 3)
except:
    print('Нет коннекта с ' + hostname)
    sys.exit(0)
tn.close()

print('Устройство ' + hostname + u' доступно.')
tn.close()
time.sleep(1)

