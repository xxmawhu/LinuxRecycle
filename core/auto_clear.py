#!/usr/bin/env python
# encoding: utf-8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : auto_clear.py
#   Created Time  : 2019-09-27 20:05
#   Last Modified : 2019-09-27 20:27
#   Describe      :
#
# ====================================================
import time
import sqlite3
import shutil
from config import local_config
def delete_old_file(raws):
    """
    delete the file in the .trash
    info[2]
    """
    for info in raws:
        file_name = info[2]
        if info[3] != 'd':
            shutil.remove(file_name)
        else:
            shutil.rmtree(file_name)
    return

def update(raws):
    """
    func: update the record information to 'removed'
    """
    update_state = 'UPDATE fileInfo SET exists="removed" WHERE id=?' 
    conn = sqlite3.connect(local_config.get('core', 'data_base_file'))
    try:
        cursor = conn.cursor()
        cursor.executemany(update_state, [i[0] for i in raws])
        rows = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return
def main():
    """
    1. select the record with time less than t_0 and exits = ""exits
    2. delete them and update the data base
    """
    conn = sqlite3.connect(local_config.get('core', 'data_base_file'))
    t0 = time.time() - 3600.0 * 24.0 *  local_config.getint('core', 'keep_days')
    query = 'SELECT * FROM fileInfo WHERE  time < {} AND exists="exists"'.format(t0)
    raws=[]
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    delete_old_file(raws)
    update(raws)
    return
if __name__ == "__main__":
    main()

