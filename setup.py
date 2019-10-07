#!/usr/bin/env python
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : setup.py
#   Created Time  : 2019-09-24 10:51
#   Last Modified : 2019-09-29 12:09
#   Describe      :
#
# ====================================================

from setuptools import setup
from setuptools import find_packages
import core
import subprocess
import sys
import os
def set_crontab():
    path = sys.path[0]
    f = open('tmp.txt', 'w')
    f.write('0 0 * * * cd {}/core; ./auto_clear.py\n'.format(path))
    f.close() 
    subprocess.Popen(['crontab', 'tmp.txt'])
    try:
        os.remove('tmp.txt')
    except OSError:
        pass
set_crontab()
setup(
    name='LinuxRecycle',
    version='1.0',
    author='Xin-Xin Ma',
    packages=find_packages(),
    entry_points={
        'console_scripts':['rm=core.main:main', 
            'rm.printDB=core.printDB:main',
            'rm.recover=core.recover:main']
        }
)
