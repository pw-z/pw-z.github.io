#!/usr/bin/env python
# -*- coding: utf-8 -*-
from _codingtools import performance_analyzer


@performance_analyzer
def solution0(s):
    """两个指针向中间迫敛，不断交换即可"""
    print(s)
    low, high = 0, len(s) - 1
    while low < high:
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1
    print(s)


if __name__ == '__main__':
    solution0(["h", "e", "l", "l", "o"])
