# LeetCode Daily Challenge

这篇文档记录每日一题的解题记录，尽可能的理解好每一道题，总结相关经验。

[TOC]

## 20240504 [1235. 规划兼职工作](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/description/)

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