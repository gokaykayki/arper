#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

def read(*fname):
    with open(os.path.join(os.path.dirname(__file__), *fname)) as f:
        return f.read()

setup(
    name = 'arper',
    version = '1.0',
    author = 'Gökay Can Kaykı',
    author_email = 'gokaykayki@gmail.com',
    keywords = 'lan arping arper local area network',
    url = 'https://github.com/gokaykayki/arper',
    py_modules = [
        'arper',
        'arping',
        'checkList',
        'getInterfaces'
    ],
    install_requires = [
        'Click',
        'Scapy',
    ],
    description = 'Simple arping script',
    long_description = read('README.md'),
    zip_safe = False,
    entry_points="""
        [console_scripts]
        arper = arper:main
    """,
)
