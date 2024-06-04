# Leetcode Daily Challenge June 2024


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


## 20240604 Easy|Medium|Hard []()

```python

```


## 20240604 Easy|Medium|Hard []()

```python

```


## 20240604 Easy|Medium|Hard []()

```python

```


## 20240604 Easy|Medium|Hard []()

```python

```


## 20240604 Easy|Medium|Hard []()

```python

```


## 20240604 Easy|Medium|Hard []()

```python

```


## 20240604 Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```


## Easy|Medium|Hard []()

```python

```

