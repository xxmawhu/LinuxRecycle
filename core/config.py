#!/usr/bin/env python
# encoding: utf-8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : config.py
#   Created Time  : 2019-09-19 23:52
#   Last Modified : 2019-09-21 15:42
#   Describe      :
#
# ====================================================
import os
db = os.path.expanduser("~/.mtdb/fileInfo.db")
user = os.environ["USER"]
db = "/tmp/fileInfo{}.db".format(user)
whiteList = [db]
tmpFile = ['tmp']
keepDB = True
