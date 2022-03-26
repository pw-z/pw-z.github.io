#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

def solution0(str_: str):
    """朴素解, 理思路
    O(n) O(n)"""
    print(str_)

    # 获取所有空格符的坐标
    space_loc = []
    for i in range(len(str_)):
        if str_[i] == ' ':
            space_loc.append(i)

    # 依次将每个子串进行反转
    ans = ''
    last = 0
    for x in space_loc:
        # str_[last:x] = str_[last:x][::-1]  # 'str' object does not support item assignment
        ans = ans + str_[last:x][::-1] + ' '
        last = x+1
    # str_[last:] = str_[last:][::-1]
    ans += str_[last:][::-1]

    print(ans)
    return ans


def solution1(str_: str):
    """双指针原地操作，见cpp"""
    pass


if __name__ == '__main__':
    test_str = '123 abc 2002 qwer jklm'
    solution0(test_str)
    a = "Let's take LeetCode contest"
    solution0(a)
