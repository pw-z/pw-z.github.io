# Leetcode Daily Challenge June 2024


## Easy[x]|Medium|Hard [2928. 给小朋友们分糖果 I](https://leetcode.cn/problems/distribute-candies-among-children-i/)

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


## Easy[x]|Medium|Hard [575. 分糖果](https://leetcode.cn/problems/distribute-candies)

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

