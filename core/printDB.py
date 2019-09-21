#!/usr/bin/env python
# encoding: utf-8
import DB
import time
if __name__ == "__main__":
    #os.system("rm ~/.mtbd/fileInfo.db")
    #initDB()
    print DB.lastID()
    for inf in DB.getAllInf():
        print inf
