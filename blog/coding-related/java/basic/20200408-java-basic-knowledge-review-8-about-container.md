# JAVA基础知识复盘（八）：集合框架基础
*2020040801-java-basic-knowledge-review-8-about-container*  
*Posted on 2020.04.08 by [pwz](https://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  

[TOC]


## 1 概述

Java的集合框架，是由标准库中的一组接口及其实现类共同构建起来的，实现了绝大部分常用的数据结构。集合框架是在1.2版本之后才被引入的，并且兼容了之前就存在的一些容器类，所以在现在的集合框架中仍然可以见到一些老旧的容器（例如Stack、Hashtable等），没有特殊情况不建议使用。

概览整个集合框架，用一张图来表示最为合适，因为整个集合框架的继承、实现关系相互交错，难以用单一的树形结构描述。在此处，先把整个集合框架拆解开，过滤掉一些不常用的中间内容，将骨架摸清。

### 1.1 两大分支

集合框架有两大分支，集合及映射。

---

to be continued