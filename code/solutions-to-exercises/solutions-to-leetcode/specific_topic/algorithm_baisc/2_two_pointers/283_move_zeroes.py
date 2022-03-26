#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022


def solution1(nums):
    """
    双指针，左边指向坑位，右边指向需要处理的数字
    处理过程对0计数，所有数字处理完毕，后面补零
    :param nums:
    :return:
    """
    count = 0
    left, right = 0, 0
    # left = right = 0
    while right < len(nums):
        if nums[right] == 0:
            count += 1
        else:
            nums[left] = nums[right]
            left += 1
        right += 1
    while count > 0:
        nums[-count] = 0
        count -= 1


def solution1_(nums):
    """计数是没有必要的"""
    left, right = 0, 0
    # left = right = 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
        right += 1
    while left < len(nums):
        nums[left] = 0
        left += 1
    print(nums)


def solution2(nums):
    """
    没必要后续补零，多花了时间
    直接按顺序将右侧非零数字与左侧指针处调换
    在起点，L=R， !=0， 则LR均向后移动，仍是一样，直到R处=0，则左右指针分离，
    L开始指向零处，R开始往后走，后续则是非零数不断与零进行置换
    零越多，则L移动次数越少，同样在R遍历nums的情况下，原子操作或略少于solution1
    （少了赋零的耗时，但是多了swap的逻辑，所以具体谁高效也需要确切计算，此处暂不分析）
    :param nums:
    :return:
    """
    print(nums)
    left = right = 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]  # python的swap便捷实现
            left += 1
        right += 1
    print(nums)
    return nums



if __name__ == "__main__":
    # li = [0, 1, 0, 3, 12]
    li = [0]
    # solution(li)
    # print(li)

    # solution1_([0, 1, 0, 3, 12])
    assert str(solution2([0, 1, 0, 3, 12])) == str([1, 3, 12, 0, 0])
