#!/bin/bash
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : auto_clear.sh
#   Created Time  : 2019-09-08 18:48
#   Last Modified : 2019-10-08 09:41
#   Describe      :
#
# ====================================================
export HOME="/besfs/users/maxx/home"
source /workfs/bes/maxx/local/python-2.7.14/setup.sh
cd /besfs/users/maxx/Tool/github/LinuxRecycle/core
python auto_clear.py
cd -
