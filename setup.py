# -*- coding: utf-8 -*-
import sys
import os
from setuptools import setup

def read(*fname):
    with open(os.path.join(os.path.dirname(__file__), *fname)) as f:
        return f.read()

if sys.version_info >= (3,0):
    sys.exit('This script may not work properly in Python 3.0 and newer. It is recommended to use Python 2.7.')

setup(
    name = 'arper',
    version = '1.0',
    author = 'Gökay Can Kaykı',
    author_email = 'gokaykayki@gmail.com',
    keywords = 'lan arping arper local area network',
    url = 'https://github.com/gokaykayki/arper',
    py_modules = [
        'main',
        'arping',
        'checkList',
        'getInterfaces'
    ],
    install_requires = [
        'scapy',
    ],
    description = 'Simple arping script. Check your LAN for unknowns devices.',
    long_description = read('README.md'),
    zip_safe = False,
    entry_points="""
        [console_scripts]
        arper = main:main
    """,
)
