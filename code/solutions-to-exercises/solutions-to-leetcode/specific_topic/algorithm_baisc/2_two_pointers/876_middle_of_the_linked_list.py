#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """双指针::快慢指针
        两个指针slow & fast，其中fast双倍速向后遍历
        若节点数量为奇数，fast.next is None，则返回slow
        若节点数量为奇数，fast.next.next is None，则返回slow"""
        slow = fast = head
        while True:
            fast = fast.next
            if fast is None:  # 判断是否奇数结束
                return slow
            fast = fast.next
            if fast is None:  # 判断是否偶数结束
                return slow.next
            slow = slow.next
