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
      - [1071. 字符串的最大公因子\*](#1071-字符串的最大公因子)
      - [1431. 拥有最多糖果的孩子\*](#1431-拥有最多糖果的孩子)
      - [605. 种花问题](#605-种花问题)
      - [](#)
      - [](#-1)
  - [双指针](#双指针)
      - [283. 移动零\*](#283-移动零)
      - [](#-2)
      - [](#-3)
  - [滑动窗口](#滑动窗口)
      - [643. 子数组最大平均数 I\*](#643-子数组最大平均数-i)
      - [](#-4)
      - [](#-5)
  - [前缀和](#前缀和)
      - [1732. 找到最高海拔\*](#1732-找到最高海拔)
      - [724. 寻找数组的中心下标\*](#724-寻找数组的中心下标)
      - [](#-6)
  - [哈希](#哈希)
      - [2215. 找出两数组的不同\*](#2215-找出两数组的不同)
      - [1207. 独一无二的出现次数\*](#1207-独一无二的出现次数)
      - [1657. 确定两个字符串是否接近\*\*](#1657-确定两个字符串是否接近)
      - [2352. 相等行列对\*\*](#2352-相等行列对)
  - [栈](#栈)
      - [](#-7)
      - [](#-8)
      - [](#-9)
  - [位运算](#位运算)
      - [338. 比特位计数\*](#338-比特位计数)
      - [136. 只出现一次的数字\*](#136-只出现一次的数字)
      - [1318. 或运算的最小翻转次数\*\*](#1318-或运算的最小翻转次数)
  - [前缀树](#前缀树)
      - [](#-10)
      - [](#-11)
  - [区间集合](#区间集合)
      - [](#-12)
      - [](#-13)
  - [单调栈](#单调栈)
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


#### [1071. 字符串的最大公因子*](https://leetcode.cn/problems/greatest-common-divisor-of-strings)

辗转相除法，也称为欧几里得算法（Euclidean Algorithm），是用于求解两个整数（a 和 b）的最大公约数（GCD）的一种算法。它的基本思想是：用较大的数除以较小的数，再用出现的余数（第一余数）去除除数，再用出现的余数（第二余数）去除第一余数，如此反复，直到最后余数为0为止。那么，最后一个除数就是所求的最大公约数。

具体步骤如下：

    初始化 a 和 b，假设 a > b。
    计算 a 除以 b 的余数，记作 r。
    将 b 的值赋给 a，将 r 的值赋给 b。
    重复步骤 2 和 3，直到 r 为 0。
    当 r 为 0 时，b 就是 a 和 b 的最大公约数。

用数学符号表示，算法可以描述为：

GCD(a, b) = GCD(b, a mod b)

其中 "mod" 表示取余操作。

下面是一个简单的 Python 实现：

```python
def gcd(a, b):  
    while b != 0:  
        a, b = b, a % b  
    return a  
  
# 示例  
print(gcd(48, 18))  # 输出 6
```
在这个例子中，48 和 18 的最大公约数是 6。

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # O(n), O(n)
        if str1+str2 == str2+str1:
            _gcd = math.gcd(len(str1), len(str2))
            return str1[:_gcd]
        return ""
```


#### [1431. 拥有最多糖果的孩子*](https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies)

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # O(n), O(1)
        _max = max(candies)
        # ans = []
        # for i in candies:
        #     ans.append(i + extraCandies >= _max)
        # return ans
        return [i + extraCandies >= _max for i in candies]
```


#### [605. 种花问题](https://leetcode.cn/problems/can-place-flowers)

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # O(len(flowerbed)), O(1)
        # 只要找到连续三个0就可以种一颗，注意左右边界的处理
        continuous_zero = 1  # 设-1坐标左边界为0，兼容0坐标可以种花的场景
        ans = 0
        for i in flowerbed + [0]: # +[0]兼容右边界可以种花的情况
            if i == 0:
                continuous_zero += 1
            else:
                continuous_zero = 0
            if continuous_zero == 3:
                ans += 1
                continuous_zero = 1 # 注意种完后不是归零
        return ans >= n
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

#### [2215. 找出两数组的不同*](https://leetcode.cn/problems/find-the-difference-of-two-arrays/)

在Python中，`set` 类型提供了一个方便的方法来执行集合之间的减法操作，即计算两个集合的差集。差集是指第一个集合中存在而第二个集合中不存在的所有元素组成的集合。

语法：
```python
set1.difference(set2)
```
或者使用更现代的语法：
```python
set1 - set2
```

示例：
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 使用 difference 方法
difference_set = set1.difference(set2)
print(difference_set)  # 输出: {1, 2}

# 使用 - 运算符
difference_set = set1 - set2
print(difference_set)  # 输出: {1, 2}
```

说明：  
- `difference()` 方法返回一个新集合，包含 `set1` 中所有不在 `set2` 中的元素。
- `-` 运算符也执行相同的操作，返回 `set1` 和 `set2` 的差集。
- 这些操作都是不可变的，意味着原始集合 `set1` 和 `set2` 不会被修改。
- 如果想要从原始集合中直接移除与另一个集合相同的元素，可以使用 `difference_update()` 方法：
  ```python
  set1.difference_update(set2)
  ```
  这会直接修改 `set1`，移除那些在 `set2` 中的元素。

时间复杂度:  
集合的差集操作的时间复杂度是 O(len(set2))，这是因为它需要遍历第二个集合 `set2` 中的每个元素，并检查它们是否在第一个集合 `set1` 中。由于集合是基于哈希表实现的，每个查找操作的平均时间复杂度是 O(1)，因此总的时间复杂度与 `set2` 中元素的数量成正比。


```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # O(n), O(n)
        set1, set2 = set(nums1), set(nums2)
        return [list(set1-set2), list(set2-set1)]
```


#### [1207. 独一无二的出现次数*](https://leetcode.cn/problems/unique-number-of-occurrences/)

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # O(n), O(n)
        count = collections.defaultdict(int)
        for num in arr:
            count[num] += 1
        return len(set(count.values())) == len(count.values())
```


#### [1657. 确定两个字符串是否接近**](https://leetcode.cn/problems/determine-if-two-strings-are-close/)

Python 的 collections 模块中的 Counter 类是一个字典子类，用于计数可哈希对象。它是一个集合，元素是存储在字典中的键，而每个键的值是该键出现的次数。

Python 中的 `Counter` 对象可以直接进行比较。`Counter` 是一个可哈希（hashable）的对象，这意味着两个 `Counter` 对象可以直接使用比较运算符（如 `==`, `!=`, `<`, `>`, `<=`, `>=`）来进行比较。

比较两个 `Counter` 对象时，它们会根据它们的元素及其计数进行比较。两个 `Counter` 对象相等（`==`）当且仅当它们的键（元素类型）相同，并且每个键的计数也相同。

示例代码：
```python
from collections import Counter

# 创建两个 Counter 对象
counter1 = Counter(['apple', 'banana', 'apple'])
counter2 = Counter(['banana', 'apple', 'apple'])

# 比较两个 Counter 对象
print(counter1 == counter2)  # 输出: True，因为它们有相同的元素和计数

# 改变 counter2 的一个元素的计数
counter2['banana'] += 1

# 再次比较
print(counter1 == counter2)  # 输出: False，因为现在它们的计数不同
```

在这个示例中，`counter1` 和 `counter2` 最初是相等的，因为它们包含相同的元素和计数。当我们改变 `counter2` 中 `banana` 的计数后，这两个 `Counter` 对象就不相等了。

这种比较非常有用，特别是在你需要检查两个数据集中元素的出现频率是否相同时。

另外在Python中，你可以直接比较两个字典的键（keys）集合。由于字典的键在Python中是无序的，并且它们是基于哈希的集合，因此比较两个字典的键是否相同通常意味着比较它们的键集合是否相等。

你可以使用集合（set）的相等性比较来做到这一点，因为集合是无序的，并且只包含唯一的元素。你可以通过将字典的键转换为集合，然后比较这两个集合来比较字典的键。

以下是一个示例：
```python
dict1 = {'a': 1, 'b': 2, 'c': 3}  
dict2 = {'c': 3, 'b': 2, 'a': 1}  
  
# 使用set来比较字典的键  
if set(dict1.keys()) == set(dict2.keys()):  
    print("两个字典的键相同")  
else:  
    print("两个字典的键不同")
```
在这个例子中，尽管dict1和dict2的键的顺序不同，但它们的键集合是相同的，因此输出将是“两个字典的键相同”。

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # O(m+n), O(26)
        m, n = len(word1), len(word2)
        if m != n: return False
        
        # count1, count2 = defaultdict(int), defaultdict(int)
        # for c1, c2 in zip(word1, word2):
        #     count1[c1] += 1
        #     count2[c2] += 1
        count1, count2 = collections.Counter(word1), collections.Counter(word2)
        # print(count1, count2)
        # print(count1.keys(), count2.keys())
        # print(count1.keys()== count2.keys())
        # print(count1.values(), count2.values())
        # print(count1.values() == count2.values())
        
        return count1.keys() == count2.keys() and Counter(count1.values()) == Counter(count2.values())
```


#### [2352. 相等行列对**](https://leetcode.cn/problems/equal-row-and-column-pairs/)

```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # O(n^2), O(n)
        n = len(grid)
        ans = 0
        cache = defaultdict(int)
        for r in grid:
            cache[tuple(r)] += 1
        for c in range(n):
            k = []
            for r in range(n):
                k.append(grid[r][c])
            ans += cache[tuple(k)]
        return ans
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


## 位运算

Python支持常见的位运算符，这些运算符对整数类型进行位级操作。以下是Python支持的位运算符：

1. **按位与** (`&`): 对应二进制位进行逻辑与操作，只有两个位都是1时，结果位才为1。
2. **按位或** (`|`): 对应二进制位进行逻辑或操作，只要两个位中有一个为1，结果位就为1。
3. **按位异或** (`^`): 对应二进制位进行逻辑异或操作，只有两个位不同的时候，结果位才为1。
4. **按位取反** (`~`): 对一个数进行按位取反操作，将所有的1变成0，0变成1。
5. **左移** (`<<`): 将一个数的所有位向左移动指定位数，右边空出的位填充0。
6. **右移** (`>>`): 将一个数的所有位向右移动指定位数，左边空出的位根据符号位进行填充（正数补0，负数补1）。

示例代码：

```python
# 定义两个整数
a = 60  # 在二进制中表示为 111100
b = 13  # 在二进制中表示为 0011001

# 按位与
print(a & b)  # 输出 12，二进制为 001100

# 按位或
print(a | b)  # 输出 61，二进制为 111101

# 按位异或
print(a ^ b)  # 输出 49，二进制为 110001

# 按位取反
print(~a)     # 输出 -61，二进制为 0000...0010111（取决于整数的大小）

# 左移
print(a << 1) # 输出 120，二进制为 11100000

# 右移
print(b >> 1) # 输出 6，二进制为 00110
```

位运算在处理二进制数据、优化算法性能（如某些加密算法、哈希函数）、硬件编程等方面非常有用。Python中的整数类型是任意精度的，这意味着位运算可以应用于非常大的整数，而不仅仅是固定大小的整数。

#### [338. 比特位计数*](https://leetcode.cn/problems/counting-bits/)

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n), O(1)
        # >>> 10 & 9  
        # 8  
        # >>> bin(10)  
        # '0b1010'  
        # >>> bin(9)  
        # '0b1001'  
        # >>> bin(8)  
        # '0b1000'  
        ans = [0]
        for i in range(1, n+1):
            ans.append(ans[i&(i-1)]+1)
        return ans
```


#### [136. 只出现一次的数字*](https://leetcode.cn/problems/single-number/)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n), O(1)
        # 异或运算满足交换律
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans
```


#### [1318. 或运算的最小翻转次数**](https://leetcode.cn/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

```python
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32): # 2**32 = 4 294 967 296
            x,y,z = (a>>i)&1,  (b>>i)&1,  (c>>i)&1
            ans += (x+y) if z == 0 else int((x+y)==0)
        return ans
```


## 前缀树

#### []()

```python

```


#### []()

```python

```



## 区间集合

#### []()

```python

```


#### []()

```python

```


## 单调栈

#### []()

```python

```


#### []()

```python

```