#!/usr/bin/env python
# encoding: utf-8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : main.py
#   Created Time  : 2019-09-19 19:46
#   Last Modified : 2019-09-19 19:46
#   Describe      :
#
# ====================================================
import concurrent.futures
from multiprocessing import Pool
import argv
import DB
import oper
import glob
import time
import sys
import config
rmForce = False
if '-f' in argv.opt:
    rmForce = True
logCol = []


def Rm(afile):
    # global logCol
    log = ()
    if rmForce:
        log = oper.RmForce(afile)
    else:
        log = oper.MoveToTrash(afile)
    # print "log", log
    # logCol.append(log)
    if config.keepDB:
        DB.insertDB([log])


def obtainAllFile():
    files = []
    for i in argv.argv:
        files += glob.glob(i)
    return files


# print obtainAllFile()


def test(f):
    f = []
    for i in range(1000000):
        f.append(i)
    # print len(f)


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
        executor.map(Rm, obtainAllFile())
        exit()
    #
    executor = Pool(argv.core)
    executor.map(Rm, obtainAllFile())
    executor.close()
    #print logCol
    # executor.map(test, range(600))
