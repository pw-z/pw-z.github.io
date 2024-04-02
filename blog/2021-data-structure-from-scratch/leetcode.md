# Leetcode刷题总结

[TOC]

## 20240401-04?[LeetCode-Hot-100](https://leetcode.cn/studyplan/top-100-liked/)


### 哈希表

#### [1. 两数之和](https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """解法1: 二层循环，O(N^2)，O(1)
        ✅PASS

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
        """解法2: 哈希表，O(N)，O(1)
        ✅PASS

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


#### [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked)

```python
class Solution:

   
    def _hash1(self, str):
        """哈希函数：对单词字母ascii码求和作为哈希值
        ❌错误，哈希冲突

        解答错误
        55 / 126 个通过的测试用例
        """
        sum = 0
        for x in str:
            sum += ord(x)
        return sum
    
    
    def _hash2(self, str):
        """哈希函数：尝试提高哈希值离散情况
        ❌错误，哈希冲突

        解答错误
        113 / 126 个通过的测试用例
        """
        sum = 0
        for x in str:
            sum += ord(x)*ord(x)
        return sum

    
    def _hash(self, mystr):
        """哈希函数：使用排序后的字母作为哈希值
        ✅PASS

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


#### [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked)

```python
class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        """哈希表降低查找复杂度，通过判断n-1是否在表中跳过重复判断
        ❌错误，特殊用例未兼容，用例[0]未通过，预期1实际0

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
        """逻辑同上，代码优化
        ✅PASS
        
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


### 双指针

#### [283. 移动零](https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked)






## [LeetCode刷题攻略](https://github.com/youngyangyang04/leetcode-master)

`数组-> 链表-> 哈希表->字符串->栈与队列->树->回溯->贪心->动态规划->图论->高级数据结构`


