# LeetCode Daily Challenge

这篇文档记录每日一题的解题记录，尽可能的理解好每一道题，总结相关经验。

[TOC]
## 20240507 [1463. 摘樱桃 II](https://leetcode.cn/problems/cherry-pickup-ii/)

> 能用动态规划解决的问题，需要满足三个条件：最优子结构，无后效性和子问题重叠。
> 
> 对于一个能用动态规划解决的问题，一般采用如下思路解决：
> 1. 将原问题划分为若干 阶段，每个阶段对应若干个子问题，提取这些子问题的特征（称之为 状态）；
> 2. 寻找每一个状态的可能 决策，或者说是各状态间的相互转移方式（用数学的语言描述就是 状态转移方程）。
> 3. 按顺序求解每一个阶段的问题。
> 
> https://oi-wiki.org/dp/basic/


> 对于一些二维 DP（例如背包、最长公共子序列），如果把 DP 矩阵画出来，其实状态转移可以视作在网格图上的移动。所以在学习相对更抽象的二维 DP 之前，做一些形象的网格图 DP 会让后续的学习更轻松（比如 0-1 背包的空间优化写法为什么要倒序遍历）。
> 
> 作者：灵茶山艾府
> 链接：https://leetcode.cn/circle/discuss/tXLS3i/
> 来源：力扣（LeetCode）
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```python

```

## 20240506 [741. 摘樱桃](https://leetcode.cn/problems/cherry-pickup/)

诶诶诶诶诶诶诶诶！

```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """题解@宫水三叶：https://leetcode.cn/problems/cherry-pickup/solutions/1658619/by-ac_oier-pz7i/"""
        n = len(grid)
        f = [[[float('-inf') for _ in range(55)] for _ in range(55)] for _ in range(2*55)]
        
        g = grid
        f[2][1][1] = g[0][0]
        for k in range(3, 2*n+1):
            for i1 in range(1, n+1):
                for i2 in range(1, n+1):
                    j1, j2 = k - i1, k - i2
                    if j1<=0 or j1>n or j2<=0 or j2>n: continue
                    A, B = g[i1-1][j1-1], g[i2-1][j2-1]
                    if A==-1 or B==-1: continue

                    a = f[k-1][i1-1][i2]
                    b = f[k-1][i1-1][i2-1]
                    c = f[k-1][i1][i2-1]
                    d = f[k-1][i1][i2]
                    t = max(max(a, b), max(c, d)) + A
                    if i1 != i2:
                        t += B
                    f[k][i1][i2] = t
        
        return 0 if f[2 * n][n][n] <= 0 else f[2 * n][n][n]
```

## 20240505 Easy [1652. 拆炸弹](https://leetcode.cn/problems/defuse-the-bomb/)

```python
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """定长滑动窗口，实际用循环取模做的累加模拟"""
        n = len(code)
        ans = [0]*n

        if k == 0:
            return ans
        
        for i in range(n):
            tmp = 0
            if k > 0:
                for j in range(1,k+1):
                    tmp += code[(i+j)%n]
            else:
                for j in range(1,-k+1):
                    tmp += code[i-j]
            ans[i] = tmp
        return ans
```


## 20240504 Hard [1235. 规划兼职工作](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/)

动态规划题，目前还不大熟，先把题解思路能看懂，顺便巩固基础。基础材料阅读：[动态规划部分简介](https://oi-wiki.org/dp/)。

```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """动态规划
        
        题解：https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1913089/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/
        """
        
        # 按照结束时间排序
        jobs = sorted(zip(endTime, startTime, profit))
        print(jobs)
        # 元组按字典顺序进行比较，先比较第一项；如果它们相同则比较第二个项目，依此类推。
        # Refer~ [排序的技术](https://docs.python.org/zh-cn/3/howto/sorting.html#sort-stability-and-complex-sorts)

        # # 如果不用内置函数这里三个数组排序要怎么写？
        # # zip：zip函数将三个数组绑定在一起，没有zip要人工执行绑定操作
        # jobs_test = []
        # for i in range(len(profit)):
        #     jobs_test.append((endTime[i], startTime[i], profit[i]))
        # print(jobs_test)  # [(3, 1, 50), (4, 2, 10), (5, 3, 40), (6, 3, 70)]
        # # sorted：排序函数，该问题场景下需要支持使用三元组第一个值作为key进行排序
        # # 此处使用冒泡排序举例
        # for i in range(len(jobs_test)-1):
        #     if jobs_test[i] > jobs_test[i+1]:
        #         jobs_test[i], jobs_test[i+1] = jobs_test[i+1], jobs_test[i]
        # print(jobs_test)

        f = [0]*(len(profit)+1) # 按照结束时间排序后的前i个工作的最大报酬
        for i, (end, start, p) in enumerate(jobs):
            # print(i)
            # 寻找最近一个结束时间【小于等于】当前开始时间的工作j
            # 由于jobs已经排序过，可以用二分查找
            l, r = 0, i
            j = -1
            while l <= r:
                mid = (l+r)//2
                # print('')
                if jobs[mid][0] <= start:
                    j = mid
                    l = mid + 1
                else:
                    r = mid - 1
                # print('i: ',i ,'\tf: ', f,'\tstart: ', start,'\tmid: ',mid, '\tmid job: ', jobs[mid], '\tcur j: ', j)

                # 状态转移方程
                # 对于第i个工作，要么选中（最大利润=f[j]+profit[i]），要么不选（最大利润=f[i-1]）
                # 为了兼容i=0时i-1=-1的情况，令f[0]=0，对后续所有的i都+1处理，j的含义不变
                f[i + 1] = max(f[i], f[j+1]+p) #前面查找j是按照索引起点为0的背景定位的，因f[0]已经被占用所以最终从f中取用j的时候要+1（便宜量）
                # print(f)
            

            # 如上二分查找过程可用标准库的二分查找函数简化代码（还需要学习～https://docs.python.org/3/library/bisect.html）：
            # j = bisect_left(jobs, (st + 1,), hi=i)
            # 注意这里找到的是第一个end大于start的j，前面手写的二分查找找到的是第一个<=的，这里的差异决定了
            # f[i + 1] = max(f[i], f[???]+p) 取值时，???到底是j还是j+1。此处有点绕，找个case走读一遍就懂了
            
        return f[-1] # 最后一位存储的即总n个工作中的最大利润
```