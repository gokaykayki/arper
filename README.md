# arper
Check your LAN for unknowns devices.

## Prerequisites

This script uses `scapy` and `click` library. You can install they with `pip` :

```
pip install scapy
pip install click
```

## How to use ?

Run `arper.py` file with root privilages :

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
sudo python arper.py
sudo python arper.py -i wlp2s0
sudo python arper.py -m 30
sudo python arper.py -i wlp2s0 -m 30
```
or

```
sudo arper
sudo arper -i wlp2s0
sudo arper -m 30
sudo arper -i wlp2s0 -m 30
```
