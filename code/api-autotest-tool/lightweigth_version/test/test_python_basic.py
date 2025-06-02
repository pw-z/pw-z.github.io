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


def test3():
    r1 = False
    r2 = False
    r3 = False

    result = r1 and r2 and r3
    print(result)


def test4():
    import time
    t = 'API AutoTest Report ' + time.strftime('%Y.%m.%d')
    print(t)


if __name__ == '__main__':
    # test2()
    # test3()
    test4()