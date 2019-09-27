#!/usr/bin/env python
# encoding: utf-8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : printDB.py
#   Created Time  : 2019-09-27 14:37
#   Last Modified : 2019-09-27 14:41
#   Describe      :
#
# ====================================================

import DB
import time
import sys
from termcolor import colored
import shutil
def recover(ID):
    """
    recover one file by the ID
    """
    inf = DB.get_record_by_id(ID)
    if not inf:
        print "Error: voild ID {}".format(ID)
        return
    record_inf = inf[0]
    # print record_inf
    try:
        shutil.copy(record_inf[2], record_inf[1])
    finally:
        pass


def main():
    '''
    usage:
       recover id1 [id2 id3]
    '''
    for ID in list(map(int, sys.argv[1:])):
        recover(ID)
if __name__ == "__main__":
    main()
