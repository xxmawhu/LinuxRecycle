#!/usr/bin/env python
# encoding: utf-8
import DB
import time
def main():
    for inf in DB.getAllInf():
        date = time.asctime(time.localtime(inf[4])).replace("Sat", "@")
        print inf[0], inf[1], date
if __name__ == "__main__":
    main()
