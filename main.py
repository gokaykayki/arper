# -*- coding: utf-8 -*-
import argparse, os, sys
import getInterfaces as gi
import arping, checkList

if sys.version_info >= (3,0):
    sys.exit('\n\n###  This script may not work properly in Python 3.0 and newer. It is recommended to use Python 2.7.')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--interface', '-i', default= '', help = 'You can select which interfaces directly.', required = False)
    parser.add_argument('--mask', '-m', default = '24', help = '(1-32)You can set mask range directly with this parameter.', required = False)
    parser.add_argument('--log', '-l',  help = 'You can see log file.', action = 'store_true', required = False)
    args = parser.parse_args()

    ''' Check your LAN for unknown devices.'''

    if args.log:
        f = open("macList.txt", "a+")
        output = f.read()
        f.close()
        userhome = os.path.expanduser('~')
        username = os.path.split(userhome)[-1]
        os.popen('chown {0} macList.txt'.format(username))
        os.popen('chgrp {0} macList.txt'.format(username))
        print("------------------------------------------------------------")
        print("       MAC              IP                  LOG DATE")
        print("------------------------------------------------------------")
        print(output)
    else:
        interfaces = gi.getInterfaces()

        if args.interface in interfaces:
            while (int(args.mask) >= 33 or int(args.mask) <= 0):
                args.mask = raw_input('Please enter valid mask(1-32): ')
        else:
            print("--- Your available interfaces ---")
            for i in range(len(interfaces)):
            	print("----- " + list(interfaces.keys())[i] + ": " + list(interfaces.values())[i])

            while (args.interface not in interfaces):
                args.interface = raw_input("Please enter valid interface name: ")
            while (int(args.mask) >= 33 or int(args.mask) <= 0):
                args.mask = raw_input('Please enter valid mask(1-32): ')
        onlineMacs = arping.arping(interfaces[args.interface]+'/'+args.mask, args.interface)
        checkList.check(onlineMacs)

if __name__ == '__main__':
    main()
