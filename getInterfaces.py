# -*- coding: utf-8 -*-
import os
import netifaces as ni

def getInterfaces():
    availableIf = {}
    lo = '127.0.0.1'
    iFaces = os.listdir('/sys/class/net/')
    for i in iFaces:
        try:
            ip = ni.ifaddresses(i)[ni.AF_INET][0]['addr']
            if (ip and i != 'lo'):
                availableIf[i]=ip;
        except:
            iFaces.remove(i)
            continue

    return availableIf
