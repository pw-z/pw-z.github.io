# Leetcode Hot100 Note

*Posted on 2024.05.25 by [pwz](http://pwz.wiki)* 

[Leetcode Hot100](https://leetcode.cn/studyplan/top-100-liked/) ，`2024.04.01 ~ 2024.05.24`，时间跨度将近两个月，每天三两道题如此做完了一遍。有很多题目非常经典，引申出一系列变型问题，期间翻看到很多大佬的题解与总结，关于这些题目，有一部分并没有理解透彻，很多专题还需要深入学习，这个阶段就当是个引子。

这篇文档的初衷只是刷题过程的电子草稿纸，后来成了某种进度条、打卡记录，刷算法题的最终目标是提高算法能力，在实际的问题场景下快速给出高效的解，记录这样一篇文档本身如何能对达成这个目标产生积极作用？要么做严谨的总结，要么就别把这太当作一回事，回归它草稿纸的本质就好。


- [Leetcode Hot100 Note](#leetcode-hot100-note)
  - [哈希](#哈希)
    - [1. 两数之和\*](#1-两数之和)
    - [49. 字母异位词分组](#49-字母异位词分组)
    - [128. 最长连续序列](#128-最长连续序列)
  - [双指针](#双指针)
    - [283. 移动零\*](#283-移动零)
    - [11. 盛最多水的容器](#11-盛最多水的容器)
    - [167. 两数之和 II - 输入有序数组](#167-两数之和-ii---输入有序数组)
    - [15. 三数之和](#15-三数之和)
    - [42. 接雨水\*\*（单调栈；双指针）](#42-接雨水单调栈双指针)
  - [滑动窗口](#滑动窗口)
    - [3. 无重复字符的最长子串](#3-无重复字符的最长子串)
    - [438. 找到字符串中所有字母异位词](#438-找到字符串中所有字母异位词)
    - [209. 长度最小的子数组](#209-长度最小的子数组)
  - [子串](#子串)
    - [560. 和为 K 的子数组（有空再瞅瞅）](#560-和为-k-的子数组有空再瞅瞅)
    - [239. 滑动窗口最大值](#239-滑动窗口最大值)
    - [76. 最小覆盖子串](#76-最小覆盖子串)
  - [普通数组](#普通数组)
    - [53. 最大子数组和（动态规划）](#53-最大子数组和动态规划)
    - [56. 合并区间（排序）](#56-合并区间排序)
    - [189. 轮转数组](#189-轮转数组)
    - [238. 除自身以外数组的乘积](#238-除自身以外数组的乘积)
    - [41. 缺失的第一个正数](#41-缺失的第一个正数)
  - [矩阵](#矩阵)
    - [73. 矩阵置零](#73-矩阵置零)
    - [54. 螺旋矩阵](#54-螺旋矩阵)
    - [48. 旋转图像](#48-旋转图像)
    - [240. 搜索二维矩阵 II （矩阵、二分、压缩搜索空间）](#240-搜索二维矩阵-ii-矩阵二分压缩搜索空间)
  - [链表](#链表)
    - [160. 相交链表\*](#160-相交链表)
    - [206. 反转链表\*](#206-反转链表)
    - [234. 回文链表\*（快慢指针）](#234-回文链表快慢指针)
    - [141. 环形链表\*（快慢指针）](#141-环形链表快慢指针)
    - [142. 环形链表 II（快慢指针 + 数学）](#142-环形链表-ii快慢指针--数学)
    - [21. 合并两个有序链表\*（双指针）](#21-合并两个有序链表双指针)
    - [2. 两数相加](#2-两数相加)
    - [19. 删除链表的倒数第 N 个结点](#19-删除链表的倒数第-n-个结点)
    - [24. 两两交换链表中的节点](#24-两两交换链表中的节点)
    - [25. K 个一组翻转链表](#25-k-个一组翻转链表)
    - [138. 随机链表的复制](#138-随机链表的复制)
    - [148. 排序链表](#148-排序链表)
    - [23. 合并 K 个升序链表](#23-合并-k-个升序链表)
    - [146. LRU 缓存](#146-lru-缓存)
  - [二叉树](#二叉树)
    - [94. 二叉树的中序遍历\*](#94-二叉树的中序遍历)
    - [104. 二叉树的最大深度\*](#104-二叉树的最大深度)
    - [226. 翻转二叉树\*](#226-翻转二叉树)
    - [101. 对称二叉树\*](#101-对称二叉树)
    - [543. 二叉树的直径\*](#543-二叉树的直径)
    - [102. 二叉树的层序遍历](#102-二叉树的层序遍历)
    - [108. 将有序数组转换为二叉搜索树\*](#108-将有序数组转换为二叉搜索树)
    - [98. 验证二叉搜索树](#98-验证二叉搜索树)
    - [230. 二叉搜索树中第K小的元素](#230-二叉搜索树中第k小的元素)
    - [199. 二叉树的右视图](#199-二叉树的右视图)
    - [114. 二叉树展开为链表](#114-二叉树展开为链表)
    - [105. 从前序与中序遍历序列构造二叉树](#105-从前序与中序遍历序列构造二叉树)
    - [112. 路径总和\*](#112-路径总和)
    - [437. 路径总和 III](#437-路径总和-iii)
    - [236. 二叉树的最近公共祖先](#236-二叉树的最近公共祖先)
    - [124. 二叉树中的最大路径和\*\*](#124-二叉树中的最大路径和)
  - [图论](#图论)
    - [200. 岛屿数量](#200-岛屿数量)
    - [463. 岛屿的周长](#463-岛屿的周长)
    - [994. 腐烂的橘子](#994-腐烂的橘子)
    - [207. 课程表](#207-课程表)
    - [208. 实现 Trie (前缀树)](#208-实现-trie-前缀树)
  - [回溯](#回溯)
    - [46. 全排列](#46-全排列)
    - [78. 子集](#78-子集)
    - [17. 电话号码的字母组合](#17-电话号码的字母组合)
    - [39. 组合总和](#39-组合总和)
    - [22. 括号生成](#22-括号生成)
    - [77. 组合](#77-组合)
    - [79. 单词搜索](#79-单词搜索)
    - [131. 分割回文串](#131-分割回文串)
    - [51. N 皇后\*\*](#51-n-皇后)
  - [二分查找](#二分查找)
    - [35. 搜索插入位置](#35-搜索插入位置)
    - [74. 搜索二维矩阵](#74-搜索二维矩阵)
    - [34. 在排序数组中查找元素的第一个和最后一个位置](#34-在排序数组中查找元素的第一个和最后一个位置)
    - [33. 搜索旋转排序数组](#33-搜索旋转排序数组)
    - [153. 寻找旋转排序数组中的最小值](#153-寻找旋转排序数组中的最小值)
    - [4. 寻找两个正序数组的中位数](#4-寻找两个正序数组的中位数)
  - [栈](#栈)
    - [20. 有效的括号](#20-有效的括号)
    - [155. 最小栈](#155-最小栈)
    - [394. 字符串解码](#394-字符串解码)
    - [739. 每日温度（单调栈）](#739-每日温度单调栈)
    - [496. 下一个更大元素 I\*（单调栈）](#496-下一个更大元素-i单调栈)
    - [503. 下一个更大元素 II](#503-下一个更大元素-ii)
    - [84. 柱状图中最大的矩形\*\*（单调栈）](#84-柱状图中最大的矩形单调栈)
  - [堆](#堆)
    - [215. 数组中的第K个最大元素](#215-数组中的第k个最大元素)
    - [347. 前 K 个高频元素](#347-前-k-个高频元素)
    - [295. 数据流的中位数](#295-数据流的中位数)
  - [贪心算法](#贪心算法)
    - [121. 买卖股票的最佳时机\*](#121-买卖股票的最佳时机)
    - [55. 跳跃游戏](#55-跳跃游戏)
    - [45. 跳跃游戏 II](#45-跳跃游戏-ii)
    - [763. 划分字母区间](#763-划分字母区间)
  - [动态规划](#动态规划)
    - [70. 爬楼梯](#70-爬楼梯)
    - [118. 杨辉三角](#118-杨辉三角)
    - [198. 打家劫舍](#198-打家劫舍)
    - [279. 完全平方数](#279-完全平方数)
    - [322. 零钱兑换](#322-零钱兑换)
    - [139. 单词拆分](#139-单词拆分)
    - [300. 最长递增子序列LIS](#300-最长递增子序列lis)
    - [152. 乘积最大子数组](#152-乘积最大子数组)
    - [416. 分割等和子集](#416-分割等和子集)
    - [32. 最长有效括号\*\*](#32-最长有效括号)
  - [多维动态规划](#多维动态规划)
    - [62. 不同路径](#62-不同路径)
    - [64. 最小路径和](#64-最小路径和)
    - [5. 最长回文子串](#5-最长回文子串)
    - [1143. 最长公共子序列LCS](#1143-最长公共子序列lcs)
    - [72. 编辑距离](#72-编辑距离)
  - [技巧](#技巧)
    - [136. 只出现一次的数字\*（位运算）](#136-只出现一次的数字位运算)
    - [169. 多数元素\*（Boyer-Moore多数投票算法）](#169-多数元素boyer-moore多数投票算法)
    - [75. 颜色分类](#75-颜色分类)
    - [31. 下一个排列](#31-下一个排列)
    - [287. 寻找重复数](#287-寻找重复数)


## 哈希

### [1. 两数之和*](https://leetcode.cn/problems/two-sum/)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """✅解法1: 二层循环，O(N^2)，O(1)

        执行用时分布
        1619ms
        击败24.74%使用 Python3 的用户
        消耗内存分布
        17.01MB
        击败88.70%使用 Python3 的用户
        """
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """✅解法2: 哈希表，O(N)，O(1)

        执行用时分布
        45ms
        击败56.32%使用 Python3 的用户
        消耗内存分布
        17.59MB
        击败43.46%使用 Python3 的用户
        """
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash.keys():
                return [i, hash[target-nums[i]]]
            hash[nums[i]] = i
```


### [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/)

```python
class Solution:

   
    def _hash1(self, str):
        """❌哈希函数：对单词字母ascii码求和作为哈希值
        哈希冲突

        解答错误
        55 / 126 个通过的测试用例
        """
        sum = 0
        for x in str:
            sum += ord(x)
        return sum
    
    
    def _hash2(self, str):
        """❌哈希函数：尝试提高哈希值离散情况
        哈希冲突

        解答错误
        113 / 126 个通过的测试用例
        """
        sum = 0
        for x in str:
            sum += ord(x)*ord(x)
        return sum

    
    def _hash(self, mystr):
        """✅哈希函数：使用排序后的字母作为哈希值

        执行用时分布
        41ms
        击败95.69%使用 Python3 的用户

        消耗内存分布
        19.24MB
        击败77.65%使用 Python3 的用户
        """
        l = list(mystr)
        l.sort()
        return ''.join(l)
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            h = self._hash(s)
            if h in res.keys():
                res[h].append(s)
            else:
                res[h] = [s]
        return list(res.values())

```


### [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/)

```python
class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        """❌哈希表降低查找复杂度，通过判断n-1是否在表中跳过重复判断
        特殊用例未兼容，用例[0]未通过，预期1实际0

        解答错误
        64 / 75 个通过的测试用例
        """
        hash_t = {}
        res = 0
        l = len(nums)
        for n in nums:
            hash_t[n] = n

        # for idx, n in enumerate(nums):
        for n in nums:
            if n - 1 in hash_t.keys():
                continue

            for i in range(l):
                if n + i not in hash_t.keys():
                    res = max(res, i)
                    break

        return res
    
    def longestConsecutive(self, nums: List[int]) -> int:
        """✅逻辑同上，代码优化
        
        执行用时分布
        79ms
        击败87.06%使用 Python3 的用户
        消耗内存分布
        32.69MB
        击败81.45%使用 Python3 的用户
        """
        nums_set = set(nums) # Python 中set、dict都基于哈希表
        max_res = 0
        for n in nums_set:
            if n-1 not in nums_set:
                count = 1
                while n + count in nums_set:
                    count += 1
                max_res = max(max_res, count)

        return max_res


```


## 双指针

### [283. 移动零*](https://leetcode.cn/problems/move-zeroes/)

```python
class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """✅双指针同时从前往后扫描，一个找0，一个找非0，不断替换
        Do not return anything, modify nums in-place instead.
        
        1、考虑特殊情况 --> 在程序中优先排除
        2、考虑适用算法 --> 实在不行试试暴力解
        3、考虑时间、空间复杂度 --> 有没有优化空间
        
        执行用时分布
        45ms
        击败69.72%使用 Python3 的用户
        消耗内存分布
        17.47MB
        击败37.19%使用 Python3 的用户
        """
        l = len(nums)

        # 初始化两个指针的位置，此处确保back处于front后面
        front = 0
        while nums[front] != 0:
            front += 1
            if front >= l:
                break
        back = front+1

        # “冒泡”
        while back < l:
            nums[front] = nums[back]
            nums[back] = 0

            while nums[back] == 0:
                back += 1
                if back >= l:
                    break
            while nums[front] != 0:
                front += 1
                if front >= l:
                    break

    def moveZeroes(self, nums: List[int]) -> None:
        """✅上述逻辑优化&&官方题解

        执行用时分布
        42ms
        击败82.97%使用 Python3 的用户
        消耗内存分布
        17.35MB
        击败82.39%使用 Python3 的用户
        """
        l = len(nums)
        front = back = 0
        while back < l:
            if nums[back] != 0:
                nums[front], nums[back] = nums[back], nums[front]
                front += 1
            back += 1
    
```


### [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)

```python
class Solution:
    def maxArea1(self, height: List[int]) -> int:
        """❌双重循环暴力解，超出时间限制

        超出时间限制
        51 / 62 个通过的测试用例
        """
        max_area = 0
        length = len(height)
        for l in range(length):
            for r in range(l+1, length):
                max_area = max(max_area, min(height[l],height[r])*(r-l))
        return max_area
    
    def maxArea(self, height: List[int]) -> int:
        """✅双指针，始终移动指向更矮的那个指针，缩减搜索空间

        执行用时分布
        127ms
        击败65.06%使用 Python3 的用户
        消耗内存分布
        26.66MB
        击败87.96%使用 Python3 的用户
        """
        max_area = 0
        left, right = 0, len(height)-1
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            if current_area > max_area:
                max_area = current_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

# 这个题解很棒：https://leetcode.cn/problems/container-with-most-water/solutions/94102/on-shuang-zhi-zhen-jie-fa-li-jie-zheng-que-xing-tu/
```


### [167. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """你所设计的解决方案必须只使用常量级的额外空间 --> 不能使用哈希表
        非递减顺序：从前往后可能是相等或者增加
        """
        l, r = 0, len(numbers)-1
        while l < r:
            current = numbers[l] + numbers[r]
            if current == target:
                return [l+1, r+1]
            # 缩减搜索范围的逻辑：
            # 当前两数和可能大于或小于target
            if current > target:
                r -= 1
            if current < target:
                l += 1
            #以上过程不会把正确答案过滤掉，参考官方题解：https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/solutions/337156/liang-shu-zhi-he-ii-shu-ru-you-xu-shu-zu-by-leet-2/
```


### [15. 三数之和](https://leetcode.cn/problems/3sum/)

```python
class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        """❌排序O(NlogN) + 双循环O(N^2) * ( 哈希表O(1)? + 遍历O(N) ), 整体复杂度 O(N^3)，超时了

        超出时间限制
        308 / 313 个通过的测试用例
        """
        size = len(nums)
        results = []
        target_mark = {}

        nums = sorted(nums)
        i = 0
        while i < size - 2:
            target = 0 - nums[i]
            j = i + 1
            while j < size - 1:
                # print("i=", i)
                s_nums_set = nums[j + 1:]
                inner_target = target - nums[j]

                if target in target_mark.keys():
                    if inner_target == target_mark[target] or nums[j] == target_mark[target]:
                        j+=1
                        continue

                if inner_target in s_nums_set:
                    results.append([nums[i], nums[j], inner_target])
                    target_mark[target] = inner_target
                j += 1
            i += 1
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """✅官方题解的复现，各种需要跳过的重复判断是提高效率的关键
        
        执行用时分布
        590ms
        击败67.23%使用 Python3 的用户
        消耗内存分布
        19.52MB
        击败28.71%使用 Python3 的用户
        """
        size = len(nums)
        results = []
        nums = sorted(nums)
        for i in range(size):

            if i>0 and nums[i] == nums[i -1]:continue #排除重复的三元组第1个值
            target = -nums[i]

            r = size-1 #随着后续l不断变大，r没有往右的空间，所以在l遍历前初始化一次即可
            for l in range(i+1, size):
                if l > i+1 and nums[l] == nums[l-1]:continue  #排除重复的三元组第2个值
                
                while l < r and nums[l] + nums[r] > target:r -= 1
                if l == r: break #上一行l<r的情况下有可能把r减成l

                if nums[l] + nums[r] == target:
                    results.append([nums[i], nums[l], nums[r]])
        
        return results
```


### [42. 接雨水**（单调栈；双指针）](https://leetcode.cn/problems/trapping-rain-water/)

一个视频把思路讲的很清晰：https://www.bilibili.com/video/BV1Qg411q7ia/?vd_source=215226f55ec25efebe70612682143c68

```python
class Solution:
    def trap1(self, height: List[int]) -> int:
        """✅单调栈，参考官解
        
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = 0
        stack = list()
        length = len(height)

        for i in range(length):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if stack:
                    left = stack[-1]
                    ans += (i-left-1) * (min(height[left],height[i]) - height[top])
                else:break

            stack.append(i)
            
        return ans
    

    def trap(self, height: List[int]) -> int:
        """✅双指针，参考官解
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        length = len(height)
        l, r = 0, length-1
        l_max = r_max = 0
        ans = 0

        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max < r_max:
                ans += l_max-height[l]
                l += 1
            else:
                ans += r_max-height[r]
                r -= 1
        return ans
```

## 滑动窗口

> 滑动窗口算法在一个特定大小的字符串或数组上进行操作，而不在整个字符串和数组上操作，这样就降低了问题的复杂度，从而也达到降低了循环的嵌套深度。
> 
> 由于区间连续，因此当区间发生变化时，可以通过旧有的计算结果对搜索空间进行剪枝，这样便减少了重复计算，降低了时间复杂度。往往类似于“ 请找到满足 xx 的最 x 的区间（子串、子数组）的 xx ”这类问题都可以使用该方法进行解决。
> 
> >[滑动窗口算法基本原理与实践](https://www.cnblogs.com/huansky/p/13488234.html)


### [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

```python
class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        """✅滑动窗口，窗口大小不固定，窗口内不能有重复字符

        执行用时分布
        91ms
        击败16.20%使用 Python3 的用户
        消耗内存分布
        16.49MB
        击败58.95%使用 Python3 的用户
        """
        l = r = 0
        max_s = 0
        w = []
        while r < len(s):
            if s[r] not in w:
                w.append(s[r])
                max_s = max(max_s, len(w))
                r+=1
            else:
                l += 1
                w.pop(0)
        return max_s

    def lengthOfLongestSubstring(self, s: str) -> int:
        """✅滑动窗口，优化效率，主要是将判断新字符是否在窗口内改成了哈希表判断

        执行用时分布
        56ms
        击败73.63%使用 Python3 的用户
        消耗内存分布
        16.63MB
        击败19.96%使用 Python3 的用户
        """
        l = r = max_s = 0
        w = set()
        while r < len(s):
            if s[r] not in w:
                w.add(s[r])
                max_s = max(max_s, len(w))
                r += 1
            else:
                w.remove(s[l]) # 移除窗口内最左边的数据
                l += 1
        return max_s
```


### [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

```python
class Solution:
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        """✅滑动窗口，窗口固定大小为len(p)，判断窗口内是否为p的异位词

        执行用时分布
        6303ms
        击败14.51%使用 Python3 的用户
        消耗内存分布
        17.00MB
        击败24.48%使用 Python3 的用户
        """
        win_size = len(p)
        p = sorted(p)
        ans = []
        for l in range(len(s)-win_size+1):
            if sorted(s[l:l+win_size]) == p:
                # 切片操作的时间复杂度为O(k),k=切片长度
                # sorted时间复杂度为O(nlogn)
                ans.append(l)
        return ans
        
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """✅滑动窗口，优化窗口内判断是否为异位词的逻辑

        执行用时分布
        53ms
        击败97.23%使用 Python3 的用户
        消耗内存分布
        16.98MB
        击败27.27%使用 Python3 的用户
        """
        win_size = len(p)
        s_size = len(s)
        ans = []

        if s_size < win_size:return []

        # 依据题目条件仅含小写字母，使用26位数组分别存储26个字母的数量，用于判断是否为异位词
        s_count = [0] * 26
        p_count = [0] * 26

        # 初始化第一个窗口及目标值
        for i in range(win_size):
            s_count[ord(s[i])-ord('a')] += 1
            p_count[ord(p[i])-ord('a')] += 1
        if s_count == p_count:
            ans.append(0)

        for start in range(len(s) - win_size):
            # 窗口向右挪动一单位
            s_count[ord(s[start]) - ord('a')] -= 1 # 窗口左侧字母消除
            s_count[ord(s[start + win_size]) - ord('a')] += 1 # 窗口右侧字母加入
            if s_count == p_count:
                ans.append(start+1)

        return ans
```

### [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # https://www.bilibili.com/video/BV1hd4y1r7Gq
        n = len(nums)
        ans = n+1
        l = 0
        s = 0
        for r, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, r-l+1)
                s -= nums[l]
                l += 1
        return ans if ans <= n else 0
```


## 子串

### [560. 和为 K 的子数组（有空再瞅瞅）](https://leetcode.cn/problems/subarray-sum-equals-k/)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        pre = 0
        mp = {0:1,}
        for i in range(n):
            pre += nums[i]
            if pre - k in mp.keys():
                ans += mp[pre-k]
            
            mp[pre] = mp.get(pre, 0) + 1
        return ans
```


### [239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)

```python
class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """❌拜托答案不是递增的，当前窗口的最大值可能小于前一窗口最大值"""
        low = 0
        high = k-1
        n = len(nums)
        ans = []
        lastTop = max(nums[low:high+1])
        while high < n:
            # print(nums[low:high+1])
            if nums[high] > lastTop:
                lastTop = nums[high]
            ans.append(lastTop)
            low += 1
            high += 1
        return ans
    
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """堆 官解思路"""
        n = len(nums)
        q = [(-nums[i],i) for i in range(k)] # 建堆 O(k)
        heapq.heapify(q) 

        ans = [-q[0][0]]
        for i in range(k, n): # 遍历 O(n)
            heapq.heappush(q, (-nums[i], i)) # 堆化 最差O(logn)
            while q[0][1] <= i-k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """双端队列 https://www.bilibili.com/video/BV1bM411X72E"""
        ans = []
        q = deque()
        for i,x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i-q[0] >= k:
                q.popleft()
            if i>= k-1:
                ans.append(nums[q[0]])
        return ans
```


### [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        cnt_t = defaultdict(int)
        for c in t:
            cnt_t[c] += 1
        def covered(a: dict, b: dict):
            # 判断 a 是否覆盖 b
            for k, v in b.items():
                if not a[k] or a[k] < v:
                    return False
            return True

        cnt_s = defaultdict(int)
        ansL, ansR = -1, len(s)
        l = 0
        for r, x in enumerate(s):
            cnt_s[x] += 1
            while covered(cnt_s, cnt_t):
                if r - l < ansR - ansL:
                    ansL, ansR = l, r
                cnt_s[s[l]] -= 1
                l += 1

        return "" if ansL < 0 else s[ansL: ansR+1]
```



## 普通数组


### [53. 最大子数组和（动态规划）](https://leetcode.cn/problems/maximum-subarray/)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """动态规划经典题
        题解：https://leetcode.cn/problems/maximum-subarray/solutions/9058/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/?envType=study-plan-v2&envId=top-100-liked
        """
        n = len(nums)
        if n == 0: return 0

        dp = [0] * n
        dp[0] = nums[0] # 初始值
        for i in range(1, n):
            dp[i] = dp[i-1] + nums[i] if dp[i-1] >= 0 else nums[i]

        return max(dp)
```


### [56. 合并区间（排序）](https://leetcode.cn/problems/merge-intervals/)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])
        for x in intervals:
            if not ans or ans[-1][1] < x[0]:
                ans.append(x)
            else:
                ans[-1][1] = max(ans[-1][1], x[1])
        return ans
```


### [189. 轮转数组](https://leetcode.cn/problems/rotate-array/)

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        每个需要被挪动的数据最终坐标可以通过数组长度及K计算出来
        """
        n = len(nums)
        k %= n
        count = 0
        for i in range(n):
            cur = i
            prev = nums[i]

            flag = True
            while flag or cur != i:
                flag = False
                next = (cur + k)%n
                temp = nums[next]
                nums[next] = prev
                prev = temp
                cur = next

                count += 1

            if count == n:
                break
        
        # 官解的O(1)求了个最大公约数，算法有质因数分解法、短除法、辗转相除法、更相减损法
        # 辗转相除法最易于用算法表达，递归实现如下：
        def gcd(a, b):
            return gcd(b, a%b) if b > 0 else a
```


### [238. 除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """前缀积 * 后缀积"""
        n = len(nums)
        L = [1]*n
        R = [1]*n

        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
            R[-i-1] = R[-i] * nums[-i]
        print(L, R)

        ans = []
        for i in range(n):
            ans.append(L[i]*R[i])
        return ans
    # O(1)空间复杂度可以借助ans数组本身存储L，然后遍历求R的同时给出ans
```


### [41. 缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/)

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 为赋新词强说愁
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        print(nums)
        
        for i in range(n):
            num = abs(nums[i])
            if num<=n:
                nums[num-1] = -abs(nums[num-1])
        print(nums)

        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1
```


## 矩阵


### [73. 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/)

没什么特殊解法，空间优化可以考虑使用传入的参数本身占据的内存空间。

```python
class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """空间复杂度 O(m+n)，顺其自然的朴素解
        """
        m, n = len(matrix), len(matrix[0])
        tag_x = [False]*m
        tag_y = [False]*n
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    tag_x[x] = True
                    tag_y[y] = True
        
        for x in range(m):
            for y in range(n):
                if tag_x[x] or tag_y[y]:
                    matrix[x][y] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """空间复杂度 O(1)，看了官解实践一次
        any关键字之前没用过，好方便，有必要把python基础巩固下
        """
        m, n = len(matrix), len(matrix[0])
        f_col0 = any(matrix[i][0] == 0 for i in range(m))
        f_row0 = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if f_col0:
            for i in range(m):
                matrix[i][0] = 0
        
        if f_row0:
            for j in range(n):
                matrix[0][j] = 0
```


### [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)

```python
class Solution:
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        """✅找规律，对结尾的判断、方向转换的判断有瑕疵，打补丁变成屎山

        00，01，02，03==None，12，22，32==None，21，20，2-1==None，10，00==visited，11，12==visited，21==visited，Done
        用两个变量标记矩阵当前的宽度、高度，转一圈需要➡️⬇️⬅️⬆️四个方向各走到头，每次⬆️or⬇️的时候高度-1，每次⬅️or➡️的时候宽度-1
        用宽高余量判断结束有点麻烦，额外申请一个变量count_stop，当访问了m*n个数据点之后结束遍历
        """
        ans = []
        m, n = len(matrix), len(matrix[0])
        w, h = n, m
        current_x, current_y = 0, 0
        ans.append(matrix[current_y][current_x])
        count = 1
        count_stop = m*n
        flag = True

        # 先把第一行走完，这一行不用改变宽度
        for i in range(1, w):
            current_x += 1
            ans.append(matrix[current_y][current_x])
            count += 1
            if count == count_stop:
                flag = False
                break
        current_d = 'down' # left, up, down

        # 开始绕圈，每次绕圈改变方向的过程都需要将对应的宽度或高度-1
        while flag and (w > 0 and h > 0):
            if current_d == 'right':
                for i in range(1, w):
                    current_x += 1
                    ans.append(matrix[current_y][current_x])
                    count += 1
                    if count == count_stop:
                        flag = False
                        break
                    print(count, current_d, ans[-1], flag, w, h)
                w -= 1
                current_d = 'down'
            elif current_d == 'down':
                for i in range(1, h):
                    current_y += 1
                    ans.append(matrix[current_y][current_x])
                    count += 1
                    if count == count_stop:
                        flag = False
                        break
                    print(count, current_d, ans[-1], flag, w, h)
                h -= 1
                current_d = 'left'
            elif current_d == 'left':
                for i in range(1, w):
                    current_x -= 1
                    ans.append(matrix[current_y][current_x])
                    count += 1
                    if count == count_stop:
                        flag = False
                        break
                    print(count, current_d, ans[-1], flag, w, h)
                w -= 1
                current_d = 'up'
            elif current_d == 'up':
                for i in range(1, h):
                    current_y-=1
                    ans.append(matrix[current_y][current_x])
                    count += 1
                    if count == count_stop:
                        flag = False
                        break
                    print(count, current_d, ans[-1], flag, w, h)
                h -= 1
                current_d = 'right'
        return ans
    

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """官方题解写法，清爽"""
        m, n = len(matrix), len(matrix[0])
        ans = []
        left, right, top, bottom = 0, n-1, 0, m-1
        while left <= right and top <= bottom:
            # 从左到右
            for col in range(left, right+1):
                ans.append(matrix[top][col])
            # 从上往下
            for row in range(top+1, bottom+1):
                ans.append(matrix[row][right])
            
            if left < right and top < bottom:
                # 从右往左
                for col in range(right-1, left, -1):
                    ans.append(matrix[bottom][col])
                # 从下往上
                for row in range(bottom, top, -1):
                    ans.append(matrix[row][left])
            
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return ans
```


### [48. 旋转图像](https://leetcode.cn/problems/rotate-image)

```python
class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        第i行j列的元素，旋转后出现在倒数第i列j行
        时间O(N^2)，空间O(N^2)
        """
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(1, n+1): #索引为0当作第1行处理
            for j in range(n):
                matrix_new[j][-i] = matrix[i-1][j] #-i直接对应倒数第i行，i-1对应正数第i行的索引
        matrix[:] = matrix_new
    
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                # 如下同时复制四个变量省掉了自己创造中间变量的过程
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
```


### [240. 搜索二维矩阵 II （矩阵、二分、压缩搜索空间）](https://leetcode.cn/problems/search-a-2d-matrix-ii/)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """❌如何有效的缩减搜索范围并且不能错过目标是关键

        解答错误
        105 / 130 个通过的测试用例

        [[-1,3]]
        -1

        对比官方题解[方法三：Z 字形查找](https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/1062538/sou-suo-er-wei-ju-zhen-ii-by-leetcode-so-9hcx/)，主要是起始位置的选择
        从矩阵右下角无论往上还是往左走都是递减，而从右上角开始往左是递减、往下是递增，是个二叉搜索树，左下角同理
        """
        row = len(matrix)-1
        col = len(matrix[0])-1
        while row >= 0 and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row-1][col] < target: # 变动行后若错过目标，则只能列变动
                col -= 1
            elif matrix[row][col-1] < target: # 变动列后若错过目标，则只能行变动
                row -= 1
            else: # 选择变动小的方向，不然可能错过目标
                if matrix[row][0] < matrix[0][col-1]:
                    col -= 1
                else:
                    row -= 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """✅根据官方题解从矩阵左下角出发进行Z字形搜索
        
        执行用时分布
        148ms
        击败54.23%使用 Python3 的用户
        消耗内存分布
        22.57MB
        击败50.48%使用 Python3 的用户
        """
        x, y = len(matrix)-1, 0  # 从左下角开始
        while x >= 0 and y < len(matrix[0]):
            if matrix[x][y] == target:
                return True
            if matrix[x-1][y] >= target:
                x -= 1
            else:
                y += 1
        return False
```


## 链表

### [160. 相交链表*](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """✅哈希，时间复杂度O(m+n)，空间复杂度O(m)，m是A链表长度

        执行用时分布
        92ms
        击败28.59%使用 Python3 的用户
        消耗内存分布
        26.84MB
        击败27.16%使用 Python3 的用户
        """
        node = headA
        hash_table = {}
        while node is not None:
            # print(node.val)
            hash_table[id(node)] = node
            node = node.next

        node = headB
        while node is not None:
            if id(node) in hash_table.keys():
                break
            node = node.next
        return node
    

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """✅双指针，没想到这个解法（遍历过程指针运行长度的恒等式），看了题解后实现一遍。

        执行用时分布
        77ms
        击败90.61%使用 Python3 的用户
        消耗内存分布
        26.68MB
        击败46.24%使用 Python3 的用户
        """
        pa = headA
        pb = headB
        while pa != pb:
            if pa is None and pb is None:
                return None
            elif pa is None:
                pa = headB
                pb = pb.next
            elif pb is None:
                pb = headA
                pa = pa.next
            else:
                pa = pa.next
                pb = pb.next
        return pa
```

### [206. 反转链表*](https://leetcode.cn/problems/reverse-linked-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """✅迭代

        执行用时分布
        34ms
        击败84.93%使用 Python3 的用户
        消耗内存分布
        17.32MB
        击败34.48%使用 Python3 的用户
        """
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """递归？晚点再研究
        """
```

### [234. 回文链表*（快慢指针）](https://leetcode.cn/problems/palindrome-linked-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """简单题我不会:(
        
        快慢指针：参考题解实现空间复杂度O(1)的解法
            在原链表上操作，快指针一次两步、慢指针一次一步找到中间节点
            反转一半的链表后进行对比
            对比完成后将链表恢复原位
        
        执行用时分布
        268ms
        击败92.76%使用 Python3 的用户
        消耗内存分布
        33.04MB
        击败91.84%使用 Python3 的用户
        """

        # slow 停在后半部份的head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 反转链表后半部份
        # 反转前：
        # 1 -> ... -> lmid_end -> rmid_start -> ... -> end
        # ^                           ^
        # |                           |
        # head                       slow
        # 反转后：
        # 1 -> ... -> lmid_end -> rmid_start <- ... <- end
        # ^                           ^
        # |                           |
        # head                       slow
        prev = slow
        current = slow.next
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        # 此时 prev 为尾节点
        # 1 -> ... -> lmid_end -> rmid_start <- ... <- end
        # ^                           ^                 ^
        # |                           |                 |
        # head                       slow              prev
        
        # 判断回文
        check_l = head
        check_r = prev
        while check_l != slow:
            if check_l.val != check_r.val:
                return False
            check_l = check_l.next
            check_r = check_r.next
        
        # 将链表恢复原状（可选，函数便携规范，不改变入参）
        prev_new = None
        current = prev
        while current != slow:
            next = current.next
            current.next = prev_new
            prev_new = current
            current = next

        return True
```


### [141. 环形链表*（快慢指针）](https://leetcode.cn/problems/linked-list-cycle/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """✅快慢指针

        执行用时分布
        44ms
        击败80.90%使用 Python3 的用户
        消耗内存分布
        18.86MB
        击败48.93%使用 Python3 的用户

        > NOTE: 兔子会不会「跳过」乌龟，从来不会和乌龟相遇呢？这是不可能的。如果有环的话，那么兔子和乌龟都会进入环中。这时用「相对速度」思考，乌龟不动，兔子相对乌龟每次只走一步，这样就可以看出兔子一定会和乌龟相遇了。
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
```


### [142. 环形链表 II（快慢指针 + 数学）](https://leetcode.cn/problems/linked-list-cycle-ii/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """✅快慢指针判断是否有环，然后通过数学关系实现入口节点的判断
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        slow  = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: #存在环
                # 数字关系分析过程：https://leetcode.cn/problems/linked-list-cycle-ii/solutions/12616/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None

```


### [21. 合并两个有序链表*（双指针）](https://leetcode.cn/problems/merge-two-sorted-lists/)

链表操作还需要熟悉。算法很简单，但代码实现不熟练。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        执行用时分布
        41ms
        击败44.17%使用 Python3 的用户
        消耗内存分布
        16.43MB
        击败54.28%使用 Python3 的用户
        """
        l1 = list1
        l2 = list2
        ans = ListNode(-1)
        prev = ans
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        prev.next = l1 if l1 is not None else l2
        return ans.next
```


### [2. 两数相加](https://leetcode.cn/problems/add-two-numbers)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """✅双指针
        时间复杂度：O(n)
        空间复杂度：O(1)

        执行用时分布
        37ms
        击败98.65%使用 Python3 的用户
        消耗内存分布
        16.53MB
        击败24.73%使用 Python3 的用户
        """
        # """反转链表然后算数运算？"""
        # def rev(head):
        #     prev = None
        #     cur = head
        #     while cur:
        #         next = cur.next
        #         cur.next = prev
        #         prev = cur
        #         cur = next
        #     return prev
        
        # l1_rev = rev(l1)
        # l2_rev = rev(l2)
        # while l1_rev: # check the rev function
        #     print(l1_rev.val)
        #     l1_rev = l1_rev.next

        # """不对啊傻逼了，算数运算就得从个位数开始加啊，不然还的对齐两个数字的数位“”“
        # 双指针指向两个链表并行前进
        ans_head = None
        ans = None
        last_addon = 0
        a = l1
        b = l2
        while a and b:
            temp = a.val+b.val + last_addon
            last_addon = 1 if temp > 9 else 0
            _ans = ListNode(temp%10)
            a = a.next
            b = b.next
            if not ans:
                ans = _ans
                ans_head = _ans
            else:
                ans.next = _ans
                ans = ans.next
        while a:
            temp = a.val + last_addon
            last_addon = 1 if temp > 9 else 0
            _ans = ListNode(temp%10)
            a = a.next
            ans.next = _ans
            ans = ans.next
        while b:
            temp = b.val + last_addon
            last_addon = 1 if temp > 9 else 0
            _ans = ListNode(temp%10)
            b = b.next
            ans.next = _ans
            ans = ans.next
        
        if last_addon:
            _ans = ListNode(last_addon)
            ans.next = _ans
            ans = ans.next
        
        return ans_head




```



### [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

看了官解所谓的一次遍历，有点自欺欺人了，本质上还是遍历了两次。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 朴素解：遍历确认链表长度，再次遍历到n的前一个位置处理链表节点关系
        # 如何一趟遍历实现？那就必须把链表每个节点对应的位置记录下来，空间换时间
        hash_dict = dict() # k = order, value = ref
        i = 0
        p = head
        while p:
            hash_dict[i] = p
            p = p.next
            i += 1  # after last round, i = numbers of linklist
        # 倒数第n个 = 正数第length-n+1个，所以从0开始的话索引值=length-n
        if n == i:
            head = head.next
        else:
            hash_dict[i-n-1].next = hash_dict[i-n].next
        return head
```


### [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """迭代解法：通过两个指针记忆上两个节点位置，通过一个计数判断当前是否偶数位，是则交换当前节点于上一个节点位置"""
        cur = head
        last = last_last = None
        tick = 0
        while cur:
            tick += 1
            if tick == 2:
                # exchange
                last.next = cur.next
                cur.next = last
                if last_last:
                    last_last.next = cur
                else: 
                    head = cur
                cur = last.next
                tick = 0
            else:
                last_last = last
                last = cur
                cur = cur.next
        return head
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """官解的迭代解法：设置一个哑节点，不断处理其后续两个节点。 比自己的解法优雅些，没那么多ifelse"""
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            n1 = temp.next
            n2 = temp.next.next
            temp.next = n2
            n1.next = n2.next
            n2.next = n1
            temp = n1
        return dummy.next
```


### [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

```python
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """用时1小时10分钟...DEBUG了很久，看看题解，应善用哨兵节点
        """

        def rev(_head, _prev, stop_at, point_stop):
            _cur = _head
            while _cur:
                _next = _cur.next
                _cur.next = _prev
                _prev = _cur
                if _cur is stop_at:
                    if point_stop:
                        point_stop.next = _cur
                    return
                _cur = _next

        last_head = cur = head
        prev_tail = None
        count = 0
        while cur:
            count += 1
            next = cur.next

            if count == 1:
                last_head = cur

            if count == k:
                # start reverse
                rev(last_head, next, cur, prev_tail)
                if not prev_tail:
                    head = cur
                prev_tail = last_head
                count = 0

            cur = next

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

    s = Solution()
    ans = s.reverseKGroup(n1, 2)
    while ans:
        print(ans.val)
        ans = ans.next

    # 2 1 4 3 5 
```


### [138. 随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer/)

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    cache = {}
    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """哈希表 + 递归回溯"""
        if not head:
            return None

        if head not in self.cache.keys():
            tmp = Node(head.val)
            self.cache[head] = tmp
            tmp.next = self.copyRandomList(head.next)
            tmp.random = self.copyRandomList(head.random)
        
        return self.cache[head]
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """二次迭代 + 哈希表"""
        p = head
        while p:
            tmp = Node(p.val)
            self.cache[p] = tmp
            p = p.next
        
        p = head
        while p:
            self.cache[p].next = self.cache.get(p.next)
            self.cache[p].random = self.cache.get(p.random)
            p = p.next
        
        return self.cache.get(head)
```


### [148. 排序链表](https://leetcode.cn/problems/sort-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？"""
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1:ListNode, l2:ListNode):
            ans = ListNode(-1)
            cur = ans
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            else:
                cur.next = l2
            return ans.next
        
        def mysort(head, tail):
            """时间：O(nlogn)，空间：O(logn)"""
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                fast = fast.next
                slow = slow.next
                if fast != tail:
                    fast = fast.next
            return merge(mysort(head, slow), mysort(slow, tail))
        
        def mysort_bot_top(head: ListNode):
            """时间：O(nlogn)，空间：O(1)
            自底向上的归并写法，by Krahets
            https://leetcode.cn/problems/sort-list/solutions/13728/sort-list-gui-bing-pai-xu-lian-biao-by-jyd
            """
            h = head
            length, intv = 0, 1
            while h:
                h = h.next
                length += 1 # 求链表长度
            res = ListNode(0)
            res.next = head
            while intv < length:
                pre, h = res, res.next
                while h:
                    h1, i = h, intv
                    while i and h:
                        h, i = h.next, i-1
                    if i: break

                    h2, i = h, intv
                    while i and h:
                        h, i = h.next, i-1
                    
                    # 合并h1与h2
                    c1, c2 = intv, intv-i
                    while c1 and c2:
                        if h1.val < h2.val:
                            pre.next = h1
                            h1 = h1.next
                            c1 -= 1
                        else:
                            pre.next = h2
                            h2 = h2.next
                            c2 -= 1
                        pre = pre.next
                    pre.next = h1 if c1 else h2
                    while c1>0 or c2>0:
                        pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                    pre.next = h
                    
                intv *= 2
            return res.next
        
        # return mysort(head, None)
        return mysort_bot_top(head)
```

### [23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        思路：官解 + https://leetcode.cn/problems/merge-k-sorted-lists/solutions/219756/he-bing-kge-pai-xu-lian-biao-by-leetcode-solutio-2/comments/2092297
        
        一开始往堆里塞的是二元组(node.val, node)，结果push的时候报错，查heapq官方文档：
            > 如果 priority 相同且 task 之间未定义默认比较顺序，则两个 (priority, task) 元组之间的比较会报错。
            > https://docs.python.org/zh-cn/3/library/heapq.html#priority-queue-implementation-notes
        解法文档里也说明了，可以再加一个参数，入堆三元组，其中第二个元素给了个计数值，不断变化即可

        ---
        复杂度分析：
            堆中一共k个元素（k=链表的数量），插入删除O(logk)
            k个链表最多有kn个节点，每个节点插入删除一次，总时间复杂度O(kn * logk)
            空间复杂度：O(k)，堆的空间大小
        """
        ans = ListNode()
        cur = ans
        heads = [h for h in lists if h]
        # print(heads)
        q = []
        cnt = 0
        for head in heads:
            # print(head.val)
            cnt += 1
            heapq.heappush(q, (head.val, cnt, head))
        
        while q:
            node = heapq.heappop(q)
            print(node)
            if node[2].next:
                cnt += 1
                heapq.heappush(q, (node[2].next.val, cnt, node[2].next))
            cur.next = node[2]
            cur = cur.next
        
        return ans.next
```

### [146. LRU 缓存](https://leetcode.cn/problems/lru-cache/)

调试吐血，像官解那样抽象成函数还是有必要的，有两个指针互相转换的过程有依赖，顺序不对导致排查半天。

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0  # 用于判断是否超过容量
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # 哈希表判断是否存在，否返回-1，存在返回并更新链表节点到头节点
        res = self.cache.get(key)
        if res:
            res.prev.next = res.next
            res.next.prev = res.prev

            res.next = self.head.next
            res.prev = self.head
            self.head.next.prev = res
            self.head.next = res

            return res.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            print('not hit')
            # 新增节点
            node = Node(key, value)
            self.cache[key] = node
            # 放到头部
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            # 判断容量，已经满了则删除末尾节点
            if self.size == self.capacity:
                self.cache.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail # 先这个
                self.tail.prev = self.tail.prev.prev # 再这个！反过来是不行的
            else:
                self.size += 1
        else:
            print('hit')
            node = self.cache[key]
            node.val = value
            # 放到头部（放置前先移除原关系）
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

        print(self.cache)

if __name__ == '__main__':
    obj = LRUCache(10)
    input = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    for i in input:
        if len(i) == 2:
            obj.put(i[0], i[1])
        else:
            obj.get(i[0])
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

## 二叉树

二叉树很久没接触了，实现下三种遍历复习下（着重注意后序遍历的非递归写法，从头实现有点绕）：

```python
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def setL(self, treeNode):
        self.left = treeNode

    def setR(self, treeNode):
        self.right = treeNode


# 先序遍历 递归
def preorder_recur(node: TreeNode):
    if node:
        print(node.val, end='')
        preorder_recur(node.left)
        preorder_recur(node.right)
    return


# 先序遍历 迭代
def preorder_non_recur(node: TreeNode):
    stack = []
    cur = node
    while stack or cur:
        if cur:
            print(cur.val, end='')
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop().right


# 中序遍历 递归
def inorder_recur(node: TreeNode):
    if node:
        inorder_recur(node.left)
        print(node.val, end='')
        inorder_recur(node.right)
    return


# 中序遍历 迭代
def inorder_non_recur(node: TreeNode):
    stack = []
    cur = node
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print(cur.val, end='')
            cur = cur.right


# 后序遍历 递归
def postorder_recur(node: TreeNode):
    if node:
        postorder_recur(node.left)
        postorder_recur(node.right)
        print(node.val, end='')
    return


# 后序遍历 递归
def postorder_non_recur(node: TreeNode):
    stack = []
    cur = node
    last_visited = None
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack[-1]
            if cur.right and cur.right != last_visited:
                cur = cur.right
            else:
                cur = stack.pop()
                print(cur.val, end='')
                last_visited = cur
                cur = None


if __name__ == '__main__':
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')

    a.setL(b)
    a.setR(c)
    c.setL(d)
    c.setR(e)

    print("先序遍历_递归：", end='')
    preorder_recur(a)
    print("\n先序遍历_迭代：", end='')
    preorder_non_recur(a)

    print("\n中序遍历_递归：", end='')
    inorder_recur(a)
    print("\n中序遍历_迭代：", end='')
    inorder_non_recur(a)

    print("\n后序遍历_递归：", end='')
    postorder_recur(a)
    print("\n后序遍历_迭代：", end='')
    postorder_non_recur(a)

# 先序遍历_递归：abcde
# 先序遍历_迭代：abcde
# 中序遍历_递归：badce
# 中序遍历_迭代：badce
# 后序遍历_递归：bdeca
# 后序遍历_迭代：bdeca
```


### [94. 二叉树的中序遍历*](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """✅借助栈实现非递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        递归实现更简单跳过；还有个优化空间复杂度的解法参考官解：https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/412886/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/
        """
        stack = []
        p = root
        ans = []
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                ans.append(p.val)
                p = p.right
        return ans
```


### [104. 二叉树的最大深度*](https://leetcode.cn/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-100-**liked**)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        # 分治、递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 层序遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return 0
        queue = [root]
        ans = 0
        while queue:
            # p = queue.pop(1)
            temp = []
            for p in queue:
                # visit node, no need here
                if p.left: temp.append(p.left)
                if p.right: temp.append(p.right)
            queue = temp
            ans += 1
        return ans
```


### [226. 翻转二叉树*](https://leetcode.cn/problems/invert-binary-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """后序遍历，每次对调根节点的左右子树"""
        stack = []
        p = root
        last = None
        while stack or p:
            if p:
              stack.append(p)
              p = p.left
            else:
                p = stack[-1].right
                if p and p != last:
                    continue
                else:
                    p = stack.pop()
                    # do something
                    p.left, p.right = p.right, p.left
                    last = p
                    p = None
        return root
```


### [101. 对称二叉树*](https://leetcode.cn/problems/symmetric-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """非递归实现：层序遍历，对于每一层使用双指针判断是否对称
        """
        if not root:
            return True

        queue = [root]
        p = None
        while queue:
            temp = []
            for_test = []
            for item in queue:
                if item.left:
                    temp.append(item.left)
                    for_test.append(item.left.val)
                else:
                    for_test.append("")

                if item.right:
                    temp.append(item.right)
                    for_test.append(item.right.val)
                else:
                    for_test.append("")

            # 判断temp是否回文
            print(for_test)
            l, r = 0, len(for_test)-1
            while l < r:
                if for_test[l] != for_test[r]:
                    return False
                l += 1
                r -= 1

            queue = temp
        
        return True
```


### [543. 二叉树的直径*](https://leetcode.cn/problems/diameter-of-binary-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._max = 1 # 题目限制节点至少1个

        def depth(node):
            if node is None:
                return 0

            l = depth(node.left)
            r = depth(node.right)
            self._max = max(self._max, l+r+1)
            return max(l, r)+1
        
        depth(root)
        return self._max-1
```


### [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        ans = []
        while queue:
            temp = []
            _ans = []
            for n in queue:
                _ans.append(n.val)
                if n.left: temp.append(n.left)
                if n.right: temp.append(n.right)
            ans.append(_ans)
            queue = temp
        return ans
```


### [108. 将有序数组转换为二叉搜索树*](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/)

二叉搜索树：https://zh.wikipedia.org/zh-cn/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(l, r):
            if l>r: return None

            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = bst(l, mid-1)
            root.right = bst(mid+1, r)

            return root
        
        return bst(0, len(nums)-1)
```


### [98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 递归+先序遍历，参考官解
        def preorder(_root, lower, upper):
            if not _root:
                return True
            
            # visit & check
            if _root.val <= lower or _root.val >= upper:
                return False

            # go on
            if not preorder(_root.left, lower, _root.val):
                return False
            if not preorder(_root.right, _root.val, upper):
                return False
            return True
        
        return preorder(root, float('-inf'), float('inf'))
```


### [230. 二叉搜索树中第K小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)

答案已经在数据结构的基本操作中了。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0
        while root or stack:
            # checkin all left
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            # checkout
            count += 1
            if count == k:
                return root.val
            
            # checkin all right
            root = root.right
```


### [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """思路：层序遍历，打印每一层最后一个节点值"""
        if not root:
            return []

        q = [root,]
        mid_q = []
        ans = []

        while q:
            tmp = q.pop(0)
            if tmp.left: mid_q.append(tmp.left)
            if tmp.right: mid_q.append(tmp.right)
            if not q: # 说明tmp是队列里最后一个元素
                ans.append(tmp.val)
                q = mid_q
                mid_q = []
        return ans
    

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        """
        可以使用collections模块中的deque，上面使用list模拟队列pop(0)的耗时是O(n)
        """
        if not root:
            return []

        q = deque([root,])
        mid_q = []
        ans = []

        while q:
            tmp = q.popleft()
            if tmp.left: mid_q.append(tmp.left)
            if tmp.right: mid_q.append(tmp.right)
            if not q: # 说明tmp是队列里最后一个元素
                ans.append(tmp.val)
                q = deque(mid_q)
                mid_q = []
        return ans
```


### [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten1(self, root: Optional[TreeNode]) -> None:
        """时间与空间复杂度都是O(n)
        """
        stack = []
        store = []
        cur = root
        while stack or cur:
            if cur:
                print(cur.val)
                store.append(cur)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop().right
        
        for i in range(len(store)-1):
            store[i].left = None
            store[i].right = store[i+1]
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """官解迭代找前缀，时间O(n),空间优化到了O(1)"""
        cur = root
        while cur:
            if cur.left:
                tmp = cur.left
                conn = tmp
                while conn.right:
                    conn = conn.right
                conn.right = cur.right
                cur.left = None
                cur.right = tmp
            cur = cur.right
```


### [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """没写出来，学习下官解 递归解法
        
        核心算法依据如下特征：
        前序遍历：[ 根节点, [左子树的前序遍历结果], [右子树的前序遍历结果] ]
        中序遍历：[ [左子树的中序遍历结果], 根节点, [右子树的中序遍历结果] ]

        每一轮：通过中序遍历从前序中确认[左子树的前序遍历结果]、[右子树的前序遍历结果]，然后递归对其继续解析，每次递归返回一个子树根节点作为当前层节点的子节点
        递归结束条件：？？ 见下面递归函数里的自问自答
        """
        
        hashtable = {node: i for i, node in enumerate(inorder)}  # 字典推导式（dictionary comprehension）一行构造hash表，消耗O(n)，题目规定了node不重复
        n = len(preorder)

        # 递归函数
        def _build(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
            # if inorder_left > inorder_right:
                # Q~这里的结束条件为啥这样写？
                # A~[preorder_left, preorder_right] 这个区间实际代表着子树本身，若子树左边界大于有边界了说明子树不成立了，返回None
                # Q~为什么用preorder判断？用inorder是否可以？
                # A~可以的，含义同上
                # Q~改成大于等于可不可以？
                # A～不可，等于的情况说明子树成立，需要创建一个root节点用于返回，而这个操作在下面代码里。
                return None
            
            # 接上面最后的QA，这里可以单独加个判断若等于则直接返回一个TreeNode，是可以Pass的。
            # 增加了一行通用判断然后在叶子节点上节省了两次递归调用。
            if preorder_left == preorder_right:
                return TreeNode(preorder[preorder_left])

            preorder_root = preorder_left # 前序遍历第一个节点一定是跟节点
            inorder_root = hashtable[preorder[preorder_root]] # 借助哈希表O(1)消耗定位跟节点在中序遍历中的位置

            # 创建根节点
            root = TreeNode(preorder[preorder_root])
            # 子树长度
            size_of_left = inorder_root - inorder_left  # [0*left, 1, 2, 3, 4*root, 5, 6, 7, 8 ]
            # 递归处理左子树
            root.left = _build(preorder_left + 1, preorder_left + size_of_left, inorder_left, inorder_root - 1)
            # 递归处理右子树
            root.right = _build(preorder_left + size_of_left + 1, preorder_right, inorder_root+1, inorder_right)
            # 返回根节点
            return root
        
        return _build(0, n-1, 0, n-1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """迭代解法
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root] # 当前节点的所有还没有考虑过右儿子的祖先节点, 栈顶等于当前节点
        inorder_idx = 0
        for i in range(1, len(preorder)):
            preorder_val = preorder[i]
            node = stack[-1] # 回忆：栈可以直接用list，队列最好用collections.deque，用list操作队首耗时O(n)
            if node.val != inorder[inorder_idx]:
                node.left = TreeNode(preorder_val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_idx]:
                    node = stack.pop()
                    inorder_idx += 1
                node.right = TreeNode(preorder_val)
                stack.append(node.right)
        return root
```


### [112. 路径总和*](https://leetcode.cn/problems/path-sum/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """❌DFS累加每个节点值，每到叶子节点时判断当前累加值是否符合target，回溯时减掉当前节点值
        值扣减条件比较麻烦
        """
        amt = 0
        stack = []
        cur = root
        last_amt = 0
        while stack or cur:
            if cur:
                amt += cur.val
                last_amt = cur.val
                stack.append(cur)

                # print(cur.val, last_amt, amt)
                if not cur.left and not cur.right:
                    if amt == targetSum: return True
                
                cur = cur.left
            else:
                cur = stack.pop().right
                amt -= last_amt  # 这里有问题，还要区分情况进行扣减，再进行特殊判断代码就写的思路太不简洁了，换种写法吧
                last_amt = 0
            # print(amt, last_amt)
        return False
    
    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """BFS借助双队列求和"""
        if not root:
            return False
        que_node = deque([root])
        que_val = deque([root.val])
        while que_node:
            node = que_node.popleft()
            val = que_val.popleft()
            if node.left is node.right: #都为None才成立
                if val == targetSum:
                    return True
                continue
            if node.left:
                que_node.append(node.left)
                que_val.append(val + node.left.val)
            if node.right:
                que_node.append(node.right)
                que_val.append(val + node.right.val)
        return False
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 递归，sum减为0且为叶子节点则命中
        if not root:
            return False
        if root.left is root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
```

### [437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/)

再遇到就能做出来了吗？

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 菜是原罪
        
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(root, cur):
            if not root:
                return 0
            
            ret = 0
            cur += root.val
            ret += prefix[cur - targetSum]
            prefix[cur] += 1
            ret += dfs(root.left, cur)
            ret += dfs(root.right, cur)
            prefix[cur] -= 1

            return ret
        
        return dfs(root, 0)
```

### [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

分析所有的可能场景，分析逐步处理过程，形式化总结。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if not root:
                return None
            if root is p or root is q:
                return root
            
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)

            if l and r:
                return root
            if l and not r:
                return l
            if r and not l:
                return r
        return dfs(root, p, q)
```

### [124. 二叉树中的最大路径和**](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float("-inf") # 所有数都比无穷小float("-inf")大，所有数都比无穷大float("inf")小

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)

            self.ans = max(self.ans, root.val+l+r)

            return max(l, r)+root.val
        dfs(root)
        return self.ans
```


## 图论


### [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 题解（非常清晰）：https://leetcode.cn/problems/number-of-islands/solutions/211211/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-
        
        # m 行 n 列
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            # 边界判断
            if c < 0 or n <= c or r < 0 or m <= r:
                return

            # 岛屿判断
            if grid[r][c] != "1":
                return
            
            grid[r][c] = "2"

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                # print(i, j,grid[i][j], grid)
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
```

### [463. 岛屿的周长](https://leetcode.cn/problems/island-perimeter/)

继上一题岛屿数量，DFS代码可以复用。

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # m 行 n 列
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            # 边界判断，遇到边界确认一条边
            if c < 0 or n <= c or r < 0 or m <= r:
                return 1

            # 海洋判断，遇到海洋确认一条边
            if grid[r][c] == 0:
                return 1
            
            # 对结果无影响的节点返回
            if grid[r][c] != 1:
                return 0

            grid[r][c] = 2

            return dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)
```


### [994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/)

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """题解：https://leetcode.cn/problems/rotting-oranges/solutions/129831/li-qing-si-lu-wei-shi-yao-yong-bfsyi-ji-ru-he-xie-
        利用队列执行广度优先搜索
        初始化队列为所有的腐烂橘子坐标，每轮将队列处理完毕后再将下一波的腐烂橘子入队，最后一波处理完检查是否还有好橘子
        """
        m, n = len(grid), len(grid[0])
        queue = []
        tmp_queue = [] # 用于存储下一轮被感染的橘子，区分每轮的轮次方便计算时间
        ans = 0 # 轮次
        good = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    queue.append((x,y))
                elif grid[x][y] == 1:
                    good += 1
        # print(queue, good)

        while queue or tmp_queue:
            if not queue: # 一轮感染完成，进入下一轮感染
                ans += 1
                queue = tmp_queue
                tmp_queue = []
            else: # 感染四周，并将被感染的橘子坐标放入tmp_queue
                cur = queue.pop(0)
                x, y = cur[0], cur[1]

                # if x-1 >= 0 and grid[x-1][y] == 1:
                #     grid[x-1][y] = 2
                #     tmp_queue.append((x-1, y))
                #     good -= 1
                # if x+1 < m and grid[x+1][y] == 1:
                #     grid[x+1][y] = 2
                #     tmp_queue.append((x+1, y))
                #     good -= 1
                # if y-1 >= 0 and grid[x][y-1] == 1:
                #     grid[x][y-1] = 2
                #     tmp_queue.append((x, y-1))
                #     good -= 1
                # if y+1 < n and grid[x][y+1] == 1:
                #     grid[x][y+1] = 2
                #     tmp_queue.append((x, y+1))
                #     good -= 1

                # 简写上述四个if为for循环
                for x,y in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if x>=0 and y>=0 and x<m and y<n and grid[x][y]==1:
                        grid[x][y] = 2
                        tmp_queue.append((x,y))
                        good -= 1
        return ans if good == 0 else -1
```


### [207. 课程表](https://leetcode.cn/problems/course-schedule/)

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS：https://leetcode.cn/problems/course-schedule/solutions/18806/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa

        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        q = collections.deque()

        # 统计每个课程的入度 && 初始化邻接表
        for a, b in prerequisites:
            indegrees[a] += 1
            adj[b].append(a)

        # 初始化任务队列，所有入度为0的入队
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            pre = q.popleft()
            numCourses -= 1
            # 每次学完一门课将相关后置课程入度-1
            for course in adj[pre]:
                indegrees[course] -= 1
                # 若入度减到0则可以开始学习，入队
                if indegrees[course] == 0:
                    q.append(course)

        return numCourses == 0
```


### [208. 实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/)

```python
class Trie:

    def __init__(self):
        self.children = [None]*26
        self.is_end = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = Trie()
            cur = cur.children[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.is_end


    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

## 回溯

> 回溯算法（backtracking algorithm）是一种通过穷举来解决问题的方法，它的核心思想是从一个初始状态出发，暴力搜索所有可能的解决方案，当遇到正确的解则将其记录，直到找到解或者尝试了所有可能的选择都无法找到解为止。
> 回溯算法通常采用“深度优先搜索”来遍历解空间。
> 
> https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/


> 回溯三问：当前操作？子问题？下一个子问题？
>
> 子集型回溯：选或不选、选哪一个 两种思路
> 组合型回溯：子集问题+剪枝
> 排列型回溯：与组合型的区别在于不需要过滤重复；全排列、N皇后
> 
> [灵茶山艾府 - 回溯算法套路](https://www.bilibili.com/video/BV1mG4y1A7Gu)

### [46. 全排列](https://leetcode.cn/problems/permutations)

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """回溯
        1、定义解空间、确定易于搜索的解空间结构
        2、DFS搜索，剪枝优化

        refer: https://www.bilibili.com/video/BV1mY411D7f6
        """
        n = len(nums)
        ans = []
        path = [0]*n
        def dfs(i, s):
            """
            i: 当前选择了多少个数字，若i=n,则排列完成
            s: 剩余未选择的数字
            """

            if i == n:
                ans.append(path.copy())
                return
            
            for x in s:
                path[i] = x
                dfs(i+1, s-{x})
            
        dfs(0, set(nums))
        return ans
```


### [78. 子集](https://leetcode.cn/problems/subsets/)

```python
class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """选或不选"""
        ans = []
        n = len(nums)
        path = []

        def dfs(i):
            # 边界
            if i==n:
                ans.append(path.copy())
                return

            # 不选
            dfs(i+1)

            # 选
            path.append(nums[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """选哪一个"""
        ans = []
        n = len(nums)
        path = []

        def dfs(i):
            # 保存当前结果
            ans.append(path.copy())
            
            for j in range(i, n):
                # 选下一个数
                path.append(nums[j])
                dfs(j+1)
                path.pop()

        dfs(0)
        return ans
```


### [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        M = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if digits == '':
            return []
        
        n = len(digits)
        ans = []
        path = ['']*n

        def dfs(i):
            """第i个数字选哪一个"""
            # print(i, path)

            # 边界条件
            if i == n:
                ans.append(''.join(path))
                return
            
            # 挨个选一遍
            for c in M[int(digits[i])]:
                path[i] = c
                dfs(i+1)
                # path[i] = '' # 这里恢复现场没必要，因为总会被覆盖，可以结合前面打印与这里是否恢复现场来理解恢复现场做的操作
        
        dfs(0)
        return ans
```


### [39. 组合总和](https://leetcode.cn/problems/combination-sum/)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        path = []
        ans = []
        n = len(candidates)

        def dfs(i):
            # 边界
            if sum(path) > target:
                return
            # 答案
            if sum(path) == target:
                ans.append(path.copy())
                return
            # 递归
            for j in range(i, n):
                path.append(candidates[j])
                dfs(j)
                path.pop()
        dfs(0)
        return ans
```


### [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/)

跟着代码思路把二叉搜索树走一遍，就能很好的理解代码思路了。

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        m = n*2
        state = []
        ans = []

        def dfs(i, l_brackets):

            if i == m:
                ans.append(''.join(state))
                return

            # 选左括号
            if l_brackets < n:
                state.append('(')
                dfs(i+1, l_brackets+1)
                state.pop()

            # 选右括号
            if i - l_brackets < l_brackets:
                state.append(')')
                dfs(i+1, l_brackets)
                state.pop()
        dfs(0, 0)
        return ans
```


### [77. 组合](https://leetcode.cn/problems/combinations/)

```python
class Solution:
    def combine1(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            # 剪枝：剩余的数不足以凑成k个数字则直接返回
            if i < k-len(path):
                return

            if len(path) == k:
                ans.append(path.copy())
                return

            for j in range(i, 0, -1):
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n) # 倒序枚举
        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            # 剪枝
            need = k - len(path)
            if n - i + 1 < need: return

            if len(path) == k:
                ans.append(path.copy())
                return

            for j in range(i, n+1):
                path.append(j)
                dfs(j+1)
                path.pop()
        dfs(1) # 正序枚举
        return ans
```


### [79. 单词搜索](https://leetcode.cn/problems/word-search/)

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """题解：https://leetcode.cn/problems/word-search/solutions/2361646/79-dan-ci-sou-suo-hui-su-qing-xi-tu-jie-5yui2"""
        m, n = len(board), len(board[0])

        # 统计起始坐标
        start = []
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    start.append((r,c))

        # 定义dfs(i,j,k)为第k步选择的字母坐标(i,j)
        def dfs(i, j, k):
            if i<0 or j<0 or i==m or j==n or board[i][j] != word[k]:
                return False
            if k == len(word)-1 and board[i][j] == word[k]:
                return True
                
            board[i][j] = ''
            res = dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            board[i][j] = word[k]
            return res

        # 任意起点能够命中word，则返回True
        for x, y in start:
            if dfs(x, y, 0): return True
        return False
```


### [131. 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/)

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        path = []
        n = len(s)

        def dfs(i): # 当前字母是否作为结束位置
            
            if i == n:
                ans.append(path.copy())
                return

            for j in range(i, n):
                cur = s[i:j+1]
                if cur == cur[::-1]: # 把j作为当前字符结尾时子串是回文串，才往下递归，不然j++
                    path.append(cur)
                    # print(i, j, path)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans
```


### [51. N 皇后**](https://leetcode.cn/problems/n-queens/)

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0]*n # 每行的皇后列坐标
        col_used = [False]*n
        m = 2*n-1
        RpC_used = [False]*m
        RsC_used = [False]*m

        def dfs(r):
            if r == n:
                ans.append(['.'*c + 'Q' + '.'*(n-1-c) for c in col])
                return
            for c in range(n): # 在第r行枚举每一列
                if not col_used[c] and not RpC_used[r+c] and not RsC_used[r-c]: # 判断当前位置是否可以放皇后
                    col[r] = c # 在第r行第c列放皇后
                    col_used[c] = RpC_used[r+c] = RsC_used[r-c] = True
                    dfs(r+1) # 处理下一行
                    col_used[c] = RpC_used[r+c] = RsC_used[r-c] = False
        dfs(0)
        return ans
```

## 二分查找

### [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/)

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """✅二分
        时间复杂度：O(logn)
        空间复杂度：O(1)
        """
        n = len(nums)
        l, r = 0, n-1
        ans = n
        while l <= r:
            mid = round((r - l)/2 + l)
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
```


### [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """把有序数组等m分拆成了n列矩阵"""
        m,n = len(matrix),len(matrix[0])
        l,r = 0, m*n-1
        while l<=r:
            idx = (r+l)//2
            idx_r = idx//n
            idx_c = idx%n
            mid_num = matrix[idx_r][idx_c]
            print(l, r, idx, idx_r, idx_c, mid_num)
            if mid_num == target:
                return True
            elif mid_num < target:
                l = idx+1
            else:
                r = idx-1
        return False
```


### [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

```python
class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        """
        二分查找未命中，直接返回[-1,-1]
        二分查找命中目标值:有可能左右有重复值，双指针向左右拓展到非目标值后，返回[l+1,r-1]
        """
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            cur = (l+r)//2
            if nums[cur] > target:
                r = cur-1
            elif nums[cur] < target:
                l = cur+1
            else:
                # 开始拓展
                l = cur-1
                r = cur+1
                while l >= 0 and nums[l] == target:
                    l -= 1
                while r < n and nums[r] == target:
                    r += 1
                return [l+1, r-1]
        return [-1, -1]
        # 最坏情况所有数字都是target，时间复杂度劣化为O(n)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """官解，通过两轮二分寻找两个下标，左右两个下标的特征要处理好"""
        def binary_s(_nums, _target, find_most_left):
            n = len(_nums)
            l, r = 0, n-1
            ans = n
            while l<=r:
                cur = (l+r)//2
                if _nums[cur] > _target or (find_most_left and _nums[cur] >= _target):
                    r = cur-1
                    ans = cur
                elif _nums[cur] <= _target:
                    l = cur+1
            return ans
        
        ll = binary_s(nums,target, True)
        rr = binary_s(nums,target, False)-1
        if ll <= rr and rr < len(nums) and nums[ll]==target and nums[rr]==target:
            return [ll, rr]

        return [-1, -1]
```


### [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """关键：一分为二后一定有一半有序
        """
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] <= nums[-1]: # 右侧有序判断
                    if nums[mid] < target <= nums[-1]:
                        l = mid+1
                    else:
                        r = mid-1
                else: # 左侧有序
                    if nums[mid] > target >= nums[l]:
                        r = mid-1
                    else:
                        l = mid+1
        return -1
```


### [153. 寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/)

```python
class Solution:
    def findMin1(self, nums: List[int]) -> int:
        """个人解，找规律"""
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] >= nums[0] and nums[m] > nums[-1]: # ordered left, unordered right
                l = m+1
            elif nums[m] <= nums[0] and nums[m] < nums[-1]: # ordered right, unordered left
                r = m-1
            else:
                break
        return nums[l]
    
    def findMin(self, nums: List[int]) -> int:
        """官解，更清晰的规律"""
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        return nums[l]
```

### [4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/)

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """官解思路，将寻找中位数转换为寻找作为第K小的数，二分法迫近第K小的数"""
        def getkth(k):
            offset1 = offset2 = 0
            while True:

                # special
                if offset1 == m:  # nums1均被排除时，直接返回nums2中第k小的数
                    return nums2[offset2 + k -1]
                if offset2 == n:  # 同上
                    return nums1[offset1 + k -1]
                if k == 1:
                    return min(nums1[offset1], nums2[offset2])

                # default
                newoffset1 = min(offset1+k//2-1, m-1)
                newoffset2 = min(offset2+k//2-1, n-1)
                if nums1[newoffset1] <= nums2[newoffset2]:
                    k -= newoffset1 - offset1 + 1
                    offset1 = newoffset1 + 1
                else:
                    k -= newoffset2 - offset2 + 1
                    offset2 = newoffset2 + 1
        
        m, n = len(nums1), len(nums2)
        count = m+n
        if (count)%2 == 1:
            return getkth((count+1)//2)
        else:
            return (getkth(count//2) + getkth(count//2+1))/2
```


## 栈

> 栈（Stack）是一种满足后进先出（LIFO）逻辑的数据结构，而单调栈实际上就是在栈的基础上增加单调的性质（单调递增或单调递减）
> 
> 单调栈是一种特别适合解决 “下一个更大元素” 问题的数据结构。
> 
> > [使用单调栈解决 “下一个更大元素” 问题](https://mdnice.com/writing/b5cd53ce22c14069b63c6d5d3ad41bd9)


### [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/)

```python
class Solution:
    def isValid1(self, s: str) -> bool:
        """✅栈基础应用

        执行用时分布
        40ms
        击败46.16%使用 Python3 的用户
        消耗内存分布
        16.42MB
        击败45.84%使用 Python3 的用户
        """
        ss = []
        for _ in s:
            if _ in ['(','{','[']:
                ss.append(_)
            elif len(ss) > 0:
                last = ss.pop()
                if _ == ')' and last == '(':continue
                if _ == '}' and last == '{':continue
                if _ == ']' and last == '[':continue
                return False
            else:
                return False
        return True if len(ss) == 0 else False
    
    def isValid(self, s: str) -> bool:
        """✅引入哈希表降低匹配括号的复杂度
        
        执行用时分布
        32ms
        击败89.12%使用 Python3 的用户
        消耗内存分布
        16.51MB
        击败18.70%使用 Python3 的用户
        
        这个耗时本来就不多，多次提交波动很明显
        """
        hashdict = {'(':')', '[':']', '{':'}'}
        ss = []
        for x in s:
            # 左括号入栈
            if x in hashdict.keys():
                ss.append(x)
                continue
            # 右括号出栈
            if len(ss) > 0:
                last = ss.pop()
                if hashdict[last] == x:
                    continue
            
            # 未入栈也未匹配则失败
            return False
        return True if len(ss) == 0 else False
```

### [155. 最小栈](https://leetcode.cn/problems/min-stack/)

使用辅助栈实现`常数时间内检索到最小元素`

```python
class MinStack1:
    """✅朴素解，pop操作因为做了遍历时间复杂度O(N)

    执行用时分布
    58ms
    击败40.95%使用 Python3 的用户
    消耗内存分布
    19.99MB
    击败64.40%使用 Python3 的用户
    """

    def __init__(self):
        self._min = None # 存储最小值，pop与push时都需要更新
        self.ss = []
        self.length = 0


    def push(self, val: int) -> None:
        self.length += 1
        self.ss.append(val)
        if self._min is None or val < self._min: self._min = val

    def pop(self) -> None:
        self.length -= 1
        last_pop = self.ss[self.length]
        del self.ss[self.length]

        # 更新最小值
        if last_pop == self._min:
            self._min = None
            for idx, x in enumerate(self.ss):
                if idx == 0 or x < self._min: 
                    self._min = x
                

    def top(self) -> int:
        return self.ss[self.length - 1]


    def getMin(self) -> int:
        return self._min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack2:
    """✅使用辅助栈优化寻找min的时间复杂度

    执行用时分布
    51ms
    击败77.69%使用 Python3 的用户
    消耗内存分布
    20.04MB
    击败49.47%使用 Python3 的用户
    """

    def __init__(self):
        self.min_stack = []
        self.stack = []
        self.length = 0


    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.length > 0:
            last_min = self.min_stack[self.length-1]
            if val < last_min:
                self.min_stack.append(val)
            else: 
                self.min_stack.append(last_min)
        else: 
            self.min_stack.append(val)

        self.length += 1


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.length -= 1


    def top(self) -> int:
        if self.length > 0:
            return self.stack[self.length-1]
        else:
            return None

    def getMin(self) -> int:
        if self.length > 0:
            return self.min_stack[self.length-1]
        else:
            return None

class MinStack:
    """✅优雅些，效率没太多区别"""

    def __init__(self):
        self.min_stack = [math.inf]
        self.stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

### [394. 字符串解码](https://leetcode.cn/problems/decode-string/)


```python
class Solution:
    def decodeString1(self, s: str) -> str:
        """❌两个栈，读题不仔细，没处理嵌套的情况"""

        num_stack = []
        patten_stack = []
        ans = ''

        for c in s:
            order = ord(c)
            if order > ord('0') and order <= ord('9'):
                num_stack.append(c)
            elif order == ord('['):
                pass
            elif order == ord(']'): # 输出，清空栈
                count = int(''.join(num_stack))
                ans += ''.join(patten_stack) * count
                patten_stack = []
                num_stack = []
            else: # 字母入模式栈
                patten_stack.append(c)
        return ans
    

    def decodeString2(self, s: str) -> str:
        """✅BUG FIX

        执行用时分布
        37ms
        击败56.43%使用 Python3 的用户
        消耗内存分布
        16.43MB
        击败24.32%使用 Python3 的用户
        """
        num_stack = []
        patten_stack = []
        ans = ''
        current_patten = ''

        for c in s:
            order = ord(c)
            if order >= ord('0') and order <= ord('9'):
                num_stack.append(c)
            elif order == ord('['):
                patten_stack.append(''.join(num_stack))
                num_stack = []
                patten_stack.append(c)
            elif order == ord(']'):
                last_pop = patten_stack.pop()
                while last_pop != '[':
                    current_patten += last_pop # 注意这里出栈拼接出来的字符串还需要反转
                    last_pop = patten_stack.pop()
                
                current_patten = int(patten_stack.pop()) * current_patten[::-1]
                for _ in current_patten:
                    patten_stack.append(_)
                current_patten = ''
            else:
                patten_stack.append(c)

            print(patten_stack)
        
        ans = ''.join(patten_stack)
        return ans


    def decodeString(self, s: str) -> str:
        """✅优化，栈里不存字符，而是存字符串

        执行用时分布
        31ms
        击败90.22%使用 Python3 的用户
        消耗内存分布
        16.42MB
        击败26.47%使用 Python3 的用户
        """
        num_stack = []
        patten_stack = []
        current_patten = ''
        current_num = ''

        for c in s:
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                current_num += c
            elif ord(c) == ord('['):
                num_stack.append(current_num)
                patten_stack.append(current_patten)
                current_patten = ''
                current_num = ''
            elif ord(c) == ord(']'):
                temp = patten_stack.pop()
                current_patten = temp + int(num_stack.pop()) * current_patten
            else:
                current_patten += c
        return current_patten
```

### [739. 每日温度（单调栈）](https://leetcode.cn/problems/daily-temperatures/)

```python
class Solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        """✅单调栈存储还没有遇到更高温度的日期坐标，栈中日期对应温度单调递减
        """
        length = len(temperatures)
        ans = [0] * length
        s = [0, ]
        for i in range(1, length):
            while temperatures[i] > temperatures[s[-1]]:
                ans[s[-1]] = i - s[-1]
                s.pop()
                if len(s) == 0:
                    break
            s.append(i)

        for _ in s:
            ans[_] = 0

        return ans


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """✅单调栈，语法优化
        """
        length = len(temperatures)
        ans = [0] * length

        s = [0, ]
        for i in range(1, length):
            while s and temperatures[i] > temperatures[s[-1]]:
                prev_idx = s.pop()
                ans[prev_idx] = i - prev_idx
            s.append(i)

        return ans
```

### [496. 下一个更大元素 I*（单调栈）](https://leetcode.cn/problems/next-greater-element-i/)

这道题用单调栈+哈希表的写法不算Easy题目了，比每日温度要复杂。

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """单调栈 + 哈希表

        执行用时分布
        35ms
        击败87.58%使用 Python3 的用户
        消耗内存分布
        16.60MB
        击败63.09%使用 Python3 的用户

        大的框架基本是最优思路了
        """
        length = len(nums2)
        stack = []
        mid_ans = [-1] * length
        mid_ans_dict = {}
        ans = []

        # 单调栈：构建nums2的每个坐标的下一个最大值坐标
        for i in range(length):
            while stack and nums2[i] > nums2[stack[-1]]:
                p = stack.pop()
                mid_ans[p] = i - p
            stack.append(i)
        # print(mid_ans)

        # 哈希表：对nums1的每个坐标进行匹配
        for idx, x in enumerate(mid_ans):
            # print(idx, nums2[idx], x)
            mid_ans_dict[nums2[idx]] = nums2[idx + x] if x != -1 else -1
        for _ in nums1:
            ans.append(mid_ans_dict[_]) 
        
        return ans
```



### [503. 下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/)

```python
class Solution:
    def nextGreaterElements1(self, nums: List[int]) -> List[int]:
        """✅单调栈，与I不同的在于循环数组，解法是直接把数组长度*2即可，另外不再需要哈希表
        
        执行用时分布
        66ms
        击败67.19%使用 Python3 的用户
        消耗内存分布
        18.73MB
        击败8.64%使用 Python3 的用户
        """

        ans = []
        l = len(nums)
        mid_ans = [-1] * l * 2
        mid_nums = nums + nums 
        stack = []
        for i in range(l*2):
            while stack and mid_nums[i] > mid_nums[stack[-1]]:
                prev = stack.pop()
                mid_ans[prev] = i - prev
            stack.append(i)
        # print(mid_ans)
        
        for i in range(l):
            ans.append(-1 if mid_ans[i] == -1 else mid_nums[i + mid_ans[i]])
        return ans
        
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """✅优化，单调栈处理过程直接往存答案即可，不用先存坐标再处理一遍
        
        执行用时分布
        49ms
        击败98.54%使用 Python3 的用户
        消耗内存分布
        18.48MB
        击败18.50%使用 Python3 的用户
        """

        l = len(nums)
        ans = [-1] * l * 2
        mid_nums = nums + nums 
        stack = []
        for i in range(l*2):
            while stack and mid_nums[i] > mid_nums[stack[-1]]:
                ans[stack.pop()] = mid_nums[i]
            stack.append(i)

        return ans[:l]
```


### [84. 柱状图中最大的矩形**（单调栈）](https://leetcode.cn/problems/largest-rectangle-in-histogram/)

```python
class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        """❌单调栈，从一个坐标开始单调递增的连续最大区间则是从该坐标高度开始能组成的最大矩形

        解答错误
        53 / 99 个通过的测试用例
        heights = [2,1,2]， 输出 = 2， 预期 = 3

        只考虑了向右延伸，没有考虑向左延伸
        """
        stack =[]
        length = len(heights)
        less_next = [0]*length

        # 通过单调栈为每个height确定下一个更小值的位置
        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:
                prev = stack.pop()
                less_next[prev] = i - prev
            stack.append(i)
        # 注意处理栈内还剩的元素，约定输入的heights之后为负无穷
        # 方便后续以这些坐标为起点计算矩形面积
        while stack:
            prev = stack.pop()
            less_next[prev] = length - prev
        print(less_next)

        max_area = 0
        for i, height in enumerate(heights):
            print(max_area)
            print(i, height, less_next[i])
            max_area = max(max_area, height*(less_next[i]))
        return max_area


    def largestRectangleArea2(self, heights: List[int]) -> int:
        """✅BUG_FIX 单调栈*2，一个从左往右，一个从右往左

        NOTE：处理stack时候左侧、右侧虚拟的无穷小的那根柱子，被称为`哨兵`

        执行用时分布
        288ms
        击败16.00%使用 Python3 的用户
        消耗内存分布
        32.70MB
        击败9.02%使用 Python3 的用户
        """
        length = len(heights)
        stack =[]
        less_l2r = [0]*length
        less_r2l = [0]*length

        # 通过单调栈为每个height确定下一个更小值的位置
        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:
                prev = stack.pop()
                less_l2r[prev] = i - prev
            stack.append(i)
        while stack:
            prev = stack.pop()
            less_l2r[prev] = length - prev
        # print(less_l2r)

        for j in range(length):
            current_idx = -j-1
            while stack and heights[current_idx] < heights[stack[-1]]:
                prev = stack.pop()
                less_r2l[prev] = prev - current_idx # 此处存的是当前节点到下一更小节点横跨的节点数量，正数
            stack.append(current_idx) # 栈里存的是负坐标，负数
        while stack:
            prev = stack.pop()
            less_r2l[prev] = prev - (-length-1)
        # print(less_r2l)
        
        max_area = 0
        for i, height in enumerate(heights):
            max_area = max(max_area, height*(less_l2r[i] + less_r2l[i] -1))
        return max_area


    def largestRectangleArea3(self, heights: List[int]) -> int:
        """✅参照官方题解，写法优化

        执行用时分布
        282ms   
        击败17.91%使用 Python3 的用户
        消耗内存分布
        28.78MB
        击败81.80%使用 Python3 的用户
        """
        length = len(heights)
        stack =[]
        less_l2r, less_r2l = [0]*length, [0]*length

        # 假设heights左右两侧各加一个负无穷
        for i in range(length):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            less_l2r[i] = stack[-1] if stack else -1
            stack.append(i)
        # print(less_l2r)
        
        stack = []
        for j in range(length-1, -1, -1):
            while stack and heights[j] <= heights[stack[-1]]:
                stack.pop()
            less_r2l[j] = stack[-1] if stack else length
            stack.append(j)
        # print(less_r2l)
        
        max_area = 0
        for i, height in enumerate(heights):
            max_area = max(max_area, height * (less_r2l[i] - less_l2r[i] -1))
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        """✅官方题解，常数优化，在确定左边界的同时，确定右边界

        作者：力扣官方题解
        链接：https://leetcode.cn/problems/largest-rectangle-in-histogram/solutions/266844/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        执行用时分布
        169ms
        击败92.31%使用 Python3 的用户
        消耗内存分布
        29.03MB
        击败56.75%使用 Python3 的用户
        """
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
```


## 堆

堆又称优先队列，是一棵完全二叉树，方便使用数组存储，根据二叉树的坐标规律可以快速计算给定节点的父节点、子节点坐标。堆通过偏序（而不是完全有序）适用于特定场景，参考[堆(Heap)这种数据结构有什么用处呢？](https://www.zhihu.com/question/466078026)。

堆参考：
* [数据结构 - 堆的原理 和 常见算法问题](https://writings.sh/post/data-structure-heap-and-common-problems)
* [堆排序中建堆过程时间复杂度O(n)怎么来的？](https://www.zhihu.com/question/20729324)

```python
class Heap:
    """实现一个大顶堆温习下这种数据结构

    root index = 0
    (let current index = i)
        left child = 2*i+1
        right child = 2*i +2
        parent of left = (i-1)/2
        parent of right = (i-2)/2
            parent = (i-1)//2
    """

    def __init__(self):
        self.heap = []

    def peek(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return None

    def parent_idx(self, current):
        return (current - 1) // 2  # here!

    def lchild_idx(self, current):
        return 2 * current + 1

    def rchild_idx(self, current):
        return 2 * current + 2

    # 末尾插入后通过上浮操作重新堆化
    def insert(self, num):
        self.heap.append(num)
        self.shift_up(len(self.heap) - 1)

    def shift_up(self, idx):
        while idx > 0 and self.heap[self.parent_idx(idx)] < self.heap[idx]:  # 这里把<改成>就成了小顶堆
            self.heap[self.parent_idx(idx)], self.heap[idx] = self.heap[idx], self.heap[self.parent_idx(idx)]
            idx = self.parent_idx(idx)

    # 堆顶弹出后将末尾元素放到堆顶并通过下浮操作重新堆化
    def pop(self):
        _ = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.shift_down()
        return _

    def shift_down(self, idx=0):
        # 不断选择更大的子节点与之对换位置，向下递归
        # 最后一个父节点的位置 = len(heap)/2-1
        while idx <= len(self.heap) / 2 - 1:
            l_idx = idx * 2 + 1
            r_idx = idx * 2 + 2
            max_child_idx = None
            if l_idx < len(self.heap) and self.heap[l_idx] > self.heap[idx]:
                max_child_idx = l_idx
            if r_idx < len(self.heap) and self.heap[r_idx] > self.heap[l_idx]:
                max_child_idx = r_idx

            if max_child_idx:
                self.heap[max_child_idx], self.heap[idx] = self.heap[idx], self.heap[max_child_idx]
                idx = max_child_idx
            else:
                return


if __name__ == '__main__':
    h = Heap()
    for i in [1, 6, -7, 2, 8, 9, 2, -1, 3]:
        h.insert(i)
        print(h.peek())
    print(h.heap)
    h.pop()
    h.pop()
    print(h.heap)

# 1
# 6
# 6
# 6
# 8
# 9
# 9
# 9
# 9
# [9, 6, 8, 3, 2, -7, 2, -1, 1]
# [6, 3, 2, -1, 2, -7, 1]
```


### [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)

用堆解决没有达到题目要求的O(n)时间复杂度。

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 小顶堆的容量=k，堆顶即答案，时间复杂度O(nlogn)
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            else:
                if n > h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h, n)
        return h[0]
```


### [347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)

熟悉下标准库中的heapq、defaultdict -> https://docs.python.org/zh-cn/3/library/heapq.html。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计频率 O(n)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        # 堆操作维护TopK，时间复杂度O(logk)
        heap = []
        for _k, v in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (v, _k))
            else:
                if v > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (v, _k))
        
        return [k for v, k in heap]
        # 整体时间复杂度O(nlogk)
```


### [295. 数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/)

```python
class MedianFinder:

    def __init__(self):
        self.smallTop = []
        self.bigTop = []

    def addNum(self, num: int) -> None:
        if len(self.smallTop) == len(self.bigTop):
            # 往小顶堆插入
            heapq.heappush(self.bigTop, -num)
            heapq.heappush(self.smallTop, -heapq.heappop(self.bigTop))
        else:
            # 往大顶堆插入，heapq为小顶堆，通过在push、pop过程求相反数实现大顶堆
            heapq.heappush(self.smallTop, num)
            heapq.heappush(self.bigTop, -heapq.heappop(self.smallTop))

    def findMedian(self) -> float:
        return self.smallTop[0] if len(self.smallTop) != len(self.bigTop) else (self.smallTop[0]+-self.bigTop[0])/2.0
```


## 贪心算法


### [121. 买卖股票的最佳时机*](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

参考：
* [动态规划(Dynamic Programming)和贪心算法(Greedy Algorithm)](https://hughesxu.github.io/posts/DP_Greedy_Algorithm/)


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ """
        minprice = 1e5
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit
```


### [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/)

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        看了题解：https://leetcode.cn/problems/jump-game/solutions/24322/55-by-ikaruga
        看了评论，我也想问为什么我这么蠢
        """
        k = 0 # 目前为止可以跳到的最远的距离
        for i in range(len(nums)):
            if i > k:
                return False
            k = max(k, i+nums[i])
        return True
```

### [45. 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/)

怎么论证？有算法思路上的模版可以用吗？每道题似乎完全不一样。

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        """「贪心」地进行正向查找，每次找到可到达的最远位置
        难呀☹️
        """
        n = len(nums)
        farthest = 0
        end = 0
        ans = 0
        for i in range(n-1):
            # if farthest >= i:
            farthest = max(farthest, i + nums[i])
            if i == end:  # 抵达上一次判断end的时候预测的最远距离
                end = farthest  # 保存目前为止在上一轮的行动距离内可选择出来的下一轮的最优解
                ans += 1
        return ans
```

### [763. 划分字母区间](https://leetcode.cn/problems/partition-labels/)

看了提示1给的思路写的，用时达到99%那岂不是很开心。

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 先写个“解：”
        n = len(s)
        ans = []

        # 初始化哈希表，每个字母最后出现的位置
        last = {}
        for i in range(n):
            last[s[i]] = i
        
        i = 0
        last_start = 0
        while i < n:
            cur_end = s[i]
            cur_end_last_index = last[cur_end]
            # print(i,cur_end,cur_end_last_index)

            # 判断在当前结束字符最后出现的位置之前，是否出现了新的字符结束位置更远，有的话必须将其纳入当前片段
            for j in range(i, cur_end_last_index+1):
                tmp_char = s[j]
                
                # 出现了新的字符结束位置更远，更新当前片段的结束字符
                if tmp_char != cur_end and last[tmp_char] > cur_end_last_index:
                    cur_end = tmp_char
                    i = j
                    break

                # 如果判断的字符位置与结束字符位置重合，说明当前片段可以独立，ans+1
                if j == cur_end_last_index:
                    ans.append(j-last_start+1)
                    last_start = j+1
                    i = j+1
        
        return ans
```


## 动态规划

参考：[动态规划基础](https://oi-wiki.org/dp/basic/)

参考：[动态规划入门：从记忆化搜索到递推](https://www.bilibili.com/video/BV1Xj411K7oF)

### [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        p = q = 0
        ans = 1
        for i in range(n):
            p = q
            q = ans
            ans = p + q
        return ans
```


### [118. 杨辉三角](https://leetcode.cn/problems/pascals-triangle/)

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """没有技巧，全是感情版解法"""
        ans = [[1],]
        for r in range(2, numRows+1):
            temp_row = [1,]
            for i in range(1, r-1):
                temp_row.append(ans[-1][i-1] + ans[-1][i])
            temp_row.append(1)
            ans.append(temp_row)
        return ans
```


### [198. 打家劫舍](https://leetcode.cn/problems/house-robber/)

```python
class Solution:
    def rob1(self, nums: List[int]) -> int:
        """记忆化搜索
        See: https://www.bilibili.com/video/BV1Xj411K7oF
        当前操作：第i房子选/不选
        当前子问题：从前i个房子里计算最大金额
        下一子问题：
            选：从前i-2个房子里计算最大金额
            不选：从前i-1个房子里计算最大金额
        """
        n = len(nums)
        cache = [-1]*n
        def dfs(i):
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]

            yes = dfs(i-2) +  nums[i]
            no = dfs(i-1)
            cur_ans = max(yes, no)
            cache[i] = cur_ans

            return cur_ans

        return dfs(n-1)


    def rob(self, nums: List[int]) -> int:
        """
        在确定了子问题的递推关系之后，下一步就是依次计算出这些子问题了。在很多教程中都会写，动态规划有两种计算顺序，一种是自顶向下的、使用备忘录的递归方法，一种是自底向上的、使用 dp 数组的循环方法。不过在普通的动态规划题目中，99% 的情况我们都不需要用到备忘录方法，所以我们最好坚持用自底向上的 dp 数组。

        # 子问题：
        # f(k) = 偷 [0..k) 房间中的最大金额

        # f(0) = 0
        # f(1) = nums[0]
        # f(k) = max{ rob(k-1), nums[k-1] + rob(k-2) }

        作者：nettee
        链接：https://leetcode.cn/problems/house-robber/solutions/138131/dong-tai-gui-hua-jie-ti-si-bu-zou-xiang-jie-cjavap/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        n = len(nums)

        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, n+1):
            dp[k] = max(dp[k-1], dp[k-2]+nums[k-1])
            print(dp)
        return dp[n]
```


### [279. 完全平方数](https://leetcode.cn/problems/perfect-squares/)

```python
class Solution:
    # 题解：https://leetcode.cn/problems/perfect-squares/solutions/823248/gong-shui-san-xie-xiang-jie-wan-quan-bei-nqes

    def numSquares1(self, n: int) -> int:
        """记忆化递归❌MLE
        n <= 10^4, k**2=n, k<=100 
        完全背包问题：k可选值1～100，可重复选择，最终目标等于n
        """
        @cache
        def dfs(i, j):
            # i当前值，j目标值
            # 定义状态：前i个数字，凑出数字总和j所需的最少数字量

            # 边界
            if i < 1:
                return 0 if j==0 else inf
            
            # 不选
            if i**2 > j:
                return dfs(i-1, j)
            # 选
            return min(dfs(i-1, j), dfs(i, j-i**2)+1)

        ans = dfs(100, n)
        return ans if ans < inf else -1


    def numSquares2(self, n: int) -> int:
        """递归改递推（二维）❌TLE
        """

        pkgs = []
        k = 1
        while k**2 <= n:
            pkgs.append(k**2)
            k += 1
        m = len(pkgs)

        # f[i][j]: 前i个数字凑出数字总和j所需的最少数字量
        f = [[inf] * (n+1) for _ in range(m+1)]
        f[0][0] = 0  # 除了临界值用0个值凑出0外（不选任何数），初始化为inf

        for i in range(1, m+1): # 总共m个数字
            x = pkgs[i-1] # 当前遍历到的数字
            for j in range(n+1): 
                # 不选第i个数字
                # print(i,x, j)
                f[i][j] = f[i-1][j]
                # 选
                k=1
                while k*x <= j:
                    # 能够选择 k 个 t 的前提是剩余的数字 j - k * t 也能被凑出
                    if f[i-1][j-k*x] != inf:
                        f[i][j] = min(f[i][j], f[i-1][j-k*x]+k)
                    k += 1
                    # print(x, k, j)
        
        ans = f[m][n]
        return ans if ans < inf else -1

    def numSquares(self, n: int) -> int:
        # 推导过程？
        f = [inf]*(n+1)
        f[0] = 0
        for t in range(1, n+1):
            cur = t*t
            if cur > n:
                break
            for j in range(cur, n+1):
                f[j] = min(f[j], f[j-cur]+1)
                # print(f)
        return f[n]
```

### [322. 零钱兑换](https://leetcode.cn/problems/coin-change/)

```python
class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        """
        背包DP，选或不选思路的典型场景：0-1背包（每个物品最多选一次）、完全背包（每个物品可以选择多次）
        Refer：https://github.com/tianyicui/pack/tree/master

        零钱兑换：完全背包问题的变种，可重复选择的基础上判断已经选择的金额是否已经刚好等于目标值
        题解：https://leetcode.cn/problems/coin-change/solutions/2119065/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-21m5
        """
        n = len(coins)
        @cache # 不加缓存会超时
        def dfs(i, j):
            """前i个物品在金额为j的情况下，是否可以凑整"""
            # 边界
            if i < 0:
                return 0 if j==0 else inf # 由于外层使用min()找最优解，此处用无穷大代表没有解
            
            # 面值超出目标值则不选
            if j < coins[i]:
                return dfs(i-1, j)
            # 否则选、不选都可以，取更符合目标的结果
            return min(dfs(i-1, j), dfs(i, j-coins[i])+1) # +1代表选择了当前货币，所以目标金额需要减掉当前货币面值

        ans = dfs(n-1, amount)
        return ans if ans < inf else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        # 改成递推 dfs递归函数改成f数组，递归过程用循环模拟
        # dfs(i,j) = min(dfs(i-1, j), dfs(i, j-w[i])+1)
        # f[i][j] = min(f[i-1][j], f[i][j-w[i]]+1)
        # 为了避免负数下表，所有的i都+1处理 --> f[i+1][j] = min(f[i][j], f[i+1][j-w[i]]+1)

        n = len(coins)
        f = [[inf] * (amount+1) for c in range(n+1)]
        f[0][0] = 0
        # print(f)
        for i, c in enumerate(coins): # 第i个硬币
            for j in range(amount+1):
                if j < c:
                    f[i+1][j] = f[i][j]
                else:
                    f[i+1][j] = min(f[i][j], f[i+1][j-c]+1)
        
        ans = f[n][amount]
        return ans if ans < inf else -1
```


### [139. 单词拆分](https://leetcode.cn/problems/word-break/)

>You: 动态规划适用于什么样的问题？

>ChatGPT:
> 动态规划适用于那些具有重叠子问题和最优子结构特性的问题。具体来说，它适用于需要在给定约束条件下优化某种指标（通常是最大化或最小化）的问题，而且问题可以被分解为相互关联的子问题，这些子问题之间存在重复计算的情况。
> 动态规划常见于解决许多优化问题，比如最短路径问题、最长公共子序列问题、背包问题等。通过存储中间结果并利用之前计算的结果，动态规划能够在多项式时间内解决许多复杂问题，而不需要重复计算相同的子问题。

> You: 你知道力扣的第139题单词拆分吗

> ChatGPT:
> 是的，我了解。力扣（LeetCode）的第139题是 "Word Break"（单词拆分）。这道题目的问题描述是给定一个非空字符串s和一个包含非空单词列表的字典wordDict，判断s是否可以被空格拆分成一个或多个字典中出现的单词。你可以在力扣的网站上找到这道题的详细描述以及解题思路。

> You: 能够分析一下这道题吗
> ChatGPT:
> 当解决这道题时，你可以使用动态规划的方法。以下是一种基本的解题思路：
>
>    定义状态： 定义一个布尔型的一维数组dp，其中dp[i]表示字符串s的前i个字符是否可以被拆分成字典中的单词。
>
>    初始化状态： 将dp[0]初始化为True，表示空字符串可以被拆分。
>
>    状态转移： 对于每个位置i（i从1到s的长度），检查s的前i个字符是否可以被拆分成字典中的单词。具体地，遍历从0到i-1的位置j，如果dp[j]为True且s[j:i]（即从位置j到位置i之间的子串）在字典中，则将dp[i]置为True。
>
>    最终结果： 返回dp[s.length()]，表示整个字符串s是否可以被拆分成字典中的单词。
>
> 这种方法的时间复杂度为O(n^2)，其中n为字符串s的长度。在实际编码中，还可以使用字典树（Trie）来优化查找字典中单词的时间复杂度，进一步提高算法效率。

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) # 消耗On将后续判断字符是否存在的时间优化为O1

        f = [False]*(len(s)+1)
        f[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                # print(i, j, f, s[j:i+1])
                if f[j] and s[j:i] in wordSet:
                    f[i] = True
                    break
        return f[len(s)]
```


### [300. 最长递增子序列LIS](https://leetcode.cn/problems/longest-increasing-subsequence/)

```python
class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        # DP题解：https://www.bilibili.com/video/BV1ub411Q7sB
        n = len(nums)

        @cache
        def dfs(i):
            # 状态：以第i个数字为结尾，最长子序列的长度
            # 状态转移：dfs(i) = max(dfs(j))+1, j<i && nums[j]<nums[i]
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1
        
        return max(dfs(i) for i in range(n))
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 递归改递推
        n = len(nums)
        f = [0]*n
        # print(f)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        # print(f)
        return max(f)
```

### [152. 乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/)

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        状态：dfs(i)为前i个数字的最大乘积
        
        转移方程1：dfs(i) = max(dfs(i-1), 1) * nums[i]  #❌反例：[-3,-1,-1]
        转移方程2：dfs(i) = max(dfs(i-1)* nums[i], nums[i]) #❌反例 [-2,3,-4]
        
        转移方程3:
        dfs(i-1)、nums[i]可能是正数、负数、0，二者乘积的最大值？
        设dfs(i-1)为a,nums[i]为b
        a < 0, b < 0 --> return ab
        a < 0, b = 0 --> return b 0
        a < 0, b > 0 --> return b
        a = 0, b < 0 --> return a 0
        a = 0, b = 0 --> return 0
        a = 0, b > 0 --> return b
        a > 0, b < 0 --> return a
        a > 0, b = 0 --> return a
        a > 0, b > 0 --> return ab
        dfs(i) = max(dfs(i-1), dfs(i-1)*nums[i], nums[i], 0) 
        ❌[2,3,-2,4]返回24而不是6，dfs([2,3,-2])得到6没问题，但不能再用6*4了，因为中间隔了个-2
        精准踩坑，可以看官方题解的第一段错误分析 https://leetcode.cn/problems/maximum-product-subarray/solutions/250015/cheng-ji-zui-da-zi-shu-zu-by-leetcode-solution
        class Solution:
            def maxProduct(self, nums: List[int]) -> int:
                n = len(nums)
                @cache
                def dfs(i):
                    if i<0:return 1
                    return max(dfs(i-1)*nums[i], nums[i]) 
                return max(dfs(i) for i in range(n))
        
        转移方程4:根据正负号分别讨论
        maxf: 以第i个元素结尾的乘积最大子数组的乘积
        minf: 以第i个元素结尾的乘积最小子数组的乘积
        """

        n = len(nums)
        maxf = nums.copy()
        minf = nums.copy()
        for i in range(1, n):
            maxf[i] = max(maxf[i-1]*nums[i], minf[i-1]*nums[i], nums[i])
            minf[i] = min(minf[i-1]*nums[i], maxf[i-1]*nums[i], nums[i])
        # print(maxf, minf)
        return max(maxf)
```


### [416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if n < 2 or s%2 != 0:
            return False
        target = s//2
        m = max(nums)
        if m > target:
            return False

        '''
        # 选若干个数字是否可以凑出target，0-1背包问题的变种
        # 状态：dp[i][j] = 从数组[0, i]选取若干数字是否可以使数字和为j
        dp = [[False]*(target+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = True
        # 状态转移
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target+1):
                if j >= num: # 选或不选都可以
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-num]
                else: # 只能不选
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[n-1][target]
        '''

        # 空间优化
        dp = [True] + [False]*target
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[target]
```


### [32. 最长有效括号**](https://leetcode.cn/problems/longest-valid-parentheses/)

```python
class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        """❌暴力解，超时，224 / 231 个通过的测试用例
        """
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                stack = []
                cnt = 0
                for c in s[i:j+1]:
                    if c == '(': # 左括号入栈
                        stack.append(c)
                    elif not stack or stack.pop() != '(': # 右扣号消除
                        break
                    cnt += 1

                if stack:
                    cnt = 0

                ans = max(ans, cnt)
        return ans

    def longestValidParentheses(self, s: str) -> int:
        """
        状态定义：dp[i] = 以下标 i 字符结尾的最长有效括号的长度
        """
        n = len(s)
        dp = [0] * (n+1)
        ans = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 + dp[i-2] # dp数组位数为n+1，最后一位作为-1下标（仅python适用），-1下标初始化为0
                elif i-dp[i-1] > 0 and s[i - dp[i-1] -1] == '(': # 把中间的连续合格子串算上，再往前找一个，看是否能跟当前的）匹配上
                    dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] -2] if (i - dp[i-1])>=2 else 0)
                ans = max(ans, dp[i])
        return ans
```


## 多维动态规划

### [62. 不同路径](https://leetcode.cn/problems/unique-paths/)

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # f(i,j) = f(i-1, j) + f(i, j-1) 走到(i, j)要么从左边走过来要么从上面走下来
        f = [[1]*n] + [[1] + [0] * (n-1) for _ in range(m-1)] # 第一排与第一列都是1（只能从左到右或从上到下一个维度）
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]
```


### [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/)

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 状态定义： dp[i][j] = 走到(i,j)的最小路径和
        # 状态转移： dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]
```


### [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 题解：https://leetcode.cn/problems/longest-palindromic-substring/solutions/63641/zhong-xin-kuo-san-fa-he-dong-tai-gui-hua-by-reedfa
        # 题解：https://leetcode.cn/problems/longest-palindromic-substring/solutions/255195/zui-chang-hui-wen-zi-chuan-by-leetcode-solution
        n = len(s)
        if n < 2:
            return s
        
        ans_start = 0
        ans_len = 1

        f = [[False] * n for _ in range(n)]
        # for i in range(n): f[i][i] = True
        for r in range(1, n):
            for l in range(r):
                if s[l] == s[r] and (r-l<3 or f[l+1][r-1]):
                    f[l][r] = True
                    if (r-l+1) > ans_len:
                        ans_len = r-l+1
                        ans_start = l
        return s[ans_start:ans_start+ans_len]
```


### [1143. 最长公共子序列LCS](https://leetcode.cn/problems/longest-common-subsequence/)

```python
class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        """DP题解: https://www.bilibili.com/video/BV1TM4y1o7ug"""
        n1 = len(text1)
        n2 = len(text2)

        def dfs(i, j):
            if i<0 or j<0: return 0

            if text1[i] == text2[j]:
                return dfs(i-1, j-1) +1
            return max(dfs(i-1,j), dfs(i, j-1))
        
        return dfs(n1-1, n2-1)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 递归改递推
        n1 = len(text1)
        n2 = len(text2)

        f = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1])
                """
                [[1, 1, 1, 0, 0], 
                [1, 1, 1, 0, 0], 
                [1, 2, 2, 0, 0], 
                [1, 2, 2, 0, 0], 
                [1, 2, 3, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]]
                """

                # if text1[i] == text2[j]:
                #     f[i+1][j+1] = f[i][j] + 1
                # else:
                #     f[i+1][j+1] = max(f[i][j+1], f[i+1][j])
                """
                [
                [0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 0], 
                [0, 1, 1, 1, 0], 
                [0, 1, 2, 2, 0], 
                [0, 1, 2, 2, 0], 
                [0, 1, 2, 3, 0], 
                [0, 0, 0, 0, 0]]
                """
        print(f)
        return f[n1-1][n2-1]
```


### [72. 编辑距离](https://leetcode.cn/problems/edit-distance/)

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if m*n == 0: return m+n

        # 状态定义: f[i][j] = word1前i个字母和word2前j个字母之间的编辑距离
        f = [[0]*(m+1) for _ in range(n+1)] # n+1行，m+1列

        # 状态参数i,j为0的情况下边界值
        for i in range(n+1): f[i][0] = i
        for j in range(m+1): f[0][j] = j

        # 状态转移：
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = 1 + min(f[i+1][j], f[i][j+1], f[i][j])

        return f[n][m]
```


## 技巧

### [136. 只出现一次的数字*（位运算）](https://leetcode.cn/problems/single-number/)

> 按位运算符是把数字看作二进制来进行计算的。
> 
> 按位异或运算符`^`：当两对应的二进位相异时，结果为1 
> 
> > Python位运算：https://www.runoob.com/python3/python3-basic-operators.html#ysf5

> 异或运算有以下三个性质:
    1. 何数和0做异或运算，结果仍然是原来的数
    2. 任何数和其自身做异或运算，结果是0
    3. 异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)
> > [力扣官方题解](https://leetcode.cn/problems/single-number/solutions/242211/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        return ans
```


### [169. 多数元素*（Boyer-Moore多数投票算法）](https://leetcode.cn/problems/majority-element/)

Robert S. Boyer and J Strother Moore 这俩人提出过很多算法，该题中用到的是多数投票算法，更著名的以他们命名的算法是BM字符串匹配算法。

* [Boyer-Moore多数投票算法](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
* [字符串匹配的Boyer-Moore算法](https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """多数投票，空间复杂度O(1)"""
        count = 0
        target = None
        for n in nums:
            if count == 0:
                target = n
            
            if target == n:
                count += 1
            else:
                count -= 1
        return target
```


### [75. 颜色分类](https://leetcode.cn/problems/sort-colors/)

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """计数后重写数组，思路及实现最简单
        
        """
        n = len(nums)
        count = [0]*3
        for x in nums:
            count[x] += 1
        
        i = 0
        while i < n:
            if count[0] > 0:
                nums[i] = 0
                count[0] -= 1
            elif count[1] > 0:
                nums[i] = 1
                count[1] -= 1
            else:
                nums[i] = 2
                count[2] -= 1
            i += 1
```


### [31. 下一个排列](https://leetcode.cn/problems/next-permutation/)

```python
class Solution:
    def nextPermutation1(self, nums: List[int]) -> None:
        """❌
        从右往左扫描交换第一个【相邻升序对】，若没有则需要反转
        思路错了，下一个更大的排列不能这样简单判断相邻两个元素，得跨位置考虑
        155 / 266 个通过的测试用例
        输入nums = [1,3,2]
        输出[3,1,2]
        预期结果[2,1,3]
        """
        p = len(nums)-1
        flag = False
        while p > 0:
            if nums[p-1] < nums[p]:
                nums[p-1], nums[p] = nums[p], nums[p-1]
                flag = True
                break
            p -= 1

        if not flag:
            l, r = 0, len(nums)-1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """找到第一个相邻升序对[a,b]后，再从后往前找第一个比a大的数c，换完a,c之后需要将c后面的数排序。
        具体分析见：https://leetcode.cn/problems/next-permutation/solutions/80560/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-
        """

        p = len(nums)-1
        flag = False
        while p > 0:
            if nums[p-1] < nums[p]:
                p -= 1
                _p = len(nums)-1
                while _p > p:
                    if nums[_p] > nums[p]:
                        nums[p], nums[_p] = nums[_p], nums[p]
                        break
                    _p -= 1
                flag = True
                break
            p -= 1
        
        l, r = 0 if not flag else p+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
```


### [287. 寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)

shit.

```python
class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 1, n-1
        ans = -1
        while l <= r:
            m = (l+r)//2
            cnt = 0
            for i in range(n):
                cnt += nums[i] <= m
            if cnt <= m:
                l = m+1
            else:
                r = m-1
                ans = m
        return ans
    
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        

        slow = nums[slow]
        fast = nums[nums[fast]]
        print(slow, fast)
        while nums[slow] != nums[fast]:
        # while nums[slow] != nums[fast]: # also okay
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```