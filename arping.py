# -*- coding: utf-8 -*-
from scapy.all import srp,Ether,ARP

def arping(ip, interface):
    onlineMacs = {}
    print(ip)
    ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst = str(ip)), timeout = 3, iface = interface, inter = 0.2)
    for snd, rcv in ans:
        onlineMacs[rcv.sprintf(r"%Ether.src%")] = rcv.sprintf(r"%ARP.psrc%")
    return onlineMacs
