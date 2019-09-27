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
def main():
    '''
    function:
        print the last #n record information about the files deleted
    '''
    n = 100
    try:
        n = int(sys.argv[1])
    except IndexError as e:
        pass
    except ValueError as e:
        print "Error:: Please input a integer!!! .> -> {}".format(sys.argv[1])
        raise e
    for inf in sorted( DB.getLastRecord(n), key=lambda x:x[0]):
        date = time.asctime(time.localtime(inf[4])).replace("Sat", "@")
        print colored(inf[0], 'blue','on_grey', attrs=['bold']), colored(date,'green'
                ), inf[1]
if __name__ == "__main__":
    main()
