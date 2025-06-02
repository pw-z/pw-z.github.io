# Leetcode Study Plan Leetcode-75 Scratch Paper

*Created on 2024.05.28 by [pwz](http://pwz.wiki)* 

这是刷题的草稿纸，随笔写写思路，没有阅读价值。

题单地址：https://leetcode.cn/studyplan/leetcode-75/

简单：`*`  
中等：`**`  
困难：`***`

- [Leetcode Study Plan Leetcode-75 Scratch Paper](#leetcode-study-plan-leetcode-75-scratch-paper)
  - [数组/字符串](#数组字符串)
      - [1768. 交替合并字符串\*](#1768-交替合并字符串)
      - [1071. 字符串的最大公因子\*](#1071-字符串的最大公因子)
      - [1431. 拥有最多糖果的孩子\*](#1431-拥有最多糖果的孩子)
      - [605. 种花问题\*](#605-种花问题)
      - [345. 反转字符串中的元音字母\*](#345-反转字符串中的元音字母)
      - [151. 反转字符串中的单词\*\*](#151-反转字符串中的单词)
      - [238. 除自身以外数组的乘积\*\*](#238-除自身以外数组的乘积)
      - [443. 压缩字符串\*\*](#443-压缩字符串)
  - [双指针](#双指针)
      - [283. 移动零\*](#283-移动零)
      - [392. 判断子序列\*](#392-判断子序列)
      - [11. 盛最多水的容器\*](#11-盛最多水的容器)
      - [1679. K 和数对的最大数目\*\*](#1679-k-和数对的最大数目)
  - [滑动窗口](#滑动窗口)
      - [643. 子数组最大平均数 I\*](#643-子数组最大平均数-i)
      - [1456. 定长子串中元音的最大数目\*\*](#1456-定长子串中元音的最大数目)
      - [1004. 最大连续1的个数 III\*\*](#1004-最大连续1的个数-iii)
      - [1493. 删掉一个元素以后全为 1 的最长子数组\*\*](#1493-删掉一个元素以后全为-1-的最长子数组)
  - [前缀和](#前缀和)
      - [1732. 找到最高海拔\*](#1732-找到最高海拔)
      - [724. 寻找数组的中心下标\*](#724-寻找数组的中心下标)
  - [哈希](#哈希)
      - [2215. 找出两数组的不同\*](#2215-找出两数组的不同)
      - [1207. 独一无二的出现次数\*](#1207-独一无二的出现次数)
      - [1657. 确定两个字符串是否接近\*\*](#1657-确定两个字符串是否接近)
      - [2352. 相等行列对\*\*](#2352-相等行列对)
  - [栈](#栈)
      - [2390. 从字符串中移除星号\*\*](#2390-从字符串中移除星号)
      - [735. 小行星碰撞\*\*](#735-小行星碰撞)
      - [394. 字符串解码\*\*](#394-字符串解码)
  - [队列](#队列)
      - [933. 最近的请求次数\*](#933-最近的请求次数)
      - [649. Dota2 参议院\*\*](#649-dota2-参议院)
  - [链表](#链表)
      - [2095. 删除链表的中间节点\*\*](#2095-删除链表的中间节点)
      - [328. 奇偶链表\*\*](#328-奇偶链表)
      - [206. 反转链表\*](#206-反转链表)
      - [2130. 链表最大孪生和\*\*](#2130-链表最大孪生和)
  - [二叉树DFS](#二叉树dfs)
      - [104. 二叉树的最大深度\*](#104-二叉树的最大深度)
      - [872. 叶子相似的树](#872-叶子相似的树)
      - [1448. 统计二叉树中好节点的数目\*\*](#1448-统计二叉树中好节点的数目)
      - [437. 路径总和 III\*\*](#437-路径总和-iii)
      - [1372. 二叉树中的最长交错路径\*\*](#1372-二叉树中的最长交错路径)
      - [236. 二叉树的最近公共祖先](#236-二叉树的最近公共祖先)
  - [二叉树BFS](#二叉树bfs)
      - [199. 二叉树的右视图\*\*](#199-二叉树的右视图)
      - [1161. 最大层内元素和\*\*](#1161-最大层内元素和)
  - [二叉树BST](#二叉树bst)
      - [700. 二叉搜索树中的搜索\*](#700-二叉搜索树中的搜索)
      - [450. 删除二叉搜索树中的节点\*\*](#450-删除二叉搜索树中的节点)
  - [图DFS/BFS](#图dfsbfs)
      - [841. 钥匙和房间\*\*](#841-钥匙和房间)
      - [547. 省份数量\*\*](#547-省份数量)
      - [1466. 重新规划路线\*\*](#1466-重新规划路线)
      - [399. 除法求值\*\*](#399-除法求值)
      - [1926. 迷宫中离入口最近的出口\*\*](#1926-迷宫中离入口最近的出口)
      - [994. 腐烂的橘子\*\*](#994-腐烂的橘子)
  - [堆/优先队列](#堆优先队列)
      - [215. 数组中的第K个最大元素\*\*](#215-数组中的第k个最大元素)
      - [](#)
  - [动态规划·一维](#动态规划一维)
      - [1137. 第 N 个泰波那契数\*](#1137-第-n-个泰波那契数)
      - [](#-1)
  - [动态规划·多维](#动态规划多维)
      - [](#-2)
      - [](#-3)
  - [位运算](#位运算)
      - [338. 比特位计数\*](#338-比特位计数)
      - [136. 只出现一次的数字\*](#136-只出现一次的数字)
      - [1318. 或运算的最小翻转次数\*\*](#1318-或运算的最小翻转次数)
  - [二分查找](#二分查找)
      - [374. 猜数字大小\*](#374-猜数字大小)
      - [2300. 咒语和药水的成功对数\*\*](#2300-咒语和药水的成功对数)
      - [162. 寻找峰值\*\*](#162-寻找峰值)
      - [875. 爱吃香蕉的珂珂\*\*](#875-爱吃香蕉的珂珂)
  - [前缀树](#前缀树)
      - [](#-4)
      - [](#-5)
  - [区间集合](#区间集合)
      - [](#-6)
      - [](#-7)
  - [单调栈](#单调栈)
      - [](#-8)
      - [](#-9)


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


#### [605. 种花问题*](https://leetcode.cn/problems/can-place-flowers)

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


#### [345. 反转字符串中的元音字母*](https://leetcode.cn/problems/reverse-vowels-of-a-string)

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        # O(n), O(1)
        CACHE = set(['a','e','i','o','u','A','E','I','O','U'])
        l, r = 0, len(s)-1
        s = list(s)
        n = len(s)
        while l < r:
            while l < n and s[l] not in CACHE:
                l += 1
            while r > 0 and s[r] not in CACHE:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
```


#### [151. 反转字符串中的单词**](https://leetcode.cn/problems/reverse-words-in-a-string)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # O(n), O(n)
        words = s.split()
        l, r = 0, len(words)-1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return ' '.join(words)
```


#### [238. 除自身以外数组的乘积**](https://leetcode.cn/problems/product-of-array-except-self/)

```python
class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        # O(n), O(n)
        n = len(nums)
        pre = [nums[0]] * n # 前缀积
        suf = [nums[-1]] * n # 后缀积
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i]

        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] * nums[i]
        
        nums[0], nums[n-1] = suf[1], pre[n-2]
        for i in range(1, n-1):
            nums[i] = pre[i-1] * suf[i+1]
        return nums

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n), O(1)
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        tmp = 1
        for i in range(n-2, -1, -1):
            tmp *= nums[i+1]
            ans[i] *= tmp
        return ans
```


#### [443. 压缩字符串**](https://leetcode.cn/problems/string-compression)

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        # O(n), O(1)
        n = len(chars)
        last = 0
        write = 0
        for read in range(n):
            # 到了边界或者字符有变化，开始处理写操作
            if read == n-1 or chars[read] != chars[read+1]:
                chars[write] = chars[read]
                write += 1
                length = read - last + 1
                
                # 处理写入操作
                if length > 1:
                    s = str(length)
                    # print(write, length, last, read, s)
                    for num in s:
                        chars[write] = num
                        write += 1
                
                last = read + 1
        return write
```

> Prompt: 帮我分析这段函数的空间复杂度：*代码略

这段代码是一个Python类`Solution`中的方法`compress`，它的目的是对一个字符列表`chars`进行压缩。压缩的规则是将连续出现的相同字符用单个字符和它的计数来表示。例如，如果字符列表是`"aaabccc"`，压缩后的结果是`"a2b1c2"`。

现在我们来分析这段代码的空间复杂度：

1. **输入数据**：`chars`是一个列表，其长度为`n`。

2. **变量使用**：
   - `n`：长度为1的整数，存储了`chars`的长度。
   - `last`：用于记录连续字符的起始位置，长度为1的整数。
   - `write`：用于记录写入新字符和计数的位置，长度为1的整数。
   - `read`：循环变量，用于遍历`chars`，长度为1的整数。
   - `length`：记录连续字符的数量，长度为1的整数。
   - `s`：用于存储`length`转换为字符串的临时变量，其长度取决于`length`的值。

3. **空间复杂度分析**：
   - 除了输入列表`chars`，代码中使用的所有变量都是单个整数或单个字符串，它们的空间占用都是常数级别的。
   - 字符串`s`的长度取决于`length`的值，但`length`的最大值不会超过`n`（因为连续字符最多是`n`个）。
   - 因此，除了输入的`chars`列表，额外的空间复杂度是O(1)，即常数级别的。

4. **总结**：这段代码的空间复杂度主要由输入列表`chars`决定，即O(n)，其中n是`chars`的长度。代码中的其他变量占用的空间是常数级别的，不影响总体的空间复杂度。

注意，这里的分析假设`chars`列表在函数内部不会被复制，如果`chars`是作为输入参数传入，并且函数内部对它进行了修改，那么实际上并没有额外的空间消耗。如果`chars`被复制了，那么空间复杂度将是O(n)。但从代码本身来看，它直接在输入的`chars`上进行操作，没有进行复制。

> Prompt: s = str(length)这段代码每次循环里都在执行，这个变量被反复的创建，怎么理解这样也算是常量级别的空间复杂度？

抱歉，我之前的解释有误。让我们重新分析这部分代码。

变量`s`在每次循环中确实被创建，但它的创建和销毁都是局部的，并且它的大小取决于`length`的值。`length`的值是连续相同字符的数量，这个值在任何时候都不会超过`n`（列表`chars`的长度）。因此，`s`的最大长度是`log10(n)`（因为`n`的数值需要的数字数量最多是`log10(n)`）。这意味着`s`的大小是与输入规模`n`成对数关系的，而不是线性关系。

然而，即使`s`的大小是`O(log n)`，它仍然不是影响整体空间复杂度的主要因素，因为`s`只是一个局部变量，每次循环结束时都会被销毁，不会在整个函数的生命周期中持续占用空间。

关键的空间消耗在于输出列表`chars`。在最坏的情况下，如果所有字符都是唯一的，那么`chars`需要的空间将是原始列表长度的两倍（因为每个字符后面都需要跟一个计数）。但是，由于`chars`是输入参数，我们通常不将其计入空间复杂度的计算中，除非我们创建了它的一个新副本。

所以，如果我们只考虑函数内部除了输入参数之外的额外空间使用，那么：

- 所有循环变量和局部变量（包括`s`）都是常数级别的或对数级别的。
- 函数的输出是通过修改输入的`chars`列表实现的，没有创建任何新的列表副本。

因此，从这个角度来看，函数的额外空间复杂度是`O(1)`，即常数级别的。但是，如果我们将`chars`列表的空间消耗考虑在内，整体的空间复杂度将是`O(n)`，其中`n`是输入列表的长度。这里的`O(n)`是针对整个算法而言的，而不是单独的某个变量。


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


#### [392. 判断子序列*](https://leetcode.cn/problems/is-subsequence/)

```python
class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        # O(n), O(1)
        ps = pt = 0
        ls, lt = len(s), len(t)
        while ps < ls and pt < lt:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        return ps == ls

    def isSubsequence(self, s: str, t: str) -> bool:
        # O(n), O(1)
        if not s: return True
        p = 0
        for c in t:
            if s[p] == c:
                p += 1
                if p == len(s):
                    return True
        return False
```


#### [11. 盛最多水的容器*](https://leetcode.cn/problems/container-with-most-water/)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n), O(1)
        l, r = 0, len(height)-1
        max_area = 0
        while l < r:
            cur_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, cur_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
```


#### [1679. K 和数对的最大数目**](https://leetcode.cn/problems/max-number-of-k-sum-pairs/)

```python
class Solution:
    def maxOperations1(self, nums: List[int], k: int) -> int:
        # 哈希
        # O(N), O(N)
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        
        ans = 0
        for i in nums:
            if (hashmap[i] > 0 and hashmap[k-i] > 0 and i != (k-i)) or (i == (k-i) and hashmap[i]>1):
                hashmap[k-i] = hashmap[k-i]-1
                hashmap[i] = hashmap[i]-1
                ans += 1
        return ans

    def maxOperations2(self, nums: List[int], k: int) -> int:
        # 哈希，逻辑简化 Refer：https://leetcode.cn/problems/max-number-of-k-sum-pairs/solutions/2701378/on-yi-ci-bian-li-pythonjavacgojsrust-by-r7obc
        # O(N), O(N)
        hashmap = defaultdict(int)

        ans = 0
        for i in nums:
            if hashmap[k-i]:
                hashmap[k-i] -= 1
                ans += 1
            else:
                hashmap[i] += 1 # 边遍历边初始化哈希表
        return ans
```


## 滑动窗口

> Prompt for 通义2.5 总结一下滑动窗口能解决的常规问题类型，并给出对应的算法思路

滑动窗口算法是一种强大的技术，尤其适用于处理数组、字符串中与“连续子序列”相关的各种问题。以下是一些滑动窗口能有效解决的常规问题类型及其对应的算法思路概述：

1. **子数组/子串的最值问题**：
   - **问题示例**：如力扣第239题“滑动窗口最大值”，需要找到大小为k的子数组中的最大值。
   - **算法思路**：使用双端队列（deque）维护可能的最大值的索引，当窗口右移时，及时移除不再窗口内的元素的索引，并保持队列降序。队首元素即为当前窗口最大值。

2. **子数组的和达到目标值**：
   - **问题示例**：如LeetCode第209题“长度最小的子数组”，要求找到和至少为目标值的最小子数组长度。
   - **算法思路**：使用两个指针定义窗口边界，一个右移扩大窗口求和，若总和超过目标值则左指针右移缩小窗口，同时记录最小窗口长度。

3. **子串包含所有字符（覆盖子串问题）**：
   - **问题示例**：如LeetCode第76题“最小覆盖子串”，寻找包含另一个字符串所有字符的最小子串。
   - **算法思路**：使用两个指针定义窗口，一个右移尝试扩展窗口，同时用哈希表记录窗口内字符频次与目标字符集的比较，满足条件时尝试缩小窗口左边界。

4. **特定模式或条件的子串计数**：
   - **问题示例**：计算字符串中满足特定条件（如连续字符不重复的子串）的数量。
   - **算法思路**：滑动窗口遍历字符串，用哈希表或计数器检查当前窗口是否满足条件，满足则计数并移动窗口右边界。

5. **连续元素频率统计**：
   - **问题示例**：统计数组中连续K个元素出现次数最多的元素及其频率。
   - **算法思路**：维护一个大小为K的窗口，使用哈希表记录元素频率，随着窗口移动更新哈希表并记录最大频率。

6. **平滑数据处理**：
   - **问题示例**：计算一段时间序列数据的滚动平均值。
   - **算法思路**：窗口在数据序列上滑动，每次计算窗口内所有数据的平均值，随窗口移动更新平均值。

滑动窗口的核心在于动态调整窗口大小，通过两个（或一个）指针的移动来高效遍历原数据，配合合适的数据结构（如哈希表、队列）来记录窗口状态，从而达到解决问题的目的。


> Prompt for 通义2.5 分析一下双指针技巧与滑动窗口算法的关系

双指针技巧和滑动窗口算法之间存在紧密的联系，可以说滑动窗口算法是双指针技巧的一个具体应用或扩展形式。

**双指针技巧概述**

双指针技巧是一种广泛应用于数组或字符串处理中的编程策略，通过使用两个指针（通常标记为`left`和`right`）来遍历或操作数据结构。这种技巧可以根据问题需求采用不同的策略，比如：

- **对撞指针**：两个指针从两端向中间移动，常用于查找数组中的目标对或翻转操作。
- **快慢指针**：一个指针移动速度比另一个快，常用于链表循环检测或删除操作。
- **滑动窗口**：一个或两个指针动态调整窗口大小，保持窗口内元素满足特定条件。

**滑动窗口算法**

滑动窗口算法本质上是双指针技巧的一个特例，它利用左右指针维护一个“窗口”，这个窗口在数据结构（如字符串、数组）上滑动，以寻找满足特定条件的子序列。其基本流程包括：

1. **初始化窗口**：通常将左右指针初始化为数据结构的起始位置，窗口大小为0或最小值。
2. **扩大窗口**：右指针向右移动，增加窗口大小，直至窗口满足题目给定的条件（如特定字符数量、和的范围等）。
3. **优化解并可能缩小窗口**：在窗口满足条件的情况下，考虑是否可以通过移动左指针来优化解（如减少子序列长度、提高某些指标等），同时确保窗口仍满足条件。
4. **重复步骤2和3**：持续调整窗口大小，直至右指针无法继续移动。

**关系总结**

- **概念上**：双指针是一种更广泛的概念，涵盖了多种通过两个指针协同工作来解决问题的方法，而滑动窗口是双指针在特定场景下的一种应用，专注于处理连续子序列问题。
- **实现上**：滑动窗口算法通常实现为双指针法中的“左右指针法”，通过动态调整左右指针的位置来控制窗口的大小和位置，以求解特定目标。
- **目的上**：两者都旨在通过减少遍历次数和空间复杂度来高效解决问题，但滑动窗口算法特别适用于那些需要在序列中寻找特定模式或统计信息的问题。

综上所述，滑动窗口算法是双指针技巧在特定问题领域的一个高效实现方式，体现了双指针技巧的灵活性和强大功能。


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


#### [1456. 定长子串中元音的最大数目**](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # O(N), O(1)

        # init ans
        target = set(['a', 'e', 'i', 'o', 'u'])
        ans = tmp_ans = sum([1 if c in target else 0 for c in s[:k]])
        print(ans)

        # double pointers
        l, r = 0, k
        n = len(s)
        for r in range(k, n):
            tmp_ans -= 1 if s[l] in target else 0
            tmp_ans += 1 if s[r] in target else 0
            ans = max(ans, tmp_ans)
            l += 1
        return ans
```


#### [1004. 最大连续1的个数 III**](https://leetcode.cn/problems/max-consecutive-ones-iii/)

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 题解：https://leetcode.cn/problems/max-consecutive-ones-iii/solutions/2126631/hua-dong-chuang-kou-yi-ge-shi-pin-jiang-yowmi
        # O(N), O(1)
        ans = l = cnt0 = 0
        for r in range(len(nums)):
            cnt0 += 1-nums[r]
            while cnt0 > k:
                cnt0 -= 1 - nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
```


#### [1493. 删掉一个元素以后全为 1 的最长子数组**](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/)

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # O(N), O(1)
        # 思路：遇到1个0的情况下可以继续拓展窗口，2个0的情况下窗口左边届更新到上一个0的右侧
        ans = l = cnt0 = last0 = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt0 += 1
                if cnt0 == 1:
                    last0 = r
            if cnt0 > 1:
                l = last0+1
                cnt0 -= 1
                last0 = r
            ans = max(ans, r-l+1)
        return max(ans - 1, 0)
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

数据结构中的栈（Stack）是一种线性数据结构，其特点是只允许在数据结构的一端进行插入和删除操作。这一端被称为栈顶（Top），而另一端固定不变，被称为栈底（Bottom）。栈的操作遵循“后进先出”（Last In, First Out, LIFO）的原则，即最后存入栈中的元素最先被取出。

栈的基本概念

- **栈顶（Top）**：栈中允许进行插入和删除操作的一端，新元素总是被添加到这里，同时这里也是移除元素的地方。
- **栈底（Bottom）**：栈的另一端，通常不允许进行插入和删除操作，用于标记栈的起始位置。
- **空栈**：不含任何元素的栈。
- **压栈（Push）**：向栈顶添加一个元素的操作，相当于入栈。
- **弹栈（Pop）**：从栈顶移除一个元素的操作，同时可以返回这个元素，相当于出栈。
- **栈顶元素（Top Element）**：最后一次压栈的元素，它位于栈顶，是下一个将要被弹出的元素。

栈的实现方式

栈可以通过两种主要方式实现：
- **基于数组的栈**：使用数组作为底层存储结构，通过索引追踪栈顶位置，入栈时增加索引，出栈时减少索引。
- **基于链表的栈**：使用链表结构，其中每个节点包含数据和指向下一个节点的指针。栈顶节点是最容易访问的节点，入栈和出栈操作通过修改链表的头部指针来完成。

栈的应用

栈因其独特的LIFO特性，在多个领域和算法中有广泛应用：
- **函数调用和递归**：在程序运行时，调用栈用来存储函数的返回地址和局部变量。
- **表达式求值**：用于解析和计算算术表达式，如中缀转后缀表达式或直接计算后缀表达式。
- **括号匹配**：验证括号序列是否合法，如编程语言中的圆括号、方括号等。
- **深度优先搜索（DFS）**：在图和树的遍历中，栈用于实现递归或非递归的深度优先搜索策略。
- **回溯算法**：解决约束满足问题时，栈用来存储状态，以便在探索失败时回溯到前一状态。
- **内存管理**：操作系统和编程语言运行时环境使用栈来管理函数调用栈和局部变量的内存分配。

总之，栈作为一种基础且强大的数据结构，在计算机科学的许多方面都扮演着重要角色。


#### [2390. 从字符串中移除星号**](https://leetcode.cn/problems/removing-stars-from-a-string/)

```python
class Solution:
    def removeStars(self, s: str) -> str:
        # O(N), O(N)
        # stack = deque()
        stack = []
        for c in s:
            if c != '*':
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)
```


#### [735. 小行星碰撞**](https://leetcode.cn/problems/asteroid-collision/)

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for cur in asteroids:

            # 不是符号相反就一定会碰撞的，要具体看方向是否相对
            # 本题的方向来看，一定是前面有向右的，当前是向左的才会碰撞
            # if not st or (cur * st[-1] > 0):
            #     st.append(cur)
            # else:
            #     # 所有比当前小的都爆炸
            #     while st and abs(st[-1]) < abs(cur):
            #         st.pop()
            #     # 要么栈空了，要么遇到更大的了，要么遇到同等大小的了
            #     if not st:
            #         st.append(cur)
            #     elif abs(st[-1]) == abs(cur):
            #         st.pop()

            alive = True
            while alive and cur < 0 and st and st[-1] > 0:
                alive = st[-1] < -cur 
                if st[-1] <= -cur:
                    st.pop()
            if alive:
                st.append(cur)
        return st
```


#### [394. 字符串解码**](https://leetcode.cn/problems/decode-string/)

```python
class Solution:
    def decodeString(self, s: str) -> str:
        # O(N), O(N)
        st = []
        for c in s:
            if c != ']':
                st.append(c)
            else:
                patten = ""
                while st and st[-1] != '[':
                    patten = st.pop() + patten
                st.pop() # pop '['
                # print("got patten: ", patten)

                number = ""
                while st and st[-1] in "0123456789":
                    number = st.pop() + number
                # print("got number: ", number)
                st.append(patten * int(number))

        return ''.join(st)
```


## 队列

#### [933. 最近的请求次数*](https://leetcode.cn/problems/number-of-recent-calls)

```python
class RecentCounter:

    def __init__(self):
        self.dq = collections.deque()


    def ping(self, t: int) -> int:
        self.dq.append(t)
        while t - 3000 > self.dq[0]:
            self.dq.popleft()
        return len(self.dq)
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```


#### [649. Dota2 参议院**](https://leetcode.cn/problems/dota2-senate/)

```python
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # O(N)不会超过N次投票就可以决出胜负, O(N)
        q = deque(senate)
        cnt = Counter(senate)
        ban_cnt = {'R':0, 'D':0} # 当前每一方有多少被ban的票数
        convert_map = {'R':'D', 'D':'R'}
        ans_map = {'R': 'Radiant', 'D':'Dire'}
        while q:
            cur = q.popleft()
            if ban_cnt[cur] > 0: # 若被ban票数>0，则直接跳过，消耗一个被ban名额
                ban_cnt[cur] -= 1
            else: # 否则就是给对方阵营ban一票，并将对方阵营人员总数-1
                ban_cnt[convert_map[cur]] += 1
                q.append(cur)
                cnt.subtract(convert_map[cur])

            if cnt[convert_map[cur]] <= 0: # 任意一方的人员总数被ban到小于等于0时则投票结束
                return ans_map[cur]
```


## 链表


#### [2095. 删除链表的中间节点**](https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针，O(N), O(1)
        _head = ListNode()
        _head.next = head
        slow = _head
        fast = _head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
            else:
                slow.next = slow.next.next
                break
        # fast在偶数情况走到最后一个节点会跳出上面的while循环
        if fast:
            slow.next = slow.next.next
        return _head.next

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 代码简化
        slow, fast, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = pre.next.next
        return head
```


#### [328. 奇偶链表**](https://leetcode.cn/problems/odd-even-linked-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        even_head = head.next
        odd, even = head, even_head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
```


#### [206. 反转链表*](https://leetcode.cn/problems/reverse-linked-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N), O(1)
        cur, last = head, None
        while cur:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp
        return last
```


#### [2130. 链表最大孪生和**](https://leetcode.cn/problems/maximum-twin-sum-of-a-linked-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 先把一半反转掉，然后从中间向两侧扩散，最后再把反转恢复
        ans = 0
        slow, fast, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        # print(slow, pre)

        mid_start = pre # 上半段的终点，等会还原用
        post_part = slow # 下半段的起点
        while pre and slow:
            ans = max(ans, pre.val + slow.val)
            slow = slow.next
            pre = pre.next
        # 还原前半段链表（非必要，仅仅出于规范）
        # print(mid_start, post_part)
        slow, fast, pre = mid_start, mid_start, post_part
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        slow.next = pre
        head = slow
        # print(head) # 确认还原成功

        return ans
```


## 二叉树DFS

二叉树的深度优先搜索（Depth-First Search, DFS）是一种遍历策略，旨在访问二叉树中的所有节点。这种遍历方法沿着树的深度方向进行，尽可能深地探索每一条分支，然后再回溯。在二叉树中，DFS主要有三种常见的遍历顺序：前序遍历、中序遍历和后序遍历。

深度优先搜索通常采用递归实现，因为递归天然符合深度优先的探索逻辑。在递归过程中，函数调用自身来处理子树，直到遇到叶子节点（无子节点的节点），然后逐级返回。递归算法简洁明了，但需要注意的是，对于极深的树可能会导致栈溢出的问题。此外，也可以使用栈来实现非递归的深度优先搜索，这种方式更加灵活，可以避免栈溢出的问题。

深度优先搜索在解决诸如查找、统计、验证等涉及树或图结构的问题时非常有用。例如，它可以用来计算树的深度、检查树中是否存在某个值、确定两个节点间是否存在路径等。此外，DFS也是许多图算法的基础，如图的连通性分析、拓扑排序等。


#### [104. 二叉树的最大深度*](https://leetcode.cn/problems/maximum-depth-of-binary-tree)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # O(N), O(N)

        def dfs(_root, cur_depth):
            if not _root:
                return cur_depth
            return max(dfs(_root.left, cur_depth+1), dfs(_root.right, cur_depth+1))
           
        return dfs(root, 0)
```


#### [872. 叶子相似的树](https://leetcode.cn/problems/leaf-similar-trees)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # O(n+m), O(n+m)
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                # print('this is a leaf: ', node.val)
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root1) == dfs(root2)
```


#### [1448. 统计二叉树中好节点的数目**](https://leetcode.cn/problems/count-good-nodes-in-binary-tree)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # O(N), O(N)

        def dfs(node, maxever):
            if not node:
                return 0

            goodcnt = 0
            if node.val >= maxever:
                goodcnt += 1
            maxever = max(maxever, node.val)
            return goodcnt + dfs(node.left, maxever) + dfs(node.right, maxever)
        
        return dfs(root, root.val)
```


#### [437. 路径总和 III**](https://leetcode.cn/problems/path-sum-iii)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 题解：https://leetcode.cn/problems/path-sum-iii/solutions/2784856/zuo-fa-he-560-ti-shi-yi-yang-de-pythonja-fmzo
        # O(N), O(N)
        ans = 0
        cnt = collections.defaultdict(int)
        cnt[0] = 1

        def dfs(node, s):
            if not node:
                return
            nonlocal ans
            s += node.val
            ans += cnt[s - targetSum]
            cnt[s] += 1
            dfs(node.left, s)
            dfs(node.right, s)
            cnt[s] -= 1

        dfs(root, 0)
        return ans
```


#### [1372. 二叉树中的最长交错路径**](https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/solutions/147425/er-cha-shu-zhong-de-zui-chang-jiao-cuo-lu-jing-b-2
        # O(n), O(1)
        ans = 0

        def dfs(node, dir, length):
            # 0左1右
            if not node:
                return
            nonlocal ans
            ans = max(ans, length)
            if dir == 0:
                dfs(node.left, 1, length+1)
                dfs(node.right, 0, 1)
            else:
                dfs(node.right, 0, length+1)
                dfs(node.left, 1, 1)
        
        dfs(root, 0, 0)
        dfs(root, 1, 0)
        return ans
```


#### [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # O(N), O(N)
        def dfs(node):
            if not node:
                return
            
            if node.val == p.val or node.val == q.val:
                return node
            else:
                l = dfs(node.left)
                r = dfs(node.right)
                if not l: return r
                if not r: return l
                return node
        return dfs(root) 
```


## 二叉树BFS

广度优先搜索（Breadth-First Search, BFS）是一种用于遍历或搜索树或图数据结构的算法。与深度优先搜索沿着树的深度深入不同，广度优先搜索倾向于首先探索离起点更近的节点，然后逐步扩展到更远的节点。它是一种分层的搜索策略，确保在移动到下一层之前，同一层次的所有节点都被访问过。

基本原理

广度优先搜索通常使用队列数据结构来实现。算法的基本步骤如下：

1. **初始化**：从起始节点（根节点）开始，将这个节点放入队列中。
2. **循环**：当队列非空时，执行以下操作：
   - **出队**：从队列头部取出一个节点，这个节点是当前层中待访问的第一个节点。
   - **访问**：对取出的节点进行所需的操作（比如打印节点值，标记节点已访问等）。
   - **入队**：将取出节点的所有未被访问过的邻接节点（子节点）放入队列的尾部。这样，队列中保持了下一个要访问的节点层。
3. **结束**：当队列变空时，搜索结束，所有可达节点都已被访问。

特点与优势

- **最短路径**：BFS保证能找到从起点到任意可达节点的最短路径，因此常用于寻找图中的最短路径问题。
- **层次遍历**：由于按层次遍历，BFS能很容易地给出树或图的层次结构信息。
- **资源利用**：适合于目标可能较近的情况，因为它先检查距离起点近的节点，避免了不必要的深度探索。
- **多任务合作**：在分布式爬虫系统中，广度优先搜索有利于多个爬虫协作，减少重复抓取，提高效率。

应用场景

- **社交网络分析**：找到两个人之间的最短关系链。
- **游戏**：解决迷宫问题，寻找最短的逃脱路径。
- **网络爬虫**：按照链接的层次抓取网页，优先抓取重要页面。
- **图的连通性判断**：确定图是否连通，找出连通分量。
- **拓扑排序**：在有向无环图中确定任务的执行顺序。

总之，广度优先搜索是一种强大且广泛应用的算法，特别适用于需要考虑节点间距离或层级关系的问题场景。


#### [199. 二叉树的右视图**](https://leetcode.cn/problems/binary-tree-right-side-view/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # O(n), O(n)
        if not root:
            return []

        q = collections.deque([root])
        tmp = []
        ans = []
        while q:
            cur = q.popleft()
            if cur.left: tmp.append(cur.left)
            if cur.right: tmp.append(cur.right)

            if not q:
                ans.append(cur.val)
                q = deque(tmp)
                tmp = []

        return ans
```


#### [1161. 最大层内元素和**](https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # O(n), O(n)
        q = collections.deque([root])
        tmp = []
        lvl_sum, max_sum, ans_lvl, cur_lvl = 0, -float('inf'), 1, 1
        while q:
            cur = q.popleft()
            lvl_sum += cur.val
            if cur.left: tmp.append(cur.left)
            if cur.right: tmp.append(cur.right)

            if not q:
                if lvl_sum > max_sum:
                    ans_lvl, max_sum = cur_lvl, lvl_sum
                q = deque(tmp)
                tmp = []
                cur_lvl += 1
                lvl_sum = 0

        return ans_lvl
```


## 二叉树BST

二叉搜索树（Binary Search Tree，BST），有时也称为二叉排序树或二叉查找树，是一种特殊的二叉树数据结构，它满足以下特性：

1. **有序性**：对于BST中的每一个节点，其左子树中所有节点的值都严格小于该节点的值，而其右子树中所有节点的值都严格大于该节点的值。这意味着，如果从根节点出发，向左走会遇到越来越小的值，向右走则会遇到越来越大的值。

2. **唯一性**：在二叉搜索树中，没有键值相等的节点，即每个节点的值都是唯一的。

3. **结构特性**：BST可以是空树，或者是由上述性质定义的左子树和右子树组成的一个树结构。这意味着二叉搜索树的每个子树也是一个二叉搜索树。

**优点**：
- **快速查找**：对于给定值的查找、插入和删除操作，二叉搜索树相较于无序的链表或数组能提供更快的平均性能。查找、最大值和最小值操作都可以达到O(log n)的时间复杂度，在树平衡时。
- **有序遍历**：容易实现有序遍历（如中序遍历），自然得到升序或降序序列，这对于排序和范围查询非常有用。

**缺点**：
- **不平衡问题**：在最坏情况下（例如，树退化成链表状），二叉搜索树的性能会退化到O(n)，这在插入或删除操作导致树变得严重不平衡时可能发生。
- **维护成本**：为了保持高效的查找性能，可能需要额外的成本来维持树的平衡，如通过AVL树或红黑树这样的自平衡二叉搜索树来实现。

**应用场景**：
- 文件系统和数据库系统中用于高效排序与检索。
- 实现动态集合，支持快速插入、删除和查找操作。
- 实现符号表和关联数组，用于编译器和解释器的符号表管理。
- 数据压缩算法中，如Huffman编码树的构建。

二叉搜索树是数据结构中的基础概念之一，广泛应用于算法设计和软件开发中。

BST不必是完全二叉树，必须是完全二叉树的数据结构通常是堆（Heap），特别是二叉堆。二叉堆是一种特殊的完全二叉树，其中每个父节点的值都小于（或等于）其子节点的值（在最小堆中）或大于（或等于）其子节点的值（在最大堆中）。

#### [700. 二叉搜索树中的搜索*](https://leetcode.cn/problems/search-in-a-binary-search-tree)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # O(n), O(1)
        node = root
        while node:
            if node.val == val:
                return node
            if val < node.val:
                node = node.left
            else:
                node = node.right
```


#### [450. 删除二叉搜索树中的节点**](https://leetcode.cn/problems/delete-node-in-a-bst)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # try to find the key
        node = root
        parent = None
        while node and node.val != key:
            parent = node
            if node.val > key:
                node = node.left
            else:
                node = node.right

        # found node that match the key
        if node:
            # put left to the most left pos of right
            if node.right and node.left:
                tmp = node.right
                while tmp.left:
                    tmp = tmp.left
                tmp.left = node.left

            # handle the child of the node
            if node.right:
                if not parent: # node == root
                    root = node.right
                elif parent.left and parent.left.val == key:
                    parent.left = node.right
                else:
                    parent.right = node.right
            elif node.left:
                if not parent: # node == root
                    root = node.left
                elif parent.left and parent.left.val == key:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else: # the node has no child
                if not parent: # node == root
                    root = None
                elif parent.left and parent.left.val == key:
                    parent.left = None
                else:
                    parent.right = None
                
        return root
```


## 图DFS/BFS


#### [841. 钥匙和房间**](https://leetcode.cn/problems/keys-and-rooms/)

DFS/BFS 样板间；

```python
class Solution:
    def canVisitAllRooms1(self, rooms: List[List[int]]) -> bool:
        # BFS O(n), O(n)
        visit, q = set([0]), collections.deque([0])
        while q:
            cur = q.popleft()
            for k in rooms[cur]:
                if k not in visit:
                    q.append(k)
                    visit.add(k)
        return len(visit) == len(rooms)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # DFS O(n), O(n)
        visit, s = set([0]), [0]
        while s:
            cur = s.pop()
            for k in rooms[cur]:
                if k not in visit:
                    visit.add(k)
                    s.append(k)
        return len(visit) == len(rooms)
```


#### [547. 省份数量**](https://leetcode.cn/problems/number-of-provinces/)

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # DFS O(N^2), O(N)
        visited = set()
        stack = []
        n = len(isConnected)
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                stack.append(i)
                # print("handle i= ", i, " stack = ", stack)
                while stack:
                    cur = stack.pop()
                    conn = isConnected[cur]
                    for idx in range(n):
                        if idx not in visited:
                            isConn = conn[idx]
                            if isConn == 1:
                                visited.add(idx)
                                stack.append(idx)
        return ans
```


#### [1466. 重新规划路线**](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

```python
class Solution:
    # 题解：https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/solutions/2553195/zhong-xin-gui-hua-lu-xian-by-leetcode-so-psl6
    # O(N), O(N)
    def dfs(self, x, parent, e):
        res = 0
        for edge in e[x]:
            if edge[0] == parent:
                continue
            res += edge[1] + self.dfs(edge[0], x, e)
        return res
            
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        e = [[] for _ in range(n)]
        for ee in connections:
            e[ee[0]].append([ee[1], 1])
            e[ee[1]].append([ee[0], 0])
        # print(e)
        return self.dfs(0, -1, e)

        # 输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        # 输出：3
        # 解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
        # [
        #     [[1, 1], [4, 0]], 
        #     [[0, 0], [3, 1]], 
        #     [[3, 1]], 
        #     [[1, 0], [2, 0]], 
        #     [[0, 1], [5, 1]], 
        #     [[4, 0]]
        # ]
```


#### [399. 除法求值**](https://leetcode.cn/problems/evaluate-division)

并查集（Disjoint Set Union, DSU）是一种高效的数据结构，用于处理不相交集合的合并（Union）和查询（Find）问题。它常用于解决诸如判断两个元素是否属于同一个集合、统计集合的数量、合并两个集合等问题。并查集的核心在于通过“并”（Union）操作将多个集合合并成一个集合，同时通过“查”（Find）操作快速判断元素的归属关系。

数据结构

并查集通常使用一个数组（称为parent数组或father数组）来表示集合关系，数组的索引代表集合中的元素，数组的值指向该元素所在集合的代表元素（通常是该集合的根节点）。初始时，每个元素都自成一个集合，parent数组中每个元素都指向自己。

基本操作

- **查找（Find）**：确定一个元素所属集合的代表元素。通常使用递归或路径压缩的方式来优化查找效率，其中路径压缩可以在查找过程中将路径上的所有节点直接连接到根节点，从而减少后续查找的时间。
- **合并（Union）**：将两个集合合并为一个集合。具体操作是找到两个集合的代表元素，将其中一个集合的代表元素指向另一个集合的代表元素，实际操作中可能还需要考虑两个集合的大小，以便高效平衡树的高度。

实现技巧

- **路径压缩**：在执行Find操作的过程中，将沿途访问的所有节点的parent指针直接指向根节点，这样下次查询时路径会更短。
- **按秩合并**（Rank-based Union）：维护一个额外的rank数组来记录树的高度或节点数量，合并时总是将rank较小的集合连接到rank较大的集合上，以此来尽量保持树的平衡，减少Find操作的深度。

时间复杂度

- 不采用任何优化时，查找和合并操作的时间复杂度均为O(n)，其中n是集合中元素的数量。
- 使用路径压缩和按秩合并后，Find和Union操作的平均时间复杂度可以降低到接近O(α(n))，其中α(n)是一个缓慢增长的函数，对于实际的n值来说，α(n)几乎是一个常数，大约为4左右。

并查集广泛应用于各种场景，如社交网络的朋友圈判断、图的连通性判断、最小生成树算法中的优化、赛事调度等。


```python
class Solution:
    # 图 + DFS，官解的并查集晚点再研究...

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(node, v, target):
            if node not in g: return False
            if node == target: return v
            visited.add(node)
            for next, r in g[node]:
                if next in visited: continue
                res = dfs(next, v*r, target)
                if res: return res
            return False

        g = defaultdict(list)
        for (x, y), r in zip(equations, values):
            g[x].append((y, r))
            g[y].append((x, 1/r))
            # print(g)
        ans = []
        for x, y in queries:
            visited = set()
            tmp = dfs(x, 1, y)
            ans.append(tmp) if tmp else ans.append(-1)
        return ans
```


#### [1926. 迷宫中离入口最近的出口**](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze)

广度优先搜索（Breadth-First Search, BFS）是一种遍历或搜索树和图的算法，它从一个节点开始，逐层遍历所有节点。在图的BFS算法中，通常遵循以下步骤：

1. 初始化：选择一个起始节点，将其标记为已访问，并将其加入到一个队列中。
2. 遍历队列：当队列不为空时，执行以下操作：
   * 从队列中取出一个节点，称为当前节点。
   * 遍历当前节点的所有未访问邻居节点：
     * 如果邻居节点未被访问，将其标记为已访问，并将其加入队列中。
3. 记录层级：在访问每个节点时，可以记录它与起始节点的距离，这通常通过一个距离数组来实现。
4. 处理特殊需求：根据题目的具体要求，可能需要记录最短路径、搜索特定节点或解决其他问题。
5. 结束条件：当队列为空时，BFS遍历结束。

BFS算法通常用于以下场景：
* 寻找最短路径。
* 确定节点之间的连通性。
* 搜索特定节点。


```python
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 队列, O(mn), O(1)
        m, n = len(maze), len(maze[0])
        q = collections.deque()
        q.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            cur = q.popleft()
            x, y, d = cur[0], cur[1], cur[2]
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                xx = x + dx
                yy = y + dy
                if 0 <= xx < m and 0 <= yy < n and maze[xx][yy] == '.':
                    if xx == 0 or xx == m-1 or yy == 0 or yy == n-1:
                        return d+1
                    q.append((xx, yy, d+1))
                    maze[xx][yy] = '+'
        return -1
```


#### [994. 腐烂的橘子**](https://leetcode.cn/problems/rotting-oranges)

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # O(mn), O(1)
        # 初始化队列为所有的腐烂橘子坐标，每轮将队列处理完毕后再将下一波的腐烂橘子入队，最后一波处理完检查是否还有好橘子
        m, n = len(grid), len(grid[0])
        q = deque() # 当前波次的烂橘子队列
        mid_q = deque() # 下一波烂橘子，区分波次方便记录时间
        good = 0
        ans = 0

        # 统计橘子
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good += 1
                elif  grid[i][j] == 2:
                    q.append((i, j))
        
        while q:
            cur = q.popleft()
            x, y = cur[0], cur[1]
            for (x, y) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2;
                    good -= 1
                    mid_q.append((x, y))
            if not q and mid_q:
                ans += 1
                q = mid_q
                mid_q = deque()
        
        return ans if good == 0 else -1
```


## 堆/优先队列


#### [215. 数组中的第K个最大元素**](https://leetcode.cn/problems/kth-largest-element-in-an-array)

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # O(nlogn)
        # nums.sort(reverse = True)
        # return nums[k-1]

        # O(N)
        # 基于快排解决TopK问题，经典问题场景，检索查看更多
        def quick(nums, k):
            more, equal, less = [], [], []
            base = nums[0]
            for n in nums:
                if n > base:
                    more.append(n)
                elif n < base:
                    less.append(n)
                else:
                    equal.append(n)
            # e.g.
            #    less | equal | more
            # 1  2  3 |   4   | 5  6
            # k = 3
            if k <= len(more):
                return quick(more, k)
            if len(nums)-len(less) < k:
                return quick(less, k - (len(nums) - len(less)))
            return base
        
        return quick(nums, k)
```


#### []()

```python

```



## 动态规划·一维


#### [1137. 第 N 个泰波那契数*](https://leetcode.cn/problems/n-th-tribonacci-number/)

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        # O(n), O(n)
        T = [0]*38
        T[0], T[1], T[2] = 0, 1, 1
        for i in range(3, len(T)):
            T[i] = T[i-1] + T[i-2] + T[i-3]
        return T[n]
```


#### []()

```python

```


## 动态规划·多维


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


## 二分查找

二分查找（Binary Search），也称为折半搜索，是一种在有序数组中查找特定元素的搜索算法。其基本思想是将数组分成两半，比较中间元素与目标值的大小，然后根据比较结果缩小搜索范围，重复这个过程直到找到目标值或搜索范围为空。

以下是二分查找算法的基本步骤：

1. **初始化**：设置两个指针，一个指向数组的起始位置（low），另一个指向数组的结束位置（high）。初始时，low = 0，high = 数组长度 - 1。

2. **循环条件**：只要low小于等于high，就继续循环。

3. **查找中间位置**：计算中间位置mid，mid = low + (high - low) / 2。注意使用整数除法以避免小数。

4. **比较中间元素**：比较数组中mid位置的元素与目标值。
   - 如果中间元素等于目标值，搜索成功，返回mid。
   - 如果中间元素大于目标值，说明目标值位于数组的左半部分，更新high = mid - 1。
   - 如果中间元素小于目标值，说明目标值位于数组的右半部分，更新low = mid + 1。

5. **循环结束**：如果low > high，说明目标值不在数组中，搜索失败，返回-1或相应的失败标志。

二分查找算法的时间复杂度为O(log n)，其中n是数组的长度。这使得它在大规模数据集上非常高效。然而，二分查找要求数组必须是有序的，如果数组无序，需要先进行排序，这可能会增加额外的时间开销。

二分查找可以应用于各种问题，如查找特定元素、查找最小值或最大值、查找满足特定条件的元素等。它是一种非常实用且强大的搜索技术。


#### [374. 猜数字大小*](https://leetcode.cn/problems/guess-number-higher-or-lower/)

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            num = (high + low)//2
            if guess(num) <= 0:
                high = num
            else:
                low = num + 1
        return low
```


#### [2300. 咒语和药水的成功对数**](https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/)

```python
class Solution:
    def successfulPairs1(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # O((n+m)logm),n=len(spells),m=len(potions), O(1)
        potions.sort()
        n = len(potions)
        ans = []
        for s in spells:
            l, h = 0, n-1
            # 先判断下最后一个药水是否符合要求
            if potions[-1] * s < success:
                ans.append(0)
                continue

            while l < h:
                mid = (h+l)//2
                if potions[mid] * s >= success:
                    h = mid
                else:
                    l = mid + 1
            # 结束循环后，l == r == 第一个可以成功的药水下标
            ans.append(n - l)
        return ans

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 利用库函数
        # 作者：灵茶山艾府
        # 链接：https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/solutions/1595712/by-endlesscheng-1kbp/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        potions.sort()
        m = len(potions)
        success -= 1
        return [m - bisect_right(potions, success // x) for x in spells]
```

`bisect_right`是Python标准库中的一个函数，位于`bisect`模块里。这个函数主要用于在有序列表中查找插入位置，以保持列表的有序状态。具体来说，`bisect_right(a, x, lo=0, hi=len(a))`函数的作用是在有序列表`a`中找到第一个大于或等于`x`的元素的位置。如果`x`已经存在于列表中，则返回的是`x`之后（右侧）第一个元素的位置，即插入点不会重复元素。如果列表中所有元素都小于`x`，则返回列表的长度，意味着新元素将被追加在列表的末尾。

参数解释：
- `a`：一个已排序的列表。
- `x`：需要插入的元素或者用于比较的值。
- `lo`：搜索范围的起始下标，默认为0。
- `hi`：搜索范围的结束下标，默认为列表长度。

示例代码：
```python
from bisect import bisect_right

# 已排序的列表
sorted_list = [1, 2, 4, 4, 6, 8]

# 查找插入位置
insert_pos = bisect_right(sorted_list, 5)

print(f"插入值5的位置（右侧插入）: {insert_pos}")
```
这段代码会输出：`插入值5的位置（右侧插入）: 4`，意味着数值5应当插入在索引为4的位置，以保持列表的升序排列。


#### [162. 寻找峰值**](https://leetcode.cn/problems/find-peak-element)

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(logn), O(1)
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = (l + r)//2
            # print(l, r, mid, nums[mid], nums[mid+1])
            if nums[mid] > nums[mid+1]:
                r = mid
            else: l = mid + 1
        return l
```


#### [875. 爱吃香蕉的珂珂**](https://leetcode.cn/problems/koko-eating-bananas)

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 题解：https://leetcode.cn/problems/koko-eating-bananas/solutions/2710324/er-fen-da-an-fu-ti-dan-pythonjavacgojsru-eb18
        # O(len(piles)log max(piles)), O(1)
        n = len(piles)
        if n == h:
            return max(piles)
        
        l, r = 0, max(piles)
        while l + 1 < r:
            mid = (l + r)//2
            if sum((p-1)//mid for p in piles) <= h-n:
                r = mid
            else:
                l = mid
        return r
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
