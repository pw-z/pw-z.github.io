# LeetCode Daily Challenge

这篇文档记录每日一题的解题记录，尽可能的理解好每一道题，总结相关经验。

[TOC]


## 20240513 Medium [994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/)

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

## 20240512 Hard [1553. 吃掉 N 个橘子的最少天数](https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/)

要多久我能独立写出这样的算法分析？

```python
class Solution:
    def minDays(self, n: int) -> int:
        """
        题解：https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/solutions/2773476/liang-chong-fang-fa-ji-yi-hua-sou-suo-zu-18jv
        所有的-1操作都是为了凑/2或/3操作，子问题dfs(i)定义为把i变为0的最小操作次数
        """
        @cache
        def dfs(i):
            if i <= 1: return i
            return min(dfs(i//2)+i%2, dfs(i//3)+i%3) + 1  # 此处的+1代表着执行一次除法
        return dfs(n)
```


## 20240511 Medium [2391. 收集垃圾的最少总时间](https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/)

```python
class Solution:
    def garbageCollection1(self, garbage: List[str], travel: List[int]) -> int:
        # 模拟，多次遍历
        n = len(garbage)
        ans = 0
        MPG_last = {'M':0, 'P':0, 'G':0}
        MPG_cnt = {'M':0, 'P':0, 'G':0}

        for i in range(n):
            for item in garbage[i]:
                MPG_cnt[item] += 1
                MPG_last[item] = i
        
        for k, v in MPG_last.items():
            ans += MPG_cnt[k]
            if v != 0:
                ans += sum(travel[:v])
        return ans
            
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # 一次遍历
        MPG_runtime = defaultdict(int)
        ans = sum_runtime = 0
        for g, t in zip(garbage, [0]+travel): # zip函数！
            ans += len(g) # 不必区分材料因为每种材料耗时相同
            sum_runtime += t
            for c in g:
                ans += sum_runtime - MPG_runtime[c]
                MPG_runtime[c] = sum_runtime # 更新每种垃圾车的车程耗时
        return ans
```


## 20240510 Easy [2960. 统计已测试设备](https://leetcode.cn/problems/count-tested-devices-after-test-operations/)

```python
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        """O(n), O(1)"""
        cnt = 0
        for x in batteryPercentages:
            if x-cnt > 0:
                cnt += 1
        return cnt
```


## 20240509 Medium [2105. 给植物浇水 II](https://leetcode.cn/problems/watering-plants-ii/)

这题如果改成没步消耗时间一样，两个人谁没水了要回去补水，计算浇完水所需的步骤...等等，那不会就是`给植物浇水III`吧。

```python
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a, b = 0, len(plants)-1
        wa, wb = capacityA, capacityB
        ans = 0
        while a<=b:
            # 先浇水
            if a == b:
                if wa >= wb:
                    wa -= plants[a]
                else:
                    wb -= plants[b]
            else:
                wa -= plants[a]
                wb -= plants[b]
            
            # 判断是否有亏空
            if wa < 0:
                ans += 1
                wa = capacityA - plants[a]
            if wb < 0:
                ans += 1
                wb = capacityB - plants[b]

            a += 1
            b -= 1

        return ans
```

## 2024050 Medium [2079. 给植物浇水](https://leetcode.cn/problems/watering-plants/)

```python
class Solution:
    def wateringPlants1(self, plants: List[int], capacity: int) -> int:
        """模拟
        1. 水桶里有水且满足plants[i]所需，不断向右移动，step++，water-=plants[i]l
        2. 不能提前补充水，即只有当水桶剩余水量不足plants[i]，才向左移动到-1位置，
            也就是i+1步，再返回到i来（又是i+1步），即每次补充水量消耗2*(i+1)
        
        时间O(n)，空间O(1)
        """
        # [-1river, 0, 1, 2, 3, ...]
        n = len(plants)
        i = -1
        steps = 0
        water_remain = capacity
        while i < n-1:
            if water_remain >= plants[i+1]:
                steps += 1
                water_remain -= plants[i+1]
                i += 1 # 向右移动
            else:
                # 回到水边补满水回到i
                steps += 2*(i+1)
                water_remain = capacity  
            # print(i-1, i,plants[i-1], water_remain, steps)
        return steps

    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        """优化写法"""
        steps = 0
        water_remain = capacity
        for i in range(len(plants)):
            if water_remain >= plants[i]:
                steps += 1
            else:
                steps += 2*i + 1
                water_remain = capacity
            water_remain -= plants[i]
        return steps
```


