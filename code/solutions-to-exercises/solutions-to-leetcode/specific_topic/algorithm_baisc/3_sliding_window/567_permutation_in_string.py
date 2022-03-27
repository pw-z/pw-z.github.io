#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

# 官方题解：https://leetcode-cn.com/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-by-leetcode-solut-7k7u/
# 区分了滑动窗口与双指针，可以对照着理解下

from _codingtools import performance_analyzer


@performance_analyzer
def solution0(s1, s2):
    """朴素解，滑动窗口+重排序，复杂度较高
    思路：在s2中寻找重排序的s1，长度是固定的==len(s1)
    如何判断是s1那些字母? 重排序后进行对比
    """
    target = str(sorted(list(s1)))
    length1, length2 = len(s1), len(s2)
    for i in range(length2-length1):
        piece = s2[i:i+length1]
        piece = str(sorted(list(piece)))
        if piece == target:
            return True

    piece = s2[-length1:]
    piece = str(sorted(list(piece)))
    if piece == target:
        return True
    return False
    # 居然可以AC，耗时5s+


@performance_analyzer
def solution1(s1: str, s2: str):
    """朴素解，滑动窗口+计数"""
    if len(s1) > len(s2):
        return False

    count1 = [0 for _ in range(26)]
    count2 = [0 for _ in range(26)]

    for c in s1:
        count1[ord(c) - ord('a')] += 1

    # 初始化右指针
    left = right = 0
    while right < len(s1):
        count2[ord(s2[right]) - ord('a')] += 1
        right += 1
    if count2 == count1:
        return True

    # 开始向右滑动，同时增减count2，比对结果
    while right < len(s2):
        count2[ord(s2[right]) - ord('a')] += 1
        count2[ord(s2[left]) - ord('a')] -= 1
        right += 1
        left += 1
        if count2 == count1:
            return True

    return False


def solution1_more(s1, s2):
    """解法1优化，将count1，count2抽象成diff，diff=count1、count2中不同值的个数"""
    pass

# 双指针解法有些强行双指针的意思。。。 固定大小的窗口。。。


if __name__ == '__main__':
    print(solution0("ab", "eidbaooo"))
    print(solution0("adc", "dcda"))
    print(solution1("ab", "eidbaooo"))
    print(solution1("adc", "dcda"))

