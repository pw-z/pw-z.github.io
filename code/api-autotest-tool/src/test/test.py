#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test1():
    dic = {
        "11": 1,
        "22": 2,
        "33": 3
    }
    print(dic)
    for key in dic:
        print(key + "  " + str(dic[key]))

def test2():
    import time
    import datetime
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)
    end = datetime.datetime.now()
    print(end)
    print(end - now)


if __name__ == '__main__':
    test2()
