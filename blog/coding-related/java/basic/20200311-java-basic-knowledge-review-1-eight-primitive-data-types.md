# JAVA基础知识复盘（一）：八大基本数据类型  
*2020031101-java-basic-knowledge-review-1-eight-primitive-data-types*  
*Posted on 2020.03.12 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


* [JAVA基础知识复盘（一）：八大基本数据类型](#java%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E5%A4%8D%E7%9B%98%E4%B8%80%E5%85%AB%E5%A4%A7%E5%9F%BA%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)
    * [1 概览](#1-%E6%A6%82%E8%A7%88)
    * [2 表示范围](#2-%E8%A1%A8%E7%A4%BA%E8%8C%83%E5%9B%B4)
        * [2\.1 数值类型：](#21-%E6%95%B0%E5%80%BC%E7%B1%BB%E5%9E%8B)
            * [2\.1\.1 整型](#211-%E6%95%B4%E5%9E%8B)
            * [2\.1\.2 浮点型](#212-%E6%B5%AE%E7%82%B9%E5%9E%8B)
                * [IEEE754概要](#ieee754%E6%A6%82%E8%A6%81)
                * [浮点型数值范围](#%E6%B5%AE%E7%82%B9%E5%9E%8B%E6%95%B0%E5%80%BC%E8%8C%83%E5%9B%B4)
                * [\*浮点型数值精度（有效位数）](#%E6%B5%AE%E7%82%B9%E5%9E%8B%E6%95%B0%E5%80%BC%E7%B2%BE%E5%BA%A6%E6%9C%89%E6%95%88%E4%BD%8D%E6%95%B0)
        * [2\.2 字符类型 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- 两字节的Unicode如何存下全世界的字符？](#22-%E5%AD%97%E7%AC%A6%E7%B1%BB%E5%9E%8B--------------------------%E4%B8%A4%E5%AD%97%E8%8A%82%E7%9A%84unicode%E5%A6%82%E4%BD%95%E5%AD%98%E4%B8%8B%E5%85%A8%E4%B8%96%E7%95%8C%E7%9A%84%E5%AD%97%E7%AC%A6)
        * [2\.3 布尔类型 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- boolean类型占多大空间？](#23-%E5%B8%83%E5%B0%94%E7%B1%BB%E5%9E%8B--------------------------boolean%E7%B1%BB%E5%9E%8B%E5%8D%A0%E5%A4%9A%E5%A4%A7%E7%A9%BA%E9%97%B4)
    * [3 包装器类型](#3-%E5%8C%85%E8%A3%85%E5%99%A8%E7%B1%BB%E5%9E%8B)
        * [3\.1 “一切都是对象”](#31-%E4%B8%80%E5%88%87%E9%83%BD%E6%98%AF%E5%AF%B9%E8%B1%A1)
        * [3\.2 包装器类型属性与方法概述](#32-%E5%8C%85%E8%A3%85%E5%99%A8%E7%B1%BB%E5%9E%8B%E5%B1%9E%E6%80%A7%E4%B8%8E%E6%96%B9%E6%B3%95%E6%A6%82%E8%BF%B0)
            * [3\.3\.1 Number类](#331-number%E7%B1%BB)
            * [3\.3\.2 内置属性](#332-%E5%86%85%E7%BD%AE%E5%B1%9E%E6%80%A7)
            * [3\.3\.3 内置方法](#333-%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95)
                * [parseXXX()](#parsexxx)
                * [valueOf()](#valueof)
                * [decode()](#decode)
                * [getXXX()](#getxxx)
                * [toString() \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- 运行System\.out\.println(Float);时发生了 什么](#tostring--------------------------%E8%BF%90%E8%A1%8Csystemoutprintlnfloat%E6%97%B6%E5%8F%91%E7%94%9F%E4%BA%86%E4%BB%80%E4%B9%88)
        * [3\.3 自动拆装箱](#33-%E8%87%AA%E5%8A%A8%E6%8B%86%E8%A3%85%E7%AE%B1)
    * [4 初始化](#4-%E5%88%9D%E5%A7%8B%E5%8C%96)
        * [4\.1 默认初始值](#41-%E9%BB%98%E8%AE%A4%E5%88%9D%E5%A7%8B%E5%80%BC)
        * [4\.2 初始化方法](#42-%E5%88%9D%E5%A7%8B%E5%8C%96%E6%96%B9%E6%B3%95)
    * [5 类型转换](#5-%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2)


## 1 概览

Java是强类型语言，有八种基本数据类型（~~Void~~）：

| 分类 |类型名称| 大小 | 最小值 | 最大值 | 初始值 |包装器类型|
|:----:|:----:|:-----:|:-----:|:------:|:------:|:------:|
| 整型 | byte  | 8 bits|-128  |+127    |   0    | Byte   |
|      | short | 16 bits|-2^15|+2^15-1 |   0    | Short  |
|      | int   | 32 bits|-2^31|+2^31-1 |   0    | Integer|
|      | long  | 64 bits|-2^63|+2^63-1 |   0    | Long   |
| 浮点 | float | 32 bits|~-E38 | ~+E38  |  0.0   | Float |
|      | double| 64 bits|~-E308|~+E308  |  0.0   | Double|
| 字符 | char  | 16 bits|\u0000 |\uFFFF | \u0000 |Character|
| 布尔 |boolean| --     |  --   |   --  | false  | Boolean |

## 2 表示范围

### 2.1 数值类型：

数值类型包括整型、浮点型，有如下特点：  

* 大小固定
* 平台无关
* 均为有符号数

#### 2.1.1 整型

*！知识回顾（关于底层存储）：不考虑特殊情况，默认现代计算机均采用补码来储存【有符号整数】，要明确如下内容（摘自《深入理解计算机系统（第2版）》第2.2.3节）：C语言标准并没有要求补码形式来表示有符号整数，但是几乎所有的机器都是这么做的……关于整数数据类型的取值范围和表示，Java标准是非常明确的，它要求采用补码表示……*

直接以byte类型为例子分析一下整型类型的数值范围是怎么来的。byte类型大小为8bits（即1字节），根据原码、补码编码规则给出下表：

    * 0   ： 原码`0000 0000`，补码`0000 0000`
    * +1  ： 原码`0000 0001`，补码`0000 0001`
    * +127： 原码`0111 1111`，补码`0111 1111`
    * -128： 原码`1 0000 0000`，补码`1000 0000`
    * -127： 原码`1111 1111`，补码`1000 0001`
    * -1  ： 原码`1000 0001`，补码`1111 1111`

从表中可以看到**补码编码将符号带入运算、消除零的不唯一编码**这两大优势（相比于原码、反码）。之前在理解-128这个值的时候产生了一些疑惑，原因在于将“补码=反码+1”这个运算技巧当成了原理，并拿来反推补码，由此产生了一些矛盾。从根源出发来看：（有符号数的）八位二进制的源码、反码的表示范围仅为`[-127~+127]`而已，表示不了`-128`，`-128`的出现是由补码的编码规则决定的，补码天生具有不对称性，在同等位数下能表示的非负数比正数多一个。

由此及同理可以得出：

* byte类型的取值范围为`[-128 ~ +127]`
* short类型为`[-32768 ~ +32767]`
* int类型为`[-2147483648 ~ +2147483647]`
* long类型为`[-9223372036854775808 ~ +9223372036854775807]`

#### 2.1.2 浮点型

##### IEEE754概要

**浮点型**稍复杂，JAVA中的浮点类型是遵从[IEEE754][IEEE754]标准的，概括一下IEEE754的核心内容：

IEEE754规定的浮点数不是通过简单的补码来存储，而是以类似科学计数法的形式将一个浮点数分为三个部分来存（基数隐含为2）：

1. 符号（sign）s：0正1负
2. 阶码（exponent）E：对应科学计数法中的指数，采用移码表示，偏移量有专门的约定
3. 尾数（fraction）M：对应科学计数法中的尾数，采用真值表示（无符号数）

各部分的大小分配：

* 单精度浮点数：符号1bit + 阶码8bits  + 尾数23bits 
* 双精度浮点数：符号1bit + 阶码11bits + 尾数52bits

根据阶码E的值，可将浮点数分为三类：

1. 规格化值：E即不全为0也不全为1，此时尾数隐含1（尾数部分=1.XXX），阶码取值范围[-126~+127]（单精度）| [-1022~+1023]（双精度）
2. 非规格化值：E全为0，此时尾数不隐含1（尾数部分=0.XXX，可以表示0），阶码为-126（单精度）| -1022（双精度） 
3. 特殊值：E全为1，此时若M全为0则表示无穷，以s来区分正负无穷，若M非零，则表示NaN（Not a Number）

##### 浮点型数值范围

由上述可知，一个规格化浮点数的值 `V1 = (-1)^s * 1.M * 2^E `，非规格化浮点数的值 `V2 = (-1)^s * 0.M * 2^E `，其中尾数M决定数值精度，阶码E决定数值范围。

注意阶码的取值范围，出于【硬件层面方便比较】的考虑，阶码使用移码表示，从而消除了负数，单精度与双精度的偏移量分别为127（即`0111 1111`）和1023，以单精度为例具体分析，为何取127这个值而不是标准移码的偏移量128（2的n-1次幂）：

8位二进制数从`0000 0000`到`1111 1111`总共有256个值，现在偏移量取127，即将原始的0加上127作为偏移后的0，所以现在的零就成了`0111 1111`，原先的零成了-127，如此换算之后我们所拥有的`0000 0000`到`1111 1111`便对应的成为了[-127~+128]，又因为前面提到，规定全1为非规格化值（其实就是0），全0为特殊值（正负无穷、NaN），所以排除掉`0000 0000`、`1111 1111`这两个编码，剩下的范围就成了[-126~+127]，IEEE754标准中单精度浮点数的阶码取值范围就是这么来的，双精度的阶码同理可以得到取值范围为[-1022~+1023]。

接下来看一下尾数的取值范围，仍以单精度浮点数为例。单精度浮点数尾数部分为23位，又因为规格化值隐藏了一位精度（1.XXX），所以尾数可以取到最大值是规格化的全1（24位），即二进制的`1.111111111……`，小数点后面共有23个1，也就是十进制的`2-2^-23`，同理尾数可以取到的**最小正非规格化值**为`0.000……0001`，小数点后面共有22个0，最后一位是1，也就是十进制的`2^-23`。综合阶码的取值范围便可以得到JAVA中单精度浮点数的两个内置值MAX_VALUE与MIN_VALUE：

* `Float.MAX_VALUE = (-1)^0 * (2-2^-23) * 2^127 ≈ 2^128 ≈ 3.4e+38 ` （最大尾数*最大阶码）
* `Float.MIN_VALUE = (-1)^0 * (2^-23) * 2^-126 ≈ 2^-149 ≈ 1.4e-45 `

注意这里的Float.MIN_VALUE，它并非单精度浮点数的最小值（最小值直接MAX_VALUE取负即可），MIN_VALUE正式的名称应该叫**最小正非规格化数**（源码中注释为`A constant holding the smallest positive normal value of type`），这里的MIN_VALUE可以理解为一种精度，由于引入非规格化数，得以让浮点数数值**平滑地逼近0**，这个"最小正非规格化数"便是IEEE754标准下可以精确表示的最逼近0的那个正数。

补充一句，Float类中还定义了一个MIN_NORMAL，值为`1.17549435E-38f`，这个MIN_NORMAL注释写的是`A constant holding the smallest positive normal value of type`，啥玩意？最小正态值？正规值？看数值与MAX_VALUE相近，再对照前面所提到的浮点数的分类（规格化值、非规格化值、特殊值），容易联想到，这个MIN_NORMAL便是**最小正规格化数**，也就是阶码取-126，尾数取`1.0000……`算出来的值：`2^-126 ≈ 1.17549435E-38`。

Double类型与Float同理，不在赘述。

[IEEE754]: https://zh.wikipedia.org/wiki/IEEE_754 "IEEE754 维基百科"

##### *浮点型数值精度（有效位数）

上文中提到MIN_VALUE这个值，它是通过让尾数与阶码取最小值得到的，接下来继续分析一下这个值。仍以单精度浮点数为例，先不管阶码，只看尾数。

单精度浮点数的尾数为23位，最小的非规格化数为`0.000000……001`，对应十进制值为`2^-23 ≈ 0.00000 01192 09289`，改动一位`0.000000……010`，对应十进制值为`2^-22 ≈ 0.00000 02384 18579`，可以看到二进制数+1，对应的十进制翻了一番，其实就是+了一个`Float.MIN_VALUE【的尾数值】`，MIN_VALUE可以作为精度就体现在这里。二进制小数与十进制之间的对应关系是离散的，这也就造成了**范围内的数不一定能够精确表示**，比方说取一个`2^-22.5 ≈ 0.00000 01686`就没法用float类型精确表示，指数部分的.5已经超出了最小精度，做不到。

其实这方面最经典的例子莫过于输出`1.0-0.9`了，虽然与此处讨论的内容有些差别，但也有异曲同工之妙：
```java
    System.out.println(1.0-0.9); //0.09999999999999998
```
二进制小数与十进制小数之间的离散关系造成了一些容易被忽视的错误。

说回来，总之，单精度尾数部分的数值只能以`2^-23`为最小单元离散着增长，小于这个值的数将无法精确表示，这是单精度浮点数的尾数的有效值下限。从另一方面思考，算上隐含位的1，尾数最大值为`2^24 -1 = 1677 7215`，也就是24位二进制尾数全为1时候的值（先把小数点丢一边），尾数超过这个值的范围就无法保证精度了，因为没法用24位二进制表示。

用代码实践一下：
```java
    //小技巧：JAVA里的数字可以用下划线分割开，方便观察不影响结果
    float frac5 = (float) 1677_7215_1;
    System.out.printf("%.20f %n", frac5);
    System.out.println(frac5);
    /** output
     * 167772144.00000000000000000000 
     * 1.67772144E8
     */
```
1677_7215_1超出了最大数值范围，结果给出的`1677_7214_4`，从第八位开始产生误差，具体分析一下这个误差产生的原因：

- 首先，1677_7215_1转成二进制为`10011111_11111111_11111111_0111`，共28位
- 将28位二进制规格化为`1.0011111_11111111_11111111_0111E27`
- 将超出24位的值按规则进行舍入操作（IEEE754规定的舍入规则为：向距离该实数最近的可表示的值舍入，且优先选择偶数），得到`1.0011111_11111111_11111111E27`
- 接下来以IEEE754的标准拆成符号、尾数、阶码存下这串数
- 将这串数往回转换，得到二进制串`10011111_11111111_11111111_0000`，换算成十进制便是`1677_7214_4`。

再看一个小想法：
```java
    //最小值离散递增
    float frac = 0.00000011920928955078125f;
    for (int i = 1;i<=21;++i){
        System.out.printf("%.25f %n", i*frac);
    }
    /**output
     * 0.0000001192092895507812500 
     * 0.0000002384185791015625000 
     * 0.0000003576278686523437500 
     * 0.0000004768371582031250000 
     * 0.0000005960464477539062000 
     * 0.0000007152557373046875000 
     * 0.0000008344650268554688000 
     * 0.0000009536743164062500000 
     * 0.0000010728836059570312000 
     * 0.0000011920928955078125000 
     * 0.0000013113021850585938000 
     * 0.0000014305114746093750000 
     * 0.0000015497207641601562000 
     * 0.0000016689300537109375000 
     * 0.0000017881393432617188000 
     * 0.0000019073486328125000000 
     * 0.0000020265579223632812000 
     * 0.0000021457672119140625000 
     * 0.0000022649765014648438000 
     * 0.0000023841857910156250000 
     * 0.0000025033950805664062000
     */
```
float本不能精确表示20多位十进制数，但由于符合最小精度，所以能精确表示。随着最小精度的离散递增，可以看到小数部分第七位有可能覆盖不到某些数字（累加十次以内覆盖不到6，20次以内覆盖不到2、8），也就是说在尾数部分，第七位的值就有可能存在误差了，那么乘以阶码之后呢？或许可以恰好凑成要表示的数字，但也可能存在表示不到的几率。

好像有点扯远了，这一小节的主题“表示范围”已经讨论清楚了 ，精度、有效数字的问题等我理一理用更干净一点的表达方式讲清楚，此处先这样。

参考：

[浮点数的有效数字位数_C#_bluewanderer的博客-CSDN博客](https://blog.csdn.net/bluewanderer/article/details/86671653)


### 2.2 字符类型 ------------------------ 两字节的Unicode如何存下全世界的字符？

JAVA的char类型存的是Unicode字符，使用两个字节16bits存储，此处有一个疑问：**16bits只能存储65536个值，那Unicode如何用16bits容下世界各国的字符呢？世界各国的字符加一起不到65536个吗？**

这个问题，简单来说，Unicode不仅是2个字节，目前它最高可以支持到32位。第一个字节将编码分为128个区（首位恒为0），第二个字节分出256个平面，接下来的两个字节才是狭义的两字节Unicode，所以每个平面都可以容纳6万多个字符，最原始的平面称为BMP(Basic Multilingual Plane，基本多文种平面），我们所说的java使用两字节Unicode，也就是指BMP。

Unicode的编号采用`\uXXXXXX`的形式，`XXXXXX`为十六进制数，后四位代表具体某个平面的字符编号，前面指定区和平面，目前区还用不到，平面也只有17个，所以`\u00000-\u10FFFF`就够了，若不指明平面，默认为BMP平面的字符。在JAVA中存一个字符，也就是存这个字符的Unicode编号。

目前在BMP平面中，`基本汉字`包括20902个字，编码范围`\u4E00-\u9FA5`，，`扩展A`包括6582个字，编码范围`\u3400-\u4DB5`，再加上类似`基本汉字补充`（包括74个字，编码范围`\u9FA6-\u9FEF`）这样的小集合，总共两万多个汉字[^汉字Unicode编码范围]。像`扩展B（包括42711字，编码范围\u20000-\u2A6D6）`里面的字符，比如这个【𠀀】字（不知道念啥），已经超出了BMP的范围，用单个char类型是没法表示的，看JAVA里Character类，char的范围就是`\u0000 - \uFFFF`，若想表示【𠀀】这个字，得借助char数组（String类）才行。

```java
    char a = '\u4E00';
    char b = '\u9FA5';
    String x = "\uD840\uDC00";
    System.out.println(a);
    System.out.println(b);
    System.out.println(x);
    /**output
     * 一
     * 龥
     * 𠀀
     */
```

关于Java的char类型先了解这么多，有关字符编码乃至String类的内部实现等问题单独作为一个话题改日再聊。附两篇博文：  

* [细说Java中的字符和字符串（一）_BuquTianya的专栏-CSDN博客](https://blog.csdn.net/BuquTianya/article/details/80685437)
* [Java中的字符集编码入门（六）Java中的增补字符 - 就只会点Java - ITeye博客](https://www.iteye.com/blog/jiangzhengjun-512083)
* [关于Unicode - 西城铁 - 博客园](https://www.cnblogs.com/xichengtie/p/3383890.html)

[^汉字Unicode编码范围]:https://zixuephp.net/article-486.html "汉字Unicode编码范围"


### 2.3 布尔类型 ------------------------ boolean类型占多大空间？

关于Java中的boolean类型，首先要明确的就是它的值只能是true或false，不像C语言里用0或非0表示真假，不过用法都是类似的。

```java
    boolean booo = true;
    booo = 1 > 2;
    System.out.println(booo);
    /**output
     * false
     */
```

有关boolean类型的大小可以聊一聊。《Java编程思想（第4版）》里有一节的节标题（3.16）是这么写的：`Java没有sizeof`，大意就是Java中类型明确，大小固定，所以不需要像C/C++语言里的sizeof方法来确定某个类型的大小，然而boolean类型算是个意外。本文开头给出的表格中关于boolean类型的大小置空了，因为boolean类型所占储存空间的大小不像数值类或字符类那么明确。boolean类型到底占用多大空间，下面稍作讨论。

根据广大网友的探索，主要有两份文档写了Boolean类型的一些说明，一个是Oracle官方的Java教程文档[The Java™ Tutorials][oracle docs]，另一个是JVM规范文档[The Java® Virtual Machine Specification][JVM spec]

【The Java™ Tutorials】里对Boolean类型的描述如下：
>boolean: The boolean data type has only two possible values: true and false. Use this data type for simple flags that track true/false conditions. This data type represents one bit of information, but its "size" isn't something that's precisely defined.

最后一句说到boolean类型的大小没有精确的定义，话是这么说，存到内存里总要有个大小。接着看虚拟机的规范文档【The Java® Virtual Machine Specification】（Java SE 13 Edition）：
>Although the Java Virtual Machine defines a boolean type, it only provides very limited support for it. There are no Java Virtual Machine instructions solely dedicated to operations on boolean values. Instead, expressions in the Java programming language that operate on boolean values are compiled to use values of the Java Virtual Machine int data type.
>
>The Java Virtual Machine does directly support boolean arrays. Its newarray instruction (§newarray) enables creation of boolean arrays. Arrays of type boolean are accessed and modified using the byte array instructions baload and bastore (§baload, §bastore).
>
>>*In Oracle’s Java Virtual Machine implementation, boolean arrays in the Java programming language are encoded as Java Virtual Machine byte arrays, using 8 bits per boolean element.*
>
>The Java Virtual Machine encodes boolean array components using 1 to represent true and 0 to represent false. Where Java programming language boolean values are mapped by compilers to values of Java Virtual Machine type int, the compilers must use the same encoding. 

机翻如下：

> 尽管Java虚拟机定义了布尔类型，但是它仅提供非常有限的支持。 没有Java虚拟机指令专门用于布尔值的操作。 相反，将对布尔值进行运算的Java编程语言中的表达式编译为使用Java虚拟机int数据类型的值。
> 
> Java虚拟机确实直接支持布尔数组。 它的newarray指令（§newarray）可以创建布尔数组。 使用字节数组指令baload和bastore（§baload，§bastore）访问和修改boolean类型的数组。
> 
>> 在Oracle的Java虚拟机实现中，将Java编程语言中的布尔数组编码为Java虚拟机字节数组，每个布尔元素使用8位。
> 
> Java虚拟机使用1表示true和0表示false来对布尔数组组件进行编码。 如果编译器将Java编程语言的布尔值映射到Java虚拟机类型int的值，则编译器必须使用相同的编码。

大概意思：

1. 在虚拟机层次，boolean类型被处理成了int类型（也就是占4字节）
2. Java虚拟机支持创建boolean数组，其访问与修改用的是byte数组的命令
3. *（在Oracle的Java虚拟机中）所谓的boolean数组其实就是byte数组，每个元素占1字节*
4. Java虚拟机创建的boolean数组中用1代表true，用0代表false

原文档中第三条是小字斜体补充的一句话，可能其他版本的JVM在这方面的处理是不一样的。这个知识点有点太偏底层了，现在也没啥实践的条件（能力），总之有个大概印象就好，以后有必要的话，从底层分析一遍，就不至于这样子朦朦胧胧的了。

参考文档：

* [ 在 Java 中 boolean 类型占多少字节 | Binkery 技术博客](https://binkery.com/archives/346.html)
* [javap命令行分析揭示boolean的本质的虚拟机指令_Java_BlankSpace的博客-CSDN博客](https://blog.csdn.net/weixin_43896318/article/details/104627729?fps=1&locationNum=2)
* [Java 11 将至，除了 Oracle JDK 还有这些版本！](https://baijiahao.baidu.com/s?id=1611312508208772003&wfr=spider&for=pc)


[JVM spec]:https://docs.oracle.com/javase/specs/jvms/se13/html/jvms-2.html#jvms-2.3.4 "JVM规范"
[oracle docs]:https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html "oracle文档"

## 3 包装器类型

### 3.1 “一切都是对象”

JAVA为每种基本类型提供了对应的包装器类型（[Primitive wrapper class][wrapper in java]），这些包装器类型封装了对应的基本类型，同时还封装了了一些基本属性和常用方法，比如前文中用到了一个`Float.MAX_VALUE`，此处的`Float`便是单精度浮点数类型float对应的包装器类型，而`MAX_VALUE`则是这个包装器类型里预置的一个常量，几乎每个包装器里都提供了大小、最值等基本信息，有需要可以直接调用。

包装器类型可谓是体现JAVA是个纯面对对象语言的很好例证。再次引用《Java编程思想（第4版）》的章标题（第二章）：`一切都是对象`，当我们新建一个基本类型的时候，这个基本类型就是一个**值**而已，但通过包装器，这个值转变成了一个**对象**，如此一来哪怕是对基本类型的操作也可以被纳入到面对对象的思维之中。

当然了，相比于包装器对象，基本类型占用系统资源较少，所以不是有了包装器就不用基本类型，应当看情况取舍选择。

各基本类型对应的包装器如下：

    - byte    ----------   Byte
    - short   ----------   Short
    - int     ----------   Integer
    - long    ----------   Long
    - float   ----------   Float
    - double  ----------   Double
    - char    ----------   Character
    - boolean ----------   Boolean

[wrapper in java]:https://en.wikipedia.org/wiki/Primitive_wrapper_class_in_Java "Primitive wrapper class in Java - wiki"

### 3.2 包装器类型属性与方法概述

#### 3.3.1 Number类

所有数值类包装器都继承自Number类。Number类是个抽象类，里面定义了六个方法，
```
    byte     byteValue()     
    abstract double     doubleValue()   
    abstract float  floatValue()    
    abstract int    intValue()  
    abstract long   longValue()     
    short   shortValue()    
```
这几个方法在具体的包装器类里有特定的实现，实际上就是做了个强制类型转换，拿Integer类举例：
```java
    Integer i = 12;
    System.out.println(i.byteValue()); //output: 12
```
Integer类中的byteValue()方法：
```java
    public byte byteValue() {
        return (byte)value;
    }
```
其他几个数值类包装器对Number类的这几个方法的实现如出一辙。

#### 3.3.2 内置属性

属性方面，包装器里面都预置了最大值最小值什么的，直接看代码:
```java
    //Byte
    System.out.println(Byte.BYTES);     //一个byte类占用的 字节数（二进制补码形式）
    System.out.println(Byte.SIZE);      //一个byte类占用的 比特数
    System.out.println(Byte.MAX_VALUE); //最大值
    System.out.println(Byte.MIN_VALUE); //最小值
    System.out.println(Byte.TYPE);      //对应的基本类的名称 （咱这是从包装器类输出的这些东西）
    /**output
     * 1
     * 8
     * 127
     * -128
     * byte
     */
```
Short类、Integer类、Long类里与Byte一样，都有且只有上面这五种属性（定义相同），浮点数略有差异，主要的前文分析浮点数的时候说过了，这里直接看代码注释就好：
```java
    //Float
    System.out.println(Float.TYPE); 
    System.out.println(Float.BYTES);
    System.out.println(Float.SIZE);
    System.out.println(Float.MAX_VALUE);            
    System.out.println(Float.MAX_VALUE);            //最大值（规格化数，通过尾数与阶码同取最值得到）
    System.out.println(Float.MIN_VALUE);            //最小正非规格化数
    System.out.println(Float.MIN_NORMAL);           //最小正规格化数
    System.out.println(Float.MAX_EXPONENT);         //阶码最大值
    System.out.println(Float.MIN_EXPONENT);         //阶码最小值
    System.out.println(Float.NaN);                  //非数值
    System.out.println(Float.NEGATIVE_INFINITY);    //负无穷
    System.out.println(Float.POSITIVE_INFINITY);    //正无穷
    /**output
     * float
     * 4
     * 32
     * 3.4028235E38
     * 1.4E-45
     * 1.17549435E-38
     * 127
     * -126
     * NaN
     * -Infinity
     * Infinity
     */
```

Boolean类没啥东西，只有一个TYPE和TRUE、FALSE两个常量，至于Character类，博大精深，放到专门总结字符操作的文档中。

#### 3.3.3 内置方法

主要看一看比较通用的方法，个别的就不说了。先来看可以放到一组来说的几个方法：parseXXX()、valueOf()、decode()以及getXXX()。

##### parseXXX()

除了Character类每个包装器类都有parse方法，比如Integer类中有parseInt方法，Double类中有parseDouble方法，Boolean类中有parseBoolean方法，其作用在于将传入的参数格式化成对应的基本类型：
```java
    //parseXXX(String s)
    Integer a = Integer.parseInt("123");
    Double b = Double.parseDouble("2.0");
    System.out.println(a);
    System.out.println(b);
    /**output
     * 123
     * 2.0
     */
```
整数类构造器的parse方法还有另一种形式，可以在传入字符串的同时指定进位制：
```java
    //parseXXX(String s, int radix)
    Integer c = Integer.parseInt("FF",16);
    System.out.println(c); //output :  255
```
其实不指定进位制的形式，内部也是调用了指定进位制形式的方法，执行`Integer.parseInt("123")`这条语句实际上（在内部）执行了`Integer.parseInt("123",10)`。

##### valueOf()

valueOf()方法是每个基本类型的包装器中都有的，valueOf()的作用与parseXXX一样，看一下Integer中valueOf()的源码：
```java
    public static Integer valueOf(String s) throws NumberFormatException {
        return Integer.valueOf(parseInt(s, 10));
    }
    public static Integer valueOf(int i) {
        if (i >= IntegerCache.low && i <= IntegerCache.high)
            return IntegerCache.cache[i + (-IntegerCache.low)];
        return new Integer(i);
    }
```
可见valueOf()也是首先通过parseXXX方法处理的（Character类特殊），区别在于，**valueOf返回的是包装器对象，parseXXX返回的是基本类型**。

##### decode()

四个整数类包装器还同时含有一个decode方法，作用仍然与前面两个类似，不过decode可以直接输入十六进制等其他进位制的数字，valueOf或parseXXX方法想实现同样功能需要指定两个参数，看代码：
```java
    System.out.println(Integer.decode("0xFF"));//output ： 255
//  System.out.println(Integer.valueOf("FF")); //报错 NumberFormatException
    System.out.println(Integer.valueOf("FF",16));//output ： 255
//  System.out.println(Integer.parseInt("FF")); //报错 NumberFormatException
    System.out.println(Integer.parseInt("FF",16));//output ： 255
```

##### getXXX()

这个getXXX方法，只用Integer与Long中有，方法名称挺唬人，以Integer类举例，先看代码：
```java
    //valueOf()以及getXXX()
    String tempString = "234";
    System.out.println("Integer.parseInt(tempString): "+Integer.parseInt(tempString));
    System.out.println("Integer.valueOf(tempString): "+Integer.valueOf(tempString));
    System.out.println("Integer.getInteger(tempString): "+Integer.getInteger(tempString));
    System.out.println("Integer.getInteger(\"234\"): "+Integer.getInteger("234"));
    /**output
     * Integer.parseInt(tempString): 234
     * Integer.valueOf(tempString): 234
     * Integer.getInteger(tempString): null
     * Integer.getInteger("234"): null
     */
```
getInteger没有取到值输出了null，可见所谓的getXXX并不是先入为主幻想出来的那种作用，直接上文档：

> Determines the integer value of the system property with the specified name.
> 
> The first argument is treated as the name of a system property. System properties are accessible through the System.getProperty(java.lang.String) method. The string value of this property is then interpreted as an integer value using the grammar supported by decode and an Integer object representing this value is returned.
> 
> If there is no property with the specified name, if the specified name is empty or null, or if the property does not have the correct numeric format, then null is returned. 
>
>确定具有指定名称的系统属性的整数值。
>
> 第一个参数被视为系统属性的名称。 系统属性可通过System.getProperty（java.lang.String）方法访问。 然后，使用解码支持的语法将此属性的字符串值解释为整数值，并返回表示该值的Integer对象。
> 
> 如果没有具有指定名称的属性，或者指定的名称为空或null，或者该属性的格式不正确，则返回null。

可见getXXX方法是用来获取系统属性的，并将属性转成数值，不过说归说，看代码：
```java
    System.out.println(System.getProperty("user.name"));
    System.out.println(Integer.getInteger("user.name"));
    System.out.println(Long.getLong("user.name"));
    /**output
     * Administrator
     * null
     * null
     */
```
getProperty能获取到的系统属性，用getInteger还是什么也拿不到，输出了null，看了下getInteger的源码，它也是调用的getProperty方法，然后又调用了decode方法将getProperty拿到的值处理后返回，上面的代码中Administrator自然是没法decode，所以输出了null。不过貌似也没有什么纯数字形式的系统信息，暂时不清楚这个getInteger到底是什么场景下使用的。

##### toString() ------------------------ 运行System.out.println(Float);时发生了什么

这里插叙一个小话题，引申自前面验证浮点数精度的例子，实践中运行过如下代码：
```java
    float frac1 = (float) 0.0000_0011_92;
    System.out.printf("%.20f %n", frac1);
    System.out.println(frac1);
    /**output
     * 0.00000011920000275722
     * 1.192E-7
     */
```
当时考虑到代码中默认的打印格式是怎么来的，现在在这里分析一下，直接在代码块里逐层查看：
```java
    //从这条语句开始
    System.out.println(frac1);
    //进入println() -- java.io.PrintStream类
    public void println(float x) {
        synchronized (this) {
            print(x);
            newLine();
        }
    }
    //进入print(x) -- java.io.PrintStream类
    public void print(double d) {
        write(String.valueOf(d));
    }
    //进入String.valueOf(d) -- String类
    public static String valueOf(float f) {
        return Float.toString(f); // -----哈哈，包装器出现了
    }
    //进入Float.toString(f) ---Float类
    public static String toString(float f) {
        return FloatingDecimal.toJavaFormatString(f);
    }
```
点到为止，总之，绕了一圈，打印语句的格式回到了类型本身的toString方法上，这也算是Java的一个套路吧。

### 3.3 自动拆装箱

拆装箱即基本类型与包装器类型之间的转换，将基本类型转成包装器类型也就是装箱，反之是拆箱。看例子：
```java
    //自动装箱例子
    int a = 2;
    Integer b = a;
    System.out.println(b); //output : 2
```
可以看到基本类型的值直接赋给了包装器对象，回想平时给对象赋值的操作，总要通过带参数的构造器new一个或者调用set方法等，此处却可以直接赋值，是因为Java提供了自动装箱的功能，具体的实现是在编译器层面处理的，实际是调用了valueOf方法，拆箱同理，调用了intValue（xxxValue）方法。

详情参考：

* [Java基础 - 包装器类型 - HRocky - 简书](https://www.jianshu.com/p/bb629b7ff97c)

## 4 初始化

### 4.1 默认初始值

先看看每种基本类型的默认初始值：
```java

    static byte byteType;
    static short shortType;
    static int intType;
    static long longType;
    static float floatType;
    static double doubleType;
    static char charType;
    static boolean booleanType;

    public static void main(String[] args) {
        //默认初始值
        System.out.println("byteType:"+byteType);
        System.out.println("shortType:"+shortType);
        System.out.println("intType:"+intType);
        System.out.println("longType:"+longType);
        System.out.println("floatType:"+floatType);
        System.out.println("doubleType:"+doubleType);
        System.out.println("charType:"+charType);
        System.out.println("booleanType:"+booleanType);
        /**output
         * byteType:0
         * shortType:0
         * intType:0
         * longType:0
         * floatType:0.0
         * doubleType:0.0
         * charType: 
         * booleanType:false
         */
    }
```
联系到boolean类在底层被当作int处理，且用零代表false，不太严谨地考虑，可以说**所有基本类型的初始值就是零**，为每一位二进制位赋零。单独说一下char类型，char类型的内容前文说过是Unicode字符编码，在Java里它的默认初始值是`\u0000`（16bits个零），查阅Unicode字符表可以看到`\u0000`属于BMP的[C0 Controls and Basic Latin][C0 Controls and Basic Latin]这部分，译为【C0控制与基本的拉丁字母】，其中C0控制符范围`\u0000-\u001F`，在码表里它的名字是NUL，别名NULL，意思是一样的，总之就是“空”，这里的“空”不是说没有占用储存空间，它也是一个字符，被解析出来就是啥也不显示。

*P.S. 空格符的Unicode编号是\u0020，不要与\u0000混为一谈*

基本类型包装器的默认初始值为null：
```java
    public static Integer iii;
    private static void wrapperDefault(){
        System.out.println(iii);  //output： null
    }
```

[C0 Controls and Basic Latin]:moz-extension://eea52af4-a28f-48b0-9a06-1ae9bce0680f/assets/pdf/web/viewer.html?file=https%3A%2F%2Funicode.org%2Fcharts%2FPDF%2FU0000.pdf "C0 Controls and Basic Latin"

### 4.2 初始化方法

基本类型的初始化基本没什么坑，前面的代码里也体现了，不初始化根本就没法通过编译检查，更没法输出，所以都是用的静态类型，像`Byte b = 129;`这种语句都是会爆红的（可谓十分贴心），非要说有什么需要注意的，一个是刚讲过的包装器类初始值为null的问题，再有就是接下来要讲的类型转换问题。
```java
    //随心所欲的初始化方法
    Short s = new Short("1");
    Integer i = new Integer("2");
    Integer ii = 2;
    Character c = '3';
    System.out.println(s);
    System.out.println(i);
    System.out.println(ii);
    System.out.println(c);
    /**output
     * 1
     * 2
     * 2
     * 3
     */
```

## 5 类型转换

关于类型转换，需要关注的只有一个点：**能不能合法转换**。理解了前文中【表示范围（2.1节）】的内容，类型转换也就不再是问题。

下表为将A转成B的情况分析，0=无法转换，1=合法，2=可能有精度损失（需要强制转换）。

|  A↓B→ | byte | short | int | long | float | double | char |boolean|
|:-----:|:----:|:-----:|:---:|:----:|:-----:|:------:|:----:|:-----:|
| byte  |  -   |   1   |  1  |   1  |   1   |   1    |  0   |   0   |
| short |  2   |   -   |  1  |   1  |   1   |   1    |  2   |   0   |
| int   |  2   |   2   |  -  |   1  |   2   |   2    |  2   |   0   |
| long  |  2   |   2   |  2  |   -  |   2   |   2    |  2   |   0   |
| float |  2   |   2   |  2  |   2  |   -   |   1    |  2   |   0   |
|double |  2   |   2   |  2  |   2  |   2   |   -    |  2   |   0   |
| char  |  2   |   2   |  1  |   1  |   1   |   1    |  -   |   0   |
|boolean|  0   |   0   |  0  |   0  |   0   |   0    |  0   |   -   |

一句话总结：**精度小的类型可以合法向精度大的类型转换，反之需要强制转换**。

注意，此处所说的精度不是表示范围，比如int转float，虽然float的表示范围更大，但是有效位数比int少，所以有可能产生精度损失。另外，不要忘了数值类皆为有符号数，这也是为什么short与char同为两字节，互相转化却需要强制转换。





