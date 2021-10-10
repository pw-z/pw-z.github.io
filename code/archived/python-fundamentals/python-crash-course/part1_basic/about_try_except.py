#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    try:
        x = 5/0
        print(x)
    except Exception as e:
        print(e)

