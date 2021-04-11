# 轻量化博客构建方案与写作规范
*2020040701-lightweight-blog-construction-plan-and-writing-standard*  
*Posted on 2020.04.08 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


* [轻量化博客构建方案与写作规范](#%E8%BD%BB%E9%87%8F%E5%8C%96%E5%8D%9A%E5%AE%A2%E6%9E%84%E5%BB%BA%E6%96%B9%E6%A1%88%E4%B8%8E%E5%86%99%E4%BD%9C%E8%A7%84%E8%8C%83)
    * [引言](#%E5%BC%95%E8%A8%80)
    * [方案](#%E6%96%B9%E6%A1%88)
    * [规范](#%E8%A7%84%E8%8C%83)


## 引言

从某种角度来说，博客有如下两种类型：

第一类：
[【CodingHorror】](https://blog.codinghorror.com/ "programming and human factors")
[【Asymptotia】](https://asymptotia.com "a professor at the Department of Physics and Astronomy, at the University of Southern California")
[【风雪之隅】](https://www.laruence.com/ "左手代码右手诗")
[【学而时嘻之】](https://www.geekonomics10000.com/ "用理工科思维理解世界")
[【王孟源】](http://blog.udn.com/MengyuanWang/article "事實與邏輯")
[【阮一峰】](http://www.ruanyifeng.com/home.html "Ruan Yifeng's Personal Website")

第二类：
[【Matt Might】](http://matt.might.net/ "Professor of Internal Medicine and Computer Science Hugh Kaul Endowed Chair in Personalized Medicine Director, Hugh Kaul Precision Medicine Institute")
[【Steve Losh】](https://stevelosh.com/ "a photographer, programmer, dancer, and bassist")
[【Homebrew Cpu】](http://www.homebrewcpu.com/ "Not a blog")


第一类博客是常规的，有丰富的UI设计及各种功能模块，第二类博客则是“简陋的”，连评论功能都没有。直接用动态网站、静态网站将这些博客作以区分似乎并不合适，上面列举的除了最后一个，其它都算不上静态。

本文暂且用【轻量化】来形容这第二类形式的博客，并提供了一套以Markdown为基础的简单构建方案。


## 方案

方案的核心思想在于**使用Markdown快捷地编写Html文件，利用操作系统的文件夹层级关系管理内容**。项目结构示例如下：

```shell
ROOT.
│  index.html
│  index.md
│
├─docs
│  ├─2018
│  ├─2019
│  └─2020
│     ├─03
│     │      2020031101-java-basic-knowledge-review-1-eight-primitive-data-types.html
│     │      2020031101-java-basic-knowledge-review-1-eight-primitive-data-types.md
│     │      2020031201-java-basic-knowledge-review-2-oop-and-its-basic-characteristics.html
│     │      2020031201-java-basic-knowledge-review-2-oop-and-its-basic-characteristics.md
│     │      2020032301-java-basic-knowledge-review-3-access-control-and-feature-modifier.html
│     │      2020032301-java-basic-knowledge-review-3-access-control-and-feature-modifier.md
│     │
│     └─04
│            2020040401-python3-zero-to-one-challenge-a-text-rpg-game.html
│            2020040401-python3-zero-to-one-challenge-a-text-rpg-game.md 
│
└─res
    ├─2018
    ├─2019
    └─2020
        └─03
                2020031101-test1.jpg
                2020031101-test2.jpg
                2020031101-test3.jpg

```

根目录内容：

* docs文件夹：用于存放文档
* res文件夹：用于存放图片等资源文件
* index.md：索引

规则：

* 文件夹内部使用年、月进行子目录划分
* 所有文件使用`日期+序号`进行分组编码
    - 2020032301 = 2020年3月23日第1篇文档
    - 2020032302 = 2020年3月23日第2篇文档
* 所有文件使用英文命名，方便链接地址的书写

说明：

Html文件都是通过Markdown解析工具生成的，我们只需要专注于markdown文档的书写，再稍微花费一点精力维护一份索引文件（主页）即可。文档中（包括索引文档）的内部链接均使用相对路径书写，这能最大程度保证整个博客的独立性，整个根目录丢到服务器上就可以访问（在本地端也一样）。

事实上，由于 Github Pages 会自动解析markdown文件，我的博客文件结构实际是这样的：
```shell
ROOT.
│  README.md
│
├─docs
│  ├─2018
│  ├─2019
│  └─2020
│     ├─03
│     │      2020031101-java-basic-knowledge-review-1-eight-primitive-data-types.md
│     │      2020031201-java-basic-knowledge-review-2-oop-and-its-basic-characteristics.md
│     │      2020032301-java-basic-knowledge-review-3-access-control-and-feature-modifier.md
│     │
│     └─04
│            2020040401-python3-zero-to-one-challenge-a-text-rpg-game.md 
│
└─res
    ├─2018
    ├─2019
    └─2020
        └─03
                2020031101-test1.jpg
                2020031101-test2.jpg
                2020031101-test3.jpg

```
也就是说，如果你只打算通过服务器访问博客，那么在服务器上架设好markdown自动解析的服务，写博客时连html文件都不必生成。



## 规范

规范是写作规范，作用是大致确定每篇文档的结构，提出规范的原因在于没有博客框架限制的情况下，需要一套规范来约束文档的格式从而让博客具有一定的统一性。

本博客中的所有文档采用如下规范进行编写：

```markdown
# 文章标题
*文档名称*  
*一句话标注日期、署名、协议*  
*更新记录*

[TOC]

## 1 第一小节

### 1.1 第一小节第一部分

[示例链接1][1-1-1]
[示例链接2][1-1-2]

### 1.2 第一小节第二部分

[commit]:第一小节链接统一存放区------------

[1-1-1]:../03/xxx "示例链接1"
[1-1-2]:../03/xxx "示例链接1"

## 2 第二小节

### 2.1
### 2.2

## 3 第三小节
```


说明：

* 在文章显著位置标注一些重要信息（尤其是时间信息）通常是必要的，附注署名与版权协议可以为潜在的传播提供便利。
* `[TOC]`是用于生成目录的命令，Github的markdown解析不支持此命令，目前我采用[github-markdown-toc](https://github.com/ekalinin/github-markdown-toc)这个工具手动生成并添加到文档中。
* 链接地址可以统一存放在文末，若文章较长则放在对应小节末（方便管理），尽量不要在文中直接用圆括号的形式插入链接地址（以保证markdown文档本身的可读性）。


示例：
```md
# Python3从零到一挑战：写个文字版RPG
*2020040401-python3-zero-to-one-challenge-a-text-rpg-game*  
*Published on 2020.04.04 by [Vilaseaka](https://vilaseaka.github.io) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  
*Updated on 2020.04.05 本文代码已归档于[AboutProgramming/AboutPython3/rpg-game][rpg-game]*  


* [Python3从零到一挑战：写个文字版RPG](#python3%E4%BB%8E%E9%9B%B6%E5%88%B0%E4%B8%80%E6%8C%91%E6%88%98%E5%86%99%E4%B8%AA%E6%96%87%E5%AD%97%E7%89%88rpg)
    * [1 前言](#1-%E5%89%8D%E8%A8%80)
    * [2 熟悉](#2-%E7%86%9F%E6%82%89)
    * [3 构建](#3-%E6%9E%84%E5%BB%BA)
    * [4 代码整理](#4-%E4%BB%A3%E7%A0%81%E6%95%B4%E7%90%86)
    * [5 试玩](#5-%E8%AF%95%E7%8E%A9)
    * [6 结语](#6-%E7%BB%93%E8%AF%AD)

## 1 前言

云淡风清一轮江月明，漂泊我此生任多情  
几分惆怅惆怅有几分，独让我自怜水中影

## 2 熟悉

* 甜蜜往事浮现在心底啊
* 多少回忆锥痛我的心啊

## 3 构建

1. 我是不是牵挂都为你
2. 怪我爱得浓时却不懂情

## 4 代码整理

*好梦易醒易醒是好梦*  
*留不住转眼成云烟*

## 5 试玩

**我问天呀天呀不应我，是不是天也不懂情**

## 6 结语

我问天呀天呀不应我  
是不是天也不懂情  
天也不懂情

```

显示效果如下：

======================================显示效果展示========================================

# Python3从零到一挑战：写个文字版RPG
*2020040401-python3-zero-to-one-challenge-a-text-rpg-game*  
*Published on 2020.04.04 by [Vilaseaka](https://vilaseaka.github.io) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  
*Updated on 2020.04.05 本文代码已归档于[AboutProgramming/AboutPython3/rpg-game][rpg-game]*  


* [Python3从零到一挑战：写个文字版RPG](#python3%E4%BB%8E%E9%9B%B6%E5%88%B0%E4%B8%80%E6%8C%91%E6%88%98%E5%86%99%E4%B8%AA%E6%96%87%E5%AD%97%E7%89%88rpg)
    * [1 前言](#1-%E5%89%8D%E8%A8%80)
    * [2 熟悉](#2-%E7%86%9F%E6%82%89)
    * [3 构建](#3-%E6%9E%84%E5%BB%BA)
    * [4 代码整理](#4-%E4%BB%A3%E7%A0%81%E6%95%B4%E7%90%86)
    * [5 试玩](#5-%E8%AF%95%E7%8E%A9)
    * [6 结语](#6-%E7%BB%93%E8%AF%AD)

## 1 前言

云淡风清一轮江月明，漂泊我此生任多情  
几分惆怅惆怅有几分，独让我自怜水中影

## 2 熟悉

* 甜蜜往事浮现在心底啊
* 多少回忆锥痛我的心啊

## 3 构建

1. 我是不是牵挂都为你
2. 怪我爱得浓时却不懂情

## 4 代码整理

*好梦易醒易醒是好梦*  
*留不住转眼成云烟*

## 5 试玩

**我问天呀天呀不应我，是不是天也不懂情**

## 6 结语

我问天呀天呀不应我  
是不是天也不懂情  
天也不懂情