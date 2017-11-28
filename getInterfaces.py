# -*- coding: utf-8 -*-
import os

def getInterfaces():
    availableIf = {}
    lo = '127.0.0.1'
    iFaces = os.listdir('/sys/class/net/')
    for i in iFaces:
        ip = os.popen('ifconfig {0} | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1'.format(i)).read()
        if (ip and i != 'lo'):
            ip = ip.replace('\n','')
            availableIf[i]=ip;
    return availableIf
