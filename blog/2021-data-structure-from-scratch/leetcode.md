# LeetCode Hot 100

20240401-04? 

题单地址：https://leetcode.cn/studyplan/top-100-liked/ ，有些相关典型题一并在这个目录下做了，不仅限于hot100。


- [LeetCode Hot 100](#leetcode-hot-100)
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
  - [子串](#子串)
    - [560. 和为 K 的子数组（有空再瞅瞅）](#560-和为-k-的子数组有空再瞅瞅)
    - [](#)
    - [](#-1)
  - [普通数组](#普通数组)
    - [53. 最大子数组和（动态规划）](#53-最大子数组和动态规划)
    - [56. 合并区间（排序）](#56-合并区间排序)
    - [189. 轮转数组](#189-轮转数组)
    - [](#-2)
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
    - [图解 K 个一组翻转链表](#图解-k-个一组翻转链表)
    - [](#-3)
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
    - [](#-4)
    - [](#-5)
    - [](#-6)
    - [](#-7)
  - [回溯](#回溯)
    - [46. 全排列](#46-全排列)
    - [](#-8)
    - [](#-9)
  - [二分查找](#二分查找)
    - [35. 搜索插入位置](#35-搜索插入位置)
    - [74. 搜索二维矩阵](#74-搜索二维矩阵)
    - [34. 在排序数组中查找元素的第一个和最后一个位置](#34-在排序数组中查找元素的第一个和最后一个位置)
    - [33. 搜索旋转排序数组](#33-搜索旋转排序数组)
    - [](#-10)
    - [](#-11)
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
  - [技巧](#技巧)
    - [136. 只出现一次的数字\*（位运算）](#136-只出现一次的数字位运算)
    - [169. 多数元素\*（Boyer-Moore多数投票算法）](#169-多数元素boyer-moore多数投票算法)
    - [](#-12)
    - [](#-13)
  - [贪心算法](#贪心算法)
    - [121. 买卖股票的最佳时机](#121-买卖股票的最佳时机)
    - [55. 跳跃游戏](#55-跳跃游戏)
  - [动态规划](#动态规划)
    - [70. 爬楼梯](#70-爬楼梯)
    - [118. 杨辉三角](#118-杨辉三角)
    - [](#-14)
    - [](#-15)


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


### []()

```python

```


### []()

```python

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


### []()

```python

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


### [图解 K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

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


### []()

```python

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


### []()

```python

```


### []()

```python

```


### []()

```python

```


### []()

```python

```


## 回溯



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


### []()

```python

```


### []()

```python

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


### []()

```python

```

### []()

```python

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

堆参考：[数据结构 - 堆的原理 和 常见算法问题](https://writings.sh/post/data-structure-heap-and-common-problems)

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


### []()

```python

```


### []()

```python

```

## 贪心算法


### [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

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
        k = 0
        for i in range(len(nums)):
            if i > k:
                return False
            k = max(k, i+nums[i])
        return True
```


## 动态规划

参考：[动态规划基础](https://oi-wiki.org/dp/basic/)


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


### []()

```python

```


### []()

```python

```