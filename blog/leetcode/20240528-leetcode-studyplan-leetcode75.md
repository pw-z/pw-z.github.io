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
      - [1768. Merge Strings Alternately*](#1768-merge-strings-alternatelyhttpsleetcodecnproblemsmerge-strings-alternately)
      - [](#)
      - [](#-1)
      - [](#-2)
      - [](#-3)
      - [](#-4)
  - [双指针](#双指针)
      - [](#-5)
      - [](#-6)
      - [](#-7)
  - [滑动窗口](#滑动窗口)
      - [](#-8)
      - [](#-9)
      - [](#-10)
  - [前缀和](#前缀和)
      - [](#-11)
      - [](#-12)
      - [](#-13)
  - [哈希](#哈希)
      - [](#-14)
      - [](#-15)
      - [](#-16)
  - [栈](#栈)
      - [](#-17)
      - [](#-18)
      - [](#-19)

<!-- /code_chunk_output -->



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