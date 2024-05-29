# Leetcode Study Plan Leetcode-75 Scratch Paper

*Created on 2024.05.28 by [Zhang Pengwei](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 


题单地址：https://leetcode.cn/studyplan/leetcode-75/

简单：`*`  
中等：`**`  
困难：`***`

## 数组/字符串

#### [1768. Merge Strings Alternately*](https://leetcode.cn/problems/merge-strings-alternately/)

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # O(n), O(1)
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

#### []()

```python

```


#### []()

```python

```


#### []()

```python

```


## 滑动窗口

#### []()

```python

```


#### []()

```python

```


#### []()

```python

```


## 前缀和

#### []()

```python

```


#### []()

```python

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