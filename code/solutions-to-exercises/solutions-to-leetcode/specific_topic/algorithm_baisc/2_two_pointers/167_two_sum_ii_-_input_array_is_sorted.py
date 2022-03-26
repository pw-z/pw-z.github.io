#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

def solution1(nums, target):
    """遍历
    尝试所有组合
    自然是会超时的
    """
    length = len(nums)
    for i in range(0, length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
    return []


def solution2(numbers, target):
    """双指针
    利用好非递减这个条件，总左右两边迫敛
    大于目标，则右指针左移
    小于目标，则左指针右移
    """
    left, right = 0, len(numbers)-1
    while True:
        cur = numbers[left] + numbers[right]
        if cur == target:
            return [left+1, right+1]
        elif cur > target:
            right -= 1
        else:
            left += 1


def solution3():
    """散列表？此处仅练习双指针，不再分析"""
    pass


if __name__ == '__main__':
    # ans1 = solution1([2, 7, 11, 15], 9)
    print(solution2([0, 0, 3, 4], 0))
    print(solution2([2, 7, 11, 15], 9))
    print(solution2([0, 0, 0, 0, 2, 7, 11, 15], 9))
