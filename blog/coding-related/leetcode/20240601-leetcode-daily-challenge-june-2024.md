# Leetcode Daily Challenge June 2024

- [Leetcode Daily Challenge June 2024](#leetcode-daily-challenge-june-2024)
  - [20240601 Easy 2928. 给小朋友们分糖果 I](#20240601-easy-2928-给小朋友们分糖果-i)
  - [20240602 Easy 575. 分糖果](#20240602-easy-575-分糖果)
  - [20240603 Easy 1103. 分糖果 II](#20240603-easy-1103-分糖果-ii)
  - [20240604 Medium 3067. 在带权树网络中统计可连接服务器对数目](#20240604-medium-3067-在带权树网络中统计可连接服务器对数目)
  - [20240605 Hard 3072. 将元素分配到两个数组中 II](#20240605-hard-3072-将元素分配到两个数组中-ii)
  - [20240606 Medium 2938. 区分黑球与白球](#20240606-medium-2938-区分黑球与白球)
  - [20240607 Easy 3038. 相同分数的最大操作数目 I](#20240607-easy-3038-相同分数的最大操作数目-i)
  - [20240608 Medium 3040. 相同分数的最大操作数目 II](#20240608-medium-3040-相同分数的最大操作数目-ii)
  - [20240609 Hard 312. 戳气球](#20240609-hard-312-戳气球)
  - [20240610 Medium 881. 救生艇](#20240610-medium-881-救生艇)
  - [20240611 Medium 419. 甲板上的战舰](#20240611-medium-419-甲板上的战舰)
  - [20240612 Easy 2806. 取整购买后的账户余额](#20240612-easy-2806-取整购买后的账户余额)
  - [20240613 Hard 2813. 子序列最大优雅度](#20240613-hard-2813-子序列最大优雅度)
  - [20240614 Medium 2786. 访问数组中的位置使分数最大](#20240614-medium-2786-访问数组中的位置使分数最大)
  - [20240615 Medium 2779. 数组的最大美丽值](#20240615-medium-2779-数组的最大美丽值)
  - [20240616 Easy 521. 最长特殊序列 Ⅰ](#20240616-easy-521-最长特殊序列-ⅰ)
  - [20240617 Medium 522. 最长特殊序列 II](#20240617-medium-522-最长特殊序列-ii)
  - [20240618 Medium 2288. 价格减免](#20240618-medium-2288-价格减免)
  - [20240619 Hard 2713. 矩阵中严格递增的单元格数](#20240619-hard-2713-矩阵中严格递增的单元格数)
  - [20240620 Easy 2748. 美丽下标对的数目](#20240620-easy-2748-美丽下标对的数目)
  - [20240621 Easy LCP 61. 气温变化趋势](#20240621-easy-lcp-61-气温变化趋势)
  - [20240622 Hard 2663. 字典序最小的美丽字符串](#20240622-hard-2663-字典序最小的美丽字符串)
  - [20240623 Easy 520. 检测大写字母](#20240623-easy-520-检测大写字母)
  - [20240624 Medium 503. 下一个更大元素 II](#20240624-medium-503-下一个更大元素-ii)


## 20240601 Easy [2928. 给小朋友们分糖果 I](https://leetcode.cn/problems/distribute-candies-among-children-i/)

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 时间复杂度O(limit^2), 空间复杂度O(1)
        ans = 0
        for i in range(0, limit+1):
            for j in range(0, limit+1):
                if 0 <= n - i - j <= limit:
                    ans += 1
        return ans
```


## 20240602 Easy [575. 分糖果](https://leetcode.cn/problems/distribute-candies)

```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # O(n), O(n)

        # n = len(candyType)
        # types = len(set(candyType))
        # # return n//2 if types > n//2 else types
        # return min(n//2, types)
        return min(len(candyType)//2, len(set(candyType)))
```


## 20240603 Easy [1103. 分糖果 II](https://leetcode.cn/problems/distribute-candies-to-people/)

```python
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        # WA，第二轮不是又从1开始分的，不好好读题
        # # 1轮分配消耗的糖果
        # one_round_count = (1+num_people)*(num_people//2) + (1+num_people)//2*(num_people%2)
        # # 能分配几轮？最后一轮还剩几个？
        # rounds, remains = candies // one_round_count, candies % one_round_count
        # # print(one_round_count, rounds, remains)
        # ans = list()
        # for i in range(1, num_people+1):
        #     ans.append(i * rounds + (i if remains >= i else remains))
        #     remains = max(remains - i, 0)
        # return ans

        # 暴力模拟， O(max(G,N))\mathcal{O}(max(\sqrt{G}, N))O(max(G​,N))， O(1)
        i = 1
        ans = [0]*num_people
        while candies > 0:
            ans[i % num_people -1] += min(i, candies)
            candies -= i
            i += 1
        return ans
```


## 20240604 Medium [3067. 在带权树网络中统计可连接服务器对数目](https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/)

今天是CV大师。

```python
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y, wt in edges:
            g[x].append((y, wt))
            g[y].append((x, wt))

        def dfs(x: int, fa: int, s: int) -> int:
            cnt = 0 if s % signalSpeed else 1
            for y, wt in g[x]:
                if y != fa:
                    cnt += dfs(y, x, s + wt)
            return cnt

        ans = [0] * n
        for i, gi in enumerate(g):
            if len(gi) == 1:
                continue
            s = 0
            for y, wt in gi:
                cnt = dfs(y, i, wt)
                ans[i] += cnt * s
                s += cnt
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/solutions/2664330/mei-ju-gen-dfs-cheng-fa-yuan-li-pythonja-ivw5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```


## 20240605 Hard [3072. 将元素分配到两个数组中 II](https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/)

树状数组！

```python
class Fenwick:
    def __init__(self, n):
        self.tree = [0]*n
    
    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i
    
    def pre(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i-1
        return res

class Solution:
    def resultArray1(self, nums: List[int]) -> List[int]:
        # 暴力模拟，超时
        arr1, arr2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            cur = nums[i]
            greaterCount1 = sum([1 if cur < x else 0 for x in arr1])
            greaterCount2 = sum([1 if cur < x else 0 for x in arr2])
            if greaterCount1 > greaterCount2:
                arr1.append(cur)
            elif greaterCount1 < greaterCount2:
                arr2.append(cur)
            else:
                if len(arr2) < len(arr1):
                    arr2.append(cur)
                else:
                    arr1.append(cur)
        return arr1 + arr2


    def resultArray(self, nums: List[int]) -> List[int]:
        # 题解：https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/solutions/2664646/chi-san-hua-shu-zhuang-shu-zu-pythonjava-3bb2
        sorted_nums = sorted(set(nums))
        m = len(sorted_nums)
        a, b = [nums[0]], [nums[1]]
        t1, t2 = Fenwick(m+1), Fenwick(m+1)
        t1.add(bisect_left(sorted_nums, nums[0]) + 1)
        t2.add(bisect_left(sorted_nums, nums[1]) + 1)
        for x in nums[2:]:
            v = bisect_left(sorted_nums, x) + 1
            gc1 = len(a) - t1.pre(v)
            gc2 = len(b) - t2.pre(v)
            if gc1 > gc2 or gc1 == gc2 and len(a) <= len(b):
                a.append(x)
                t1.add(v)
            else:
                b.append(x)
                t2.add(v)
        return a + b
```

`bisect_left` 是 Python 标准库 `bisect` 模块中的一个函数，它用于在一个已排序的列表中进行高效的插入位置查找。具体来说，`bisect_left` 函数返回应该插入 `x` 以保持列表排序的索引，假设列表是已排序的。如果 `x` 已经存在于列表中，`bisect_left` 会返回 `x` 的最左边（即最小索引）的插入点。

这是它的基本用法：

```python
import bisect

# 假设我们有一个已排序的列表
lst = [1, 3, 5, 7, 9]

# 我们想找到3应该插入的位置（如果它不在列表中）
index = bisect.bisect_left(lst, 3)
print(index)  # 输出：1

# 如果我们查找一个不在列表中的数，比如4
index = bisect.bisect_left(lst, 4)
print(index)  # 输出：2

# 注意，如果我们查找的数是列表中的一个元素，它会返回该元素的最左边索引
index = bisect.bisect_left(lst, 5)
print(index)  # 输出：2
```
这个函数在需要保持列表排序的同时频繁插入元素的场景中非常有用。与简单地遍历列表以找到插入位置相比，`bisect_left` 提供了更快的查找速度，因为它利用了列表的已排序性质。

另外，`bisect` 模块还提供了一个类似的函数 `bisect_right`（或 `bisect`，它们是等价的），该函数与 `bisect_left` 的主要区别在于，当 `x` 存在于列表中时，`bisect_right` 会返回 `x` 的最右边（即最大索引）的插入点。


`bisect` 是 Python 的一个内置模块，它提供了支持维护已排序列表的函数。这个模块主要用于在不破坏列表排序的情况下高效地插入新元素或查找元素的插入位置。

`bisect` 模块主要提供了以下几个函数：

1. **bisect_left(a, x, lo=0, hi=len(a))**:
   这个函数返回应该插入元素 `x` 到已排序列表 `a` 中的索引，以保持列表的排序。如果 `x` 已经存在于 `a` 中，则返回 `x` 的最左边（即最小索引）的插入点。`lo` 和 `hi` 参数可以指定搜索的范围，默认搜索整个列表。

2. **bisect_right(a, x, lo=0, hi=len(a))** (也称为 **bisect(a, x, lo=0, hi=len(a))**):
   这个函数与 `bisect_left` 类似，但是如果 `x` 已经存在于 `a` 中，则返回 `x` 的最右边（即最大索引）的插入点。在 Python 3.3 版本之前，`bisect` 函数就是 `bisect_right` 的别名。

3. **insort_left(a, x, lo=0, hi=len(a))**:
   这个函数将元素 `x` 插入到已排序列表 `a` 的适当位置，以保持列表的排序。它与 `a.insert(bisect_left(a, x, lo, hi), x)` 的效果相同，但是更加高效。

4. **insort_right(a, x, lo=0, hi=len(a))**:
   这个函数与 `insort_left` 类似，但是将 `x` 插入到 `a` 的最右边（如果存在相同元素的话）。它与 `a.insert(bisect_right(a, x, lo, hi), x)` 的效果相同。

5. **bisect_key(func, a, x, lo=0, hi=len(a))**:
   这个函数与 `bisect_left` 类似，但是允许你指定一个函数 `func` 来计算列表 `a` 中每个元素的排序键。然后，`bisect_key` 会根据这些键来查找 `x` 的插入位置。

6. **insort_key(func, a, x, lo=0, hi=len(a))**:
   这个函数与 `insort_left` 类似，但是允许你指定一个函数 `func` 来计算列表 `a` 中每个元素的排序键。然后，`insort_key` 会根据这些键来将 `x` 插入到适当的位置。

这些函数在需要频繁对列表进行插入操作，同时又希望保持列表排序的情况下非常有用。它们提供了比简单的线性搜索和插入更高效的方法。



## 20240606 Medium [2938. 区分黑球与白球](https://leetcode.cn/problems/separate-black-and-white-balls/)

```python
class Solution:
    def minimumSteps1(self, s: str) -> int:
        # O(n), O(1)
        # 冒泡排序？每一个0冒泡到最左边消耗的步骤 = 0当前位置 - 左边第一个1的位置
        # 0111010111
        first_one = r = 0
        n = len(s)
        while first_one < n and s[first_one] == '0':
            first_one += 1
        
        # 没有1的情况
        if first_one >= n:
            return 0

        ans = 0
        cnt = 0 # 已经冒泡过几个0，对应的最左边的1也就往右挪过几个位置
        for r in range(first_one+1, n):
            # print(first_one, r, s[r], s[r]=='0', cnt)
            if s[r] == '0':
                ans += r - first_one - cnt
                cnt += 1
        return ans
            
    def minimumSteps(self, s: str) -> int:
        # O(n), O(1)
        ans = cnt = 0
        for n in s:
            if n == '1': cnt += 1
            else: ans += cnt
        return ans
```


## 20240607 Easy [3038. 相同分数的最大操作数目 I](https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-i)

```python
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # O(n), O(1)
        ans = 0
        for i in range(1,len(nums), 2):
            score = nums[i-1] + nums[i]
            if i == 1:
                first = score
                ans += 1
            else:
                if score == first:
                    ans += 1
                else:
                    break
        return ans
```


## 20240608 Medium [3040. 相同分数的最大操作数目 II](https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/)

```python
class Solution:
    def maxOperations1(self, nums: List[int]) -> int:
        # O(n^2), O(1)
        # 题解：https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/solutions/2643756/qu-jian-dp-de-tao-lu-pythonjavacgo-by-en-nynz
        @cache
        def dfs(i, j, target):
            if i >= j: return 0
            res = 0
            if nums[i] + nums[i+1] == target:
                res = max(res, dfs(i+2, j, target)+1)
            if nums[j-1] + nums[j] == target:
                res = max(res, dfs(i, j-2, target)+1)
            if nums[i] + nums[j] == target:
                res = max(res, dfs(i+1, j-1, target)+1)
            return res
        
        n = len(nums)
        return max(dfs(2, n-1, nums[0]+nums[1]), dfs(1, n-2, nums[0]+nums[-1]), dfs(0, n-3, nums[-2]+nums[-1]))+1        
```


## 20240609 Hard [312. 戳气球](https://leetcode.cn/problems/burst-balloons/)

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # O(n^3), O(n^2)
        # 区间DP
        # 题解：https://leetcode.cn/problems/burst-balloons/solutions/1930450/by-ac_oier-9r9c
        # f[l][r] = max(f[l][k] + f[k][r] + nums[l]*nums[k]*nums[r]),  l < k < r
        n = len(nums)
        nums = [1] + nums + [1]
        f = [[0] * (n+2) for _ in range(n+2)]
        for length in range(3, n+3):
            for l in range(n+1 -length+1 +1):
                r = l + length -1
                for k in range(l+1, r):
                    f[l][r] = max(f[l][r], f[l][k]+f[k][r]+ nums[l]*nums[k]*nums[r])
        return f[0][n+1]
```

区间DP（Dynamic Programming）算法是一种特殊的动态规划方法，它用于解决涉及区间（连续子数组或子序列）的优化问题。与传统的动态规划不同，区间DP通常处理的是区间上的问题，而不是单个元素。以下是区间DP的一些关键概念和特点：

1. 问题类型
区间DP通常用于解决以下类型的问题：
- 最小化或最大化区间内元素的总和或乘积。
- 区间内的子问题可能依赖于区间的起始点和结束点。

2. 状态定义
在区间DP中，状态通常定义为与区间相关的某种属性。例如，对于一个数组`A`，状态可以定义为`dp[i][j]`，表示从索引`i`到`j`的区间的某种最优值。

3. 状态转移
区间DP的状态转移通常涉及将一个或多个较小的区间合并为一个较大的区间。状态转移方程需要考虑如何将较小区间的最优解组合起来，以得到较大区间的最优解。

4. 初始化
区间DP的初始化通常涉及计算单个元素或最小区间的最优解。例如，如果问题涉及最小化区间和，那么初始化可能只是将数组中的每个元素视为一个单独的区间。

5. 计算顺序
区间DP的计算顺序通常从最小的区间开始，逐步合并区间以计算更大区间的最优解。这可能涉及到嵌套循环或递归。

6. 优化技巧
区间DP可能需要一些优化技巧，如：
- **单调队列**：用于处理区间最小/最大值问题，保持单调性以优化查询。
- **树状数组（Binary Indexed Tree, BIT)**：用于快速更新和查询区间的累积值。
- **线段树**：用于处理更复杂的区间操作，如区间加法或区间查询。

7. 示例问题
一个典型的区间DP问题是“区间加和最大化”问题，即在一个数组中找到一个子区间，使得该区间的元素和最大。

示例代码（Python）：
```python
def max_sum_subarray(arr):
    n = len(arr)
    # 初始化dp数组，每个元素自身是一个区间的最大和
    dp = [[0] * 2 for _ in range(n)]
    dp[0][1] = arr[0]
    
    for i in range(1, n):
        # 当前元素作为区间的开始
        dp[i][0] = max(dp[i-1][0], 0) + arr[i]
        # 当前元素作为区间的结束
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]) + arr[i]
    
    # 最大的区间和
    return max(max(dp[i][0] for i in range(n)), max(dp[i][1] for i in range(n)))

# 测试代码
arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(max_sum_subarray(arr))  # 输出最大区间和
```

在这个示例中，`dp[i][0]`表示以`arr[i]`为结束的区间的最大和，`dp[i][1]`表示以`arr[i]`为开始的区间的最大和。通过这种方式，我们可以逐步构建出整个数组的最大区间和。

区间DP是一种强大的技术，可以解决许多涉及区间的复杂问题。掌握它需要对动态规划有深入的理解以及对问题特性的洞察。



## 20240610 Medium [881. 救生艇](https://leetcode.cn/problems/boats-to-save-people/)

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # O(nlogn), O(logn) 时间与空间主要都消耗在排序上
        people.sort()
        l, r = 0, len(people)-1
        ans = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            ans += 1
        return ans
```


## 20240611 Medium [419. 甲板上的战舰](https://leetcode.cn/problems/battleships-in-a-board)

```python
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'X' and (row == 0 or board[row-1][col] =='.') and (col == 0 or board[row][col-1]=='.'):
                    ans += 1
        return ans
```


## 20240612 Easy [2806. 取整购买后的账户余额](https://leetcode.cn/problems/account-balance-after-rounded-purchase/)

```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # return 100 - (10 * (purchaseAmount//10 + int(purchaseAmount % 10 > 4)))
        return 100 - (purchaseAmount+5)//10 * 10
```


## 20240613 Hard [2813. 子序列最大优雅度](https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/)

```python
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key = lambda it: -it[0])
        categories = set()
        stack = []
        ans = profit = 0
        for i, item in enumerate(items):
            if i < k:
                profit += item[0]
                if item[1] in categories:
                    stack.append(item[0])
                else:
                    categories.add(item[1])
            elif item[1] not in categories and len(stack) > 0:
                profit += item[0]-stack.pop()
                categories.add(item[1])
            ans = max(ans, profit + len(categories)**2)
        return ans
```


## 20240614 Medium [2786. 访问数组中的位置使分数最大](https://leetcode.cn/problems/visit-array-positions-to-maximize-score/)

```python
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        # https://leetcode.cn/problems/visit-array-positions-to-maximize-score/solutions/2810386/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-jhvr
        # O(N), O(N)
        @cache
        def dfs(i, j):
            if i == len(nums):
                return 0
            if nums[i] % 2 != j:
                return dfs(i+1, j)
            return max(dfs(i+1, j), dfs(i+1, j^1)-x) + nums[i]
            
        return dfs(0, nums[0]%2)
```


## 20240615 Medium [2779. 数组的最大美丽值](https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation)

```python
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/2345805/pai-xu-shuang-zhi-zhen-by-endlesscheng-hbqx
        # O(nlogn), O(1)
        nums.sort()
        # top, bot = [], []
        # for n in nums:
        #     top.append(n + k)
        #     bot.append(n - k)
        # print(nums, bot, top)
        ans = l = 0
        for r, n in enumerate(nums):
            while n - nums[l] > k*2:
                l += 1
            ans = max(ans, r-l+1)
        return ans
```


## 20240616 Easy [521. 最长特殊序列 Ⅰ](https://leetcode.cn/problems/longest-uncommon-subsequence-i/)

```python
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # O(n), O(1)
        if a == b:
            return -1
        return max(len(a), len(b))
```


## 20240617 Medium [522. 最长特殊序列 II](https://leetcode.cn/problems/longest-uncommon-subsequence-ii/)

```python
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # https://leetcode.cn/problems/longest-uncommon-subsequence-ii/solutions/1623415/zui-chang-te-shu-xu-lie-ii-by-leetcode-s-bo2e
        ans = -1
        n = len(strs)
        for i in range(n):
            s = strs[i]
            flag = True
            for j in range(n):
                t = strs[j]
                if i != j:
                    # 判断s是否为t的子序列
                    ps = pt = 0
                    while ps < len(s) and pt < len(t):
                        if s[ps] == t[pt]:
                            ps += 1
                        pt += 1
                    if ps == len(s):
                        flag = False
                        break
            if flag:
                ans = max(ans, len(s))
        return ans
```


## 20240618 Medium [2288. 价格减免](https://leetcode.cn/problems/apply-discount-to-prices)

```python
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        # O(N + 单词数*单词长度) ~ O(N), O(N)
        words = sentence.split(" ")
        # print(words)
        for i in range(len(words)):
            w = words[i]
            if w.startswith("$") and len(w) > 1:
                flag = True
                for _ in w[1:]:
                    if _ not in "0123456789":
                        flag = False
                        break
                if flag:
                    # print(w[1:])
                    words[i] = f"${int(w[1:]) * (100-discount)/100:.2f}"
        return " ".join(words)

        # Note: 判断数字可以用`.isdigit()`
```


## 20240619 Hard [2713. 矩阵中严格递增的单元格数](https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/)

```python
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        # https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/solutions/2809597/ju-zhen-zhong-yan-ge-di-zeng-de-dan-yuan-ff4v
        m, n = len(mat), len(mat[0])
        mp = defaultdict(list)
        row = [0]*m
        col = [0]*n

        for i in range(m):
            for j in range(n):
                mp[mat[i][j]].append((i, j))

        for _, pos in sorted(mp.items(), key=lambda k: k[0]):
            res = [max(row[i], col[j])+1 for i, j in pos]
            for (i, j), d in zip(pos, res):
                row[i] = max(row[i], d)
                col[j] = max(col[j], d)

        return max(row)
```


## 20240620 Easy [2748. 美丽下标对的数目](https://leetcode.cn/problems/number-of-beautiful-pairs/)

```python
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if gcd(int(str(nums[i])[0]), nums[j]%10) == 1:
                    ans += 1
        return ans
```


## 20240621 Easy [LCP 61. 气温变化趋势](https://leetcode.cn/problems/6CE719)

```python
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        # O(n), O(1)
        ans = tmp = 0
        for i in range(1, len(temperatureA)):
            a = temperatureA[i] - temperatureA[i-1]
            b = temperatureB[i] - temperatureB[i-1]
            if (a > 0 and b > 0) or (a<0 and b < 0) or (a == 0 and b == 0):
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 0
        return max(ans, tmp)
```


## 20240622 Hard [2663. 字典序最小的美丽字符串](https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/)

```python
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        # 斗宗强者恐怖如斯：https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/solutions/2251229/tan-xin-pythonjavacgo-by-endlesscheng-yix5
        # O(n), O(n)
        a = ord('a')
        k += a
        s = list(map(ord, s))
        n = len(s)
        i = n-1
        s[i] += 1
        while i < n:
            if s[i] == k: # 处理进位
                if i==0:
                    return ""
                s[i] = a
                i -= 1
                s[i] += 1
            elif i and s[i] == s[i-1] or i > 1 and s[i] == s[i-2]: # 处理回文
                s[i] += 1
            else:
                i += 1
        return ''.join(map(chr, s))
```


## 20240623 Easy [520. 检测大写字母](https://leetcode.cn/problems/detect-capital/)

```python
class Solution:
    def detectCapitalUse1(self, word: str) -> bool:
        # O(n), O(1)
        if len(word) < 2:
            return True
        lowL, lowR = ord("a"), ord("z")
        highL, highR = ord("A"), ord("Z")

        isFirstCapital = highL <= ord(word[0]) <= highR
        countCapital = 0
        countNonCaptial = 0
        for c in word:
            curIsCapital = highL <= ord(c) <= highR
            countCapital += curIsCapital
            countNonCaptial += not curIsCapital
            if not isFirstCapital and curIsCapital:
                return False
            if isFirstCapital and (countCapital-isFirstCapital) and countNonCaptial:
                return False
        return True

    def detectCapitalUse(self, word: str) -> bool:
        # O(n), O(1)
        cnt = sum([c.isupper() for c in word])
        return cnt==0 or cnt==len(word) or cnt==1 and word[0].isupper()
```


## 20240624 Medium [503. 下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii)

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [-1] * l
        stack = []
        for i in range(l*2):
            p = nums[i%l]
            while stack and p > nums[stack[-1]]:
                ans[stack.pop()] = p
            
            if i < l:
                stack.append(i)

        return ans
```