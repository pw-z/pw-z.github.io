#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    dic = {
        "11": 1,
        "22": 2,
        "33": 3
    }
    print(dic)
    for key in dic:
        print(key + "  " + str(dic[key]))
