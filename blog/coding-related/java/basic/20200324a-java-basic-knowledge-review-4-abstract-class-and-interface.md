# JAVA基础知识复盘（四）：抽象类与接口
*2020032401-java-basic-knowledge-review-4-abstract-class-and-interface*  
*Posted on 2020.03.25 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


* [JAVA基础知识复盘（四）：抽象类与接口](#java%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E5%A4%8D%E7%9B%98%E5%9B%9B%E6%8A%BD%E8%B1%A1%E7%B1%BB%E4%B8%8E%E6%8E%A5%E5%8F%A3)
    * [1 抽象类](#1-%E6%8A%BD%E8%B1%A1%E7%B1%BB)
        * [1\.1 问题引入](#11-%E9%97%AE%E9%A2%98%E5%BC%95%E5%85%A5)
        * [1\.2 abstract关键字](#12-abstract%E5%85%B3%E9%94%AE%E5%AD%97)
        * [1\.3 明确抽象类的意义](#13-%E6%98%8E%E7%A1%AE%E6%8A%BD%E8%B1%A1%E7%B1%BB%E7%9A%84%E6%84%8F%E4%B9%89)
        * [1\.4 抽象类的实例化](#14-%E6%8A%BD%E8%B1%A1%E7%B1%BB%E7%9A%84%E5%AE%9E%E4%BE%8B%E5%8C%96)
        * [1\.5 小结](#15-%E5%B0%8F%E7%BB%93)
    * [2 接口](#2-%E6%8E%A5%E5%8F%A3)
        * [2\.1 接口的使用](#21-%E6%8E%A5%E5%8F%A3%E7%9A%84%E4%BD%BF%E7%94%A8)
        * [2\.2 接口的特性](#22-%E6%8E%A5%E5%8F%A3%E7%9A%84%E7%89%B9%E6%80%A7)
            * [接口本身](#%E6%8E%A5%E5%8F%A3%E6%9C%AC%E8%BA%AB)
            * [接口中的域](#%E6%8E%A5%E5%8F%A3%E4%B8%AD%E7%9A%84%E5%9F%9F)
            * [接口中的方法](#%E6%8E%A5%E5%8F%A3%E4%B8%AD%E7%9A%84%E6%96%B9%E6%B3%95)
                * [接口中的静态方法](#%E6%8E%A5%E5%8F%A3%E4%B8%AD%E7%9A%84%E9%9D%99%E6%80%81%E6%96%B9%E6%B3%95)
            * [接口变量](#%E6%8E%A5%E5%8F%A3%E5%8F%98%E9%87%8F)
            * [“多重继承”](#%E5%A4%9A%E9%87%8D%E7%BB%A7%E6%89%BF)
        * [2\.3 标记接口（Marker Interface）](#23-%E6%A0%87%E8%AE%B0%E6%8E%A5%E5%8F%A3marker-interface)
    * [3 小结](#3-%E5%B0%8F%E7%BB%93)


## 1 抽象类

### 1.1 问题引入

[JAVA基础知识复盘（二）：面向对象程序设计及其基本特性][2020031201]一文中回顾了多态存在的意义：进一步释放父类与子类之间因继承关系产生的耦合，换种方式说，就是让父类中的方法通过子类的重写产生多种形态。

多态存在的前提条件之一是子类重写父类方法，这个过程父类起到的作用只是作为子类定义的基础，**我们不一定会单独用到父类，甚至有时候我们根本不希望父类被（通过new）主动实例化**。考虑这样的场景：People类有speak方法，我们希望speak方法必须被子类重写，当不知道People到底是Student还是Teacher亦或是某种具体身份的时候，我们希望speak方法干脆不要被调用，因为不知道具体是什么人，也就无从得知他到底怎么讲话。针对这个问题场景，可以在代码中人工确定每个子类都重写了父类方法，但Java提供了abstract关键字帮助我们更好的处理此问题。

[2020031201]:./2020031201-java-basic-knowledge-review-2-oop-and-its-basic-characteristics "2020031201 JAVA基础知识复盘（二）：面向对象程序设计及其基本特性"


### 1.2 abstract关键字

针对1.1引入的问题，可以直接用abstract修饰People类中的speak方法，这样speak方法就成了一个**抽象方法**，此时编译器会提示必须将People定义为一个**抽象类**：
```java
abstract class People {
    String name;
    char gender;
    //抽象方法
    public abstract void speak();//抽象方法无方法体
}
```
抽象方法顾名思义，只是一个抽象的声明（人会说话），不包含具体实现（具体某种人怎么说话不管）。到此时会发现，只要把多态中的父类方法的方法体删掉再加上abstract关键字，抽象类就定义完成了。

抽象类是以多态的概念为根基的，可以将抽象类理解为增加了严格的重写要求的多态的实现途径。一个类被abstract关键字修饰为抽象类之后，这个类就成了不能通过new实例化的父类，其必须通过子类继承来产生作用，且子类必须重写这个抽象父类中的抽象方法。

### 1.3 明确抽象类的意义

当我们用abstract将一个类修饰为抽象类的时候，我们希望达成什么效果呢？

最直接的需求是，确保这个类中的某些方法（抽象方法）一定会被子类重写，所以普通情况下没有抽象方法的抽象类没有存在的意义*（但特殊场景下还是有意义的，参考【装饰器模式】）*，由需求产生的一个要求在于，抽象类必须能够被继承，所以用final修饰的抽象类也没有存在的意义（不允许将final与abstract组合）。

### 1.4 抽象类的实例化

前面提到抽象类不可以通过new来实例化，但抽象类本质上也是一个类，可以定义普通的实例变量，按道理也是要通过实例化之后才可以使用，所以抽象类总要有一个实例化的机制，这个机制就是**通过子类实现抽象类的实例化**：
```java
abstract class People {
    String name = "人";
    public abstract void speak();//抽象方法无方法体
    People(){
        System.out.println("People的构造器");
    }

}
class Student extends People {
    Student(){
        System.out.println("Student的构造器");
    }
}
public class AboutAbstractClass {
    public static void main(String[] args) {
        Student st = new Student();
        System.out.println("People的name属性初始值："+st.name);
        /**output
         * People的构造器
         * Student的构造器
         * People的name属性初始值：人
         */
    }
}
```
可以看到抽象类通过子类实现了实例化。

### 1.5 小结

* 含有抽象方法的类必须声明为抽象类
* 子类必须重写父类中所有的抽象方法
* 抽象方法不包含方法体，只是一个声明
* 抽象类通过子类完成实例化（不能new）


## 2 接口

接口（Interface）用于描述一个类能够实现什么方法（定义行为），接口内部只是声明出这些方法，但是没有具体的实现，可以把接口理解为进一步抽象的抽象类：抽象类中可以像一个正常的类一样定义实例域、实例方法，但接口中不允许，接口中所有域隐含为public static final，接口中所有方法隐含为public abstract。

### 2.1 接口的使用

接口通过interface关键字定义：
```java
interface SuperPower{//超能力接口
    void BattleCry();//战吼
}
```
一个类若想实现某个接口，要用implements关键字：
```java
//定义接口
interface SuperPower{//超能力接口
    void BattleCry();//战吼  隐含为抽象方法
}
//抽象类
abstract class People {
    String name = "人";
    char gender;
    public abstract void speak();//抽象方法无方法体
}
//实现接口
class HarryPotter extends People implements SuperPower{
    //HarryPotter继承了People抽象类，实现了SuperPower接口

    @Override
    public void BattleCry() {
        System.out.println("阿瓦达索命");
    }

    @Override
    public void speak() {
        System.out.println("HarryPotter在讲话");
    }
}
```


### 2.2 接口的特性

#### 接口本身

1. 接口本身隐含为abstract
2. 非内部类的情况下：
    1. 接口用public修饰时：
        - （这意味着此接口为当前文件中唯一的那个public）
        - 文件名与接口名须保持一致
    2. 接口没有public修饰时，隐含为包访问权限
3. 接口可以继承其他接口


#### 接口中的域

接口中的域（属性）隐含为public static final，不能用protected或private修饰，相当于（包内）全局常量。
```java
interface SuperPower{//超能力接口
    protected int x;//报错
    private int xx;//报错
    void BattleCry();//战吼
}
```
JavaSE5版本之前，在接口中借助隐含的static final来声明常量是惯用操作，SE5之后引入枚举类型，这种操作也就没啥必要了。
```java
interface SuperPower{//超能力接口
    String
        AA = "AA", BB = "BB", CC = "CC";//各种预设超能力
    void BattleCry();//战吼
}
```

#### 接口中的方法

前面说了，接口中所有的方法隐含为public abstract，且与域一样，接口中的方法也不能用protected或private修饰。

##### 接口中的静态方法

JavaSE8及之后版本中，可以为接口声明静态方法，且静态方法必须有实现：
```java
interface RichMan{
    int money = 999999999;
    static void Fly(){
        System.out.println("RichMan can fly");
    }
}
public class AboutInterface {
    public static void main(String[] args) {
        RichMan.Fly();//RichMan can fly
    }
}
```

#### 接口变量

虽然不可以通过new创建一个接口对象，却可以声明接口变量（叫引用似乎也没毛病）：
```java
public static void main(String[] args) {
        Batman batman = new Batman();
        SuperPower aSuperMan;//定义一个接口变量
        aSuperMan = batman; //
        aSuperMan.BattleCry();//I'm Rich
}
```

#### “多重继承”

接口除了实现了与抽象类类似的功能之外，另有一个非常重要的特性（甚至可以说是接口最重要的特性），那就是**通过接口可以实现"多重继承"**：
```java
//接口示例
interface SuperPower{//超能力接口
    void BattleCry();//战吼
}
interface RichMan{//大富翁接口
    int money = 999999999;
}
//实现接口
class Batman implements SuperPower,RichMan{

    @Override
    public void BattleCry() {
        System.out.println("I'm Rich");
    }
    public void showMoney() {
        System.out.println("I have "+this.money + "...$");
    }
}
//入口
public class AboutInterface {
    public static void main(String[] args) {
        Batman batman = new Batman();
        batman.BattleCry();
        batman.showMoney();
        /**output
         * I'm Rich
         * I have 999999999...$
         */
    }
}
```
接口的“多重继承”这种特性，让接口与抽象类产生了质的差别。

*准确地说，应该叫多重实现（implements）才对*

### 2.3 标记接口（Marker Interface）

*这段内容是Blog上偶然看到的，算一个额外知识点*

标记接口又称标签接口（Tag Interface），顾名思义，它只起到一个标记的作用，本身不定义任何抽象方法：
```java
//标记接口
interface NiceClass{
    //标记接口内部留空
}
class MyClass implements NiceClass{
    
}
```
上述代码相当于给MyClass类加了个Nice标签，这么做有什么意义呢？回顾Java的向上转型，通过`NiceClass niceClass = new MyClass();`可以将MyClass类当作NiceClass类处理，也就是说，加上的这个标签相当于让MyClass类多了一种可以转换的类型，这就好理解了，给不同的类打上同样的标签，然后统一处理之类的。

另一方面，标记接口还可以作为一组接口的父接口（说到底还是个标签），一个典型的例子：
```java
package java.util;

/**
 * A tagging interface that all event listener interfaces must extend.
 * @since JDK1.1
 */
public interface EventListener {
}
```
这个java.util.EventListener这个接口的源代码就长这样，它作为一个父接口，只是起到一种声明的作用，具体的单击事件也好，键盘事件也好，都放在它底下统一管理。

参考：

[java中的标记接口（标签接口） - 杨冠标 - 博客园](https://www.cnblogs.com/yanggb/p/10664155.html)


## 3 小结

抽象类这个概念是针对1.1中介绍的问题场景而引入的，抽象类说到底是一个类，可以正常定义一些实例变量与非抽象方法，如果将抽象类处理的再极端一些，所有的方法都定义为抽象的，那就成了一个接口（Interface）。
```java
abstract class People {
    String name;
    char gender;
    //抽象方法
    public abstract void speak();//抽象方法无方法体
    public void walk(){//抽象类中的普通方法（非抽象方法）
        //……
    }
}
```

接口这个概念与抽象类的初衷是一致的，但接口相比于抽象类要灵活的多，因为接口实现了“多重继承”，这在描述非层次结构的关系时候非常好用。有利也有弊，越灵活的组件越容易失控，这方面还需要多多参考设计模式。