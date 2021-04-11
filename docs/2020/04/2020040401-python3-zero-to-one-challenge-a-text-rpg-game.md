# Python3从零到一挑战：写个文字版RPG
*2020040401-python3-zero-to-one-challenge-a-text-rpg-game*  
*Posted on 2020.04.04 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  
*Updated on 2020.04.05 本文代码已归档于[AboutProgramming/AboutPython3/rpg-game][rpg-game]*  


* [Python3从零到一挑战：写个文字版RPG](#python3%E4%BB%8E%E9%9B%B6%E5%88%B0%E4%B8%80%E6%8C%91%E6%88%98%E5%86%99%E4%B8%AA%E6%96%87%E5%AD%97%E7%89%88rpg)
    * [1 前言](#1-%E5%89%8D%E8%A8%80)
    * [2 熟悉](#2-%E7%86%9F%E6%82%89)
        * [2\.1 构建项目](#21-%E6%9E%84%E5%BB%BA%E9%A1%B9%E7%9B%AE)
            * [2\.1\.1 打开PyCharm先把项目构建起来再说](#211-%E6%89%93%E5%BC%80pycharm%E5%85%88%E6%8A%8A%E9%A1%B9%E7%9B%AE%E6%9E%84%E5%BB%BA%E8%B5%B7%E6%9D%A5%E5%86%8D%E8%AF%B4)
            * [2\.1\.2 Python怎么进行包管理？](#212-python%E6%80%8E%E4%B9%88%E8%BF%9B%E8%A1%8C%E5%8C%85%E7%AE%A1%E7%90%86)
                * [重新调整包结构](#%E9%87%8D%E6%96%B0%E8%B0%83%E6%95%B4%E5%8C%85%E7%BB%93%E6%9E%84)
        * [2\.2 熟悉基础语法](#22-%E7%86%9F%E6%82%89%E5%9F%BA%E7%A1%80%E8%AF%AD%E6%B3%95)
        * [2\.3 内置数据类型](#23-%E5%86%85%E7%BD%AE%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)
            * [2\.3\.1 “声明变量”](#231-%E5%A3%B0%E6%98%8E%E5%8F%98%E9%87%8F)
                * [通过type()函数检测变量类型](#%E9%80%9A%E8%BF%87type%E5%87%BD%E6%95%B0%E6%A3%80%E6%B5%8B%E5%8F%98%E9%87%8F%E7%B1%BB%E5%9E%8B)
            * [2\.3\.2 8个重要的内置数据类型](#232-8%E4%B8%AA%E9%87%8D%E8%A6%81%E7%9A%84%E5%86%85%E7%BD%AE%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)
                * [数值运算](#%E6%95%B0%E5%80%BC%E8%BF%90%E7%AE%97)
                * [删除对象](#%E5%88%A0%E9%99%A4%E5%AF%B9%E8%B1%A1)
                * [List、Tuple、Set、Dictionary](#listtuplesetdictionary)
                    * [List](#list)
                    * [Tuple](#tuple)
                    * [Set(集合)](#set%E9%9B%86%E5%90%88)
                    * [Dictionary](#dictionary)
        * [2\.4 函数与类](#24-%E5%87%BD%E6%95%B0%E4%B8%8E%E7%B1%BB)
            * [2\.4\.1 认识函数](#241-%E8%AE%A4%E8%AF%86%E5%87%BD%E6%95%B0)
                * [数学函数](#%E6%95%B0%E5%AD%A6%E5%87%BD%E6%95%B0)
                * [随机函数](#%E9%9A%8F%E6%9C%BA%E5%87%BD%E6%95%B0)
                    * [range函数](#range%E5%87%BD%E6%95%B0)
                    * [random模块](#random%E6%A8%A1%E5%9D%97)
            * [2\.4\.2 定义函数](#242-%E5%AE%9A%E4%B9%89%E5%87%BD%E6%95%B0)
            * [2\.4\.3 认识并定义“类”（class）](#243-%E8%AE%A4%E8%AF%86%E5%B9%B6%E5%AE%9A%E4%B9%89%E7%B1%BBclass)
                * [使用继承](#%E4%BD%BF%E7%94%A8%E7%BB%A7%E6%89%BF)
        * [2\.5 输入输出](#25-%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA)
            * [2\.5\.1 控制台I/O](#251-%E6%8E%A7%E5%88%B6%E5%8F%B0io)
                * [带颜色的输出](#%E5%B8%A6%E9%A2%9C%E8%89%B2%E7%9A%84%E8%BE%93%E5%87%BA)
                    * [参数](#%E5%8F%82%E6%95%B0)
            * [2\.5\.2 文件I/O](#252-%E6%96%87%E4%BB%B6io)
                * [写入文件](#%E5%86%99%E5%85%A5%E6%96%87%E4%BB%B6)
                * [从文件读](#%E4%BB%8E%E6%96%87%E4%BB%B6%E8%AF%BB)
        * [2\.6 控制语句](#26-%E6%8E%A7%E5%88%B6%E8%AF%AD%E5%8F%A5)
    * [3 构建](#3-%E6%9E%84%E5%BB%BA)
        * [3\.1 游戏构想](#31-%E6%B8%B8%E6%88%8F%E6%9E%84%E6%83%B3)
        * [3\.2 数值策划](#32-%E6%95%B0%E5%80%BC%E7%AD%96%E5%88%92)
        * [3\.3 代码编写](#33-%E4%BB%A3%E7%A0%81%E7%BC%96%E5%86%99)
            * [3\.2\.1 英雄类编写](#321-%E8%8B%B1%E9%9B%84%E7%B1%BB%E7%BC%96%E5%86%99)
            * [3\.2\.2 怪物类编写](#322-%E6%80%AA%E7%89%A9%E7%B1%BB%E7%BC%96%E5%86%99)
            * [3\.2\.3 装备模块](#323-%E8%A3%85%E5%A4%87%E6%A8%A1%E5%9D%97)
                * [英雄、怪物、装备阶段测试](#%E8%8B%B1%E9%9B%84%E6%80%AA%E7%89%A9%E8%A3%85%E5%A4%87%E9%98%B6%E6%AE%B5%E6%B5%8B%E8%AF%95)
            * [3\.2\.4 主框架](#324-%E4%B8%BB%E6%A1%86%E6%9E%B6)
    * [4 代码整理](#4-%E4%BB%A3%E7%A0%81%E6%95%B4%E7%90%86)
        * [4\.1 hero\.py](#41-heropy)
        * [4\.2 monster\.py](#42-monsterpy)
        * [4\.3 equip\.py](#43-equippy)
        * [4\.4 main\.py](#44-mainpy)
    * [5 试玩](#5-%E8%AF%95%E7%8E%A9)
    * [6 结语](#6-%E7%BB%93%E8%AF%AD)


## 1 前言

眼下要用到Python但对其一无所知，系统化学习需要时间，突然想到不如换种形式，直接上手做开发，实现点什么，来一次字面意义上的“极限编程”，这样是否能更高效的快速上手一门编程语言呢?也没试过不知道效果如何，今天就借这篇文档试一试。

初步设想是实现一个简单的文字版RPG小游戏，“月黑风高之绿明村大冒险”啥的，只有这么个设想。电脑里安装了Python3.7.2、PyCharm2019.1.1，可以联网。手里有《[深入Python3][1-1]》、《[Think Python 2e 中文版][1-2]》、《[Python Cookbook 3rd Edition][1-3]》这三本书。现在的时间是2020年4月4日06点52分，来吧，挑战开始。

*尽量把整个过程都记录一下，求效率就顾不上章节安排之类的，估计很乱。*

[1-1]:https://woodpecker.org.cn/diveintopython3/ "深入 Python 3"
[1-2]:https://legacy.gitbook.com/book/wizardforcel/think-python-2e/details "Think Python 2e 中文版"
[1-3]:https://github.com/yidao620c/python3-cookbook "Python Cookbook 3rd Edition"

## 2 熟悉

### 2.1 构建项目

#### 2.1.1 打开PyCharm先把项目构建起来再说

根目录名称为AboutPython3，项目结构如下：
```shell
(venv) E:\Code\PythonRepo\AboutPython3>tree
卷 软件 的文件夹 PATH 列表
卷序列号为 000B-DFAB
E:.
├─.idea
│  └─libraries
└─venv
```

* Q1： 这里提示创建了一个默认的venv，venv是啥？
    - P: 以pycharm venv为关键字检索：[pycharm-虚拟环境安装第三方库](https://www.jianshu.com/p/b4b2a686423e)
    - A: venv是为当前项目创建的虚拟环境，此项目的依赖都放在这个虚拟环境里统一管理，从而与系统的全局类库区分开

*此处临时定义，每次遇到一个小问题，可以通过无序列表的形式进行处理，Q=问题，P=中间过程，A=结果*  


#### 2.1.2 Python怎么进行包管理？

现在直接在根目录里创建子文件夹可以吗？尝试创建com.vilaseaka.game包后：
```shell
(venv) E:\Code\PythonRepo\AboutPython3>tree /f
卷 软件 的文件夹 PATH 列表
卷序列号为 000B-DFAB
E:.
├─.idea
│  │  AboutPython3.iml
│  │  misc.xml
│  │  modules.xml
│  │  workspace.xml
│  │
│  └─libraries
│          R_User_Library.xml
│
├─com
│  │  __init__.py
│  │
│  └─vilaseaka
│      │  __init__.py
│      │
│      └─game
│              __init__.py
│
└─venv

```
每个子文件夹下都生成了一个`_init_.py`，这是啥，似乎不能把Java的包管理思想直接挪用，Python怎么进行项目结构的安排呢？

* Q1: “\_init\_.py”是什么？
    - P：[Python __init__.py 文件使用](https://www.jianshu.com/p/b233b158ca51?utm_source=desktop&utm_medium=timeline)
    - A: \__init\__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件

*取消前面的Q、P、A临时定义，每一个问题单独作为一个子标题来处理，这样更工整一点*

##### 重新调整包结构

貌似Python的包管理不像Java那样用复杂的层次结构区分命名空间，好多\__init\__.py看着难受，重新安排目录结构：
```shell
(venv) E:\Code\PythonRepo\AboutPython3>tree /f
卷 软件 的文件夹 PATH 列表
卷序列号为 000B-DFAB
E:.
├─.idea
│  │  AboutPython3.iml
│  │  misc.xml
│  │  modules.xml
│  │  workspace.xml
│  │
│  └─libraries
│          R_User_Library.xml
│
├─rpg-game
│      __init__.py
│
└─venv
```
项目暂时就构建成这样，接下来可以在里面写代码了。

### 2.2 熟悉基础语法

Python代码是以.py的形式存放的，新建一个basicSyntaxTest.py文件，熟悉下基础语法。

*此处打开[Python3 基础语法 - 菜鸟教程](https://www.runoob.com/python3/python3-basic-syntax.html)*


**1. 编码格式**

    * 默认格式UTF-8
    * 更改编码格式：`# -*- coding: cp-1252 -*-`

**2. 标识符**

    * 首字母必须是字母或下划线
    * 大小写敏感

**3. 保留字**

打开PyCharm的PythonConsole输入Python命令进行查看：
```python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

```
**4. 注释**
```python
# 单行注释
print ("Hello, Python!")  # 代码后的单行注释

# 通过
# 单行
# 注释
# 假装
# 多行
# 注释

'''
通过单引号
实现多行注释
'''

"""
通过双引号
实现多行注释
"""
```
**5. 行与缩进**

Python中不适用分号与花括号组织代码，而是使用行与缩进表示代码块：
```python
if True:
    print ("True")
else:
    print ("False")
'''output
True
'''
```

**6. 多行语句**  

**方式一：使用反斜杠**
```python
print("这是一句为了测试\
      而写的有点长但是\
      没啥用的话")
# 这是一句为了测试      而写的有点长但是      没啥用的话
print("这是一句为了测试"
      "而写的有点长"
      "但是没啥用的话")
# 这是一句为了测试而写的有点长但是没啥用的话
```
这里把反斜杠用在字符串里面似乎会有副作用，下面是代码提示给出的，它可以自动拼接
```python
total = item_one + \
        item_two + \
        item_three
```
这是菜鸟教程里的例子，这种才是反斜杠的常规使用场景吧。

**方式二：通过 [], {}, 或 ()**

大概是这个意思：
```python
{print("A"),print("B"),
print("C"),print("D")}
'''
A
B
C
D
'''

# 菜鸟教程的例子：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)
# ['item_one', 'item_two', 'item_three', 'item_four', 'item_five']
```
看来默认的print语句会自动换行，变量名也不用规定类型，会自动识别。

**7. 数字类型**

> python中数字有四种类型：整数、布尔型、浮点数和复数。
> 
> * int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
> * bool (布尔), 如 True。
> * float (浮点数), 如 1.23、3E-2
> * complex (复数), 如 1 + 2j、 1.1 + 2.2j

原生支持复数，还是基本类型，联想到很方便用python进行科学计算

**8. 字符串**

搬运：
> * python中单引号和双引号使用完全相同。
> * 使用三引号('''或""")可以指定一个多行字符串。
> * 转义符 '\\'
>     - 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
> * 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
> * 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
> * Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
> * Python中的字符串不能改变。
> * Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
> * 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]

自己实践：
```python
# 多行字符串
print("""啥叫多行字符串啊
是这个意思？
？？？
？？？？""")
'''output
啥叫多行字符串啊
是这个意思？
？？？
？？？？
'''
# 看来就是这个意思

# 转义字符
print("你好\n世界")
'''output
你好
世界
'''
# 停用转义字符
print(r"你好\n世界")
'''output
你好\n世界
'''

# 自动连接、通过+连接、通过*重复
print("你好""啊""世界" + "!"*5)
'''output
你好啊世界!!!!!
'''

# 字符串截取
string = "0123456789"
print(string[0:2])
print(string[2:-1])
print(string[2:-2])
print(string[1:])
print(string[2:-1])
'''output
01
2345678
234567
123456789
2345678
'''
```

关于字符串截取单独拎出来说一下：

* Python索引两种方式:  
    - 从左往右为从0开始逐一递增
    - 从右往左为从-1开始逐一递减；
* 区间是前闭后开区间string[0:2]相当于string[0:2)，所以2是取不到的
```python
# 字符串截取 前闭后开原则
string = "0123456789"
print(string[1])
print(string[3])
print(string[1:3])
print(string[-1])
print(string[-3])
print(string[-3:-1])
'''output
1
3
12
9
7
78
'''
```

**9. 空行分隔代码段**

使用空行来区分不同的代码块，类和函数入口之前都用空行区分，

>空行与代码缩进不同，空行并不是Python语法的一部分。  
>书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。  
>**记住**：空行也是程序代码的一部分。


**10. 多个语句构成代码组**

循环块、定义函数、定义类等语句，首行用关键字开始，用冒号结尾，之后的一行或几行代码构成代码组：
```python
# 代码组的概念
if False:
    print("这里是不会被执行的")
elif False:
    print("一样")
else:
    print("第三个代码组")
    print("缩进相同")
    print("所以还是")
    print("同一个代码组的代码")
'''output
第三个代码组
缩进相同
所以还是
同一个代码组的代码
'''
```
首行及后面的代码组称为一个子句(clause)
```python
# 这是一个clause
if False:
    print("这里是不会被执行的")
```

**11. Print 输出**

>print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

```python
print("这是一句不换行的话+",end="")
print("这句就换行了")
print("不信你看")
'''output
这是一句不换行的话+这句就换行了
不信你看
'''
```

**12. 导入包**

> * 将整个模块(somemodule)导入，格式为： import somemodule
> * 从某个模块中导入某个函数,格式为： from somemodule import somefunction
> * 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
> * 将某个模块中的全部函数导入，格式为： from somemodule import *

这个与java一样，用import关键字，不过还附赠了个from关键字，用于从某个包中导入一部分，另外可以通过as关键字给导入的模块起一个别名，看例子：
```python
import pickle
import numpy as np
import tensorflow as tf
from tqdm import tqdm
```


### 2.3 内置数据类型

数据类型、数据结构什么的还是重要，程序等于算法+数据结构（+文档），把基本的内置数据类型熟悉完，看看我们都能操纵什么，再开始尝试功能实现。

继续通过菜鸟教程熟悉基本数据结构，链接：[Python3 基本数据类型](https://www.runoob.com/python3/python3-data-type.html)，同时通过《深入Python3》查缺补漏。

新建一份.py文件，BasicDataType.py，刚刚那份代码也改个名，当前项目结构：
```shell
(venv) E:\Code\PythonRepo\AboutPython3>tree /f
卷 软件 的文件夹 PATH 列表
卷序列号为 000B-DFAB
E:.
├─.idea
│  │  AboutPython3.iml
│  │  misc.xml
│  │  modules.xml
│  │  workspace.xml
│  │
│  └─libraries
│          R_User_Library.xml
│
├─rpg-game
│      BasicDataType.py
│      BasicSyntax.py
│      __init__.py
│
└─venv
```


#### 2.3.1 “声明变量”

在Python中不需要手动声明类型，或者说根本不需要所谓的声明变量，不用像Java，以某种类型声明一个引用，在new一个实例化对象赋值给引用，在Python中你想用一个变量，直接起名字赋值就行，Python会自动识别数据类型。
```python
# “声明变量”
str1 = "不用声明变量，直接定义赋值就好"
a,b,c = 1,2,"vivil"
d = e = f = "赋值方式十分灵活"
print(str1 ,a, b , c , d , e , f)
'''
不用声明变量，直接定义赋值就好 1 2 vivil 赋值方式十分灵活 赋值方式十分灵活 赋值方式十分灵活
'''
```

##### 通过type()函数检测变量类型

```python
# 使用type检测任何值或变量的类型
test1 = "hello"
print(type(1))
print(type(1.1))
print(type(test1))
'''
<class 'int'>
<class 'float'>
<class 'str'>
'''
```

#### 2.3.2 8个重要的内置数据类型

* Booleans（布尔型）  
>*在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。*
* Number（数值型）
    - int
    - float
    - bool
    - complex
* String（字符串）
* Bytes（字节）与Byte Arrays（字节数组）
* List（列表）
* Tuple（元组）
* Set（集合）
* Dictionary（字典）

##### 数值运算

除了平常的加减乘除取余运算外，还有如下两个特殊的：
```python
x = 5//2  #结果取整
y = 2**3  #平方运算
print(x,y)
'''
2 8
'''
```
##### 删除对象

使用del关键字删除某个已经定义了的对象（比如某个Number），补充：Python里所有东西都是对象，一个Number是一个对象，一个函数也是一个对象，Python里定义的“对象”条件很宽松

```python
xx = 1
print(xx)
del xx  #卸磨杀驴
print(xx) #这里会报错，因为xx已经被我们删除了
```

##### List、Tuple、Set、Dictionary

> * List是写在方括号 [] 之间、用逗号分隔开的元素列表。
> * 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。 
> * 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。可以使用大括号 { } 或者 set() 函数创建集合。
> * 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

实践：

###### List

    1. List写在方括号之间，元素用逗号隔开。  
    2. 和字符串一样，list可以被索引和切片(就是前面的string[1:3])。  
    3. List可以使用+操作符进行拼接。  
    4. List中的元素是可以改变的。  

```python
# List
myList1 = [1,2,3,4,5]
myList2 = [myList1,"ha",22]
print(myList2)
print(myList2[1:])
'''
[[1, 2, 3, 4, 5], 'ha', 22]
['ha', 22]
'''
```


###### Tuple

与List基本一样，不过元素不能修改

```python
# Tuple
myTuple1 = (1,2,3,4,5)
myTuple2 = (myTuple1,"ha",22)
print(myTuple1)
print(myTuple2)
print(myTuple1[1:3]*3)
print(myTuple1 + myTuple2)
'''
(1, 2, 3, 4, 5)
((1, 2, 3, 4, 5), 'ha', 22)
(2, 3, 2, 3, 2, 3)
(1, 2, 3, 4, 5, (1, 2, 3, 4, 5), 'ha', 22)
'''
```

> 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：  
> 
>     tup1 = ()    # 空元组
>     tup2 = (20,) # 一个元素，需要在元素后添加逗号


###### Set(集合)

**Set的基本功能是成员关系测试和删除重复元素。**

```python
# Set
mySet = {"AA","BB","AA","CC","DD"}
print(mySet)        #自动删除重复元素
if "AA" in mySet:   #成员关系测试
    print("YES")
else:
    print("No")
'''
{'BB', 'DD', 'CC', 'AA'}
YES
'''
```

###### Dictionary

    1、字典是一种映射类型，它的元素是键值对。
    2、字典的关键字必须为不可变类型，且不能重复。
    3、创建空字典使用 { }。

```python
# Dictionary
myDictionary = {"key1":"value1","key2":"value2","key3":"value3"}
print(myDictionary)
print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.clear())
'''
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
dict_keys(['key1', 'key2', 'key3'])
dict_values(['value1', 'value2', 'value3'])
None
'''
```



### 2.4 函数与类

#### 2.4.1 认识函数

如何定义函数、类是迫切想知道的，不然只能进行顺序执行的程序不是。这里参考《Think Python 2e 中文版》这本书，主题阅读，都看看。

关于函数，前面已经用了好几个，不对，好像只用了两个，首先就是print函数了，内置的打印函数，另一个是type函数，可以用来验证值或变量的数据类型。

```python
# 函数
print("青城山下白素贞")
print(type("洞中千年修此身"))
'''
青城山下白素贞
<class 'str'>
'''
```
另外与Java类似，基本类型可以像构造器一样将某个值转化为对应类型，其实就是强制类型转换，不过它是通过函数实现的：
```python
# 基本类型转化
myInt = int(3.14)
myFloat = float(3)
print(myInt)
print(myFloat)
'''
3
3.0
'''
```

##### 数学函数

Python内置了math模块，提供了很多常用的数学工具：
```python
# math模块
import math
print(math.sqrt(4))      #开方
print(math.degrees(15))  #将弧度转换为角度
print(math.sin(30))
print(math.log10(1000))
print(math.pow(2,3))
'''
2.0
859.4366926962348
-0.9880316240928618
3.0
8.0
'''
```
另外有几个函数是内置的，不用导math就可以直接使用：
```python
# 非math模块的数学函数
print(abs(-3.14))          # 返回绝对值
print(max(1,2,3,4))        # 最大值，参数可以为序列
print(min(1,2,3,4))        # 最小值
print(pow(3,2))            # 乘方
print(round(3.1415926,2))  # 四舍五入，n为可选参数,表示舍入位数
'''
3.14
4
1
9
3.14
'''
```

##### 随机函数

随机函数也是必需品，游戏总的有点随机性。

###### range函数

* 补充：内置函数range()可创建一个整数列表，range(start, stop[, step])
    - start：开始值，默认从0开始
    - stop：结束值
    - step：补偿，可选，默认为1
    - 此列表是不可变列表
>There are three basic sequence types: lists, tuples, and range objects.(有三种基本的序列类型：列表、元组和范围（range）对象) 

```python
# range函数
a1 = range(10)
a2 = range(2,8)
a3 = range(1,20,2)
print(a1)
print(a2)
print(a3)
for i in a1:
    print(i,end="")
print()
for i in a2:
    print(i,end="")
print()
for i in a3:
    print(i,end="")
print()
'''
range(0, 10)
range(2, 8)
range(1, 20, 2)
0123456789
234567
135791113151719
'''
```

###### random模块

python的随机函数封装在random模块里：

> * choice(seq) 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
>     - seq -- 可以是一个列表，元组或字符串。
> * randrange ([start,] stop [,step])   从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
> * random()    随机生成下一个实数，它在[0,1)范围内。
> * seed([x])   改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
> * shuffle(lst)    将序列的所有元素随机排序
> * uniform(x, y)   随机生成下一个实数，它在[x,y]范围内。  
> 
> *[https://www.runoob.com/python3/python3-number.html](https://www.runoob.com/python3/python3-number.html)*

```python
# random模块
import random
testList = [1,2,3,45,56,765,12]
print(random.choice(range(10)))
print(random.choice(range(10)))
print(random.random())

print(testList)
print(random.shuffle(testList))
print(testList)
'''
8
8
0.7439232058660369
[1, 2, 3, 45, 56, 765, 12]
None
[765, 1, 56, 12, 2, 3, 45]
'''
```

#### 2.4.2 定义函数

函数定义通过def关键字实现，def后面接上函数名，冒号，下面用缩进构建一个代码块即可：
```python
# 定义函数
def print_hello(time):
    x=0
    while x<time:
        print("hello啊")
        x = x+1

print_hello(4)
'''
hello啊
hello啊
hello啊
hello啊
'''
```

*!-----------去买东西！暂停下，时间戳：2020年4月4日08点17分--------!*  
*!-----------继续，时间戳：2020年4月4日11点02分--------!*


#### 2.4.3 认识并定义“类”（class）

前面说了python里一切都是对象，python在设计之初就实现了面向对象。

在python中也用class关键字表示一个类，可以在里面封装属性、方法，同样的也可以通过继承、重写方法实现多态。

直接把面向对象那一套思想拿过来实践，这里先新建一个Hero.py文件：
```python
# 英雄父类
class Hero:
    name = ''   # 角色名
    hp = 0      # 生命值
    mp = 0      # 法力值
    atk = 0     # 攻击力
    deff = 0    # 防御力

    def __init__(self):
        self.name = '普通英雄'
        self.hp = 100
        self.mp = 100
        self.atk = 50
        self.deff = 50

    def battleCry(self): # 战吼技能 遇到敌人后自动释放
        print("battleCry")

    def activeSkill(self): # 主动技能 手动释放
        print("activeSkill")

    def passiveSkill(self): # 被动技能 默认增益
        print("passiveSkill")


# 定义一个类之后最好空两行以上

myTestHero = Hero()
print(myTestHero.name)
'''
普通英雄
'''
```

* 类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
*  __init__() 方法是python类的构造方法

##### 使用继承

继承在类名后面加括号填写，可以使用多重继承，在括号里用逗号分隔就行：
```python
# 使用继承
class HumanHero(Hero):

    def __init__(self):
        self.name = '人类英雄'

    def battleCry(self):
        super().battleCry()

    def activeSkill(self):
        super().activeSkill()

    def passiveSkill(self):
        super().passiveSkill()


# 多重继承举例
class xxx(y1,y2,y3):
    //……

myTestHero2 = HumanHero()
print(myTestHero2.name)
'''
人类英雄
'''
```

### 2.5 输入输出

#### 2.5.1 控制台I/O

输出就不说了，print函数，格式化方面的内容等用到的时候再说。

通过键盘输入东西，关键字为input，直接看例子：
```python
# 输入输出
inputSomething = input()
print(inputSomething)
'''
你好
你好
'''

# 添加提示信息
inputSomething = input("请输入点啥：")
print("您输入的为：" + inputSomething)
'''
请输入点啥：你好
您输入的为：你好
'''
```

##### 带颜色的输出

> 终端的字符颜色是用转义序列控制的，是文本模式下的系统显示功能，和具体的语言无关。
> 转义序列是以ESC开头,即用\033来完成（ESC的ASCII码用十进制表示是27，用八进制表示就是033）。
> *[Python3使用Print输出带颜色字体](https://www.cnblogs.com/fangbei/p/python-print-color.html)*

具体到python的print语句中：

    print("\033[显示方式;前景色;背景色m输出内容\033[0m")

###### 参数

**显示方式：**

* 0（默认）
* 1（高亮(好像就是加粗)）
* 22（非粗体）
* 4（下划线）
* 24（非下划线）
* 5（闪烁）
* 25（非闪烁）
* 7（反显）
* 27（非反显）


**颜色：**

|字体色|背景色|颜色|
|:---:|:--:|:---:|
|30  |40  |黑色|
|31  |41  |红色|
|32  |42  |绿色|
|33  |43  |黄色|
|34  |44  |蓝色|
|35  |45  |紫色|
|36  |46  |青色|
|37  |47  |白色|


举例：
```python
print('This is a \033[1;35m test \033[0m!')
print("\033[1;31;42m黄金号角！\033[0m")
```
显示效果就不妨上来了，markdown显示颜色还挺麻烦。



#### 2.5.2 文件I/O

文件通过open函数打开：open(filepath, mode)，mode包括只读、读写、追加等等，mode参数可选，不手动指定的情况下默认为r（只读）。

> * r  
>     * 以只读方式打开文件。文件的指针将会放在文件的开头。
>     * 这是默认模式。
> * r+
>     * 打开一个文件用于读写。
>     * 文件指针将会放在文件的开头。
> * w
>     * 打开一个文件只用于写入。
>     * 如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
>     * 如果该文件不存在，创建新文件。
> * w+
>     * 打开一个文件用于读写。
>     * 如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
>     * 如果该文件不存在，创建新文件。
> * a
>     * 打开一个文件用于追加。
>     * 如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。
>     * 如果该文件不存在，创建新文件进行写入。
> * a+
>     * 打开一个文件用于读写。
>     * 如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。
>     * 如果该文件不存在，创建新文件用于读写。
>
> *from:[file:///C:/users/admini~1/appdata/local/temp/14.html#252-io](file:///C:/users/admini~1/appdata/local/temp/14.html#252-io)*

##### 写入文件

通过write方法进行写入：
```python
f = open("log.txt","w")
f.write("It's so easy to fall in love\nPeople tell me love's for fools\nHere I go breaking all the rules")
```
以上代码会在同级目录中创建log.txt，内容如下：
```txt
It's so easy to fall in love
People tell me love's for fools
Here I go breaking all the rules
```

##### 从文件读

读取通过read函数，read函数有很多种，read()是全部读入，readline()只读一行，诸如此类，看例子：
```python
# 读取整个文件
f = open("log.txt","r")
print(f.read())
f.close()
'''
It's so easy to fall in love
People tell me love's for fools
Here I go breaking all the rules
'''

# 按行读取
f = open("log.txt","r")
print(f.readline())
print(f.readline())
f.close()
'''
It's so easy to fall in love

People tell me love's for fools

'''

# 读取多行，放入List中
f = open("log.txt","r")
print(f.readlines())
f.close()
'''
["It's so easy to fall in love\n", "People tell me love's for fools\n", 'Here I go breaking all the rules']
'''
```



### 2.6 控制语句

稍微过一遍控制语句，循环、条件什么的，虽然各类编程语言在这方面都差不多，这里直接写代码里了：

```python
n = int(input("请输入n的值"))
if n%2==0:
    print(str(n) + "为偶数\n开始倒数")
    while n>0:
        print(n)
        n=n-1
    else:
        print("数到0了！")
else:
    print(str(n)  + "为奇数\n向上数3个数")
    for i in range(3):
        print(n + i)
'''
请输入n的值6
6为偶数
开始倒数
6
5
4
3
2
1
数到0了！

请输入n的值5
5为奇数
向上数3个数
5
6
7
'''
```
基本就这样，语法熟悉就到这里，下面开始正式构建游戏。


*时间戳：2020年4月4日12点41分*



## 3 构建

### 3.1 游戏构想

主线剧情：打怪升级攒装备，消灭最终BOSS秦义绝，还天下天平。

0. 主菜单
    1. 选择冒险：进入地图选择模块
    2. 查看属性：基本属性+装备属性
1. 地图模块
    1. 地图里包括不同的关卡
    2. 每个关卡里有随机的怪物，可以掉落装备
2. 装备模块
    1. 装备等级：普通（白）->稀有（紫）->传奇（金）
    2. 装备基本属性为加攻击、防御
    2. 稀有装备具有特殊技能
3. 英雄模块
    1. 英雄就是我们使用的角色
    2. 英雄基本属性都一样，通过战吼与技能加以区分
    3. 基本属性包括：hp、mp、atk
4. 怪物模块
    1. 同等级的怪物与英雄相比，血量略厚，攻击略高（人物有防御力）
    2. 怪物只有生命值与攻击力两个基本属性
    3. 精英怪在上述基础上属性翻倍，精英怪可以掉落装备
5. 战斗模块
    1. 负责计算是否遇到怪物
    2. 负责计算一场战斗的结果并回显
    3. 战斗结束后回复角色状态，显示继续探险还是返回城镇
6. 记录模块
    1. 负责记录每一步操作
        1. 移动
        2. 战斗
        3. 发动技能等等
        4. 战斗结果
    2. 写入log文件


### 3.2 数值策划

没了解过游戏的数值策划，这里随便YY一下，就不管合不合理了：

1. 英雄基本属性（1级）
    1. hp 100 每升一级+20
    2. mp 100 每升一级+2
    3. atk 50 每升一级+5
    5. level 1 升级所需经验10 每升一级所需经验+10
2. 怪物基本属性（三个级别的地图）
    0. 基础：
        1. hp 100 每升一级+40
        2. atk 30 每升一级+5
    1. 级别1（1~10级怪）
    2. 级别2（11~30级怪）
        1. 级别2开始有精英怪（有装备）
        2. 30级的精英怪必掉装备
    3. 级别3（31~50级怪）
        1. 40级以上精英怪有几率掉落传奇装备
3. 装备数值
    1. 只有攻击装备，等级与怪物等级一致，属性为怪物攻击力的一半
    2. 稀有装备加防御
    3. 传奇装备有一个主动技能
4. 技能属性
    + 主动技能按百分比计算耗蓝，每次消耗30%的蓝，战斗期间不可恢复
    + 装备技能发动一次耗蓝65%
    + 战吼与被动技能不耗蓝 
    + 主动技能的攻击力按照1.5倍基础伤害计算



### 3.3 代码编写

#### 3.2.1 英雄类编写

前文举例子的时候已经写了一个Hero.py，以那个为基础重新处理完善一下：
```python
#./Hero.py 

class Hero:
    name = ''   # 角色名
    hp = 0      # 生命值
    mp = 0      # 法力值
    atk = 0     # 攻击力

    def __init__(self):
        self.name = '未命名的普通英雄'
        self.hp = 100
        self.mp = 100
        self.atk = 50

    def battleCry(self): # 战吼技能 遇到敌人后自动释放
        print("battleCry")

    def activeSkill(self): # 主动技能 手动释放
        print("activeSkill")

    # def passiveSkill(self): # 被动技能 默认增益
    #     print("passiveSkill")


# 人族攻高
class HumanHero(Hero):

    level = 1   # 初始等级
    exp = 0     # 经验值
    equip = ''  # 初始装备为空

    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.mp = 100
        self.atk = 60

    def battleCry(self): # 人族战吼：对敌人造成60%攻击力的伤害
        return self.atk*0.6

    def activeSkill(self): # 人族主动技能：对敌人造成160%攻击力的伤害
        if self.mp>40:
            self.mp = self.mp - 40
            return self.atk*1.5
        else:
            return 0


# 兽人血厚
class BeastHero(Hero):

    level = 1   # 初始等级
    exp = 0     # 经验值
    equip = ''  # 初始装备为空

    def __init__(self,name):
        self.name = name
        self.hp = 150
        self.mp = 100
        self.atk = 50

    def battleCry(self): # 兽人战吼：对敌人造成50%攻击力的伤害
        return self.atk*0.5

    def activeSkill(self): # 兽人主动技能：对敌人造成150%攻击力的伤害
        if self.mp>40:
            self.mp = self.mp - 40
            return self.atk*1.5
        else:
            return 0
```
把被动技能取消了，麻烦，另外按照百分比扣蓝也换成了按固定值扣，反正升级只加一点（改成只加2点好了）。


#### 3.2.2 怪物类编写

怪物类直接把英雄类的技能去掉，数值改一下就好：
```python
import random

nameList1 = ['魔化大蜘蛛','魔化大老鼠','魔化大鸵鸟','腐败香菇蘑','冲角团教员','冲角团临时工','楼上的拖鞋','游荡的鬼魂','饥饿的小鬼']  # 场景1怪物名字
nameList2 = ['大地之熊','玄冰毒蚁','迅影斑斓豹','紫尾貂','堕落魔蛹','不死雪狐','八翼雷鹰王']  # 场景2怪物名字
nameList3 = ['魂灭先知','狂飙毁灭者','鬼剑圣人','火爆龙将','逆焰斗神','星辰玉龙','无双赤鬼']  # 场景3怪物名字


class Monster:
    name = ''   # 怪物名
    level = 0   # 等级
    exp = 0     # 经验
    hp = 0      # 生命值
    atk = 0     # 攻击力

    def __init__(self, level):
        if level <= 10:
            self.name = str(level) + "级的" + random.choice(nameList1)
        elif level <= 30:
            self.name = str(level) + "级的" + random.choice(nameList2)
        else:
            self.name = str(level) + "级的" + random.choice(nameList3)
        self.level = level
        self.exp = (5 + 5*(level-1))    # 每 +1 级 +5 经验
        self.hp = (100 + 40*(level-1))*(random.random()+0.5)  # 每 +1 级 +40 血  //再乘上(0.5-1.5)倍随机量
        self.atk = (30 + 5*(level-1))*(random.random()+0.5)   # 每 +1 级 +5 攻击 //再乘上(0.5-1.5)倍随机量


class MonsterPro(Monster):  # 精英怪
    equip = ''

    def __init__(self, level):
        if level <= 10:
            self.name = str(level) +"级的精英"+ random.choice(nameList1)
        elif level <= 30:
            self.name = str(level) +"级的精英"+ random.choice(nameList2)
        else:
            self.name = str(level) +"级的精英"+ random.choice(nameList3)
        self.level = level
        self.exp = (5 + 5*(level-1))*2    # 精英怪经验翻倍
        self.hp = ((100 + 40*(level-1))*2)*(random.random()+0.5)  # 精英怪血量翻倍 //再乘上(0.5-1.5)倍随机量
        self.atk = ((30 + 5*(level-1))*2)*(random.random()+0.5)  # 精英怪攻击翻倍 //再乘上(0.5-1.5)倍随机量
```

#### 3.2.3 装备模块

装备的名称 = 怪物名称 + 随机选取的某个物件

```python
import random

nameList1 = ['脚趾甲','牙齿','胳膊','鼻涕','头盖骨','汗毛','大眼睛','小拇指']
nameList2 = ['匕首','长剑','短斧','铃铛','乾坤袋','金枪']
nameList = [nameList1,nameList2]

class Equip:
    name = ''
    level = 0
    atk = 0

    def __init__(self, monster):
        self.name = monster.name + "的" + random.choice(random.choice(nameList))
        self.level = monster.level
        self.atk = monster.atk*0.5
```

##### 英雄、怪物、装备阶段测试

```python
mm = MonsterPro(32)
print("怪物名称：" + mm.name)
ee = Equip(mm)
print("装备名称：" + ee.name)
mm.equip = ee
print("怪物身上的装备名称：" + mm.equip.name)
print("怪物身上的装备攻击力：",mm.equip.atk)
hh = HumanHero("vilaseaka")
hh.equip = ee
print("人族角色名称：" + hh.name)
print("人族身上的装备：" + hh.equip.name)
'''output1
怪物名称：12级的精英玄冰毒蚁
装备名称：12级的精英玄冰毒蚁的小拇指
怪物身上的装备名称：12级的精英玄冰毒蚁的小拇指
怪物身上的装备攻击力： 104.80340124698391
人族角色名称：vilaseaka
人族身上的装备：12级的精英玄冰毒蚁的小拇指
'''
'''output2
怪物名称：32级的精英无双赤鬼
装备名称：32级的精英无双赤鬼的乾坤袋
怪物身上的装备名称：32级的精英无双赤鬼的乾坤袋
怪物身上的装备攻击力： 136.4451802748062
人族角色名称：vilaseaka
人族身上的装备：32级的精英无双赤鬼的乾坤袋
'''
```
嗯，还不错。继续。

#### 3.2.4 主框架

OK，此处过去约三个小时……基本完成了，简单测试了几轮，似乎还OK。

这里就不单独贴模块了，令起一个小节将代码整理到这篇文档里，一共就四个小文件：

```shell
(venv) E:\Code\PythonRepo\AboutPython3>tree /f
卷 软件 的文件夹 PATH 列表
卷序列号为 000B-DFAB
E:.
├─.idea
│  │  AboutPython3.iml
│  │  misc.xml
│  │  modules.xml
│  │  workspace.xml
│  │
│  └─libraries
│          R_User_Library.xml
│
├─rpg-game
│  │  equip.py
│  │  hero.py
│  │  main.py
│  │  monster.py
│  │  __init__.py
│  │
│  ├─aboutPython3BasicSyntax
│  │      BasicDataType.py
│  │      BasicSyntax.py
│  │      Herobak.py
│  │      __init__.py
│  │
│  └─__pycache__
│          equip.cpython-37.pyc
│          hero.cpython-37.pyc
│          monster.cpython-37.pyc
│
└─venv
```


## 4 代码整理

### 4.1 hero.py
```python
from equip import *


class Hero:
    name = ''   # 角色名
    hp = 0      # 生命值
    mp = 0      # 法力值
    atk = 0     # 攻击力

    def __init__(self):
        self.name = '未命名的普通英雄'
        self.hp = 100
        self.mp = 100
        self.atk = 50

    def battleCry(self): # 战吼技能 遇到敌人后自动释放
        print("battleCry")

    def activeSkill(self): # 主动技能 手动释放
        print("activeSkill")

    # def passiveSkill(self): # 被动技能 默认增益
    #     print("passiveSkill")


# 人族攻高
class HumanHero(Hero):

    level = 1   # 初始等级
    exp = 0     # 经验值
    equip = ''  # 初始装备为空
    kind = "人族"

    temp_hp = 100  # 初始血槽
    temp_mp = 100  # 初始蓝槽
    need_exp = 10  # 升级所需要的经验

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 100
        self.atk = 60
        self.equip = DefaultEquip()

    def update(self,exp):  # 根据传入的经验值进行升级
        self.exp += exp
        while self.exp > self.need_exp:
            self.level +=1
            self.hp += 20
            self.temp_hp = self.hp
            self.atk += 5
            self.exp -= self.need_exp
            self.need_exp += 10
            print("\033[0;30;46m您升级了！\033[0m  当前等级：" + str(self.level) + "   当前生命值：" + str(self.hp) + "   当前攻击力：" + str(self.atk) + "   下一级所需经验：" + str(int(self.need_exp)))
        return self

    def recover(self):
        self.temp_hp = self.hp
        self.temp_mp = self.mp
        return self

    def battleCry(self): # 人族战吼：对敌人造成60%攻击力的伤害
        return self.atk*0.6

    def activeSkill(self): # 人族主动技能：对敌人造成160%攻击力的伤害
        if self.temp_mp>40:
            self.temp_mp = self.temp_mp - 40
            return self.atk*1.5
        else:
            return 0


# 兽人血厚
class BeastHero(Hero):

    level = 1   # 初始等级
    exp = 0     # 经验值
    equip = ''  # 初始装备为空
    kind = "兽族"

    temp_hp = 150  # 初始血槽
    temp_mp = 100  # 初始蓝槽
    need_exp = 10  # 升级所需要的经验

    def __init__(self,name):
        self.name = name
        self.hp = 150
        self.mp = 100
        self.atk = 50
        self.equip = DefaultEquip()

    def battleCry(self): # 兽人战吼：对敌人造成50%攻击力的伤害
        return self.atk*0.5

    def activeSkill(self): # 兽人主动技能：对敌人造成150%攻击力的伤害
        if self.temp_mp>40:
            self.temp_mp = self.temp_mp - 40
            return self.atk*1.5
        else:
            return 0

    def update(self,exp):  # 根据传入的经验值进行升级
        self.exp += exp
        while self.exp > self.need_exp:
            self.level +=1
            self.hp += 20
            self.temp_hp = self.hp
            self.atk += 5
            self.exp -= self.need_exp
            self.need_exp += 10
            print("\033[0;30;46m您升级了！\033[0m  当前等级：" + str(self.level) + "   当前生命值：" + str(self.hp) + "   当前攻击力：" + str(self.atk) + "   下一级所需经验：" + str(int(self.need_exp)))
        return self

    def recover(self):
        self.temp_hp = self.hp
        self.temp_mp = self.mp
        return self
```

### 4.2 monster.py
```python

import random
from equip import *

from hero import HumanHero

nameList1 = ['魔化大蜘蛛','魔化大老鼠','魔化大鸵鸟','腐败香菇蘑','冲角团教员','冲角团临时工','楼上的拖鞋','游荡的鬼魂','饥饿的小鬼']  # 场景1怪物名字
nameList2 = ['大地之熊','玄冰毒蚁','迅影斑斓豹','紫尾貂','堕落魔蛹','不死雪狐','八翼雷鹰王']  # 场景2怪物名字
nameList3 = ['魂灭先知','狂飙毁灭者','鬼剑圣人','火爆龙将','逆焰斗神','星辰玉龙','无双赤鬼']  # 场景3怪物名字


class Monster:
    name = ''   # 怪物名
    level = 0   # 等级
    exp = 0     # 经验
    hp = 0      # 生命值
    atk = 0     # 攻击力
    equip = ''

    def __init__(self, level):
        if level <= 10:
            self.name = str(level) + "级的" + random.choice(nameList1)
        elif level <= 30:
            self.name = str(level) + "级的" + random.choice(nameList2)
        else:
            self.name = str(level) + "级的" + random.choice(nameList3)
        self.level = level
        self.exp = (5 + 5*(level-1))    # 每 +1 级 +5 经验
        self.hp = (100 + 40*(level-1))*(random.random()+0.5)  # 每 +1 级 +40 血  //再乘上(0.5-1.5)倍随机量
        self.atk = (30 + 5*(level-1))*(random.random()+0.5)   # 每 +1 级 +5 攻击 //再乘上(0.5-1.5)倍随机量


class MonsterPro(Monster):  # 精英怪
    equip = ''

    def __init__(self, level):
        if level <= 10:
            self.name = str(level) +"级的精英"+ random.choice(nameList1)
        elif level <= 30:
            self.name = str(level) +"级的精英"+ random.choice(nameList2)
        else:
            self.name = str(level) +"级的精英"+ random.choice(nameList3)
        self.level = level
        self.equip = DefaultEquip()
        self.exp = (5 + 5*(level-1))*2    # 精英怪经验翻倍
        self.hp = ((100 + 40*(level-1))*2)*(random.random()+0.5)  # 精英怪血量翻倍 //再乘上(0.5-1.5)倍随机量
        self.atk = ((30 + 5*(level-1))*2)*(random.random()+0.5)  # 精英怪攻击翻倍 //再乘上(0.5-1.5)倍随机量


class QinYijue():
    name = "秦义绝"
    level = 100  # 等级
    exp = 0  # 经验
    hp = 9999  # 生命值
    atk = 500  # 攻击力
    equip = ''
```

### 4.3 equip.py
```python
import random

nameList1 = ['脚趾甲','牙齿','胳膊','鼻涕','头盖骨','汗毛','大眼睛','小拇指']
nameList2 = ['匕首','长剑','短斧','铃铛','乾坤袋','金枪']
nameList = [nameList1,nameList2]

class Equip:
    name = ''
    level = 0
    atk = 0

    def __init__(self, monster):
        self.name = monster.name + "的" + random.choice(random.choice(nameList))
        self.level = monster.level
        self.atk = monster.atk*0.5


class DefaultEquip():
    name = "default"
    atk = 0

    def __init__(self):
        self.atk = 0
```

### 4.4 main.py
```python
from hero import *
from monster import *
import random
import time

# 初始化新游戏
def init_new_game():
    print("\033[1;30;41m==================开始新游戏==================\033[0m")
    print("1.人族英雄（攻高）            2.兽族英雄（血厚）")
    heroTypt = input("请选择英雄类型：")
    while (heroTypt!=str(1) and heroTypt!=str(2)):
        heroTypt = input("\033[0;31;m输入有误，请重新选择（只能是1或2）：\033[0m")
    else:
        heroName = input("请输入英雄名称：")
    if heroTypt==str(1):
        humanHero = HumanHero(heroName)
        print("您新建了人族英雄：" + humanHero.name)
        show_hero_info(humanHero)
        return humanHero
    else:
        beastHero = BeastHero(heroName)
        print("您新建了兽族英雄：" + beastHero.name)
        show_hero_info(beastHero)
        return beastHero

# 读取展示英雄信息
def show_hero_info(hero):
    print("\033[0;30;m--------------当前英雄信息--------------\033[0m")
    print("英雄名称：" + hero.name + "   种族：" + hero.kind + "\n"
          "生命值：" + str(hero.hp) + "   法力值：" + str(hero.mp) + "\n"
          "攻击力：" + str(hero.atk) + "")
    if hero.equip.name != 'default':
        print("装备：" + hero.equip.name + "   攻击：" + str(int(hero.equip.atk)))
    else:
        print("目前无装备")

# 主菜单响应
def handle_menu(hero):
    print("\033[0;30;42m-----------------绿明村中-----------------\033[0m")
    print("1.外出历练        2.角色状态")
    code = input("请选择操作：")
    if code==str(1):
        handle_map(hero)
    else:
        show_hero_info(hero)
        handle_menu(hero)

# 战斗处理
def handle_battle(hero, monster):
    print("您遇到了：" + monster.name + "  怪物生命值：" + str(int(monster.hp)) + "  怪物攻击力：" + str(int(monster.atk)))
    print("1.勇敢战斗      2.逃跑")
    code = input("请选择操作：")
    if code==str(2):
        x = abs(hero.level - monster.level)
        y = random.choice(range(1,10))
        if y<x:  # 差10级以上100%逃跑成功
            print("逃跑成功")
            return hero
        else:
            print("逃跑失败，即将进入战斗…")

    while monster.hp > 0:
        print("1.普通攻击  2.主动技能")
        code = input("请选择操作：")
        if code == str(1):
            tempatk = hero.atk+hero.equip.atk
            monster.hp -= tempatk
            print("您进行了普通攻击，对怪物造成" + str(int(tempatk)) + "点伤害,  怪物剩余生命值：" + str(int(monster.hp)))
            if monster.hp < 0:
                continue
        else:
            tempatk = hero.activeSkill()
            if tempatk != 0:
                monster.hp -= tempatk
                print("您发动了主动技能，对怪物造成" + str(tempatk) + "点伤害,  怪物剩余生命值：" + str(int(monster.hp)))
            else:
                print("\033[7;31;40m您没蓝了\033[0m，请使用普通攻击")
                continue
        hero.temp_hp -= monster.atk
        print("怪物发动攻击对您造成" + str(int(monster.atk)) + "点伤害,  您剩余生命值：" + str(int(hero.temp_hp)))
        if hero.temp_hp < 0:
            print("\033[7;31;40m您被拍死了，游戏结束\033[0m")
            exit(0)

    # 怪物死掉了才能到达这一步：
    hero.recover()    # 恢复
    if monster.name != "秦义绝":
        print("\033[0;36;47m战斗胜利！\033[0m获得经验：" + str(monster.exp) + "！ 您的生命值与魔法值已经恢复")
        hero.update(monster.exp)  # 判断升级
        # 装备掉落判断：
        if monster.equip != '' and monster.equip.name != 'default':
            if random.random() > 0.5:  # 0.5的几率掉落装备
                print("\033[1;30;45m怪物掉落了一件装备:\033[0m" + monster.equip.name + "  攻击力为：" + str(int(monster.equip.atk)) + "   您当前武器为：" + hero.equip.name + "   攻击力为：" + str(int(hero.equip.atk)))
                code = input("是否更换装备（y/n）：")
                if code == 'y':
                    hero.equip = monster.equip
                    print("更换装备成功，当前装备：" + hero.equip.name)
                else:
                    print("您已经放弃了这个装备。正在返回绿明村。")
                    return hero
            else:
                return hero
    else:
        print("\033[1;30;45m您战胜了秦义绝！天下终于太平了。\033[0m")
        print("\033[1;30;42m全剧终,即将自动退出游戏\033[0m")
        slow_print()
        exit(0)

# 地图探索
def handle_map(hero):
    while True:
        print("\033[0;30;42m-----------------绿明村头-----------------\033[0m")
        print("1.村头小树林   2.风之平原   3.红莲墓地   4.白青山脉   5.国师府邸   0.回到村中")
        code = input("请选择目的地：")
        if code == str(1):
            print("\033[0;30;42m----------------村头小树林----------------\033[0m")
            print("探索中…"+" ")
            slow_print()
            mm = monster_generator(random.choice(range(1, 3)))  # 随机生成一个[1，3]级别的怪物
            handle_battle(hero, mm)  # 处理战斗过程,如果没死，会返回新的hero，死了就结束了
        elif code == str(2):
            print("\033[0;30;42m-----------------风之平原-----------------\033[0m")
            print("探索中…"+" ")
            slow_print()
            mm = monster_generator(random.choice(range(1, 10)))  # 随机生成一个[1，10]级别的怪物
            handle_battle(hero, mm)  # 处理战斗过程,如果没死，会返回新的hero，死了就结束了
        elif code == str(3):
            print("\033[0;30;42m-----------------红莲墓地-----------------\033[0m")
            print("探索中…" + " ")
            slow_print()
            mm = monster_generator(random.choice(range(11, 30)))
            handle_battle(hero, mm)
        elif code == str(4):
            print("\033[0;30;42m-----------------白青山脉-----------------\033[0m")
            print("探索中…" + " ")
            slow_print()
            mm = monster_generator(random.choice(range(31, 50)))
            handle_battle(hero, mm)
        elif code == str(5):
            print("\033[0;30;42m-----------------国师府邸-----------------\033[0m")
            print("")
            code = input("您确定要现在挑战秦义绝吗?(y/n)")
            if code == 'y':
                qinyijue = QinYijue()
                handle_battle(hero,qinyijue)
        elif code == str(0):
            handle_menu(hero)
        else:
            print("输入有误")

# 怪物生成器
def monster_generator(level):
    # print("正在生成怪物")
    if random.random()>0.8:  # 0.2的几率生成精英怪
        m = MonsterPro(level)
        if random.random() > 0.4:  # 0.6的几率生成装备
            m.equip = Equip(m)   # 这样互相依赖貌似……
        return m
    else:
        m = Monster(level)
        return m

# 延迟打印以防止刷屏
def slow_print():
    for x in range(3, -1, -1):
        mystr = "探索中" + str(x) + "秒"
        print(mystr, end="")
        print("\b" * (len(mystr) * 2), end="", flush=True)
        time.sleep(0.2)

if __name__ == '__main__':
    hero = init_new_game()  # 开始新游戏：创建新角色
    handle_menu(hero)       # 提供主菜单，在主菜单进行接下来的操作
```

## 5 试玩

游戏角色初始值较低，此处调整到死不了的状态进行游戏，简单看一下流程：

*实际的控制台因为有颜色，不至于像下面这么乱*
```shell
E:\Code\PythonRepo\AboutPython3\venv\Scripts\python.exe E:/Code/PythonRepo/AboutPython3/rpg-game/main.py
==================开始新游戏==================
1.人族英雄（攻高）            2.兽族英雄（血厚）
请选择英雄类型：1
请输入英雄名称：Vilaseaka
您新建了人族英雄：Vilaseaka
--------------当前英雄信息--------------
英雄名称：Vilaseaka   种族：人族
生命值：10000   法力值：100
攻击力：6000
目前无装备
-----------------绿明村中-----------------
1.外出历练        2.角色状态
请选择操作：2
--------------当前英雄信息--------------
英雄名称：Vilaseaka   种族：人族
生命值：10000   法力值：100
攻击力：6000
目前无装备
-----------------绿明村中-----------------
1.外出历练        2.角色状态
请选择操作：1
-----------------绿明村头-----------------
1.村头小树林   2.风之平原   3.红莲墓地   4.白青山脉   5.国师府邸   0.回到村中
请选择目的地：1
----------------村头小树林----------------
探索中… 
您遇到了：2级的游荡的鬼魂  怪物生命值：202  怪物攻击力：18
1.勇敢战斗      2.逃跑
请选择操作：1
1.普通攻击  2.主动技能
请选择操作：2
您发动了主动技能，对怪物造成9000.0点伤害,  怪物剩余生命值：-8797
怪物发动攻击对您造成18点伤害,  您剩余生命值：9981
战斗胜利！获得经验：10！ 您的生命值与魔法值已经恢复
-----------------绿明村头-----------------
1.村头小树林   2.风之平原   3.红莲墓地   4.白青山脉   5.国师府邸   0.回到村中
请选择目的地：2
-----------------风之平原-----------------
探索中… 
您遇到了：6级的精英饥饿的小鬼  怪物生命值：427  怪物攻击力：73
1.勇敢战斗      2.逃跑
请选择操作：1
1.普通攻击  2.主动技能
请选择操作：2
您发动了主动技能，对怪物造成9000.0点伤害,  怪物剩余生命值：-8572
怪物发动攻击对您造成73点伤害,  您剩余生命值：9926
战斗胜利！获得经验：60！ 您的生命值与魔法值已经恢复
您升级了！  当前等级：2   当前生命值：10020   当前攻击力：6005   下一级所需经验：20
您升级了！  当前等级：3   当前生命值：10040   当前攻击力：6010   下一级所需经验：30
您升级了！  当前等级：4   当前生命值：10060   当前攻击力：6015   下一级所需经验：40
怪物掉落了一件装备:6级的精英饥饿的小鬼的长剑  攻击力为：36   您当前武器为：default   攻击力为：0
是否更换装备（y/n）：y
更换装备成功，当前装备：6级的精英饥饿的小鬼的长剑
-----------------绿明村头-----------------
1.村头小树林   2.风之平原   3.红莲墓地   4.白青山脉   5.国师府邸   0.回到村中
请选择目的地：3
-----------------红莲墓地-----------------
探索中… 
您遇到了：27级的八翼雷鹰王  怪物生命值：1577  怪物攻击力：219
1.勇敢战斗      2.逃跑
请选择操作：2
逃跑成功
-----------------绿明村头-----------------
1.村头小树林   2.风之平原   3.红莲墓地   4.白青山脉   5.国师府邸   0.回到村中
请选择目的地：4
-----------------白青山脉-----------------
探索中… 
您遇到了：49级的精英火爆龙将  怪物生命值：3862  怪物攻击力：472
1.勇敢战斗      2.逃跑
请选择操作：1
1.普通攻击  2.主动技能
请选择操作：2
您发动了主动技能，对怪物造成9022.5点伤害,  怪物剩余生命值：-5159
怪物发动攻击对您造成472点伤害,  您剩余生命值：9587
战斗胜利！获得经验：490！ 您的生命值与魔法值已经恢复
您升级了！  当前等级：5   当前生命值：10080   当前攻击力：6020   下一级所需经验：50
您升级了！  当前等级：6   当前生命值：10100   当前攻击力：6025   下一级所需经验：60
您升级了！  当前等级：7   当前生命值：10120   当前攻击力：6030   下一级所需经验：70
您升级了！  当前等级：8   当前生命值：10140   当前攻击力：6035   下一级所需经验：80
您升级了！  当前等级：9   当前生命值：10160   当前攻击力：6040   下一级所需经验：90
您升级了！  当前等级：10   当前生命值：10180   当前攻击力：6045   下一级所需经验：100
您升级了！  当前等级：11   当前生命值：10200   当前攻击力：6050   下一级所需经验：110
怪物掉落了一件装备:49级的精英火爆龙将的乾坤袋  攻击力为：236   您当前武器为：6级的精英饥饿的小鬼的长剑   攻击力为：36
是否更换装备（y/n）：y
更换装备成功，当前装备：49级的精英火爆龙将的乾坤袋
-----------------绿明村头-----------------
1.村头小树林   2.风之平原   3.红莲墓地   4.白青山脉   5.国师府邸   0.回到村中
请选择目的地：0
-----------------绿明村中-----------------
1.外出历练        2.角色状态
请选择操作：2
--------------当前英雄信息--------------
英雄名称：Vilaseaka   种族：人族
生命值：10200   法力值：100
攻击力：6050
装备：49级的精英火爆龙将的乾坤袋攻击：236
-----------------绿明村中-----------------
1.外出历练        2.角色状态
请选择操作：1
-----------------绿明村头-----------------
1.村头小树林   2.风之平原   3.红莲墓地   4.白青山脉   5.国师府邸   0.回到村中
请选择目的地：5
-----------------国师府邸-----------------

您确定要现在挑战秦义绝吗?(y/n)y
您遇到了：秦义绝  怪物生命值：9999  怪物攻击力：500
1.勇敢战斗      2.逃跑
请选择操作：1
1.普通攻击  2.主动技能
请选择操作：1
您进行了普通攻击，对怪物造成6286点伤害,  怪物剩余生命值：3712
怪物发动攻击对您造成500点伤害,  您剩余生命值：9700
1.普通攻击  2.主动技能
请选择操作：2
您发动了主动技能，对怪物造成9075.0点伤害,  怪物剩余生命值：-5362
怪物发动攻击对您造成500点伤害,  您剩余生命值：9200
您战胜了秦义绝！天下终于太平了。
全剧终,即将自动退出游戏

Process finished with exit code 0
```

*时间戳：2020年4月5日00点23分*


## 6 结语

中午来了客人，拖到现在半夜了才写完，算是用一整天完成了对python基本语法的熟悉，这种操作以后可以再优化优化，有值得被发扬光大的潜力。

网络方面的学习资源实在零散，质量也参差不齐，开头提到的那三本python书还是不错的，推荐。


P.S. 本文中的代码统一归档在GitHub上的[练习代码归档仓库][baserepo]中，地址[AboutProgramming/AboutPython3/rpg-game][rpg-game]  

**P.P.S. 清明，公祭，鸣笛、警报、降半旗。致哀。希望疫情的阴霾早日散去。**

[baserepo]:https://github.com/Vilaseaka/AboutProgramming "Vilaseaka/AboutProgramming"
[rpg-game]:https://github.com/Vilaseaka/AboutProgramming/tree/master/AboutPython3/rpg-game "Vilaseaka/AboutProgramming/AboutPython3/rpg-game/"
