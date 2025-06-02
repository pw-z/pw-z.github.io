# JAVA基础知识复盘（二）：面向对象程序设计及其基本特性
*2020031201-java-basic-knowledge-review-2-oop-and-its-basic-characteristics*  
*Posted on 2020.03.13 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


* [JAVA基础知识复盘（二）：面向对象程序设计及其基本特性](#java%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E5%A4%8D%E7%9B%98%E4%BA%8C%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E5%8F%8A%E5%85%B6%E5%9F%BA%E6%9C%AC%E7%89%B9%E6%80%A7)
    * [1 概述](#1-%E6%A6%82%E8%BF%B0)
        * [1\.1 面向对象程序设计思想简析](#11-%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E6%80%9D%E6%83%B3%E7%AE%80%E6%9E%90)
        * [1\.2 Java中的面向对象基础概念](#12-java%E4%B8%AD%E7%9A%84%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E5%9F%BA%E7%A1%80%E6%A6%82%E5%BF%B5)
            * [1\.2\.1 类、对象与引用](#121-%E7%B1%BB%E5%AF%B9%E8%B1%A1%E4%B8%8E%E5%BC%95%E7%94%A8)
            * [1\.2\.2 属性与方法](#122-%E5%B1%9E%E6%80%A7%E4%B8%8E%E6%96%B9%E6%B3%95)
                * [方法的重载](#%E6%96%B9%E6%B3%95%E7%9A%84%E9%87%8D%E8%BD%BD)
            * [1\.2\.3 参数与返回值](#123-%E5%8F%82%E6%95%B0%E4%B8%8E%E8%BF%94%E5%9B%9E%E5%80%BC)
            * [1\.2\.4 构造器](#124-%E6%9E%84%E9%80%A0%E5%99%A8)
    * [2 面向对象三大特性](#2-%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E4%B8%89%E5%A4%A7%E7%89%B9%E6%80%A7)
        * [2\.1 封装](#21-%E5%B0%81%E8%A3%85)
        * [2\.2 继承](#22-%E7%BB%A7%E6%89%BF)
            * [2\.2\.1 问题场景](#221-%E9%97%AE%E9%A2%98%E5%9C%BA%E6%99%AF)
            * [2\.2\.2 方法的重写](#222-%E6%96%B9%E6%B3%95%E7%9A%84%E9%87%8D%E5%86%99)
            * [2\.2\.3 this与super](#223-this%E4%B8%8Esuper)
            * [2\.2\.4 关于根类、构造器](#224-%E5%85%B3%E4%BA%8E%E6%A0%B9%E7%B1%BB%E6%9E%84%E9%80%A0%E5%99%A8)
            * [2\.2\.5 小结](#225-%E5%B0%8F%E7%BB%93)
        * [2\.3 多态](#23-%E5%A4%9A%E6%80%81)
            * [2\.3\.1 问题场景](#231-%E9%97%AE%E9%A2%98%E5%9C%BA%E6%99%AF)
            * [2\.3\.2 向上转型与动态绑定](#232-%E5%90%91%E4%B8%8A%E8%BD%AC%E5%9E%8B%E4%B8%8E%E5%8A%A8%E6%80%81%E7%BB%91%E5%AE%9A)
                * [向上转型](#%E5%90%91%E4%B8%8A%E8%BD%AC%E5%9E%8B)
                * [动态绑定](#%E5%8A%A8%E6%80%81%E7%BB%91%E5%AE%9A)
            * [2\.3\.3 重识多态](#233-%E9%87%8D%E8%AF%86%E5%A4%9A%E6%80%81)
        * [2\.4 总结](#24-%E6%80%BB%E7%BB%93)


## 1 概述

[JAVA基础知识复盘（一）：八大基本数据类型][2020031101]中的认识是建立在旧有的C语言经验上的，且当作是一个过度，接下来要将程序设计的思想方法彻底转到面向对象上来。本文先介绍一些（Java中）关于面向对象程序设计的基本概念，接着重点回顾三个重要特性：**封装、继承、多态**。

[2020031101]:./2020031101-java-basic-knowledge-review-1-eight-primitive-data-types "JAVA基础知识复盘（一）：八大基本数据类型"

### 1.1 面向对象程序设计思想简析

面向对象程序设计(Object Oriented Programming)是一种很符合人类思维方式的程序设计思想，也是如今主流的程序设计思想之一，它诞生挺早的但流行较晚（与Python有点像），《Java编程思想（第四版）》介绍面向对象时提到的“第一个成功的面向对象语言”——Smalltalk语言，19世纪70年代就被开发出来了，那还是面向过程、结构化编程大行其道的时候，直到第二次软件危机，人们追求程序的拓展性、可维护性等需求时，面向对象才彻底流行起来。

用一个学生成绩统计的例子来区分一下面向对象与其他几种设计思想。假设现有A组5名学生的成绩需要进行处理，输入：学生姓名、学生成绩，输出：对应学生的成绩等级、所有学生的平均分。

最开始不带任何设计思想，按照事件的处理流程直接来写代码（C语言）：
```c
//代码1-1-1
#include<stdio.h>
#include<stdlib.h> 
int main(){
    int sum;
    char *name;
    int score;

    name=(char *)malloc(sizeof(char));
    while(scanf("%s%d",name,&score)!=EOF){
        sum+=score;
        if(score<60){//不及格 
            printf("%s : 不及格\n",name);
        }else if(score>=60 && score<70){//及格 
            printf("%s : 及格\n",name);
        }else if(score>=70 && score<80){//一般 
            printf("%s : 一般\n",name);
        }else if(score>=80 && score<90){//良好 
            printf("%s : 良好\n",name);
        }else{//优秀 
            printf("%s : 优秀\n",name);
        }
    }
    printf("平均分 ：%.1f",sum/5.0);
}

//小a 45 小b 61 小c 78 小d 82 小e 98
//小a : 不及格
//小b : 及格
//小c : 一般
//小d : 良好
//小e : 优秀
//^Z
//平均分 ：72.8 
```
以上代码（1-1-1）可以算是较为典型的面向过程了，代码主要关注逻辑处理，一旦逻辑复杂起来代码量达到一定规模之后，读起来、改起来都极为麻烦（这还是没有goto语句、引入了一些结构化编程思想的情况（while循环代码块）），如果现在想加入一个排名统计，得从头到尾改一遍。接下来稍作改进，前面的代码耦合程度过高，牵一发动全身导致灵活性太差，不如把成绩处理的部分单独拎出来作为子程序（C语言）：
```c
//代码1-1-2
#include<stdio.h>
#include<stdlib.h> 
int main(){
    void judge(char *name, int score);
    int sum;
    char *name;
    int score;
    
    name=(char *)malloc(sizeof(char));
    while(scanf("%s%d",name,&score)!=EOF){
        sum+=score;
        judge(name,score);
    }
    printf("平均分 ：%.1f",sum/5.0);
}

//输出成绩等级
void judge(char *name, int score){
    if(score<60){//不及格 
        printf("%s : 不及格\n",name);
    }else if(score>=60 && score<70){//及格 
        printf("%s : 及格\n",name);
    }else if(score>=70 && score<80){//一般 
        printf("%s : 一般\n",name);
    }else if(score>=80 && score<90){//良好 
        printf("%s : 良好\n",name);
    }else{//优秀 
        printf("%s : 优秀\n",name);
    }
}
```
代码1-1-2输出结果与代码1-1-1完全一致，但引入了更好的模块化的思想，将某一个小功能独立成一个模块，试想需求复杂之后，以这种设计思想写出来的代码将具有较为清晰的结构，从而也就具有更好的可读性与可维护性，这已经有了**结构化编程**的雏形：采用分治思想，将整体需求这个大问题、长流程分割成多个小部分（小结构）来处理。然而结构化编程说到底没有脱离面向过程的范畴，代码量较大时依旧处处受限难以进行拓展，究其原因，结构化采用自顶向下的设计思想，这要求代码的编写者需要对整体有较为清楚的认知，可谓是从最开始就对代码的可能性做出了较强的限制。

接下来看若用面向对象的设计思想，以上问题如何处理（Java语言）：
```java
//代码1-1-3
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ScoreResult rs = new ScoreResult();
        while (in.hasNext()){

            Student st = new Student();
            st.name = in.next();
            st.score = in.nextInt();

            JudgeUtil.judge(st);

            rs.sumScore+=st.score;
            rs.stNumber++;
        }
        rs.averageScore = (float) rs.sumScore/rs.stNumber;
        System.out.println(rs.averageScore);
    }
    /** output
     * 小a 45 小b 61 小c 78 小d 82 小e 98
     * 小a不及格
     * 小b及格
     * 小c一般
     * 小d良好
     * 小e优秀
     * ^D
     * 72.8
     */
}

class Student {
    String name;
    int score;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getScore() { return score; }
    public void setScore(int score) { this.score = score; }
}

class ScoreResult {
    public int stNumber;//学生数量
    public int sumScore;//总分
    public float averageScore;//均分
    public void setStNumber(int stNumber) { this.stNumber = stNumber; }
    public int getSumScore() { return sumScore; }
    public void setSumScore(int sumScore) { this.sumScore = sumScore; }
    public float getAverage() { return averageScore; }
    public void setAverage(float average) { this.averageScore = average; }
}

class JudgeUtil{
    public static void judge(Student student){
        if(student.score<60){//不及格
            System.out.println(student.name + "不及格");
        }else if(student.score>=60 && student.score<70){//及格
            System.out.println(student.name + "及格");
        }else if(student.score>=70 && student.score<80){//一般
            System.out.println(student.name + "一般");
        }else if(student.score>=80 && student.score<90){//良好
            System.out.println(student.name + "良好");
        }else{//优秀
            System.out.println(student.name + "优秀");
        }
    }
}
```
代码1-1-3正式引入了【对象】这个概念，可以看到学生、成绩情况以及成绩处理工具分别被编写成为（封装）一个类，类就是对象的模板，在主函数中，成绩统计这个命题通过处理不同对象之间的关系逐步被解决，由此也可以看到面向对象的核心，即，将所有操作都转移到“对象”上来，以对象为中心进行数据处理、逻辑处理。

一个对象就是程序中的一个基本组成单元，面向对象设计思想下的程序可谓是对象的集合体。对象与现实世界中的客观实体有直接联系，以对象为中心刻画问题、处理问题符合人的思维习惯。相比于面向过程或者是结构化编程，面向对象牺牲了一点性能（代码1-1-3明显不如1-1-1或1-1-2简洁，占用了更多系统资源），但以此为代价换来的是代码可读性、可维护性、可拓展性等等方面极大的提升。在多数情况下，这点性能的牺牲是绝对值得的。

参考：

[面向对象程序设计的由来(历史故事)  - Dr-wei - 博客园](https://www.cnblogs.com/Dr-wei/p/11861849.html)

### 1.2 Java中的面向对象基础概念

面向对象仅仅是一种思想，就像计算机不懂整数、小数这些概念但是Java提供了基本数据类型一样，为了实现面向对象编程，Java提供了类、对象以及继承、多态等概念。下面简要回顾。

#### 1.2.1 类、对象与引用

**类（class）**相当于模板，代码1-1-3中的`class Student{}`定义了一个“学生模板”，**对象**是某个模板对应的具体的实例。`Student st = new Student();`这条语句便是使用`new`这个关键字以Student类为模板在内存中创建了一个具体的实例，这个过程叫做类的**实例化**，其中`st`称为**引用**，可以理解为C语言中的指针，我们可以通过这个引用来操作具体的某一个对象。

```java
    Student st1;
    Student st2 = new Student();
    //System.out.println(st1.score);//报错
    System.out.println(st2.score);//0
```
代码中st1仅仅是一个引用，内存中并没有具体与之对应的实例，所以没法对其进行输出操作。st2则指向了一个实例，又因为没有为其赋值，所以输出的score默认为int类型的初始值“0”。

#### 1.2.2 属性与方法

继续看前文中定义的Student类：
```java
class Student {
    String name;
    int score;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getScore() { return score; }
    public void setScore(int score) { this.score = score; }
}
```
类中包含两种内容，即属性与方法，Java中的方法与C语言中的函数时一个概念，仅是用词差异。属性与方法（乃至类本身）可以用修饰符进行修饰，修饰符决定了对应属性或方法的访问权限，如上述中的`public`修饰符，属性与方法可以**在访问权限内**通过小数点进行调用。关于修饰符、访问权限等话题另作主题讨论。

##### 方法的重载

还记得在C语言中函数命名有一条规则，即必须独一无二，若写了两个不同的函数，但是函数名字相同，则没办法区分到底调用的是哪一个。Java提供了重载这项操作，即通过不同的参数来区分命名相同的一个函数（方法）。
```java
    public void setScore(int score) { this.score = score; }
    public void setScore(float score) { this.score = (int) score; }
```

#### 1.2.3 参数与返回值

针对某一个方法，参数是传递给此方法的数据，返回值是此方法返回给调用处的数据。`public int getScore() { return score; }`这个方法无参数，返回了int类型的score。`public void setName(String name) { this.name = name; }`传入了一个String对象，没有返回值。

注意：除了基本类型之外，方法传递与返回的均为对象的引用。有关引用的使用还需多加注意：
```java
    Student st1 = new Student();
    st1.setName("小F");
    Student st2 = st1;
    System.out.println(st2.name); //小F
```

#### 1.2.4 构造器

**构造器是**实例化过程中自动被调用的**一种特殊方法**。构造器这个概念由C++引入，目的在于更好地进行变量初始化，Java沿用了此概念。

构造器的名字与类名相同，一个类可以**通过重载**设定多个不同的构造器。如果没有手动指定一个构造器，编译器会自动生成一个无参数的默认构造器；如果手动指定了一个构造器，无论这个构造器有无参数，编译器都不会再生成默认构造器。
```java
class Student {
    String name;
    int score;
    Student(){} //不写构造器的话，就会生成一个这样的默认构造器
    Student(String name){ this.name = name; } //有参数的构造器
}
```
在上述代码中，若将无参构造器删除，则不能再通过`Student st = new Student();`来实例化Student对象，因为Student类中不再含有无参构造器，必须提供有参构造器的参数，`Student st = new Student("小F");`，才可正常初始化。

## 2 面向对象三大特性

面向对象的程序设计语言有三大基本特性，**封装（抽象）、继承、多态**。封装是基础，将学生的属性与行为抽象出来写成一个单独的类，这便是封装；继承与多态则是为了更好的描述类间关系而诞生的产物。学生是人，那么先定义一个“人”类，人有名字，学生在人的基础上在添加一条成绩属性，这个过程便是继承；“人”这个类中有“讲话”方法，我们新建一个聋哑人继承了人这个类，但又想让聋哑人的讲话方式与“人”中定义的不一样，此时可以在聋哑人类中重新定义一个通过手语实现的“讲话”方法，这个过程中，人这个类因为聋哑人这个类的一些操作而衍生出一种用手语“讲话”的新的类型，这便是多态。接下来详细说明。

### 2.1 封装

封装并非面向对象独有的特性，它是一种通用的思维方式，面向过程编程时我们也会将相关内容放到一块来实现，那也算是某种程度上的封装。封装的过程，是抽象化的过程，人本就是通过抽象建立各种概念来认识这个世界，将现实世界中某一事物的属性、方法抽象出来封装成类，以此为基础进行后续操作，稍作适应之后会觉得这简直是自然而然的，本文开头说【面向对象很符合人类思维方式】一方面就体现在这里。

封装带来的最显而易见的好处：**解耦合**。

代码1-1-3中JudgeUtil类里面定义了一个输出成绩等级的方法，若需求变更需要一个排序功能，只需要在JudgeUtil这个工具类里添加一个新的排序方法，原主函数的部分则调用一下即可。另外，由于属性也被封装到了类中，通过修饰符可以对每种属性进行更细致的管理（比如设置访问权限），如此一来每个类自成体系，各个类之间通过开放的接口进行通信而非通过强逻辑代码，从而大大降低了代码间的耦合程度。

并非解耦合就是好的，也要看解耦合的粒度合不合适，在软件工程领域，经过几次软件危机发展而来的面向对象的程序设计思想下，以【类】作为最小粒度进行解耦合，似乎刚刚好。

### 2.2 继承

#### 2.2.1 问题场景

通过封装完成了类间解耦合，但一些问题场景下解耦合的粒度又不需要细致到某一个类上，看一下问题场景：
```java
//代码2-2-1
class Student {
    String name;
    char gender;
    int age;
    int score; //成绩
}
class Teacher {
    String name;
    char gender;
    int age;
    int salary; //工资
}
```
代码2-2-1的两个类Student与Teacher之间大部分属性是一致的，因为老师学生都是人，人有一些共同的属性，按照代码2-2-1这样写，代码的冗余度太高了，这样也不好，索性新建一个类将人的共同属性封装起来，让老师、学生作为这个类的子类，子类中可以使用父类的属性、方法：
```java
//代码2-2-2
class People {
    String name;
    char gender;
    int age;
    public void speak(){ System.out.println("说话"); }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
class Student extends People {
    int score; //成绩
}
class Teacher extends People {
    int salary; //工资
}
public static void main(String[] args) {
    Student st = new Student();
    Teacher te = new Teacher();
    st.setName("小明");
    te.setName("老王");
    System.out.print(st.getName());
    st.speak();
    System.out.print(te.getName());
    te.speak();
    /**output
     * 小明说话
     * 老王说话
     */
}
```
如代码2-2-2所示，Java通过**extend**关键字实现**继承**这一概念，被继承的类称为父类，继承者称为子类，子类拥有父类所有的**非private**属性、方法。

若某个类不想被其它类继承，可以用final关键字加以修饰：
```java
final class Student extends People {
    int score; //成绩
}
```

#### 2.2.2 方法的重写

子类可以以自己的方式重新定义父类中的方法，这在Java中叫做方法的重写：
```java
//代码2-2-2
class People {
    String name;
    char gender;
    int age;
    public void speak(){ System.out.println("说话"); }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
class Student extends People {
    int score; //成绩
    @Override
    public void speak(){
        System.out.println("兴高采烈地说话");
    }
}
class Teacher extends People {
    int salary; //工资
    @Override
    public void speak(){
        System.out.println("文质彬彬地说话");
    }
}
public static void main(String[] args) {
    Student st = new Student();
    Teacher te = new Teacher();
    st.setName("小明");
    te.setName("老王");
    System.out.print(st.getName());
    st.speak();
    System.out.print(te.getName());
    te.speak();
    /**output
     * 小明兴高采烈地说话
     * 老王文质彬彬地说话
     */
}
```
重写父类方法时可以用“@Override”进行“注释”，编译器会检查其后的方法是否是父类中拥有的方法，若没有，则会报错。若不标注@Override的时候写错了方法名，那就相当于给子类写了一个其它的方法。另外注意，一个类不可同时继承多个类（多继承×），但是可以继承以及继承了某个类的类（多重继承√）。

重写不可改变返回值与参数。若类中的方法不想被子类重写，也可用final关键字进行修饰：
```java
class Student extends People {
    int score; //成绩
    final public void speak(){
        System.out.println("兴高采烈地说话");
    }
}
```

#### 2.2.3 this与super

* “**this**关键字”只能在方法内调用，表示的**是**调用此方法的那个对象的**引用**。
* “**super**关键字”只能在子类中调用，表示的**是**对应父类的**引用**。

代码2-2-2中我们重写了老师与学生的speak方法，然而虽然老师可以文质彬彬地说话，有时候我们又想让老师普通地说话，有时候让老师文质彬彬回来，这种需求可以通过this与super关键字来实现：
```java
class People {
    public void speak(){ System.out.println("说话"); }
}
class Teacher extends People {
    public void speak(){ System.out.println("文质彬彬地说话"); }
    public void speakModel(int i){
        if (i==1){
            this.speak();
        }else {
            super.speak();
        }
    }
}
public static void main(String[] args) {
    Teacher te = new Teacher();
    te.speakModel(1);
    te.speakModel(2);
    /**output
     * 文质彬彬地说话
     * 说话
     */
}

```

#### 2.2.4 关于根类、构造器

Java的类间关系是一颗单根树，根节点即Object类，所有未显式指明继承关系的类都隐式继承自Object类，这一点可以在查阅文档的时候清晰地看到。

子类在实例化过程中，会在构造器中插入父类构造器，实例化一个父类的对象，这个对象将作为子类对象的一部分。`Teacher te = new Teacher();`这句代码首先在构造器中插入People类的构造器，实例化一个People，People类实例化的过程中则在构造器里插入了Object的构造器……
```java
class People {
    People (){System.out.println("People");}
}
class Teacher extends People {
    Teacher(){System.out.println("Teacher");}
}
public static void main(String[] args) {
     Teacher te = new Teacher();
     /**output
     * People
     * Teacher
     */
}

```

#### 2.2.5 小结

继承通过提高一些类之间的耦合性（父类与子类）解决了代码冗余的问题，提高了代码复用率，而以继承为基础构建的分级类间关系本身也符合现实世界中的概念层次关系，这算是【面向对象很符合人类思维方式】另一方面的体现。

### 2.3 多态

前面通过封装确定了类的独立性，又通过继承增加了一定的类间耦合性，多态的作用说来有趣，正是为了解除继承所增加的这部分耦合性:D。

#### 2.3.1 问题场景

回想【2.2.2 方法的重写】中的例子，我们想让根据继承的思想抽象到People类中的speak方法在每一个具体的子类中有不同的表现形式，于是重写了每个子类中的speak方法，这已经在一定程度上体现了多态，不过只是一部分。现在假如要实现一个功能叫做“提问”，这个方法接受一个People作为参数，功能是让传递过来的这个People说话。

对于这个需求，可以写很多个提问的重载形式，`提问（学生）`、`提问（老师）`:
```java
class Util{
    public static void ask(Student student){
        student.speak();
    }
    public static void ask(Teacher teacher){
        teacher.speak();
    }
}
```
这种解决方案显然不够优美，某一天想新增一个“校长”类，对应的又要在提问方法中添加对校长提问的处理代码，可不可以只传递People这个父类，通过某种机制判断这个人是学生、老师还是校长，再调用对应类中的讲话方法呢？可以：
```java
class Util{
    public static void ask(People people){
        people.speak();
    }
}
public static void main(String[] args) {
    Teacher te = new Teacher();
    Util.ask(te);//文质彬彬地说话
}
```
我们期待如上代码可以识别出对应的People是学生还是老师，这段代码事实上也可以满足我们的期待。main方法中`Util.ask(te)`隐含着一步【向上转型】，理解为类型转换即可，接着在ask方法中隐含着一步【动态绑定】，正是通过动态绑定我们才能用People类指代Teacher类，这便是使用多态的一个简单例子。整个过程中，我们编写的代码只与父类打交道，**通过父类引用（people）指向子类对象（te）**，具体的功能实现通过调用子类的重写方法完成。

#### 2.3.2 向上转型与动态绑定

##### 向上转型

>把对某个对象的引用视为对其基类型的引用的做法被称作向上转型——因为在继承树的画法中，基类是放置在上方的[^Java编程思想8.1]

Teacher类继承了People类，在调用某一个Teacher实例对象时，自动将此Teacher对象当作People对象处理，这就是Java中的向上转型，再看一个例子：
```java
class Teacher extends People {
    int salary; //工资
    public void speak(){    System.out.println("文质彬彬地说话");}
    public void teach(){    System.out.println("Teacher类独有的方法teach()");}
}
public static void main(String[] args) {
    People people = new Teacher();
    people.speak();
    //! people.teach();//报错
}
```
`People people = new Teacher();`将一个Teacher对象赋给了一个People引用，这也是典型的向上转型，向上转型之后，Teacher类独有的方法属性都不能用了，所以调用`people.teach()`会报错，这个过程可以类比基本类型的转换，精度大的（属性、方法多的）类型向精度小的（属性、方法少的）类型转换会造成精度损失，这个过程的一个重要之处在于：向上转换的引用调用的方法是子类中重写过的方法（如果子类中重写了）而不是父类中原本的方法，属性同理。

[^Java编程思想8.1]:《Java编程思想》第四版第8章8.1再论向上转型

##### 动态绑定

如前面提到的，给`Util.ask()`传入了一个People引用，ask方法如何知道这个People是学生还是老师呢？实际在Java语言的使用中，Java通过在运行时根据对象自行判断其类型并与对应的引用进行绑定（运行的时候虚拟机知道people这个引用指向的是一个teacher对象），这种类型绑定方式称为后期绑定，也叫动态绑定或运行时绑定，举个不太恰当的例子，在C语言中使用常规方法定义一个数组需要指定类型与大小，这个过程中数组在内存中对应的内容已经确定下来了，这就是前期绑定，若通过某种机制可以实现运行之后根据情况自动判断数组类型与大小，这就是后期绑定了。实际上C语言并不支持这种后期绑定的操作，而Java由于对象与引用这种基础概念的存在，默认状态就是使用后期（动态）绑定的。
```java
    People people = new Teacher();
    people.speak();
    System.out.println(people.hashCode());
//  people.teach();//报错
    Teacher teacher = (Teacher) people;
    teacher.speak();
    System.out.println(teacher.hashCode());
    /**output
     * 文质彬彬地说话
     * 685325104
     * 文质彬彬地说话
     * 685325104
     */
```
从“引用”这个名字也能理解一二，某一个引用到底指向哪个对象并不是确定好的，而是运行中根据情况动态绑定的。与继承中使用final关键字限制继承一样，使用final关键字同样可以停用（限制住）这种动态绑定。

>Java中除了static方法和final方法（private方法属于final方法）之外，其他所有的方法都是后期绑定。这意味着通常情况下，我们不必判定是否应该进行后期绑定——它会自动发生。[^Java编程思想8.2.1]

[^Java编程思想8.2.1]:《Java编程思想》第四版第8章8.2.1方法调用绑定

#### 2.3.3 重识多态

经过前面的例子与知识补充，回过头来重新看一看多态这个特性，大概可以更好的理解`多态的作用是减少类间耦合`这句话了。以前看[菜鸟教程][菜鸟教程-Java多态]里提到多态存在的三个必要条件：继承、重写、父类引用指向子类对象，尤其是第三个条件，也不再难以理解。

[菜鸟教程-Java多态]:https://www.runoob.com/java/java-polymorphism.html "Java多态-菜鸟教程"

### 2.4 总结

纵览面向对象的基本特性，逃不开解耦合、降冗余等话题，说到底都是为了追求更优美更高质的代码，至于到底什么是更优美的更高质量的代码，前辈们已经探索出很多道路，面向对象是其中一条，还有无数条道路等着我们去探索。






