# JAVA基础知识复盘（五）：异常处理与日志记录
*2020032402-java-basic-knowledge-review-5-exception-handling-and-log-logging*  
*Posted on 2020.03.25 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  

* [JAVA基础知识复盘（五）：异常处理与日志记录](#java%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E5%A4%8D%E7%9B%98%E4%BA%94%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86%E4%B8%8E%E6%97%A5%E5%BF%97%E8%AE%B0%E5%BD%95)
    * [1 引言](#1-%E5%BC%95%E8%A8%80)
    * [2 异常处理](#2-%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86)
        * [2\.1 异常的分类](#21-%E5%BC%82%E5%B8%B8%E7%9A%84%E5%88%86%E7%B1%BB)
            * [受查与非受查异常](#%E5%8F%97%E6%9F%A5%E4%B8%8E%E9%9D%9E%E5%8F%97%E6%9F%A5%E5%BC%82%E5%B8%B8)
        * [2\.2 异常的处理](#22-%E5%BC%82%E5%B8%B8%E7%9A%84%E5%A4%84%E7%90%86)
            * [2\.2\.1 try/catch 捕获异常](#221-trycatch-%E6%8D%95%E8%8E%B7%E5%BC%82%E5%B8%B8)
                * [捕获多个异常](#%E6%8D%95%E8%8E%B7%E5%A4%9A%E4%B8%AA%E5%BC%82%E5%B8%B8)
                * [捕获所有异常](#%E6%8D%95%E8%8E%B7%E6%89%80%E6%9C%89%E5%BC%82%E5%B8%B8)
            * [2\.2\.2 finally 收尾](#222-finally-%E6%94%B6%E5%B0%BE)
            * [2\.2\.2 throws/throw 抛出](#222-throwsthrow-%E6%8A%9B%E5%87%BA)
            * [2\.2\.3 自定义异常](#223-%E8%87%AA%E5%AE%9A%E4%B9%89%E5%BC%82%E5%B8%B8)
        * [2\.3 Throwable类](#23-throwable%E7%B1%BB)
    * [3 日志记录](#3-%E6%97%A5%E5%BF%97%E8%AE%B0%E5%BD%95)
        * [3\.1 java\.util\.logging（原生日志支持）](#31-javautillogging%E5%8E%9F%E7%94%9F%E6%97%A5%E5%BF%97%E6%94%AF%E6%8C%81)
        * [3\.2 简单使用](#32-%E7%AE%80%E5%8D%95%E4%BD%BF%E7%94%A8)
            * [默认配置信息](#%E9%BB%98%E8%AE%A4%E9%85%8D%E7%BD%AE%E4%BF%A1%E6%81%AF)
        * [3\.2 Level（日志级别）](#32-level%E6%97%A5%E5%BF%97%E7%BA%A7%E5%88%AB)
        * [3\.3 普通使用](#33-%E6%99%AE%E9%80%9A%E4%BD%BF%E7%94%A8)
            * [3\.3\.1 新建Logger](#331-%E6%96%B0%E5%BB%BAlogger)
            * [3\.3\.2 新建Handler输出到控制台](#332-%E6%96%B0%E5%BB%BAhandler%E8%BE%93%E5%87%BA%E5%88%B0%E6%8E%A7%E5%88%B6%E5%8F%B0)
            * [3\.3\.3 新建Handler输出到文件](#333-%E6%96%B0%E5%BB%BAhandler%E8%BE%93%E5%87%BA%E5%88%B0%E6%96%87%E4%BB%B6)


## 1 引言

对使用环境中可能遇到的异常情况进行妥善处理是一份程序可以被使用的底线，试想办公软件每次遇到问题都直接闪退并且不自动保存中间结果，这是多么令人抓狂的一件事情。指望程序完全不会遇到异常情况这不太现实，如果可以，还是让程序的异常处理机制越完善越好，这是本文要讨论的第一个也是主要的内容，在Java中对异常情况进行妥善处理。

另一方面，写代码的时候，总是习惯用`System.out.println();`输出中间结果来查看程序的运行状况，Java提供了更方便的日志记录机制，值得熟悉掌握一下，不过不作为本文重点，只回顾一些基础。


## 2 异常处理

先抛开Java，从宏观的软件开发的角度看，一份代码中可能存在的错误，主要有三种类型*（此处的分类并不严谨）*：

1. 语法错误：最低级的错误，不能通过编译
2. 逻辑错误：最令人难受的错误，隐藏在代码中，可能让程序产生意想不到的结果，解决Bug通常是处理这类错误。
3. 运行错误：一份语法、逻辑都没有问题的代码在运行的时候仍有可能遇到问题，比如电脑内存满了，要处理的文件损坏了，这些是代码本身没法掌控的，需要在开发过程中提前预置一些应对策略。

Java的异常处理机制，主要针对的就是上述第三类错误。注意此处的异常、错误都是比较笼统的说法，Java中有一份比较严谨的分类体系，下面就先来讲这个分类。

### 2.1 异常的分类

Java语言规范中有一章的标题为“Exceptions”，讲的就是所谓的“异常”处理机制，细纠字眼的话，异常（Exception）与错误（ Error）还是很不一样的（实际上确实很不一样），那么叫“错误”处理机制行不行呢，也没什么不行，这个处理机制处理的东西包括了狭义的异常与狭义的错误（看你怎么定义错误与异常的范畴了）。在Java中我们具体讨论某种类型的“状况”的时候，要么用“异常”来形容，要么用“错误”来形容，这都是狭义的概念，而当我们称呼这种处理机制的时候，因为这些狭义的概念都可以叫作“异常情况”，所以选择了“异常处理”这种称呼来命名这个处理机制。好了，纠字眼到此结束。

在Java中，所有的【表准异常情况】都被描述为一个个的类，这些类的继承树的顶端是【java.lang.Throwable】类，【Throwable】有两种直接子类：

1. Error类：用于描述编译错误或者系统级别的错误，如资源耗尽等，通常普通程序对这种错误无能为力，只能通知用户（并尽量使程序安全终止）。
2. Exception类：用来描述非系统级别的异常情况，可以被抛出并处理，通常普通程序可以从这种异常情况中恢复并正常执行下去，所以是写代码时需要重点关注的。 Exception类又有两种类型的子类：
    1. RuntimeException类：chou
        1. NullPointerException
        2. ……
    2. 非RuntimeException类：
        1. SQLException
        2. IOException
        3. ……

通过API文档可以更清楚地看到继承关系（不完整，只挑了几个展示）：

* java.lang.Throwable
    - java.lang.Error
        + javax.xml.parsers.FactoryConfigurationError
        + java.io.IOError
        + java.lang.ThreadDeath
        + ……
    - java.lang.Exception
        + com.sun.jdi.ClassNotLoadedException
        + com.sun.jdi.InvalidTypeException
        + java.io.IOException
        + java.lang.RuntimeException
            * java.lang.ArrayStoreException
            * java.util.NoSuchElementException
            * java.lang.NullPointerException
            * ……
        + java.util.concurrent.TimeoutException
        + ……

以上便是Java中异常类的基本层级关系。


#### 受查与非受查异常

先看文档原文：

>The unchecked exception classes are the run-time exception classes and the error classes.
>
>The checked exception classes are all exception classes other than the unchecked exception classes. That is, the checked exception classes are Throwable and all its subclasses other than RuntimeException and its subclasses and Error and its subclasses. 
>
>节选自《The Java® Language Specification (Java SE 13 Edition)》

Java语言规范把派生自Error类及RuntimeException类的异常称为**非受查异常（unchecked exception）**，除此之外的称为**受查异常（checked exception）**，所谓受查，是指受编译器的检查，受查异常必须得有对应的异常处理器，不然是无法通过编译的。

可以这么理解：受查异常的存在相当于为程序提供了一种底线，就算你什么都不考虑，那为了通过编译，至少也得稍微处理一下这些受查异常。对应的，非受查异常是考验开发者功底的内容，Error这种情况先不讨论（它不受代码本身控制），对于RuntimeException类型的异常，开发者应该尽量避免，并且这些都是可以避免的（有点类似逻辑错误，若发生了那主要怪开发者考虑的不周全），比如在访问变量之前先检查其是否为空从而避免空指针异常。
```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        int array[]=null;
        System.out.println(array[1]);
        /**
         * Exception in thread "main" java.lang.NullPointerException
         *  at com.vilaseaka.main.AboutExceptionHandling.main(AboutExceptionHandling.java:6)
         */
    }
}
```

### 2.2 异常的处理

#### 2.2.1 try/catch 捕获异常

try catch 这俩关键字成对出现，用来处理有可能产生异常的代码，try用来执行代码块，catch用来捕获潜在的异常:
```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        int array[]=null;
        try {
            System.out.println(array[1]);
        }catch (NullPointerException e){
            System.out.println(e);//java.lang.NullPointerException
        }
    }
}
```

##### 捕获多个异常

catch可以写多个以捕获不同类型的异常：
```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        int array[]=null;
        try {
            int x = 2/0;//除零
            System.out.println(array[1]);//访问空指针
        }catch (NullPointerException e){
            System.out.println(e);
        }catch (ArithmeticException e){
            System.out.println(e);
        }
        System.out.println("try/catch 执行完毕");
    }
    /**
     * java.lang.ArithmeticException: / by zero
     * try/catch 执行完毕
     */
}
```
由上可知，try中的代码按顺序执行遇到异常之后，会去catch中找对应的异常，找到了就执行对应catch中的代码，执行完之后正常执行try catch后面的代码。

##### 捕获所有异常

可以用一个catch捕获所有可能的异常：
```java
    try {
        int x = 2/0;//异常运算 除零
        System.out.println(array[1]);//访问空指针
    }catch (NullPointerException | ArithmeticException e){
        System.out.println(e);
    }
```
或者干脆借助向上转型：
```java
    try {
        int x = 2/0;//异常运算 除零
        System.out.println(array[1]);//访问空指针
    }catch (Exception e){
        System.out.println(e);
    }
```
对应的效果与分开写catch的效果是一致的。

#### 2.2.2 finally 收尾

try可以与catch组合，还可以与finally组合（但是try不能单独出现）：
```java
    try {
        int x = 2/0;//异常运算 除零
        System.out.println(array[1]);//访问空指针
    }catch (Exception e){
        System.out.println(e);
    }finally {
        System.out.println("finally中的内容总会被执行");
    }
    /**
     * java.lang.ArithmeticException: / by zero
     * finally中的内容总会被执行
     */
```
无论try catch怎么执行，最后**finally中的代码一定会被执行**，finally中一般用来放一些收尾性质的代码，比如清理垃圾，初始化资源等：
```java
public class AboutExceptionHandling {
    private static int intFunc(){
        try {
            return 10;
        }finally {
            System.out.println("return之后finally中的内容仍旧会被执行");
        }
    }
    public static void main(String[] args) {
        System.out.println(intFunc());
        /**
         * return之后finally中的内容仍旧会被执行
         * 10
         */
    }
}
```

#### 2.2.2 throws/throw 抛出

2.2.1中处理的异常都是来自系统自动抛出来的，我们可以通过throws或throw关键字主动往外抛异常，其中throws用于方法，throw就是普通的可执行语句，直接看例子即可：
```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        try {
            try {
                testThrows();
            }catch (Exception e){
                System.out.println("内层代码拿到了一个异常：" + e);
                throw e;
            }finally {
                System.out.println("内层代码将异常抛出去了");
            }
        }catch (Exception e){
            System.out.println("外层代码拿到了内层跑出来的异常");
        }
        /**
         * 内层代码拿到了一个异常：java.lang.ArithmeticException: / by zero
         * 内层代码将异常抛出去了
         * 外层代码拿到了内层跑出来的异常
         */
    }
    //一个肯定会抛出异常的方法
    public static int testThrows() throws Exception{
        int x = 2/0;
        return x;
    }
}
```

#### 2.2.3 自定义异常

可以通过继承已有的异常类来自定义新的异常，习惯上新定义的异常中要包含两个构造器，一个默认的，一个带有描述信息的，看例子：
```java
//自定义异常： +1异常
class PlusOneException extends Exception{
    public PlusOneException(){}
    public PlusOneException(String info){
        super(info);
    }
}
//特殊运算类  ： 不允许+1
class SpecialOperationUtil {
    int plusNumber(int number,int plus) throws PlusOneException {
        if (plus == 1){
            throw new  PlusOneException("+1异常，不允许+1");
        }else {
            return number+plus;
        }
    }
}
public class AboutExceptionHandling {
    public static void main(String[] args) {
        SpecialOperationUtil soUtil = new SpecialOperationUtil();
        int x = 1;
        try {
            soUtil.plusNumber(x,1);
        }catch (PlusOneException e){
            e.printStackTrace(System.out);
        }
        /**output
         * com.vilaseaka.main.PlusOneException: +1异常，不允许+1
         *  at com.vilaseaka.main.SpecialOperationUtil.plusNumber(AboutExceptionHandling.java:98)
         *  at com.vilaseaka.main.AboutExceptionHandling.main(AboutExceptionHandling.java:82)
         */
    }
}
```
**分析**：在例子中，定义了一个“+1异常”，并将其运用到了SpecialOperationUtil类（特殊运算）中，这个特殊运算类里定义了一个加法，这个加法不允许对数字进行+1操作，main函数的运行结果也在例子中给出了，其中printStackTrace()方法是从Throwable类继承过来的（中间还经过了一个Exception），作用是打印*从方法调用处到异常抛出处*的*方法调用序列*。


### 2.3 Throwable类

2.1中分析了Java中异常类的层级关系，Throwable类无疑是根本，在处理异常的时候，常用的方法也都是这个父类中的，文档很方便查看，这里只是拿过来扫一眼：

| Modifier and Type |    Method        |             Description            |
| :---------------: | :---------------:| :----------------------:           |
|void|addSuppressed​(Throwable exception)|Appends the specified exception to the exceptions that were suppressed in order to deliver this exception.|
|Throwable|fillInStackTrace()|Fills in the execution stack trace.|
|Throwable|getCause()|Returns the cause of this throwable or null if the cause is nonexistent or unknown.|
|String|getLocalizedMessage()|Creates a localized description of this throwable.|
|String|getMessage()|Returns the detail message string of this throwable.|
|StackTraceElement[]|getStackTrace()|Provides programmatic access to the stack trace information printed by printStackTrace().|
|Throwable[]|getSuppressed()|Returns an array containing all of the exceptions that were suppressed, typically by the try-with-resources statement, in order to deliver this exception.|
|Throwable|initCause​(Throwable cause) |Initializes the cause of this throwable to the specified value.|
|void|printStackTrace()|Prints this throwable and its backtrace to the standard error stream.|
|void|printStackTrace​(PrintStream s)|Prints this throwable and its backtrace to the specified print stream.|
|void|printStackTrace​(PrintWriter s)|Prints this throwable and its backtrace to the specified print writer.|
|void|setStackTrace​(StackTraceElement[] stackTrace)|Sets the stack trace elements that will be returned by getStackTrace() and printed by printStackTrace() and related methods.|
|String|toString()|Returns a short description of this throwable.|


异常类的主要内容基本都在Throwable这个超级父类中了，其下面的子类基本都是空壳子，有个构造方法而已，这很好理解，异常类本身的作用就像一个标签一样，自然没必要有什么内容。


## 3 日志记录

### 3.1 java.util.logging（原生日志支持）

Java官方类库提供了原生的日志记录支持（since1.4），相关类都放在java.util.logging这个包中，包结构如下：

* java.util.logging
    - ErrorManager
    - **Formatter**--------格式化处理：修改日志格式
        + SimpleFormatter
        + XMLFormatter
    - **Handler**----------日志处理器：确定输出位置等
        + MemoryHandler
        + StreamHandler
            * ConsoleHandler--输出到控制台
            * FileHandler-----输出到文件
            * SocketHandler---网络输出
    - **Level**------------日志级别
    - **Logger**-----------日志本志：负责记录日志
    - LoggingPermission
    - LogManager
    - LogRecord

### 3.2 简单使用

最简单的，直接调用Logger的工厂方法获得一个全局Logger：
```java
public static void main(String[] args) {
        Logger.getGlobal().info("logger test");
        /**output
         * 三月 26, 2020 3:32:27 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 信息: logger test
         */
    }
```
这条语句获得一个全局Logger，并向控制台输出了一份info级别的日志信息。

#### 默认配置信息

默认的配置信息存储在jre/lib/logging.properties中。


### 3.2 Level（日志级别）

Level类定义了日志记录的等级：
```
    SEVERE      严重---级别最高
    WARNING     警告
    INFO        信息
    CONFIG      配置
    FINE        良好
    FINER       较好
    FINEST      最好---级别最低

    ALL         开启所有级别日志记录
    OFF         关闭所有级别日志记录
```
默认级别为INFO，也就是SEVERE、WARNING、INFO这三个级别，默认配置信息下控制台也只会输出这三个级别的信息，其它的信息不会输出：
```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        Logger.getGlobal().severe("logger test");
        Logger.getGlobal().warning("logger test");
        Logger.getGlobal().info("logger test");
        Logger.getGlobal().config("logger test");
        Logger.getGlobal().fine("logger test");
        Logger.getGlobal().finer("logger test");
        Logger.getGlobal().finest("logger test");
        /**output
         * 三月 26, 2020 3:32:27 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 严重: logger test
         * 三月 26, 2020 3:32:27 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 警告: logger test
         * 三月 26, 2020 3:32:27 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 信息: logger test
         */
    }
}
```

### 3.3 普通使用

#### 3.3.1 新建Logger

```java
    Logger logger = Logger.getLogger("myLogger");
```
gitLogger的参数是记录器的名字，它会先去找有没有已经存在的对象，没有就新建一个。

#### 3.3.2 新建Handler输出到控制台

```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        Logger myLogger = Logger.getLogger("myLogger");
        myLogger.setLevel(Level.ALL);
        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(FINE);
        myLogger.addHandler(consoleHandler);//为myLogger添加控制器

        myLogger.severe("logger test");
        myLogger.warning("logger test");
        myLogger.info("logger test");
        myLogger.config("logger test");
        myLogger.fine("logger test");
        myLogger.finer("logger test");
        myLogger.finest("logger test");
        /**
         * 三月 26, 2020 3:51:18 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 严重: logger test
         * 三月 26, 2020 3:51:18 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 严重: logger test
         * 三月 26, 2020 3:51:18 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 警告: logger test
         * 三月 26, 2020 3:51:18 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 警告: logger test
         * 三月 26, 2020 3:51:18 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 信息: logger test
         * 三月 26, 2020 3:51:18 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 信息: logger test
         * 三月 26, 2020 3:51:18 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 配置: logger test
         * 三月 26, 2020 3:51:18 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 详细: logger test
         *
         */
    }
}
```
可以看到前三个级别都输出了两次，这是因为myLogger本身还有一个默认的Handler，可以通过`myLogger.setUseParentHandlers(false);`禁用：
```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        Logger myLogger = Logger.getLogger("myLogger");
        myLogger.setLevel(Level.ALL);
        myLogger.setUseParentHandlers(false);
        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(FINE);
        myLogger.addHandler(consoleHandler);

        myLogger.severe("logger test");
        myLogger.warning("logger test");
        myLogger.info("logger test");
        myLogger.config("logger test");
        myLogger.fine("logger test");
        myLogger.finer("logger test");
        myLogger.finest("logger test");
        /**
         * 三月 26, 2020 3:53:37 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 严重: logger test
         * 三月 26, 2020 3:53:37 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 警告: logger test
         * 三月 26, 2020 3:53:37 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 信息: logger test
         * 三月 26, 2020 3:53:37 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 配置: logger test
         * 三月 26, 2020 3:53:37 下午 com.vilaseaka.main.AboutExceptionHandling main
         * 详细: logger test
         */
    }
}
```

#### 3.3.3 新建Handler输出到文件

输出到文件与输出到控制台没啥差别，添加一个FileHandler即可：
```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        Logger myLogger = Logger.getLogger("myLogger");
        myLogger.setLevel(Level.ALL);
        myLogger.setUseParentHandlers(false);

        FileHandler fileHandler = new FileHandler("log.txt");
        fileHandler.setLevel(Level.ALL);
        myLogger.addHandler(fileHandler);

        myLogger.severe("logger test");
        myLogger.warning("logger test");
        myLogger.info("logger test");
        myLogger.config("logger test");
        myLogger.fine("logger test");
        myLogger.finer("logger test");
        myLogger.finest("logger test");
    }
}
```
上述代码会在项目运行的根目录中生成一个log.txt，不过默认的格式是XML形式的。

系统提供了两个Formatter：SimpleFormatter普通文本格式，XMLFormatter XML格式。我们可以自己指定一个Formatter，也可以新建一个Formatter，来处理日志输出的格式。

```java
public class AboutExceptionHandling {
    public static void main(String[] args) {
        Logger myLogger = Logger.getLogger("myLogger");
        myLogger.setLevel(Level.ALL);
        myLogger.setUseParentHandlers(false);

        FileHandler fileHandler = new FileHandler("log.txt");
        fileHandler.setLevel(Level.ALL);
        //指定一个内置的SimpleFormatter
        fileHandler.setFormatter(new SimpleFormatter());
        myLogger.addHandler(fileHandler);

        myLogger.severe("logger test");
        myLogger.warning("logger test");
        myLogger.info("logger test");
        myLogger.config("logger test");
        myLogger.fine("logger test");
        myLogger.finer("logger test");
        myLogger.finest("logger test");
    }
}
```
```
    //log.txt:
    三月 26, 2020 4:10:26 下午 com.vilaseaka.main.AboutExceptionHandling main
    严重: logger test
    三月 26, 2020 4:10:26 下午 com.vilaseaka.main.AboutExceptionHandling main
    警告: logger test
    三月 26, 2020 4:10:26 下午 com.vilaseaka.main.AboutExceptionHandling main
    信息: logger test
    三月 26, 2020 4:10:26 下午 com.vilaseaka.main.AboutExceptionHandling main
    配置: logger test
    三月 26, 2020 4:10:26 下午 com.vilaseaka.main.AboutExceptionHandling main
    详细: logger test
    三月 26, 2020 4:10:26 下午 com.vilaseaka.main.AboutExceptionHandling main
    较详细: logger test
    三月 26, 2020 4:10:26 下午 com.vilaseaka.main.AboutExceptionHandling main
    非常详细: logger test
```


