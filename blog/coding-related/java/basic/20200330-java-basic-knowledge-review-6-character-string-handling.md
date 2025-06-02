# JAVA基础知识复盘（六）：字符串处理
*2020033001-java-basic-knowledge-review-6-character-string-handling*  
*Posted on 2020.03.30 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


* [JAVA基础知识复盘（六）：字符串处理](#java%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E5%A4%8D%E7%9B%98%E5%85%AD%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%A4%84%E7%90%86)
    * [1 前言](#1-%E5%89%8D%E8%A8%80)
    * [2 不可变的字符串](#2-%E4%B8%8D%E5%8F%AF%E5%8F%98%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2)
        * [2\.1 为何让字符串不可变](#21-%E4%B8%BA%E4%BD%95%E8%AE%A9%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%8D%E5%8F%AF%E5%8F%98)
    * [3 String类概览](#3-string%E7%B1%BB%E6%A6%82%E8%A7%88)
        * [3\.1 属性](#31-%E5%B1%9E%E6%80%A7)
            * [offset](#offset)
            * [String中无length属性](#string%E4%B8%AD%E6%97%A0length%E5%B1%9E%E6%80%A7)
        * [3\.2 方法](#32-%E6%96%B9%E6%B3%95)
            * [3\.2\.1 构造方法](#321-%E6%9E%84%E9%80%A0%E6%96%B9%E6%B3%95)
            * [3\.2\.2 基本方法](#322-%E5%9F%BA%E6%9C%AC%E6%96%B9%E6%B3%95)
    * [4 StringBuffer与StringBuilder](#4-stringbuffer%E4%B8%8Estringbuilder)
        * [4\.1 源码简单分析](#41-%E6%BA%90%E7%A0%81%E7%AE%80%E5%8D%95%E5%88%86%E6%9E%90)
            * [4\.1\.1 继承关系](#411-%E7%BB%A7%E6%89%BF%E5%85%B3%E7%B3%BB)
            * [4\.1\.2 append方法](#412-append%E6%96%B9%E6%B3%95)
        * [4\.2 提升字符串处理性能<a href="%E8%BF%99%E4%B8%80%E9%83%A8%E5%88%86%E4%B8%BB%E8%A6%81%E5%8F%82%E8%80%83%E3%80%8AJava%E7%BC%96%E7%A8%8B%E6%80%9D%E6%83%B3%E3%80%8B%E7%AC%AC%E5%9B%9B%E7%89%88%E7%AC%AC13%E7%AB%A0%E4%B8%AD%E7%9A%84%E8%AE%B2%E8%A7%A3">^Java编程思想4th</a>](#42-%E6%8F%90%E5%8D%87%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%A4%84%E7%90%86%E6%80%A7%E8%83%BDjava%E7%BC%96%E7%A8%8B%E6%80%9D%E6%83%B34th)
            * [4\.2\.1 javap的使用](#421-javap%E7%9A%84%E4%BD%BF%E7%94%A8)
            * [4\.2\.2 重载运算符“\+”的底层调用](#422-%E9%87%8D%E8%BD%BD%E8%BF%90%E7%AE%97%E7%AC%A6%E7%9A%84%E5%BA%95%E5%B1%82%E8%B0%83%E7%94%A8)
                * [自动优化的性能问题](#%E8%87%AA%E5%8A%A8%E4%BC%98%E5%8C%96%E7%9A%84%E6%80%A7%E8%83%BD%E9%97%AE%E9%A2%98)
                * [通过StringBuilder提升性能](#%E9%80%9A%E8%BF%87stringbuilder%E6%8F%90%E5%8D%87%E6%80%A7%E8%83%BD)
                * [性能对比](#%E6%80%A7%E8%83%BD%E5%AF%B9%E6%AF%94)
    * [5 小结](#5-%E5%B0%8F%E7%BB%93)


## 1 前言

这组文档写到第六篇，每一篇的内容都离不开**字符串处理**，最起码每一篇中都包括`System.out.println()`语句（输出一个字符串），而这个输出的过程又隐含着一步调用`toString()`方法。字符串不是却胜似基本数据类型，是程序设计中绕不开的基本话题，这一篇就对Java中的字符串处理相关知识做一个小总结。

## 2 不可变的字符串

Java标准类库中使用String类描述字符串及其基本操作，对String类必须要有的一个基础认知，那就是它的定义使用了final进行修饰：
```java
public final class String {
    /** The value is used for character storage. */
    private final char value[]; //字符串本质上是char数组
    //……
}
```
这意味着在Java中实例化的每一个字符串都是“最终的”，不可改变的。看下面的例子：  
*此处用到了`System.identityHashCode(Obj)`，它返回的是Obj对象的标识哈希码（identity hash code）（一个对象在其生命周期中标识哈希码是不变的）*。
```java
class HaClass {
    public String name;
}
public class AboutString {
    public static void main(String[] args) {
        HaClass haClass = new HaClass();
        haClass.name = "hh";
        System.out.println(haClass.name + System.identityHashCode(haClass));
        haClass.name = "he";
        System.out.println(haClass.name + System.identityHashCode(haClass));

        String string = "你好";
        System.out.println(string + System.identityHashCode(string));
        string = "不好";
        System.out.println(string + System.identityHashCode(string));
    }
    /**
     * hh685325104
     * he685325104
     * 你好460141958
     * 不好1163157884
     */
}
```
可以看到更改自定义类haClass的属性，其标识哈希码并没有改变，这个对象还是最开始在内存中申请的那块地址上的那个对象，但是将string对象“的属性”改变之后，其哈希码改变了，“不好”对应的对象已经不是原来“你好”对应的那个对象，`string = "不好";`这句代码相当于new了一个新的“不好”对象，并将string这个引用指向到新对象上。

**Note：String类被final修饰，一个String对象是不可被改变的，所有看起来改变了String对象的操作实际是生成了一个新对象。**

### 2.1 为何让字符串不可变

每次都新开辟内存重新创建一个对象，无论怎么想这都要比在原有基础上修改付出更多的系统开销，那么将String类设计为final型的目的何在呢？这当然得有一个很具说服力的理由才行，先看例子：
```java
public static void main(String[] args) {
    String string1 = "你好";
    System.out.println(string1 + System.identityHashCode(string1));
    String string2 = "你好";
    System.out.println(string2 + System.identityHashCode(string2));
}
/**
 * 你好685325104
 * 你好685325104
 */
```
可以看到尽管string1与string2是分别定义并赋值的，却指向了同一个“你好”，这是Java为字符串提供的一种“共享”机制，Java在编译阶段会将字符串文字放到一个文字池(pool of literal strings)中，运行时这个文字池会成为常量池的一部分，执行`String string1 = "你好";`这句代码时，系统会先在常量池中查找“你好”这个字符串（对象），如果有就直接返回，没有才创建新的。在存在大量字符串操作的情况下，这种共享机制效果显著。

>Java的设计者认为共享带来的高效率远远胜过于提取、拼接字符串所带来的低效率。[^Java核心技术卷Ⅰ]

当然也不要想当然的理解这种共享机制：
```java
public static void main(String[] args) {
    String string1 = "你好";
    System.out.println(string1 + System.identityHashCode(string1));
    String string2 = new String("你好");
    System.out.println(string2 + System.identityHashCode(string2));

    Scanner in = new Scanner(System.in);
    String inputString;
    inputString = in.next();//此处输出： 你好
    in.close();
    System.out.println(inputString + System.identityHashCode(inputString));

    HaClass haClass = new HaClass();
    haClass.name = "你好";
    System.out.println(haClass.name + System.identityHashCode(haClass));
}
/**
 * 你好685325104
 * 你好460141958
 * 你好
 * 你好692404036
 * 你好1554874502
 */
```
*依这组文档的初衷，文中基本上不谈底层只讲应用，这里就不展开探究了，对共享机制有个印象即可，底层的事情等我们关注底层的时候再说。*


[^Java核心技术卷Ⅰ]:《Java核心技术》-卷Ⅰ-第三章3.6.3

## 3 String类概览

熟悉某个类还是看文档加实践比较快捷，这里概览的目的是通过回顾巩固印象。

### 3.1 属性
```java
//这段代码节选自String类
public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence {
    /** The value is used for character storage. */
    private final char value[];//以字符数组的形式存储字符串
 
    /** The offset is the first index of the storage that is used. */
    private final int offset;//索引偏移量
 
    /** The count is the number of characters in the String. */
    private final int count;//字符个数
 
    /** Cache the hash code for the string */
    private int hash; //哈希值
}
```
#### offset
索引偏移量理解一下：构造器中有一个`String​(char[] value, int offset, int count)`，假如传过去一个字符数组“[a,b,c,d,e]”，指定offset为2，count为3，那么得到的字符串就是“cde”。
```java
    public static void main(String[] args) {
        char[] x = {'a','b','c','d','e'};
        String string = new String(x,2,3);
        System.out.println(string);//cde
    }
```
这就是偏移量的意义。

#### String中无length属性
length很常用了，但String类中并没有一个length属性，而是有一个名为length的方法，方法返回的是value的长度：
```java
/**
 * Returns the length of this string.
 * The length is equal to the number of <a href="Character.html#unicode">Unicode
 * code units</a> in the string.
 *
 * @return  the length of the sequence of characters represented by this
 *          object.
 */
public int length() {
    return value.length;
}
```

### 3.2 方法

字符串操作太过常见，String类提供了大量方法，大概数了一下有80多个（重载形式也算上了），这些方法多数都很常用（或者说都很有用）。

#### 3.2.1 构造方法

除了前面用到的直接通过等号赋常量法，String类还提供了十多种（Java SE 13中有16种）构造方法，可以通过各种参数新建String对象，大概看一看：

1. String​(String original)：用字符串初始化字符串，其实作用相当于等号赋值，不过都调用构造器了，说明生成了新的对象，与等号赋值还是有差别的。
```java
    String aa = "abcde";
    System.out.println(aa);//abcde
```
2. String​(char[] value)：通过字符数组初始化。
```java
    char[] x = {'a','b','c','d','e'};
    String bb = new String(x);
    System.out.println(bb);//abcde
```
3. String​(char[] value, int offset, int count)：通过字符数组的一部分初始化。
```java
    char[] x = {'a','b','c','d','e'};
    String cc = new String(x,2,3);
    System.out.println(cc);//cde
```
4. public String​(byte[] bytes)：通过解码byte数组生成字符串(使用平台默认的编码方式)。
```java
    byte[] xx = {88,89,90};
    String xxx = new String(xx);
    System.out.println(xxx);//XYZ
```
5. 一大堆使用不同参数的4的衍生版本。
6. String​(int[] codePoints, int offset, int count)：通过unicode数组初始化。
```java
    int[] unicode = {0x5b98,0x4eba,0x5b98,0x4eba,0x4e0d,0x5fc5,0x5fe7,0x5728,0x5fc3};
    String ee = new String(unicode,0,unicode.length);
    System.out.println(ee);//官人官人不必忧在心
```
7. String​(StringBuffer buffer)与String​(StringBuilder builder) 一会详解

#### 3.2.2 基本方法

这里的基本方法指的是特别常用的那种。

1. char charAt​(int index):  返回索引处的字符
2. int codePointAt​(int index)： 返回索引处的Unicode编码（int类型的）
3. int compareTo​(String anotherString): 按词典顺序比较两个字符串
4. String concat​(String str)： 追加字符串
5. boolean contains​(CharSequence s)： 检查是否包含某个字符
6. boolean equals​(Object anObject)： 比较两个字符串是否相同，注意equals与`==`的差别
```java
    String ss = "你好";
    String sss = "你好";
    String ssss = new String("你好");
    System.out.println(ss.equals(sss));
    System.out.println(ss==sss);
    System.out.println(ss.equals(ssss));
    System.out.println(ss==ssss);
    /**
     + true
     + true
     + true
     + false
     */    
```
7. boolean equalsIgnoreCase​(String anotherString)：忽略大小写进行比较
8. boolean endsWith​(String suffix)：是否已某后缀结束，对应还有startsWith
```java
    String qq = "abcdeee";
    System.out.println(qq.endsWith("eee"));//true
```
9. byte[] getBytes()：将String转为byte数组
```java
    String qq = "abcdeee";
    byte[] qqq = qq.getBytes();
    System.out.println(qqq[0]);//97
```
10. int hashCode(): 字符串的哈希值，注意是字符串的不是字符串对象的
```java
    String ff = "hello world";
    String fff = new String("hello world");
    System.out.println("hashCode -- ff: " + ff.hashCode() + " fff: " + fff.hashCode());
    System.out.println("identityHashCode -- ff: " + System.identityHashCode(ff) + " fff: " + System.identityHashCode(fff));
    /**
     + hashCode -- ff: 1794106052 fff: 1794106052
     + identityHashCode -- ff: 685325104 fff: 460141958
     */
```
11. int indexOf​​(String str): 返回字符串中指定子字符串的索引开始位置，参数有其他重载形式，lastIndexOf​是从后往前搜索
```java
    String gg = "abbcccdddd";
    System.out.println(gg.indexOf("bc"));//2
```
12. String replace​(char oldChar, char newChar)：替换串中的字符
```java
    String gg = "abbcccdddd";
    System.out.println(gg.replace('c','f'));//abbfffdddd
```
13. String substring​(int beginIndex, int endIndex)： 提取子字符串，endIndex可缺省
```java
    String gg = "abbcccdddd";
    System.out.println(gg.substring(2));//bcccdddd
    System.out.println(gg.substring(3,7));//cccd
```
14. String trim()：移除首尾空白字符(空格、tab键、换行符)，判断标准为是否小于等于Unicode空格字符(U+0020)
15. String strip()： 移除首尾空格，判断标准为是否为Unicode中的空白字符，since11  
*java早期就有trim函数，当时Unicode还没发展出今天这样的标准，如今Unicode中有专门给空白字符分配的编码，比如'\u2000'就是其中一个，trim却识别不了，JavaSE11之后提供了strip方法，填了这个坑*
```java
    String kk = " abc  de";
    System.out.println(kk);
    System.out.println(kk.trim());
    kk = '\u2000' + kk;
    System.out.println(kk.trim());
    /**
     +  abc  de
     + abc  de
     +   abc  de
     */   
```

String类中的方法还有不少，就先看这么多吧。


## 4 StringBuffer与StringBuilder

前面说过了，String类的实例对象是不可变的，每次对其进行操作都会产生新的对象，尽管共享机制为其弥补了一部分因过多的中间对象造成的开销，有时候我们还是希望能够更高效的执行这个过程，尤其是在有非常多的字符串修改操作的情况下，这时候就可以用到StringBuffer或StringBuilder这两个类，简单来说，他们是允许修改其对象的另一种形式的String类。

StringBuffer与StringBuilder功能基本相同，其中StringBuilder是在JavaSE5引入的，两者最大的差别在于，StringBuffer线程安全，后者线程不安全。性能上，由于StringBuffer为保证线程安全，开销要大一些，在普通场景下，使用StringBuilder即可。

实践之前先看看它们的源码。

### 4.1 源码简单分析

这里有个小问题先讲一下，从API文档中看，无论是StringBuffer还是StringBuilder，都是直接继承自java.lang.Object类，但是从JDK的源码中看，会发现中间还有一个AbstractStringBuilder类，这个AbstractStringBuilder类还挺重要的，不知道为何API文档中没有体现，SE8还有SE13都是这个情况，以下以JDK中的代码为准。

#### 4.1.1 继承关系
以下截取自**JDK13**中的源码：
```java
abstract class AbstractStringBuilder implements Appendable, CharSequence {
    /**
     * The value is used for character storage.
     * 使用byte[]储存字符，Jdk9之前用的是char数组
     */
    byte[] value;

    /**
     * The id of the encoding used to encode the bytes in {@code value}.
     * 编码值
     */
    byte coder;
    //...
}
public final class StringBuilder
    extends AbstractStringBuilder
    implements java.io.Serializable, Comparable<StringBuilder>, CharSequence
{
    //...
}
 public final class StringBuffer
    extends AbstractStringBuilder
    implements java.io.Serializable, Comparable<StringBuffer>, CharSequence
{
    //...
}
```
可以看到在AbstractStringBuilder中使用了可变的数组（而不像String类中使用final修饰）储存字符串序列，所以说它（们）是可变形式的字符串类。

#### 4.1.2 append方法

基本的API这里就不赘述了，AbstractStringBuilder中对字符串的操作方法很完善，增删改查均可很方便的实现，这里重点说一下append方法，append意为增补、追加，它有相当多的重载形式，从而可以以不同的参数、位置向某一个StringBuilder或StringBuffer中追加字符，如下是最基本的使用方式，稍后用这个来测试字符串操作的性能问题。
```java
public void testStringBuilder(){
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append("hello vilaseaka~");
    System.out.println(stringBuilder);//hello vilaseaka~
}
```

### 4.2 提升字符串处理性能[^Java编程思想4th]

稍微涉及一点底层，把字符串处理这方面的问题分析的更深入一些，这里先熟悉一下javap的使用，借助它来看看字符串操作的底层实现。

[^Java编程思想4th]:这一部分主要参考《Java编程思想》第四版第13章中的讲解

#### 4.2.1 javap的使用

最开始学Java的时候都用javac命令编译过.java文件，也用java命令运行过通过javac命令编译生成的.class字节码文件，javac、java都是JDK提供的工具，位于JDK的bin目录下，这个javap也一样，其功能是反向解析.class字节码文件，输出java底层的汇编指令、变量表等内容，通过javap我们能看到Java底层是怎么处理我们编写的代码的。

javap的命令格式：`javap <options> <classes>`，参数如下
```shell
PS C:\Users\Administrator> javap
用法: javap <options> <classes>
其中, 可能的选项包括:
  -help  --help  -?        输出此用法消息
  -version                 版本信息
  -v  -verbose             输出附加信息
  -l                       输出行号和本地变量表
  -public                  仅显示公共类和成员
  -protected               显示受保护的/公共类和成员
  -package                 显示程序包/受保护的/公共类
                           和成员 (默认)
  -p  -private             显示所有类和成员
  -c                       对代码进行反汇编
  -s                       输出内部类型签名
  -sysinfo                 显示正在处理的类的
                           系统信息 (路径, 大小, 日期, MD5 散列)
  -constants               显示最终常量
  -classpath <path>        指定查找用户类文件的位置
  -cp <path>               指定查找用户类文件的位置
  -bootclasspath <path>    覆盖引导类文件的位置
```

简单使用一下（这里用的是JDK8的javap），以上面用过的代码新建了一个TestJavap.java内容如下：
```java
//TestJavap.java
public class TestJavap {
    public static void main(String[] args) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("hello vilaseaka~");
        System.out.println(stringBuilder);  
    }
}
```
使用javap -c 对字节码进行反汇编：
```shell
PS C:\Users\Administrator\Desktop> javac TestJavap.java
PS C:\Users\Administrator\Desktop> java TestJavap
hello vilaseaka~
PS C:\Users\Administrator\Desktop> javap -c TestJavap
Compiled from "TestJavap.java"
public class TestJavap {
  public TestJavap();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: new           #2                  // class java/lang/StringBuilder
       3: dup
       4: invokespecial #3                  // Method java/lang/StringBuilder."<init>":()V
       7: astore_1
       8: aload_1
       9: ldc           #4                  // String hello vilaseaka~
      11: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
      14: pop
      15: getstatic     #6                  // Field java/lang/System.out:Ljava/io/PrintStream;
      18: aload_1
      19: invokevirtual #7                  // Method java/io/PrintStream.println:(Ljava/lang/Object;)V
      22: return
}
```
可以看到javap提供了很清楚的注释，由于源代码非常简单，汇编指令也是顺序执行，在第11行调用了一次StringBuilder.append，19行输出完毕就结束了。这就是javap的简单实用，汇编代码先不管，看注释理解方法的调用过程就好。

#### 4.2.2 重载运算符“+”的底层调用

Java中不允许开发者自己重载运算符，但是有两个被官方重载了的运算符，那就是“+”与“+=”，使用这俩运算符可以直接进行字符串拼接操作：
```java
    String ss = "官人官人不必忧在心";
    ss += "，听为妻为你说分明";
    System.out.println(ss);//官人官人不必忧在心，听为妻为你说分明
```
我们使用javap看一下这个被重载的运算符底层是怎么实现的：
```java
//Windows下使用记事本编写，采用GBK编码
public class Test {
    public static void main(String[] args) {
        String ss = "官人官人不必忧在心";
        ss += "，听为妻为你说分明";
        System.out.println(ss);
    }
}
```
```shell
PS C:\Users\Administrator\Desktop> javac Test.java
PS C:\Users\Administrator\Desktop> java Test
官人官人不必忧在心，听为妻为你说分明
PS C:\Users\Administrator\Desktop> javap -c Test
Compiled from "Test.java"
public class Test {
  public Test();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: ldc           #2                  // String 官人官人不必忧在心
       2: astore_1
       3: new           #3                  // class java/lang/StringBuilder
       6: dup
       7: invokespecial #4                  // Method java/lang/StringBuilder."<init>":()V
      10: aload_1
      11: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
      14: ldc           #6                  // String ，听为妻为你说分明
      16: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
      19: invokevirtual #7                  // Method java/lang/StringBuilder.toString:()Ljava/lang/String;
      22: astore_1
      23: getstatic     #8                  // Field java/lang/System.out:Ljava/io/PrintStream;
      26: aload_1
      27: invokevirtual #9                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
      30: return
}
```
可以看到第三行代码，new了一个StringBuilder，之后就一个道理了，通过StringBuilder进行字符串拼接，所以说，通过“+”与“+=”这两个重载运算符拼接字符串的时候，本质上还是通过StringBuilder进行的。

那么既然编译器为我们自动调用了StringBuilder了，意味着没有产生过多的无用的中间对象，为什么还要手动构建StringBuilder进行字符串操作呢？

##### 自动优化的性能问题
看下面这个例子：
```java
//Test.java
public class Test {
    public static void main(String[] args) {
        String ss = "vilaseaka+++";
        for (int i=0;i<10;i++){
            ss+=i;
        }
        System.out.println(ss);
    }
}
```
```shell
PS C:\Users\Administrator\Desktop> javac Test.java
PS C:\Users\Administrator\Desktop> java Test
vilaseaka+++0123456789
PS C:\Users\Administrator\Desktop> javap -c Test
Compiled from "Test.java"
public class Test {
  public Test();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: ldc           #2                  // String vilaseaka+++
       2: astore_1
       3: iconst_0
       4: istore_2
       5: iload_2
       6: bipush        10
       8: if_icmpge     36
      11: new           #3                  // class java/lang/StringBuilder
      14: dup
      15: invokespecial #4                  // Method java/lang/StringBuilder."<init>":()V
      18: aload_1
      19: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
      22: iload_2
      23: invokevirtual #6                  // Method java/lang/StringBuilder.append:(I)Ljava/lang/StringBuilder;
      26: invokevirtual #7                  // Method java/lang/StringBuilder.toString:()Ljava/lang/String;
      29: astore_1
      30: iinc          2, 1
      33: goto          5
      36: getstatic     #8                  // Field java/lang/System.out:Ljava/io/PrintStream;
      39: aload_1
      40: invokevirtual #9                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
      43: return
}
```
可以看到第33行有个goto5，也就是说第5行与第33行之间产生了一个循环，每一次循环的过程都新建了一个StringBuilder对象用来向上一次循环的结果中追加字符，这不就是之前所说的，产生了大量无用的中间对象么。

##### 通过StringBuilder提升性能

继上文，在有大量字符串修改操作的情况下，靠编译器自动调用StringBuilder会产生很多无用的中间对象，徒增系统开销，不如我们手动新建一个StringBuilder（或StringBuffer），然后利用其append方法动态追加字符，那么就不用像编译器的默认处理方式那样在每一层循环中新建对象了，看例子：
```java
public class Test {
    public static void main(String[] args) {
        StringBuilder sss = new StringBuilder("vilaseaka+++");
        for (int i=0;i<10;i++){
            sss.append(i);
        }
        System.out.println(sss);
    }
}
```
```shell
PS C:\Users\Administrator\Desktop> javac Test.java
PS C:\Users\Administrator\Desktop> java Test
vilaseaka+++0123456789
PS C:\Users\Administrator\Desktop> javap -c Test
Compiled from "Test.java"
public class Test {
  public Test();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: new           #2                  // class java/lang/StringBuilder
       3: dup
       4: ldc           #3                  // String vilaseaka+++
       6: invokespecial #4                  // Method java/lang/StringBuilder."<init>":(Ljava/lang/String;)V
       9: astore_1
      10: iconst_0
      11: istore_2
      12: iload_2
      13: bipush        10
      15: if_icmpge     30
      18: aload_1
      19: iload_2
      20: invokevirtual #5                  // Method java/lang/StringBuilder.append:(I)Ljava/lang/StringBuilder;
      23: pop
      24: iinc          2, 1
      27: goto          12
      30: getstatic     #6                  // Field java/lang/System.out:Ljava/io/PrintStream;
      33: aload_1
      34: invokevirtual #7                  // Method java/io/PrintStream.println:(Ljava/lang/Object;)V
      37: return
}
```
可以看到，由于StringBuilder是手动创建的，这次第12行到27行的循环体之中，只有调用StringBuilder.append的代码，也就是说整个10次的字符串修改操作只借助一个中间对象就完成了。

##### 性能对比
```java
package com.vilaseaka.main;
public class Test {
    public void m1(){
        String ss = "vilaseaka+++";
        long startTime=System.currentTimeMillis();
        for (int i=0;i<10000;i++){
            ss+=i;
        }
//        System.out.println(ss);
        long endTime=System.currentTimeMillis(); //获取结束时间
        System.out.println("M1运行时间：" + ( endTime - startTime ) + "ms");
    }
    public void m2(){
        StringBuilder sss = new StringBuilder("vilaseaka+++");
        long startTime2=System.currentTimeMillis();
        for (int i=0;i<10000;i++){
            sss.append(i);
        }
//        System.out.println(sss);
        long endTime2=System.currentTimeMillis(); //获取结束时间
        System.out.println("M2运行时间：" + ( endTime2 - startTime2 ) + "ms");
    }
    public static void main(String[] args) {
        Test test = new Test();
        test.m1();
        test.m2();
    }
    /**
     * M1运行时间：146ms
     * M2运行时间：5ms
     */
}
```
循环操作一万次的情况下时间相差几十倍，虽然这里输出的测试时间并不是特别严谨，但也足以窥见两种方式的性能差距了。

## 5 小结

这一篇文档首先对String类的final属性进行了探究，之后对其属性、方法进行了基本的回顾与实践，后半篇重点分析了字符串拼接操作的底层实现，并通过StringBuilder进行了性能优化，未对StringBuffer进行过多描述，其使用与StringBuilder基本一致。