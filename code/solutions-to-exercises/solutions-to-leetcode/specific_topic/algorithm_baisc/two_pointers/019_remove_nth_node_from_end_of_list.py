#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

import _codingtools


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    @_codingtools.performance_analyzer
    def removeNthFromEnd(head: ListNode, n: int):
        """朴素解，遍历计数"""
        print('='*50)

        # 统计一共有多少个节点
        temp_ = head
        count = 0
        while temp_ is not None:
            count += 1
            temp_ = temp_.next

        # 找到该移除节点的前一个节点
        tag_loc = count - n - 1
        temp_ = head
        while tag_loc > 0:
            temp_ = temp_.next
            tag_loc -= 1

        # 移除对应节点
        if temp_.next is None:  # 只有一个节点的情况
            return None
        elif tag_loc == -1:  # 移除head的情况
            head = head.next
            return head
        else:
            temp_.next = temp_.next.next
            return head

    @staticmethod
    @_codingtools.performance_analyzer
    def removeNthFromEnd2(head: ListNode, n: int):
        """双指针::快慢指针，优化掉计数操作
        思想：快指针比慢指针领先n个，则快指针到底时，慢指针处于倒数第n个"""
        slow = fast = head

        while n > 0:
            fast = fast.next
            n -= 1
        if fast is None:  # 移除首节点
            head = head.next
            return head

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    temp = n1
    while temp is not None:
        print(temp.val)
        temp = temp.next

    Solution.removeNthFromEnd(n1, 2)
    """
    exec removeNthFromEnd():
    ==================================================
    cost: 0.004699999999999843ms
    """

    temp = n1
    while temp is not None:
        print(temp.val)
        temp = temp.next
