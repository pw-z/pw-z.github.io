# JAVA基础知识复盘（三）：访问权限控制与特征修饰
*2020032301-java-basic-knowledge-review-3-access-control-and-feature-modifier*  
*Posted on 2020.03.24 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  

* [JAVA基础知识复盘（三）：访问权限控制与特征修饰](#java%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E5%A4%8D%E7%9B%98%E4%B8%89%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90%E6%8E%A7%E5%88%B6%E4%B8%8E%E7%89%B9%E5%BE%81%E4%BF%AE%E9%A5%B0)
    * [1 前言](#1-%E5%89%8D%E8%A8%80)
    * [2 访问权限控制](#2-%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90%E6%8E%A7%E5%88%B6)
        * [2\.1 从作用域到命名空间](#21-%E4%BB%8E%E4%BD%9C%E7%94%A8%E5%9F%9F%E5%88%B0%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4)
        * [2\.2 成员的访问权限](#22-%E6%88%90%E5%91%98%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90)
            * [2\.2\.1 概览](#221-%E6%A6%82%E8%A7%88)
            * [2\.2\.2 关于protected的实践](#222-%E5%85%B3%E4%BA%8Eprotected%E7%9A%84%E5%AE%9E%E8%B7%B5)
            * [2\.2\.3 小结](#223-%E5%B0%8F%E7%BB%93)
        * [2\.3 类的访问权限](#23-%E7%B1%BB%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90)
    * [3 特征修饰](#3-%E7%89%B9%E5%BE%81%E4%BF%AE%E9%A5%B0)
        * [3\.1 概览](#31-%E6%A6%82%E8%A7%88)
        * [3\.2 详解](#32-%E8%AF%A6%E8%A7%A3)
            * [3\.2\.1 STATIC](#321-static)
                * [类的初始化顺序](#%E7%B1%BB%E7%9A%84%E5%88%9D%E5%A7%8B%E5%8C%96%E9%A1%BA%E5%BA%8F)
            * [3\.2\.3 FINAL](#323-final)
                * [final属性](#final%E5%B1%9E%E6%80%A7)
                    * [空白final \- 运行后赋值](#%E7%A9%BA%E7%99%BDfinal---%E8%BF%90%E8%A1%8C%E5%90%8E%E8%B5%8B%E5%80%BC)
                * [final方法](#final%E6%96%B9%E6%B3%95)
                * [final类](#final%E7%B1%BB)
                * [final参数](#final%E5%8F%82%E6%95%B0)
            * [3\.2\.4 ABSTRACT与INTERFACE](#324-abstract%E4%B8%8Einterface)
            * [3\.2\.5 SYNCHRONIZED与VOLATILE](#325-synchronized%E4%B8%8Evolatile)
            * [3\.2\.6 \*TRANSIENT](#326-transient)
            * [3\.2\.7 \*NATIVE](#327-native)
            * [3\.2\.8 \*STRICTFP](#328-strictfp)
    * [4 声明顺序规范](#4-%E5%A3%B0%E6%98%8E%E9%A1%BA%E5%BA%8F%E8%A7%84%E8%8C%83)


## 1 前言

Java提供了一组**修饰符（Modifier）**关键字，可置于类名、属性或方法前面起到修饰作用，本文主要是关于这些修饰符的总结，标题为了更好的概括两个子话题稍微绕了些。

在【java.lang.reflect.Modifier】这个类中能直观地看到所有修饰符*（大写字母）*：
```java
    - public static final int PUBLIC  = 0x00000001;      //公共的
    - public static final int PRIVATE  = 0x00000002;     //私有的
    - public static final int PROTECTED  = 0x00000004;   //受保护的
    - public static final int STATIC  = 0x00000008;      //静态的
    - public static final int FINAL  = 0x00000010;       //最终的
    - public static final int SYNCHRONIZED  = 0x00000020;//同步的
    - public static final int VOLATILE  = 0x00000040;    //易变的
    - public static final int TRANSIENT  = 0x00000080;   //短暂的
    - public static final int NATIVE  = 0x00000100;      //本地的
    - public static final int INTERFACE  = 0x00000200;   //接口
    - public static final int ABSTRACT  = 0x00000400;    //抽象的
    - public static final int STRICT  = 0x00000800;      //strictfp  精确的浮点
```
官方似乎没有给这些修饰符分什么类别，本文姑且将public、private、protected分为一组，称为访问权限控制修饰符，将其它的分为一组，称为特征修饰符，对应标题中的两个话题。

*Abstract（抽象的）与Interface（接口）、SYNCHRONIZED（同步的）与VOLATILE（易变的）另作主题细讲，本文中一笔带过。*

## 2 访问权限控制

面向对象程序设计中有一条经典的设计原则，“对接口编程，而不是对实现编程”，这是在说多态的解耦合思想，由于父类的通用设计使我们不必关注子类的具体实现。类似的思想应用在如下的问题场景下：如何在改动某些代码时不必担心代码调用处会因为改动而出问题？答案便是访问权限控制，通过访问权限控制修饰符，为代码调用者提供公开的通用的接口，同时**隐藏具体的实现**，这相当于制造了一个黑盒子，功能给出来了你随便用，我升级更新的时候只要保证公开的接口没有改动，就不会影响你。

以最低的权限给出调用者需要的，剩下的都隐藏起来，防止调用者访问到不该访问的内容，同时也方便开发者更省心地作出改动，而不必担心对调用者造成影响，这就是访问权限控制的意义所在。

### 2.1 从作用域到命名空间

刚刚接触编程的时候老师没少强调过要尽量减少全局变量的使用，过多的全局变量很容易引起混乱。全局变量亦或是局部变量，说的是变量的作用域问题。Java中的作用域与C或C++一样，由花括号决定，不同的地方在于，Java中嵌套的花括号属于一个域：
```java
public void aboutScope(){
    {//作用域1的开始位置
        int x;
        {
            for (int x=0;x<1;++x); //报错:Variable 'x' is already defined in the scope
        }
    }//作用域1的结束位置

    {//作用域2的开始位置
        int x;//与1中重名的变量可以正常定义，作用域不同
        {
            int x;//报错:Variable 'x' is already defined in the scope
        }
    }//作用域2的结束位置
}
```
不同的作用域中可以有相同的变量名，那么两个人写出了重名的类、重名的方法怎么办，如何识别调用的具体是哪一个？Java提供了命名空间来解决这个问题。

Java的命名空间以包（package）作为组织单元，每个package都是一个独立的命名空间。包的命名规范是作者域名倒写，如域名为vilaseaka.github.io，则包名为io.github.vilaseaka，域名的独一无二性保证了包名的独一无二。若想在类中引入某个包，需要用到**import**关键字。
```java
import java.io.File;
```
在程序执行时，一个包对应的命名空间本质上是一条独一无二的系统路径，Java程序在加载某一个包的时候，首先会找到系统中的环境变量，在环境变量的路径下找被调用的包（中的类）

本机(Windows系统)当前环境变量中的Java路径为`C:\D\Program\JDK8_64`，当调用`java.io.File`这个包的时候，实际的加载路径是`C:\D\Program\JDK8_64\src.zip!\java\io\File.java`

在不import的情况下可以直接写包名来调用其下的类，这也可以解决引入的包中重复命名的问题。
```java
    java.io.File file = new java.io.File("/");
```
等同于
```java
import java.io.File;
...
File file = new File("/");
```

有了命名空间之后，可以来看看public、private、protected这三个修饰符了。

### 2.2 成员的访问权限

#### 2.2.1 概览

相对于修饰类，访问修饰符更普通的使用场景是用在类的成员（属性、方法）前面:
```java
class AboutModifiers {
    public int hp;
    private int lucky;
    protected int star;
    public void accessControl(){ }
}
```

* 无修饰符(default)：包访问权限
    - 没有任何修饰符的成员将获得一种默认的访问权限，称为**包访问权限**，意味着同一包下的其他类都可以访问这个成员，而对于包外的类，这个成员是隐藏的（private）。
    - 若两个类文件中都没有声明包，且这两个文件处于同一路径下，那么这两个类会被认为是同一个包下的，即**默认包**。
* public:接口访问权限
    - public即公开的，它所修饰的成员可以被所有人访问，故称之为接口访问权限。
* private：被隐藏的内容
    - private修饰的成员只有此类中的其他成员可以访问，同一包下面的其他类都访问不到。
* protected：继承访问权限
    - 矛：若父类子类不在同一个包下，那么父类中的私有成员子类即使继承了也访问不了
    - 盾：若将父类中的成员设置成public那除了子类其他类也都可以访问了
    - protected修饰符实现了**子类可访问但其他类不可访问**，解决了上述矛盾  

#### 2.2.2 关于protected的实践

【protected修饰符实现了**子类可访问但其他类不可访问**】这句话还得好好理解一下，看如下代码注释中的问题：
```java
//第一个包
package com.vilaseaka.main;
public class AboutModifiers {
    public int hp;
    private int lucky;
    protected int star;
    public void accessControl(){ }
}

//第二个包
package com.vilaseaka.newbranch;
import com.vilaseaka.main.AboutModifiers;
//不同包非子类
public class NotChild {
    public static void main(String[] args) {
        Child child = new Child();
        System.out.println(child.star);//！ 此处能成功调用吗？
    }
}
//不同包子类
class Child extends AboutModifiers{}
```
答案是不能。第二个包中的NotChild类不是AboutModifiers类的子类，虽然child是AboutModifiers的子类对象，但因为是在NotChild类*（不同包非子类）*中实例化的对象，所以没有对父类中受保护的属性`protected int star`的访问权限。如下代码才可行：
```java
//不同包子类
class Child extends AboutModifiers{
    public static void main(String[] args) {
        Child child = new Child();
        System.out.println(child.star);
    }
}
```

#### 2.2.3 小结

|       | 同一类内   | 同包不同类| 不同包子类  | 不同包非子类|
|:-----:|:----------:|:-------:|:-----------:|:---------:|
|public |      1     |    1    |      1      |     1     |
|protected|    1     |    1    |      1      |           |
|default |     1     |    1    |             |           |
|private |     1     |         |             |           |


### 2.3 类的访问权限

类的前面也可加访问修饰符，但只能加public（内部类特殊，此处不讨论）。一个编译单元（一份.java文件）中只能有一个Public类，并且这个类需要与文件名完全一致，其余的类都处于包访问权限下（即无访问修饰符）。

## 3 特征修饰

### 3.1 概览

排除掉一个Interface修饰符，以下八个是接下来要讲的：

    STATIC        //静态的
    FINAL         //最终的
    ABSTRACT      //抽象的
    SYNCHRONIZED  //同步的
    VOLATILE      //易变的
    TRANSIENT     //短暂的
    NATIVE        //本地的
    STRICT        //strictfp  精确的浮点

### 3.2 详解

#### 3.2.1 STATIC

被static修饰的属性或方法称为静态属性或静态方法，叫静态成员好了，静态成员是属于一个类的，普通的属性与方法只有在实例化对象中才可以调用，但静态的不需要实例化便可以调用。
```java
class A{
    //静态属性：直接通过类即可调用
    public static int property1;
    //实例属性： 实例化之后才能调用
    private int property2;
    //静态域
    static {
        System.out.println("A的静态域中的输出语句输出了这句话");
    }
    //静态方法
    public static void talk(){
        System.out.println("A的静态方法：talk（）");
    }
}

public static void main(String[] args) {
    A.talk();
    A a = new A();
    /**output
     * 静态域中的输出语句输出了这句话
     * 静态方法：talk（）
     */
}
```
明明是先调用了A.talk方法，为什么先输出了静态域中的语句呢？这涉及到一个额外知识点，加载顺序。

##### 类的初始化顺序

一个类的生命周期分为**加载、连接、初始化、使用、和卸载**五个阶段，加载简单理解就是把类放到虚拟机中准备被调用，连接阶段会为静态变量分配内存并赋默认值，初始化则是在类被直接引用（实例化对象、使用类的静态属性、调用类的静态方法等）时进行的。加载与连接有可能交叉进行。

先考虑没有继承的情况。当使用A.talk()调用talk方法的时候，首先要往虚拟机中加载A这个类，加载与连接的过程调用了静态域的内容，输出了那句话，然后才是调用A.talk()，产生了直接引用，触发了类的初始化，此时类的初始化过程就是按顺序自上而下调用类中的静态语句（静态赋值语句、静态域）且这个过程只在类第一次加载的时候执行一次，之后再调用类或者实例化类时，静态内容始终是第一次初始化的那个。
```java
    A.talk();
    A a = new A();
    A aa = new A();
    /**
     * A的静态域中的输出语句输出了这句话
     * A的静态方法：talk（）
     */
```
可以看到，继A.talk()执行之后，实例化两个新对象都没有输出东西，因为静态内容已经在首次加载类的时候执行（初始化）完了，且之后都不用再执行（初始化）了。从这里可以更好的理解【类成员】的概念，一个类定义了一个static属性，那么不管通过这个类实例化了多少对象，所有的对象共享这一个static属性。

再看看有继承关系的情况：
```java
class A{
    A(){
        System.out.println("A的构造器");
    }

    private int  property1;
    public static int  property2;
    {
        System.out.println("A的普通域");
    }
    static {
        System.out.println("A的静态域");
    }
}

class B extends A{
    B(){
        System.out.println("B的构造器");
    }
    private int  property1;
    public static int  property2;
    {
        System.out.println("B的普通域");
    }
    static {
        System.out.println("B的静态域");
    }

}
public class AboutModifiers{
    public static void main(String[] args) {
        B b = new B();
        B bb = new B();
        /**
         * A的静态域
         * B的静态域
         * A的普通域
         * A的构造器
         * B的普通域
         * B的构造器
         * A的普通域
         * A的构造器
         * B的普通域
         * B的构造器
         */
    }
}
```
从结果可见静态内容的初始化优先级最高，且根据继承关系，先初始化父类中的静态内容，再初始化子类中的静态内容（有父才有子）。因为有实例化，可以看到非静态内容也开始初始化，同时构造器开始调用，并依旧遵从先父后子的顺序。new第二个对象bb时，静态内容没有再次执行。

总结，首次调用并且实例化一个类的过程中，内容的调用顺序：

1. 初始化之前
    1. 父类静态内容
    2. 子类静态内容
2. 初始化阶段
    1. 父类普通内容
    2. 父类构造器
    3. 子类普通内容
    4. 子类构造器

关于类的加载机制，还是得从底层分析才能透彻，此处有个大概理解即可。

#### 3.2.3 FINAL

*final关键字已经用过两次了，讲继承的时候，使用final关键字可以让类（或其成员）无法被继承，讲多态的时候，使用final可以停用动态绑定。*

与static一样，final可以用在类及其成员前面（以及方法的参数），意为最终的、无法改变的。

##### final属性

用final修饰的属性，一旦初始化之后就无法再改变。若想定义一个常量，可用final修饰基本数据类型（数组亦可）来实现；若用final修饰对象的引用，那么这个引用所指向的对象将固定不变。
```java
class AboutFinal{
    final double PI = 3.141592657;
    final String string = new String("这是一个final修饰的引用所指向的对象");
    public void test(){
        System.out.println(string);
    }
}
public class AboutModifiers {
    public static void main(String[] args) {
        AboutFinal af = new AboutFinal();
        af.test();//这是一个final修饰的引用所指向的对象
    }
}
```
###### 空白final - 运行后赋值
final属性必须得保证能被初始化，不然无法通过编译，但是final属性不一定非得在编译之前被初始化，可以通过构造器在运行时为final属性赋值，这种操作被称为生成一个“空白final”：
```java
class AboutFinal{
    final int x;
    AboutFinal(int x) {
        this.x = x;
    }
    public void test(){
        System.out.println(x);
    }
}
public class AboutModifiers {
    public static void main(String[] args) {
        AboutFinal af = new AboutFinal(12);
        af.test();//12
    }
}
```

final修饰属性时可以与static联合使用，得到的就是一个静态常量了：
```java
package com.vilaseaka.main;
class StaticFinal{ //包访问权限
    public static final double PI = 3.1415926; //静态常量
}
public class AboutModifiers { //公共接口
    public static void main(String[] args) {
        System.out.println(StaticFinal.PI);//3.1415926
    }
}
```

##### final方法

如今用final修饰一个方法的目的有且只有一个，防止这个方法被子类重写，上一篇文档回顾继承的时候讲过了，此处不再重复。

*老版本的Java环境中，final的另一个作用是提高效率，现已不再使用*


##### final类

final类与final方法一样，也在继承中讲过了，一个类若被final修饰，则无法被继承。

由于类无法被继承，final类中的方法也就没法被重写，所以final类中的方法即使没有用final修饰，实际上也是final的。

##### final参数

补充个知识点，final还可用来修饰参数，当用final修饰一个参数的时候，只可以读这个参数，不可以改：
```java
    public void soutNumberPlus1(final int x){
        //！System.out.println(++x);//final修饰的参数，不可改变
        System.out.println(1+x);
    }
```

#### 3.2.4 ABSTRACT与INTERFACE

Abstract与Interface这两个修饰符就其存在的意义而言，有很大相似性，但这俩又是完全不同的概念：抽象类是个类，接口只是接口。具体内容放在下一篇【抽象类与接口】中细讲。

#### 3.2.5 SYNCHRONIZED与VOLATILE

synchronized与volatile这两个修饰符主要用于并发场景，synchronized相当于提供了一个互斥锁，被synchronized标记的资源同时只能被一个线程访问，而volatile修饰符标记的资源值会实时刷新，即每个线程访问此资源时该资源都是最新的。具体内容放在【并发处理】中细讲。

#### 3.2.6 *TRANSIENT

不太常用的修饰符之transient（短暂的）。讲transient之前先稍微讲讲【序列化】。

序列化（Serialize）是Java I/O系统中的知识点，通过序列化机制可以将对象转换为字节序列，然后保存到磁盘上也好进行网络传输也好，回头可以通过反序列化机制重建对象。
```java
//可序列化对象
class Info implements Serializable{
    public String id;
    public String password;
    public Info(String id, String password) {
        this.id = id;
        this.password = password;
    }
}
//测试序列化过程
public class AboutModifiers {
    public static void main(String[] args) {
        try (//序列化
            ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("test.dat"))) {
            Info info = new Info("111","abc");
            oos.writeObject(info);
        } catch (Exception e) {
            e.printStackTrace();
        }
        try (//反序列化
            ObjectInputStream ois = new ObjectInputStream(new FileInputStream("test.dat"))) {
            Info info2 = (Info) ois.readObject();
            System.out.println("id = "+info2.id+" / pw = "+info2.password); 
            //id = 111 / pw = abc
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```
如上代码，通过序列化操作正常将对象存储、重建。讲到这里，transient关键字的作用也就好理解了，其修饰的属性，在序列化过程中会被忽略。
```java
    public transient String password;//用transient修饰的属性不被序列化
    System.out.println("id = "+info2.id+" / pw = "+info2.password); 
    //id = 111 / pw = null
```
transient关键字的使用场景在于，序列化过程中有些敏感信息不希望被外界接触到，即，让这些敏感信息只存在于内存中，而不经过外存（一个private数据序列化之后也就可以被访问了）。

#### 3.2.7 *NATIVE

不太常用的修饰符之native（本地的）。

native修饰符用于修饰方法，一个native方法相当于一个调用非Java代码的接口，即native方法的具体实现将由其它语言的代码完成。目前来讲，这个修饰符不是不太常用，是太不常用了，暂时有个概念即可。

参考阅读：

* [Java中Native关键字的作用 - 萌小Q - 博客园](https://www.cnblogs.com/Qian123/p/5702574.html)
* [java Native Method初涉 - J2ME - mobile - ITeye论坛](https://www.iteye.com/topic/72543)

#### 3.2.8 *STRICTFP

不太常用的修饰符之strictfp。 

strictfp即strict float point，精确的浮点数，这个修饰符也属于那种“太不常用”的，没有这次系统总结的话还真没注意过有这么个修饰符，中文社区详细讨论这个的少，直接看Wiki吧：
>Some hardware also provides extended precision formats that provide higher precision and/or a larger exponent range. On such architectures it may be more efficient to compute intermediate results using such extended formats. This may avoid round-off errors, overflows and underflows that would otherwise occur, but can cause programs to produce different output on such architectures. It was particularly expensive to avoid the use of extended precision on x86 machines with the traditional x87 floating-point architecture. Although it was easy to control calculation precision, limiting the exponent range for intermediate results required additional costly instructions.
> 
> Prior to JVM 1.2, floating-point calculations were required to be strict; that is, all intermediate floating-point results were required to behave as if represented using IEEE single or double precisions. This made it expensive on common x87-based hardware to ensure that overflows would occur where required.
> 
> Since JVM 1.2, intermediate computations are, by default, allowed to exceed the standard exponent ranges associated with IEEE 32 bit and 64 bit formats. They may instead be represented as a member of the "extended-exponent" value set. On platforms like x87, overflows and underflows may not occur where expected, producing possibly more meaningful, but less repeatable, results instead. 
> 
> Since x87 floating point is no longer widely used by Java implementations, there is an active proposal to again make all floating-point operations strict, effectively restoring the pre-1.2 semantics.
> 
> [strictfp - Wikipedia](https://en.wikipedia.org/wiki/Strictfp)


总结一下：一些硬件采用扩展精度进行运算，比方说用80位来算64位的double类型，这导致了运算结果可能在舍入之后不是严格遵守IEEE754的float或double标准的（该溢出的时候没溢出），在不同的机器上的结果可能不同，虽然这是个问题，但禁用这种拓展精度会消耗不少系统资源，所以1.2版本之后就不限制底层采用拓展精度了（1.2之前是严格限制的）。如果想要在程序中进行严格的IEEE754标准下的float或double运算，可通过strictfp修饰符来实现。


## 4 声明顺序规范

【The Java® Language Specification 】这份文档里针对类、域（属性）、方法、接口等均给出了一份修饰符的声明顺序的规范，大概长这样：

    A class declaration may include class modifiers.
        ClassModifier:
        (one of)
        Annotation public protected private
        abstract static final strictfp

把几个小节里的内容综合起来，就成了java.lang.reflect.Modifier类中toString方法里给出的这份可以拿来当“总的规范”的说明：

>The modifier names are returned in an order consistent with the suggested modifier orderings given in sections 8.1.1, 8.3.1, 8.4.3, 8.8.3, and 9.1.1 of The Java™ Language Specification. The full modifier ordering used by this method is:

>**public protected private abstract static final transient volatile synchronized native strictfp interface**

大家都按这个顺序写，大家读着都方便（习惯），不按这个顺序来没有技术上的问题：
```java
    final static public double PI = 3.14;//看着习惯不）
```
