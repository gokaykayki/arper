# -*- coding: utf-8 -*-
import errno, os, datetime

def changeIp(mac):
    answers = ["y", "Y", "N", "n"]
    while True:
        try:
            select = raw_input("\nThe MAC address %s 's IP address has changed. Do you want to change in registry file? (y/n): " % mac)
        except ValueError:
            print ('Invalid input. Enter y or n.')
            continue
        if select in answers:
            break
        else:
            print ('Invalid input. Enter y or n.')
            continue

    if select in ["y", "Y"]:
        return True
    else:
        return False


def addMac(mac):
    answers = ["y", "Y", "N", "n"]
    while True:
        try:
            select = raw_input("\nThe MAC address %s is new. Do you want to add in registry file? (y/n): " % mac)
        except ValueError:
            print ('Invalid input. Enter y or n.')
            continue
        if select in answers:
            break
        else:
            print ('Invalid input. Enter y or n.')
            continue
    if select in ["y", "Y"]:
        return True
    else:
        return False

def oldIP(mac):
    answers = ["y", "Y", "N", "n"]
    while True:
        try:
            select = raw_input("\nThe MAC address %s has old IP. Do you want to delete in registry file? (y/n): " % mac)
        except ValueError:
            print ('Invalid input. Enter y or n.')
            continue
        if select in answers:
            break
        else:
            print ('Invalid input. Enter y or n.')
            continue
    if select in ["y", "Y"]:
        return True
    else:
        return False

def check(onlineMacs):
    try:
        try:
            f = open('macList.txt', 'r+')
        except (OSError, IOError) as e:
            if getattr(e, 'errno', 0) == errno.ENOENT:
              f = open('macList.txt', 'w+')
              userhome = os.path.expanduser('~')
              username = os.path.split(userhome)[-1]
              os.popen('chown {0} macList.txt'.format(username))
              os.popen('chgrp {0} macList.txt'.format(username))

        txtList = f.readlines()
        macs = list(onlineMacs.keys())
        f.close()
        os.remove('macList.txt')

        newTxtList = []
        lenMacs = len(macs)
        lenTxtList = len(txtList)
        addMacsCompare = []

        for i in txtList:
            for j in macs:
                iMAC = i.split("|")[0]
                iIP = i.split("|")[1].split("\n")[0]
                if(iMAC == j and iIP == onlineMacs[j]):
                    newTxtList.append(i)
                    addMacsCompare.append(j)
                    break
                elif(iMAC == j and iIP != onlineMacs[j]):
                    decision = changeIp(j)
                    if(decision):
                        newTxtList.append("%s|%s|%s\n" % (iMAC, onlineMacs[j], datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")))
                        addMacsCompare.append(iMAC)
                    else:
                        newTxtList.append(i)
                        addMacsCompare.append(iMAC)
                    break
                elif(iMAC != j and iIP == onlineMacs[j]):
                    decision = oldIP(iMAC)
                    if(decision):
                        break
                    else:
                        newTxtList.append(i)
                        addMacsCompare.append(iMAC)
                        break
            else:
                newTxtList.append(i)
                addMacsCompare.append(iMAC)

        for i in macs:
            if(i not in addMacsCompare):
                decision = addMac(i)
                if(decision):
                    newTxtList.append("%s|%s|%s\n" % (i, onlineMacs[i],str(datetime.datetime.now())))


    except Exception as error:
        f = open("macList.txt", "w")
        f.writelines(txtList)
        f.close
        print('Caught this error: ' + repr(error))
    finally:
        f = open("macList.txt", "w+")
        f.writelines(newTxtList)
        f.seek(0)
        output = f.read()
        f.close()
        userhome = os.path.expanduser('~')
        username = os.path.split(userhome)[-1]
        os.popen('sort -t "|" -k 3r,3 macList.txt > log.txt')
        os.popen('mv log.txt macList.txt')
        os.popen('chown {0} macList.txt'.format(username))
        os.popen('chgrp {0} macList.txt'.format(username))
        print("------------------------------------------------------------")
        print("       MAC              IP                  LOG DATE")
        print("------------------------------------------------------------")
        print(output)