## 20240507 Hard [1463. 摘樱桃 II](https://leetcode.cn/problems/cherry-pickup-ii/)

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
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #题解： https://leetcode.cn/problems/cherry-pickup-ii/solutions/2768158/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-i70v/

        m, n = len(grid), len(grid[0])

        # 缓存
        memo = {}

        # 机器人每轮一定会往下走一行，即每轮i++
        # 状态定义：dp(i, j, k)代表在第i行，robot1在j列，robot2在k列，能摘取的最大值
        # 状态转移：当前第i行能拿到的樱桃 + 第i+1行（j的三种取值情况 * k的三种取值情况)九种情况里的最大值
        # 边界条件：到最底部或者超出左右边界的时候dp()=0
        # @cache 缓存可以直接通过这个装饰器实现，见底部备注
        def dp(i, j, k):
            # 缓存消费
            if (i, j, k) in memo:
                return memo[(i, j, k)]                

            if i >= m or j < 0 or k >= n or j >= n or k < 0:
                return 0

            a1 = dp(i+1, j-1, k)
            a2 = dp(i+1, j, k)
            a3 = dp(i+1, j+1, k)

            a4 = dp(i+1, j-1, k-1)
            a5 = dp(i+1, j, k-1)
            a6 = dp(i+1, j+1, k-1)

            a7 = dp(i+1, j-1, k+1)
            a8 = dp(i+1, j, k+1)
            a9 = dp(i+1, j+1, k+1)

            max_next_amt = max(a1, a2, a3, a4, a5, a6, a7, a8, a9)
            ith_amt = grid[i][j] + grid[i][k] if j != k else 0

            # 缓存更新
            memo[(i, j, k)] = max_next_amt + ith_amt

            return max_next_amt + ith_amt

        return dp(0, 0, n-1)

"""@cache介绍（ChatGPT3.5）
请介绍下python的@cache装饰器
---
@cache 装饰器通常用于缓存函数的返回值，以提高程序的性能。Python 3.9 开始提供了内置的 functools 模块，其中包含了 @cache 装饰器。
这个装饰器可以应用在纯函数（pure function）上，也就是说，对于相同的输入，函数应该始终返回相同的输出，而不依赖于程序的状态或外部环境。

@cache的大小是多少，可以自定义吗
---
在 Python 3.9 中，@cache 装饰器使用的是基于 LRU（Least Recently Used，最近最少使用）算法的缓存策略，并且没有提供直接设置缓存大小的选项。缓存的大小由 Python 解释器自行管理，通常会根据可用的内存空间和系统资源进行动态调整。
如果你需要自定义缓存大小或者其他高级缓存策略，可以考虑使用第三方库，比如 functools_lru_cache。这个库提供了一个高度可定制的 LRU 缓存装饰器，可以设置缓存大小、过期时间等参数，以满足更复杂的需求。
"""
```


## 20240506 Hard [741. 摘樱桃](https://leetcode.cn/problems/cherry-pickup/)

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


## 20240510 Easy [1491. 去掉最低工资和最高工资后的工资平均值](https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/)

补卡。

```python
class Solution:
    def average(self, salary: List[int]) -> float:
        bottom = top = salary[0]
        total, length = 0, len(salary)
        for s in salary:
            total += s
            bottom, top = min(s, bottom), max(s, top)
        return (total - top - bottom)/(length - 2)

    def average_pythonic(self, salary: List[int]) -> float:
        """sum, max, min, len 这四个内置函数的时间复杂度都是O(n)"""
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
```