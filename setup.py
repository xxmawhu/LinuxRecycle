#!/usr/bin/env python
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : setup.py
#   Created Time  : 2019-09-24 10:51
#   Last Modified : 2019-09-24 10:51
#   Describe      :
#
# ====================================================

from setuptools import setup
from setuptools import find_packages
import core
setup(
    name='LinuxRecycle',
    version='1.0',
    author='Xin-Xin Ma',
    packages=find_packages(),
    entry_points={
        'console_scripts':['rm=core.main:main',]
        }
)
