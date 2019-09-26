#!/usr/bin/env python
# encoding: utf-8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : main.py
#   Created Time  : 2019-09-19 19:46
#   Last Modified : 2019-09-26 15:38
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
from config import local_config
rmForce = False
if '-f' in argv.opt:
    rmForce = True


def Rm(afile):
    # rm one file for use of pool.map
    # rm_status is the status of oprater 'mv' or 'rm'
    rm_status = ()
    if rmForce:
        rm_status = oper.RmForce(afile)
    else:
        rm_status = oper.MoveToTrash(afile)
    return rm_status


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

def main():
    executor = Pool(local_config.getint('core', 'Num_Processor'))
    logs  =  executor.map(Rm, obtainAllFile())
    executor.close()
    executor.join() 
    DB.insertDB(logs)

if __name__ == "__main__":
    main()
    exit(0)
