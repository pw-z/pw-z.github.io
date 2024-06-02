# Leetcode Study Plan Leetcode-75 Scratch Paper

*Created on 2024.05.28 by [Zhang Pengwei](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 

这是刷题的草稿纸，随笔写写思路，没有阅读价值。

题单地址：https://leetcode.cn/studyplan/leetcode-75/

简单：`*`  
中等：`**`  
困难：`***`


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Leetcode Study Plan Leetcode-75 Scratch Paper](#leetcode-study-plan-leetcode-75-scratch-paper)
  - [数组/字符串](#数组字符串)
      - [1768. 交替合并字符串\*](#1768-交替合并字符串)
      - [](#)
      - [](#-1)
      - [](#-2)
      - [](#-3)
      - [](#-4)
  - [双指针](#双指针)
      - [283. 移动零\*](#283-移动零)
      - [](#-5)
      - [](#-6)
  - [滑动窗口](#滑动窗口)
      - [643. 子数组最大平均数 I\*](#643-子数组最大平均数-i)
      - [](#-7)
      - [](#-8)
  - [前缀和](#前缀和)
      - [1732. 找到最高海拔\*](#1732-找到最高海拔)
      - [724. 寻找数组的中心下标\*](#724-寻找数组的中心下标)
      - [](#-9)
  - [哈希](#哈希)
      - [](#-10)
      - [](#-11)
      - [](#-12)
  - [栈](#栈)
      - [](#-13)
      - [](#-14)
      - [](#-15)

<!-- /code_chunk_output -->



## 数组/字符串

#### [1768. 交替合并字符串*](https://leetcode.cn/problems/merge-strings-alternately/)

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 时间复杂度O(n), 空间复杂度O(1)
        l1, l2 = len(word1), len(word2)
        ans = ""
        i1 = i2 = 0
        while i1 < l1 and i2 < l2:
            ans += word1[i1]
            ans += word2[i2]
            i1 += 1
            i2 += 1
        
        ans += word1[i1:] if i1 < l1 else word2[i2:]
        return ans
```


#### []()

```python

```


#### []()

```python

```


#### []()

```python

```


#### []()

```python

```


#### []()

```python

```


## 双指针

#### [283. 移动零*](https://leetcode.cn/problems/move-zeroes/)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # O(n), O(1)
        slow_zero, fast_nonzero, n = 0, 0, len(nums)
        while fast_nonzero < n:
            if nums[fast_nonzero] != 0:
                nums[slow_zero], nums[fast_nonzero] = nums[fast_nonzero], nums[slow_zero]
                slow_zero += 1
            fast_nonzero += 1
```


#### []()

```python

```


#### []()

```python

```


## 滑动窗口

#### [643. 子数组最大平均数 I*](https://leetcode.cn/problems/maximum-average-subarray-i/)

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # O(n), O(1)
        n = len(nums)
        ans_sum = cur_sum = sum(nums[:k])
        for end in range(k, n):
            cur_sum = cur_sum + nums[end] - nums[end-k]
            ans_sum = max(cur_sum, ans_sum)
        return ans_sum/k
```


#### []()

```python

```


#### []()

```python

```


## 前缀和

前缀和算法是一种在数据结构和算法中常用的技术，它通过预先计算数据序列的累积和来优化某些特定类型的查询，从而提高查询效率。下面是前缀和算法的一些核心思想、典型场景以及解题思路。

前缀和算法思想：
1. **累积计算**：前缀和算法的核心是将一个序列的每个元素与其前面的所有元素相加，得到一个新的序列，其中每个元素是原序列中从第一个元素到当前元素的和。
2. **空间换时间**：通过牺牲额外的空间来存储前缀和，可以显著减少计算时间，特别是对于需要频繁查询的场合。
3. **快速查询**：一旦前缀和数组构建完成，对于任意区间的和，可以通过常数时间的计算得到。

典型场景：
1. **区间求和**：快速计算序列中任意两个索引之间的和。
2. **最大子数组和**：Kadane算法利用前缀和来找到最大子数组和。
3. **区间更新**：在某些情况下，前缀和可以用于快速更新区间值。
4. **滑动窗口问题**：在需要在滑动窗口内进行求和的场景中，前缀和可以快速计算窗口内元素的和。

解题思路：
1. **构建前缀和数组**：
   - 初始化一个与原序列等长的数组。
   - 遍历原序列，计算每个位置的前缀和，存储在新数组中。

2. **区间求和**：
   - 要计算从索引i到j的和，使用公式：`sum(i, j) = prefix[j] - prefix[i-1]`。
   - 如果i为0，则直接使用`prefix[j]`。

3. **最大子数组和**：
   - 使用Kadane算法，维护当前最大子数组和以及全局最大子数组和。
   - 遍历序列，更新前缀和，同时更新当前最大和全局最大。

4. **区间更新**：
   - 如果需要更新区间[i, j]的值，可以计算更新前的区间和，然后更新前缀和数组。

5. **滑动窗口问题**：
   - 使用双指针维护窗口的开始和结束位置。
   - 通过前缀和快速计算窗口内的和。

示例代码（Python）：
```python
def build_prefix_sum(arr):
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    return prefix_sum

def sum_query(prefix_sum, i, j):
    return prefix_sum[j] - prefix_sum[i]

# 示例使用
arr = [1, 2, 3, 4, 5]
prefix_sum = build_prefix_sum(arr)
print(sum_query(prefix_sum, 1, 3))  # 输出 6，即2+3+4
```

通过这种方式，前缀和算法可以显著提高某些计算密集型问题的处理速度，特别是在需要频繁进行区间查询的场景中。

#### [1732. 找到最高海拔*](https://leetcode.cn/problems/find-the-highest-altitude/)

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 计算过程取求前缀和最大值
        # O(n), O(1)
        ans = cur = 0
        for g in gain:
            cur = cur + g
            ans = max(ans, cur)
        return ans
```

#### [724. 寻找数组的中心下标*](https://leetcode.cn/problems/find-pivot-index/)

```python
class Solution:
    def pivotIndex1(self, nums: List[int]) -> int:
        # O(n), 空间复杂度O(1)但利用了入参空间
        n = len(nums)
        # 前缀和
        for i in range(1, n):
            nums[i] = nums[i-1] + nums[i]
        # 前缀和末尾添个0兼容边界
        nums.append(0)
        for i in range(n):
            if nums[i-1] == nums[-2] - nums[i]:
                return i
        return -1
    
    def pivotIndex(self, nums: List[int]) -> int:
        # O(n), O(1)
        sum_l, sum_r = 0, sum(nums)
        for i in range(len(nums)):
            sum_r -= nums[i]
            if sum_l == sum_r:
                return i
            sum_l += nums[i]
        return -1
```

#### []()

```python

```


## 哈希

#### []()

```python

```


#### []()

```python

```


#### []()

```python

```


## 栈

#### []()

```python

```


#### []()

```python

```


#### []()

```python

```