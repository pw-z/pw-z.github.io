#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
from _codingtools import performance_analyzer


@performance_analyzer
def solution0(s: str):
    """双指针::滑动窗口？
    没有搞清楚双指针、滑动窗口的区别，等再多做写题目后总结下

    本题思路：
    窗口不断向前，每次向前移动，判断是否引入重复字符
        若不引入，count值++，继续右移
        若引入，记录一次count值，窗口左边界收缩至无重复状态，继续右移
    tips：使用散列表判断是否引入重复字符
    时间O(n)，空间O(m) m=连续不重复字符数量
    """
    length = len(s)
    left = right = 0
    count = 0
    record = set()
    while right < length:
        if s[right] not in record:
            record.add(s[right])
            right += 1
        else:
            count = max(count, len(record))
            record.remove(s[left])
            left += 1
    count = max(count, len(record))
    return count


@performance_analyzer
def solution_official(s: str):
    """作者：LeetCode - Solution
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            # 不断地移动右指针
            occ.add(s[rk + 1])
            rk += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i + 1)
    return ans


if __name__ == '__main__':
    print(solution0('lkajsdhflgkiuyaweuihgfbjhmadyyyyyyyyyyyyyyyyyyyyyysgfvuiljawheklfgvoiuyasghlkfjehgwljfgaskjdghfkjhwageuyrghialwsyr8723yr87gsjludgfuatw3ufyhsdgbkjfg2qu34grfkjhasdgvbkfjh'))
    print(solution_official('lkajsdhflgkiuyaweuihgfbjhmadyyyyyyyyyyyyyyyyyyyyyysgfvuiljawheklfgvoiuyasghlkfjehgwljfgaskjdghfkjhwageuyrghialwsyr8723yr87gsjludgfuatw3ufyhsdgbkjfg2qu34grfkjhasdgvbkfjh'))

"""
exec solution0():
cost: 0.07269999999999499ms
14

exec solution_offcial():
cost: 0.08129999999999943ms
14
"""