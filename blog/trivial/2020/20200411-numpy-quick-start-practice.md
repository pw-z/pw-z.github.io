# NumPy入门实践
*2020041101-numpy-quick-start-practice*  
*Posted on 2020.04.11 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


* [NumPy入门实践](#numpy%E5%85%A5%E9%97%A8%E5%AE%9E%E8%B7%B5)
    * [认知](#%E8%AE%A4%E7%9F%A5)
    * [实践](#%E5%AE%9E%E8%B7%B5)
        * [ndarray](#ndarray)
            * [构建](#%E6%9E%84%E5%BB%BA)
                * [常规数组](#%E5%B8%B8%E8%A7%84%E6%95%B0%E7%BB%84)
                * [特殊数组（全零、全一）](#%E7%89%B9%E6%AE%8A%E6%95%B0%E7%BB%84%E5%85%A8%E9%9B%B6%E5%85%A8%E4%B8%80)
                * [数字序列（等比、等差）](#%E6%95%B0%E5%AD%97%E5%BA%8F%E5%88%97%E7%AD%89%E6%AF%94%E7%AD%89%E5%B7%AE)
                * [随机数组](#%E9%9A%8F%E6%9C%BA%E6%95%B0%E7%BB%84)
            * [属性](#%E5%B1%9E%E6%80%A7)
                * [ndarray\.ndim 数组的【维数】](#ndarrayndim-%E6%95%B0%E7%BB%84%E7%9A%84%E7%BB%B4%E6%95%B0)
                * [ndarray\.shape 数组的【维度】](#ndarrayshape-%E6%95%B0%E7%BB%84%E7%9A%84%E7%BB%B4%E5%BA%A6)
                * [ndarray\.size 元素总数](#ndarraysize-%E5%85%83%E7%B4%A0%E6%80%BB%E6%95%B0)
                * [ndarray\.dtype 元素类型](#ndarraydtype-%E5%85%83%E7%B4%A0%E7%B1%BB%E5%9E%8B)
            * [操作](#%E6%93%8D%E4%BD%9C)
                * [打乱](#%E6%89%93%E4%B9%B1)
                * [变形](#%E5%8F%98%E5%BD%A2)
                * [转置](#%E8%BD%AC%E7%BD%AE)
                * [索引、切片](#%E7%B4%A2%E5%BC%95%E5%88%87%E7%89%87)
            * [运算](#%E8%BF%90%E7%AE%97)
                * [广播机制](#%E5%B9%BF%E6%92%AD%E6%9C%BA%E5%88%B6)
                * [基本运算（加减乘除取余开方）](#%E5%9F%BA%E6%9C%AC%E8%BF%90%E7%AE%97%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%8F%96%E4%BD%99%E5%BC%80%E6%96%B9)
                * [矩阵运算（线性代数）](#%E7%9F%A9%E9%98%B5%E8%BF%90%E7%AE%97%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0)
                * [统计运算](#%E7%BB%9F%E8%AE%A1%E8%BF%90%E7%AE%97)
                * [小结](#%E5%B0%8F%E7%BB%93)
            * [储存](#%E5%82%A8%E5%AD%98)
                * [原生格式（\.npy \.npz）](#%E5%8E%9F%E7%94%9F%E6%A0%BC%E5%BC%8Fnpy-npz)
                * [文本格式](#%E6%96%87%E6%9C%AC%E6%A0%BC%E5%BC%8F)
    * [小结](#%E5%B0%8F%E7%BB%93-1)



***继续强化这样的观念：在有条件的情况下，阅读官方文档加上动手实践是快速入门新技术最好的方式。***潜在的不利条件则包括语言障碍、官方文档不够优质、学习难度处在恐慌区（对应的为学习区）等等。本文是在条件良好的情况下进行的实践，（阅读与）实践对应到大脑中的本质活动是通过例子塑造并强化新的神经回路，从而形成新的组块（chunk），这个过程让我们学习到新的知识。


## 认知

NumPy是使用Python进行科学计算的一个基础包，官网地址[https://numpy.org](https://numpy.org/)，是由美国一家非盈利慈善机构[NumFOCUS](https://numfocus.org/)赞助的项目。

NumPy提供了一些非常好用的工具、特性等，包括但不限于如下内容：

* 强大的N维数组对象（ndarray）
* 复杂巧妙的（广播（broadcasting））功能
* 集成C/C ++和Fortran代码的工具
* 有用的线性代数、傅立叶变换和随机数相关功能


## 实践

NumPy的使用需要一点点Python基础、线性代数基础。  
接下来的所有引用没有特殊标注均来自官网的[Quickstart tutorial](https://numpy.org/devdocs/user/quickstart.html)。

### ndarray

>NumPy’s array class is called ndarray. 

ndarray是NumPy提供的一个强大的**容器**，它能容纳一切序列型的对象，包括嵌套的序列（多维数组），是NumPy的核心数据结构，NumPy中大部分操作都是以ndarray为基础的。

在官方文档的[基础篇](https://numpy.org/devdocs/user/absolute_beginners.html)中详细描述了ndarray的重要性，简单理解，它是python内建list的究极体。


#### 构建

##### 常规数组

最普通的构建ndarray的方法是通过调用numpy.array()，其可以接受很多参数：

```python
# 菜鸟教程 https://www.runoob.com/numpy/numpy-ndarray-object.html
np.array(object, dtype = complex, copy = True, order = None, subok = False, ndmin = 0)

'''
object  数组或嵌套的数列
dtype   数组元素的数据类型，可选
copy    对象是否需要复制，可选
order   创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok   默认返回一个与基类类型一致的数组
ndmin   指定生成数组的最小维度
'''
```

举例子：

```python
import numpy as np

x = "a"
y = "b"
a = np.array([x,y])
b = np.array([[x,y,y],
              [x,y,x],
              [y,y,x],])
print(a)
print(b)
'''
['a' 'b']
[['a' 'b' 'b']
 ['a' 'b' 'a']
 ['b' 'b' 'a']]
'''
```

##### 特殊数组（全零、全一）

除了调用array方法，还可以用一系列内置方法直接生成一些特殊数组，对应的方法名字简单易懂:

```python
import numpy as np

a = np.zeros((3,4))
b = np.ones((2,3,4))
c = np.empty((3,4))
print("a:\n",a)
print("b:\n",b)
print("c:\n",c)
'''
a:
 [[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
b:
 [[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]
c:
 [[6.23042070e-307 2.00272265e-307 6.23046145e-307 3.44900029e-307]
 [1.37961234e-306 1.60216183e-306 7.56602523e-307 1.33511562e-306]
 [8.01070728e-307 3.33780771e-307 2.22522597e-306 0.00000000e+000]]
'''
```
>The function zeros creates an array full of zeros, the function ones creates an array full of ones, and the function empty creates an array whose initial content is random and depends on the state of the memory. By default, the dtype of the created array is float64.

empty函数不是构建字面意义上的“空”数组，而是说不对构建的实例进行初始化，其值取决于内存状态。


##### 数字序列（等比、等差）

数字序列是字面意义上的“序列（sequences）”。  
>To create sequences of numbers, NumPy provides the arange function which is analogous to the Python built-in range, but returns an array.

```python
import numpy as np
# arange方法创建给定范围内的递增序列
# np.arange(start=0, stop, step=1, dtype=输入的类型)
a = np.arange(1,10,2)
b = np.arange(9)
print(a)
print(b)
'''
[1 3 5 7 9]
[0 1 2 3 4 5 6 7 8]
'''

# linspace方法用于创建给定范围内的等差数列
# np.linspace(start, stop, num=要生成的等步长的样本数量，默认为50, endpoint=True, retstep=False, dtype=None)
a = np.linspace(1,10,10)
b = np.linspace(1,10,4)
print(a)
print(b)
'''
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
[ 1.  4.  7. 10.]
'''
```


##### 随机数组

随机生成是一项常规需求，numpy.random中提供了方法，并且覆盖了绝大多数概率分布，比python内置的random方法高效很多。

```python
import numpy as np

a = np.random.rand()     # 生成一个随机数（数值范围为0到1之间，与python的一直）
print("a:\n",a)
a = np.random.rand(2,2)  # 生成一个指定形状的随机数组（相比于python内置的，这太方便了）
print("a':\n",a)
'''
a:
 0.4985070123025904
a':
 [[0.22479665 0.19806286]
 [0.76053071 0.16911084]]
'''
```


要明确，numpy通过算法生成伪随机数，可以通过指定种子让生成结果保持一致（某一特定种子对应特定数字序列）。

```python
import numpy as np

a = np.random.rand(2,2)
b = np.random.rand(2,2)
print("a:\n",a)
print("b:\n",b)
np.random.seed(10)
a = np.random.rand(2,2)
np.random.seed(10)
b = np.random.rand(2,2)
print("a':\n",a)
print("b':\n",b)
'''
a:
 [[0.27029008 0.07359186]
 [0.71322077 0.95964336]]
b:
 [[0.53951187 0.51123483]
 [0.47131233 0.88495348]]
a':
 [[0.77132064 0.02075195]
 [0.63364823 0.74880388]]
b':
 [[0.77132064 0.02075195]
 [0.63364823 0.74880388]]
'''
```

`numpy.random.rand()`方法生成的随机数是符合**均匀分布**的，类似的还有：

* numpy.random.random()
* numpy.random.ranf()
* numpy.random.randint() 
    - numpy.random.random_integers()是旧版本的方法，不建议使用

```python
import numpy as np

a = np.random.random((2,2))
b = np.random.ranf((2,3))
c = np.random.randint(1,21,5)
d = np.random.random_integers(1,20,5)  # DeprecationWarning: This function is deprecated. Please call randint(1, 20 + 1) instead
print("a:\n",a)
print("b:\n",b)
print("c:\n",c)
print("d:\n",d)
'''
a:
 [[0.08833981 0.68535982]
 [0.95339335 0.00394827]]
b:
 [[0.51219226 0.81262096 0.61252607]
 [0.72175532 0.29187607 0.91777412]]
c:
 [14  6 14 20 14]
d:
 [13  2  5 19 14]
'''
```

前面说了numpy.random覆盖了大部分概率分布，比如：

* numpy.random.randn(d0, d1, ..., dn) 正态分布
* numpy.random.beta(a, b[, size]) 贝塔分布，数值范围`[0, 1]`
* numpy.random.binomial(n, p[, size]) 二项分布
* numpy.random.dirichlet(alpha[, size]) 狄利克雷分布
* numpy.random.exponential([scale, size]) 指数分布
* numpy.random.geometric(p[, size]) 几何分布
* numpy.random.multinomial(n, pvals[, size]) 多项分布

还有很多不再赘述，有需要的时候查阅API即可


#### 属性

##### ndarray.ndim 数组的【维数】

>the number of axes (dimensions) of the array.  

这里的“维数”容易与“维度”引起混淆，可以简记为**轴的数量**，比如`[[1,2][2,3][3,4]]`是一个二维数组（只有x、y两个轴），所以ndim=2。
```python
import numpy as np
# just a line
a = np.array([1,2])
b = np.array([[1,2],[1,2],[1,2]])
c = np.array([[[1,2],[1,2],[1,2]],
              [[1,2],[1,2],[1,2]],
              [[1,2],[1,2],[1,2]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
'''
1
2
3
'''
```

##### ndarray.shape 数组的【维度】  

>For a matrix with n rows and m columns, shape will be (n,m).

对于一个n行m列的矩阵，其维度即(n,m)。

```python
import numpy as np
# just a line
a = np.array([1,2])
b = np.array([[1,2],[1,2],[1,2,3]])
c = np.array([[[1,2],[1,2],[1,2]],
              [[1,2],[1,2],[1,2]],
              [[1,2],[1,2],[1,2]]])
print(a.shape)
print(b.shape)
print(c.shape)
'''
(2,)
(3,)
(3, 3, 2)
'''
```

##### ndarray.size 元素总数

>the total number of elements of the array. This is equal to the product of the elements of shape.

元素总数=维度相乘

```python
import numpy as np

a = np.array([1,2])
b = np.array([[1,2],[1,2],[1,2]])
c = np.array([[[1,2],[1,2],[1,2]],
              [[1,2],[1,2],[1,2]],
              [[1,2],[1,2],[1,2]]])
print(a.shape,"  ",a.size)
print(b.shape,"  ",b.size)
print(c.shape,"  ",c.size)
'''
(2,)    2
(3, 2)    6
(3, 3, 2)    18
'''
```

##### ndarray.dtype 元素类型

>an object describing the type of the elements in the array. 

```python
import numpy as np
a = np.array([1,2])
print(a.dtype)  # int32
```

还有若干属性，暂且略过。


#### 操作

再次明确，NumPy中大量操作都是以ndarray为基础的，在官网的快速入门教程里，对ndarray的各种操作被划分为几个子话题分别描述，比如`Shape Manipulation`、`Copies and Views`等，这里简单实践几个。


##### 打乱

针对同一数组，经常需要打乱顺序，numpy.random中有两个相关方法：

* numpy.random.shuffle(arr)
* numpy.random.permutation(arr)

这两个方法都有打乱顺序的功能，前者是原地操作无返回值，后者令开辟内存空间生成新的数组。

```python
import numpy as np

np.random.seed(200)
a = np.random.randint(0,100,10) # [0,100)内随机的10个数字
print(a)
# 打乱顺序
np.random.shuffle(a)
print(a)
# 返回一个被打乱顺序的数组
b = np.random.permutation(a)
print(b)
# np.random.permutation(a)操作之后a本身没有被改变
print(a)
'''
[26 16 68 42 55 76 79 89 14 91]
[14 89 76 55 42 16 26 68 79 91]
[91 42 76 55 26 79 14 16 68 89]
[14 89 76 55 42 16 26 68 79 91]
'''
```

##### 变形

shape属性描述了数组的“形状”，reshape方法则提供了数组的变形能力：

```python
import numpy as np

a = np.random.randint(0,100,10)
print('a:\n',a)
b = a.reshape((2,5))
print('b:\n',b)
'''
a:
 [35 31 32 45 59 45 61 20 85  0]
b:
 [[35 31 32 45 59]
 [45 61 20 85  0]]
'''
```

##### 转置

numpy.transpose可以很方便的转置数组，此处的转置仅为字面意思，不是特指矩阵的转置，可以理解为“翻转”、“转位”等。对二维数组操作时若不指定参数，则相当于矩阵的转置。

```python
import numpy as np

a = np.random.randint(0,100,10)
print('a:\n',a)
b = a.reshape((2,5))
print('b:\n',b)
c = np.transpose(b)
print('c:\n',c)
'''
a:
 [ 3 55 95 56  3 33 72  0 52 90]
b:
 [[ 3 55 95 56  3]
 [33 72  0 52 90]]
c:
 [[ 3 33]
 [55 72]
 [95  0]
 [56 52]
 [ 3 90]]
'''
```

ndarray中提供了`.T`属性输出矩阵转置:

```python
import numpy as np

a = np.array([[1,2,3],
              [1,2,3],
              [1,2,3]])
print('a:\n',a)
print('a.T:\n',a.T)
'''
a:
 [[1 2 3]
 [1 2 3]
 [1 2 3]]
a.T:
 [[1 1 1]
 [2 2 2]
 [3 3 3]]
'''
```

可以参考：[numpy之转置（transpose）和轴对换](https://www.cnblogs.com/sunshinewang/p/6893503.html)


##### 索引、切片

ndarray的索引、切片方式与python的list基本一致，***一个重要区别在于，在ndarray上索引出来的数组与原数组共享内存***，改变切片内容，相当于改变原数组。

索引举例：

```python
import numpy as np

a = np.arange(10)
print(a)
print(a[2])
print(a[5:])
print(a[3:-1])
a[5:] = -1
print(a)
'''
[0 1 2 3 4 5 6 7 8 9]
2
[5 6 7 8 9]
[3 4 5 6 7 8]
[ 0  1  2  3  4 -1 -1 -1 -1 -1]
'''
```

**多维数组的索引、切片:**

为了方便描述，下面例子中生成的三维数组中的维度分别成为`块、组、个`:

```python
import numpy as np

a = np.arange(12)
b = a.reshape((2,3,2))
print('a:\n',a)
print('b:\n',b)
print('b中第1块:\n',b[0])
print('b中第2块第2组:\n',b[1,1])
print('b中第2块第3组第1个数:\n',b[1,2,0])
'''
a:
 [ 0  1  2  3  4  5  6  7  8  9 10 11]
b:
 [[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]]
b中第1块:
 [[0 1]
 [2 3]
 [4 5]]
b中第2块第2组:
 [8 9]
b中第2块第3组第1个数:
 10
'''
```


#### 运算

##### 广播机制

>The term broadcasting describes how numpy treats arrays with different shapes during arithmetic operations.
> *NumPy1.18的文档中对广播机制的介绍：[Array Broadcasting in Numpy](https://numpy.org/doc/1.18/user/theory.broadcasting.html?highlight=broadcast)*

NumPy的广播机制，***是一种对不同形状的数组运算进行自动处理的机制***。一个典型的例子，若要进行矩阵的数乘运算，常规操作需要通过for循环进行处理，这很麻烦，通过numpy的广播机制，可以一步达成：

```python
import numpy as np

a = np.arange(6)
b = a.reshape((2,3))
print(b)
c = b*2
print(c)
'''
[[0 1 2]
 [3 4 5]]
[[ 0  2  4]
 [ 6  8 10]]
'''
```

广播机制的使用条件：

> The rule governing whether two arrays have compatible shapes for broadcasting can be expressed in a single sentence.  
> 
> **The Broadcasting Rule:**  
> **In order to broadcast, the size of the trailing axes for both arrays in an operation must either be the same size or one of them must be one.**

官方文档这里所说的【trailing axes】是理解这句话的重点，也是理解广播机制的重点。先看例子后分析：

```python
import numpy as np

a = np.ones((2,2,3))*3
b = np.ones((2,3))*2
print('a:\n', a)
print('b:\n', b)
print('a+b:\n', a+b)
'''
a:
 [[[3. 3. 3.]
  [3. 3. 3.]]

 [[3. 3. 3.]
  [3. 3. 3.]]]
b:
 [[2. 2. 2.]
 [2. 2. 2.]]
a+b:
 [[[5. 5. 5.]
  [5. 5. 5.]]

 [[5. 5. 5.]
  [5. 5. 5.]]]
'''
# c = np.ones((2,4))*2
# print('a+c:\n', a+c)
```
这个例子中，a是一个2\*2\*3的3维数组，这里我用形象化的语言将之描述为：`一共两块儿，每块两组，每组三个`，而b是一个2\*3的2维数组，称为`一共两组，每组三个`，可以看到直接用`a+b`进行运算会触发广播机制（不然是没法运算的）。怎么理解这个广播过程呢？可以想象一下，numpy将b作为一个`块儿`的模板，根据这个模板复制出来了与a中相同个数的块，这样a与b便**形状一致**了，然后进行运算。

同理，3\*4\*5的数组可以与4\*5的数组进行运算，也可以与长度为5的一维数组进行运算，只要尾部的维度能够一致即可（能够作为一个模板进行复制扩展）。上面代码底部注释处的`c`是一个2\*4的数组，`a+c`将会报错，因为尾部不一致。

另外一种情形是`or one of them must be one`，即不匹配的某个维度只有一个元素，这很好理解，就是将那个单一的元素扩展成需要的长度，与上述的逻辑是一致的。比如，刚刚提到3\*4\*5的数组可以与4\*5的数组进行运算，那么3\*4\*5的数组与4\*1的数组也是可以进行运算的，这里的`1`会被扩展到`5`。


##### 基本运算（加减乘除取余开方）


进行良好的ndarray的基本运算，需要理解广播机制并加以利用。

广播机制下，对数组的运算会自动拓展到元素级别，先看最简单的情形 ，数组与标量之间的运算：

```python
# 数组与标量之间的运算
import numpy as np

a = np.ones((2,3))
print('a:\n', a)
print('a+2:\n', a+2)
print('a*2:\n', a*2)
print('0.5/a:\n', 0.5/a)
print('a*9开根号:\n', (9*a)**0.5)
print('a*9整除2:\n', (9*a)//2)
'''
a:
 [[1. 1. 1.]
 [1. 1. 1.]]
a+2:
 [[3. 3. 3.]
 [3. 3. 3.]]
a*2:
 [[2. 2. 2.]
 [2. 2. 2.]]
0.5/a:
 [[0.5 0.5 0.5]
 [0.5 0.5 0.5]]
a*9开根号:
 [[3. 3. 3.]
 [3. 3. 3.]]
a*9整除2:
 [[4. 4. 4.]
 [4. 4. 4.]]
'''
```

数组与标量的运算比较简单，只要记住在广播机制下所有运算会自动扩展到每个元素上即可。数组与数组之间的运算也是一样的，不过要注意前面介绍的***广播机制的适用条件***。

另外需要注意，在NumPy中，两个数组之间使用乘法符号，就是对应元素相乘，要进行传统的矩阵乘法（点乘、叉乘）运算，需要调用函数方法实现。

```python
# 数组与数组之间的运算
import numpy as np

a = np.ones((2,3))*3
b = np.ones((2,3))*2
print('a:\n', a)
print('b:\n', b)
print('a+b:\n', a+b)
print('a-b:\n', a-b)
print('a*b:\n', a*b)
print('a/b:\n', a/b)
print('a**b:\n', a**b)
'''
a:
 [[3. 3. 3.]
 [3. 3. 3.]]
b:
 [[2. 2. 2.]
 [2. 2. 2.]]
a+b:
 [[5. 5. 5.]
 [5. 5. 5.]]
a-b:
 [[1. 1. 1.]
 [1. 1. 1.]]
a*b:
 [[6. 6. 6.]
 [6. 6. 6.]]
a/b:
 [[1.5 1.5 1.5]
 [1.5 1.5 1.5]]
a**b:
 [[9. 9. 9.]
 [9. 9. 9.]]
'''
```


##### 矩阵运算（线性代数）

numpy中有大量线性代数相关的运算工具，大多数都封装在numpy.linalg中，比如`numpy.linalg.inv()`函数可以对矩阵求逆，可以求特征值，可以解线性方程组等等，详细的文档[在这里](https://numpy.org/doc/1.18/reference/routines.linalg.html "Linear algebra (numpy.linalg)")。

前面介绍的两个矩阵用`*`符号进行乘法运算，是将矩阵每个元素分别相乘，这里再介绍一个常用的函数`numpy.dot()`，字面意义似乎是`点乘`的样子，实际上这个函数方法既能运算点乘（数量积），也可以运算叉乘（矢量积）：当两个数组都是一维数组的时候，结果为数量积，都是二维矩阵的时候，结果为矢量积，对于多维数组，嗯，先不管它。

示例：

```python
import numpy as np

a = np.array([1,2,3])
b = np.array([2,3,4])
print('a.dot(b):\n', a.dot(b))
print('numpy.dot(a,b):\n', np.dot(a,b))
'''
a.dot(b):
 20
numpy.dot(a,b):
 20
'''

a = np.array([[1,2,3],  # 2行3列的矩阵
             [1,2,3]])
b = np.array([[2,3],    # 3行2列的矩阵
             [2,3],
             [2,3]])
print('a.dot(b):\n', a.dot(b))
print('numpy.dot(a,b):\n', np.dot(a,b))
'''
a.dot(b):
 [[12 18]
 [12 18]]
numpy.dot(a,b):
 [[12 18]
 [12 18]]
'''
```


##### 统计运算

NumPy中提供了求平均值、求最大最小值、求和等等这些常规的统计运算，有些运算需要通过numpy包调用，有些可以直接通过ndarray调用，下面给出一些示例：

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([1, 2, 3, 4, 5])
print('全部元素求和a.sum():\n', a.sum())
print('沿着第一维求和a.sum(axis=0):\n', a.sum(axis=0))
print('全部元素中的最大值a.max():\n', a.max())
print('沿着第一维求最小值a.min(axis=0):\n', a.min(axis=0))
print('全部元素求均值a.mean():\n', a.mean())
print('标准差a.std():\n', a.std())
print('方差a.var():\n', a.var())
'''
全部元素求和a.sum():
 45
沿着第一维求和a.sum(axis=0):
 [12 15 18]
全部元素中的最大值a.max():
 9
沿着第一维求最小值a.min(axis=0):
 [1 2 3]
全部元素求均值a.mean():
 5.0
标准差a.std():
 2.581988897471611
方差a.var():
 6.666666666666667
'''
```

##### 小结

关于ndarray的运算先看到这里，额外补充一点，通过ndarray进行运算通常比原始python代码的效率高很多，因为其底层是通过调用C或Fortran等优化过的运算库实现的，若不清楚底层效率，尽管选择ndarray即可。

可以参考这篇博客：[What makes Numpy Arrays Fast: Memory and Strides](http://www.jessicayung.com/numpy-arrays-memory-and-strides/)


#### 储存

ndarray如此好用，一个常见的需求是将待处理的文件转化为ndarray，一方面可以通过各种第三方工具包进行这种操作，比如通过PIL包中的Image工具将一张图片转化为ndarray：`arr = numpy.array(Image.open('abc.jpg'))`，另一方面，NumPy提供了save、load等方法，可以用来保存和读取ndarray。

##### 原生格式（.npy .npz）

先看例子：

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
np.save('a',a)
```

这个例子会在当前目录下保存一个a.npy文件，.npy是numpy保存数组的拓展格式，可以在保存的时候手动写上，不写它会自动加上，调用`np.save('a.txt',a)`这样的语句，将会保存出一个`a.txt.npy`文件。

加载npy文件，直接调用load方法即可：

```python
aa = np.load('a.npy')
print(aa)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
```

savez方法可以保存多个数组，保存的文件格式为`.npz`，实际上就是打包的多个`.npy`文件，同样通过load方法进行加载，得到的是一个可以通过关键字索引的可迭代对象。

看代码：

```python
import numpy as np

arrA = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
arrB = arrA.T
np.savez('arrs', a=arrA, b=arrB)

aaa = np.load('arrs.npz')
print('a:\n', aaa['a'])
print('b:\n', aaa['b'])
'''
a:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
b:
 [[1 4 7]
 [2 5 8]
 [3 6 9]]
'''

for i in aaa:
    print(aaa[i])
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 4 7]
 [2 5 8]
 [3 6 9]]
'''
```

对应`numpy.savez`方法，还有一个`numpy.savez_compressed`方法，同样存储的是`.npz`文件，只是会进行压缩，使用方法上没有任何差别。


##### 文本格式

前面的例子中处理的都是numpy的原生格式，实际的项目中处理的更多是诸如`.CSV、.json`或者干脆`.txt`等格式的文本文件，此处稍作实践。

先看加载数据的方法，比较常用的是`numpy.lodtxt`函数，完整的函数形式如下：

```python
numpy.loadtxt(fname, dtype=, comments='#', delimiter=None, converters=None,
 skiprows=0, usecols=None, unpack=False, ndmin=0)
```

>
fname   被读取的文件名（文件的相对地址或者绝对地址）  
dtype   指定读取后数据的数据类型  
comments    跳过文件中指定参数开头的行（即不读取）  
delimiter   指定读取文件中数据的分割符  
converters  对读取的数据进行预处理  
skiprows    选择跳过的行数  
usecols     指定需要读取的列  
unpack  选择是否将数据进行向量输出  
encoding    对读取的文件进行预编码  
————————————————  
版权声明：本文为CSDN博主「勿叨จุ๊บ」的原创文章，遵循 CC 4.0 BY-SA   版权协议，转载请附上原文出处链接及本声明。  
原文链接：https://blog.csdn.net/ACID_lv_ing/java/article/details/87092714  

构建一个测试用的txt文件，内容填充如下：
```txt
1==!==2==!==3==!==4==!==5==!==6==!==7==!==8==!==9
1==!==2==!==3==!==4==!==5==!==6==!==7==!==8==!==9
1==!==2==!==3==!==4==!==5==!==6==!==7==!==8==!==9
1==!==2==!==3==!==4==!==5==!==6==!==7==!==8==!==9
```

下面的代码通过`numpy.lodtxt`方法将这个4行9列的矩阵加载成ndarray：

```python
import numpy as np

arr = np.loadtxt('test.txt',np.float,delimiter='==!==')
print(arr)
'''
[[1. 2. 3. 4. 5. 6. 7. 8. 9.]
 [1. 2. 3. 4. 5. 6. 7. 8. 9.]
 [1. 2. 3. 4. 5. 6. 7. 8. 9.]
 [1. 2. 3. 4. 5. 6. 7. 8. 9.]]
 '''
```

保存操作是类似的：

```python
import numpy as np

arr = np.loadtxt('test.txt',np.float,delimiter='==!==')
print(arr)
'''
[[1. 2. 3. 4. 5. 6. 7. 8. 9.]
 [1. 2. 3. 4. 5. 6. 7. 8. 9.]
 [1. 2. 3. 4. 5. 6. 7. 8. 9.]
 [1. 2. 3. 4. 5. 6. 7. 8. 9.]]
 '''
arr2 = arr.T
np.savetxt('test2.txt',arr2,'%.1e',delimiter='  ^-^  ')
```

上述代码保存的`test2.txt`中的内容如下：

```
1.0e+00  ^-^  1.0e+00  ^-^  1.0e+00  ^-^  1.0e+00
2.0e+00  ^-^  2.0e+00  ^-^  2.0e+00  ^-^  2.0e+00
3.0e+00  ^-^  3.0e+00  ^-^  3.0e+00  ^-^  3.0e+00
4.0e+00  ^-^  4.0e+00  ^-^  4.0e+00  ^-^  4.0e+00
5.0e+00  ^-^  5.0e+00  ^-^  5.0e+00  ^-^  5.0e+00
6.0e+00  ^-^  6.0e+00  ^-^  6.0e+00  ^-^  6.0e+00
7.0e+00  ^-^  7.0e+00  ^-^  7.0e+00  ^-^  7.0e+00
8.0e+00  ^-^  8.0e+00  ^-^  8.0e+00  ^-^  8.0e+00
9.0e+00  ^-^  9.0e+00  ^-^  9.0e+00  ^-^  9.0e+00
```

关于文件的处理是一个大话题，不同的格式如何加载如何转化等，本文不再展开。

## 小结

本文对NumPy进行了简单认识与实践，参考资料主要是官网的[Quickstart tutorial](https://numpy.org/devdocs/user/quickstart.html)文档。本文的整个实践部分都围绕着ndarray展开，在Python的语法特色（主要是变量不用声明类型、使用缩进区分代码块）加持下，简直将运算变成了像手写草稿一样（而不像是在编写程序代码）顺畅。

NumPy已经有[官方中文网站](https://www.numpy.org.cn/)，但目前文档基本都是机器翻译的，质量极差，不建议参考，下面是来自[某位仁兄的中肯评价](https://www.numpy.org.cn/about/#%E8%B5%9E%E5%8A%A9%E5%95%86)（或者说是嘲讽？lol）：

```
Fountain  Chrome 69.0.3497.100  Windows 10.0  2020-03-26

This Chinese version is very standard,which is infinitely close to the original.
```