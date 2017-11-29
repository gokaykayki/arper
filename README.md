# arper
Check your LAN for unknowns devices.

## Prerequisites

This script uses the `scapy` library. You can install it with `pip` :

```
pip install scapy
```

## How to use ?

Run `main.py` file with root privilages :

```
sudo python main.py
```

or install script with `setup.py` file :

```
sudo python setup.py install
```

## Command line arguments

`-i` or `--interface`: Select network interface for arp scan

`-m` or `--mask`: Set your mask range (Default range: 24)

`-l` or `--log`: You can see log file.

## Examples
```
sudo python main.py
sudo python main.py -i wlp2s0
sudo python main.py -m 30
sudo python main.py -i wlp2s0 -m 30
sudo python main.py -l
```
or

```
sudo arper
sudo arper -i wlp2s0
sudo arper -m 30
sudo arper -i wlp2s0 -m 30
sudo arper -l
```
