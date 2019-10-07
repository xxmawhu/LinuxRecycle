#!/usr/bin/env python
# encoding: utf-8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : trashInfo.py
#   Created Time  : 2019-09-19 15:05
#   Last Modified : 2019-09-19 19:46
#   Describe      :
#
# ====================================================
import sys
import os
import argv
from config import local_config

def getTrashAddress(afileName):
    """
    Warning: the file name can't contain ~, or $USER,
    please expand them 
    1. split the name by $USER 
    2. [0]/$USER/.trash
    """
    user = os.environ["USER"]
    if user in afileName:
        pp = afileName.split(user)
        print('pp=', pp)
        print("getTrashAddress: the trash address",
                os.path.join(pp[0], user, '.trash'))
        return os.path.join(pp[0], user, '.trash')
    else:
        trs="/"+afileName.split("/")[1]+ '/.trash'
        print("getTrashAddress: the trash address",trs)
        return trs


def inTrash(afileName):
    """
    True if the afile is within a .trash
    False not
    Once found ${USER}/.trash in the path, then the path is determined within
    a trash
    """
    tak = '{}/.trash'.format(os.environ["USER"])
    if tak in afileName:
        return True
    return False


def tmpFile(afileName):
    """
    True if the file is fileInfo.db
    """
    tak = afileName.split("/")[1]
    if afileName in ['tmp']:
        return True
    return False


def whiteFile(afileName):
    """
    True if the in /tmp/...
    """
    tak = afileName.split("/")[1]
    if tak in local_config['core']['white_files'].split(','):
        return True
    return False


if __name__ == "__main__":
    testf = os.environ["PWD"]
    print(getTrashAddress(testf))
    ff = getTrashAddress(testf) + "/dada/dada"
    if inTrash(ff):
        print(ff)
        print("In trash")
