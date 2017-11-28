#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import getInterfaces as gi
import arping, checkList

@click.command()
@click.option('--interface', '-i', default= '', help = 'You can select which interfaces directly.', required = False)
@click.option('--mask', '-m', default = '24', help = '(1-32)You can set mask range directly with this parameter.')

def main(interface, mask):
    ''' Check your LAN for unknown devices.'''

    interfaces = gi.getInterfaces()

    if interface in interfaces:
        while (int(mask) >= 33 or int(mask) <= 0):
            mask = raw_input('Please enter valid mask(1-32): ')
    else:
        for i in range(len(interfaces)):
        	print("--- Your available interfaces ---")
        	print("----- " + list(interfaces.keys())[i] + ": " + list(interfaces.values())[i])

        while (interface not in interfaces):
            interface = raw_input("Please enter valid interface name: ")
        while (int(mask) >= 33 or int(mask) <= 0):
            mask = raw_input('Please enter valid mask(1-32): ')
    onlineMacs = arping.arping(interfaces[interface]+'/'+mask, interface)
    checkList.check(onlineMacs)

if __name__ == '__main__':
    main()
