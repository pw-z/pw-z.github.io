# JAVA基础知识复盘（七）：泛型程序设计入门
*2020033101-java-basic-knowledge-review-7-generic-programming*  
*Posted on 2020.04.02 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


* [JAVA基础知识复盘（七）：泛型程序设计](#java%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E5%A4%8D%E7%9B%98%E4%B8%83%E6%B3%9B%E5%9E%8B%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1)
    * [1 认识泛型](#1-%E8%AE%A4%E8%AF%86%E6%B3%9B%E5%9E%8B)
        * [1\.1 直观感受](#11-%E7%9B%B4%E8%A7%82%E6%84%9F%E5%8F%97)
        * [1\.2 具体概念](#12-%E5%85%B7%E4%BD%93%E6%A6%82%E5%BF%B5)
    * [2 使用泛型](#2-%E4%BD%BF%E7%94%A8%E6%B3%9B%E5%9E%8B)
        * [2\.1 调用现有泛型类](#21-%E8%B0%83%E7%94%A8%E7%8E%B0%E6%9C%89%E6%B3%9B%E5%9E%8B%E7%B1%BB)
        * [2\.2 构建简单泛型类](#22-%E6%9E%84%E5%BB%BA%E7%AE%80%E5%8D%95%E6%B3%9B%E5%9E%8B%E7%B1%BB)
            * [2\.2\.1 命名规范](#221-%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83)
        * [2\.3 限定类型参数](#23-%E9%99%90%E5%AE%9A%E7%B1%BB%E5%9E%8B%E5%8F%82%E6%95%B0)
    * [3 理解泛型](#3-%E7%90%86%E8%A7%A3%E6%B3%9B%E5%9E%8B)
        * [3\.1 类型安全](#31-%E7%B1%BB%E5%9E%8B%E5%AE%89%E5%85%A8)
        * [3\.2 类型擦除](#32-%E7%B1%BB%E5%9E%8B%E6%93%A6%E9%99%A4)
            * [3\.2\.1 问题引入](#321-%E9%97%AE%E9%A2%98%E5%BC%95%E5%85%A5)
            * [3\.2\.2 类型擦除具体过程](#322-%E7%B1%BB%E5%9E%8B%E6%93%A6%E9%99%A4%E5%85%B7%E4%BD%93%E8%BF%87%E7%A8%8B)
                * [对【无】限定类型变量的类进行类型擦除](#%E5%AF%B9%E6%97%A0%E9%99%90%E5%AE%9A%E7%B1%BB%E5%9E%8B%E5%8F%98%E9%87%8F%E7%9A%84%E7%B1%BB%E8%BF%9B%E8%A1%8C%E7%B1%BB%E5%9E%8B%E6%93%A6%E9%99%A4)
                * [对【有】限定类型变量的类进行类型擦除](#%E5%AF%B9%E6%9C%89%E9%99%90%E5%AE%9A%E7%B1%BB%E5%9E%8B%E5%8F%98%E9%87%8F%E7%9A%84%E7%B1%BB%E8%BF%9B%E8%A1%8C%E7%B1%BB%E5%9E%8B%E6%93%A6%E9%99%A4)
                * [对泛型方法进行类型擦除](#%E5%AF%B9%E6%B3%9B%E5%9E%8B%E6%96%B9%E6%B3%95%E8%BF%9B%E8%A1%8C%E7%B1%BB%E5%9E%8B%E6%93%A6%E9%99%A4)
            * [3\.2\.3 翻译执行类型擦除后的代码](#323-%E7%BF%BB%E8%AF%91%E6%89%A7%E8%A1%8C%E7%B1%BB%E5%9E%8B%E6%93%A6%E9%99%A4%E5%90%8E%E7%9A%84%E4%BB%A3%E7%A0%81)
                * [为何通过类型擦除实现泛型](#%E4%B8%BA%E4%BD%95%E9%80%9A%E8%BF%87%E7%B1%BB%E5%9E%8B%E6%93%A6%E9%99%A4%E5%AE%9E%E7%8E%B0%E6%B3%9B%E5%9E%8B)
    * [4 Java泛型局限性总结](#4-java%E6%B3%9B%E5%9E%8B%E5%B1%80%E9%99%90%E6%80%A7%E6%80%BB%E7%BB%93)
    * [5 小结](#5-%E5%B0%8F%E7%BB%93)


## 1 认识泛型

### 1.1 直观感受

泛型这个概念是在JavaSE5引入的，先上代码直观感受一下**泛型**：
```java
//代码1-1
class TestGeneric {
    public static void main(String[] args) {
        ArrayList<Integer> integerList = new ArrayList<>();
        ArrayList<String> stringList = new ArrayList<>();
    }
}
```
代码1-1中的ArrayList是Java标准库中提供的容器，其后面的尖括号<>中传入了一个具体的类型参数（type parameters），从而新建了可以存放对应类型对象的ArrayList（数组列表），简单来说，这里我们只有一种“桶”，但可以盛水也可以盛牛奶（还可以盛很多其他液体），这就是泛型的典型应用，乍一看似乎跟多态有点像，再看一下这份代码：
```java
//代码1-2
class TestGeneric {
    public static void main(String[] args) {
        List<Integer> integerList = new ArrayList<Integer>();
        List<String> stringList = new ArrayList<String>();
    }
}
```
代码1-2中将`ArrayList<>()`尖括号中本可以省略的类型参数给加上了，同时声明的引用也换成了List，这不是像，这就是多态。再加一行：
```java
//代码1-3
class TestGeneric {
    public static void main(String[] args) {
        List<Integer> integerList = new ArrayList<>();
        List<String> stringList = new ArrayList<>();
        List<String> stringList2 = new LinkedList<>();
    }
}
```
代码1-3这里可以简单把List当成ArrayList的父类（虽然List只是其父类实现的接口），我们声明了父类引用（List）并将引用指向了通过new实例化的子类对象，这是向上转型，同时子类又有不同的形式（ArrayList<Integer>()，LinkedList<>()），展现出多种形态，可以说这是典型的多态了。

多态归多态，与尖括号没太大关系，尖括号（泛型）的存在，是在这一套多态的体系之下横向展开了无数微调版拓本，List<Integer>、List<String>、List<Float>、List<Double>…这可以说是另一个维度下另一种形式的多态，只不过设计者赋予其一个更具体的名字叫“泛型”而已。

### 1.2 具体概念

拆开看**泛型**二字：泛，generic，一般的、通用的，型，参数类型。

泛型，也就是通用的参数类型，拿前面代码来说，一个List可以存放某种对象，这个对象既可以是Integer也可以是String，一个List容器可以适用于多种具体的类型，如果某个方法实现了泛型机制，那么这个方法也可以以多种类型作为参数。将“类型”设置为一个参数，调用时再通过传参确定类型，即**参数化类型**，这是泛型编程最基本也最核心的概念，它让某个类或某个方法拥有了极强的泛化能力。

可以想象，如果没有泛型机制，我们得为每种具体的对象单独实现一套List、ArrayList、LinkedList（StringList、StringArrayList、StringLinkedList;IntList、IntArrayList、IntLinkedList…），再单独实现一套Set，单独实现一套Map……那得是多么臃肿的体系，多态无法（至少无法很好地）解决这种问题，泛型机制可以。


## 2 使用泛型

### 2.1 调用现有泛型类

Java的日常使用中最常见的泛型类就是标准类库中的各种容器类了，比如前面拿来举例子的ArrayList、LinkedList等，这些类的使用很简单，给出对应的类型参数即可:
```java
    List<String> stringList = new ArrayList<>();
```
JavaSE7之后，new语句中（构造函数）的类型参数（<>中的参数）可以省略掉，因为编译器可以从变量定义处（List<String> stringList）得到足够的信息了。

### 2.2 构建简单泛型类

如节标题，泛型可用于构建类、方法乃至接口，这里先构建一个简单的泛型类——“Hero栈”（是个假栈，只能存一个对象）：
```java
class HeroStack<T>{//英雄栈
    private T hero;
    //注意如下两个不是泛型方法，它们只是使用了泛型类的类型参数而已
    public void push(T newHero){this.hero = newHero;}
    public T pop(){return hero;} 
}
```
接着尝试一下泛型方法（将类型参数放在修饰符后返回类型前），顺便将场景补充完整：
```java
//英雄栈
class HeroStack<T>{
    private T hero;
    //注意如下两个不是泛型方法，它们只是使用了泛型类的类型参数而已
    public void push(T newHero){ this.hero = newHero; }
    public T pop(){
        return hero;
    }

    /**
     * 英雄升级器
     * @param t 具体某个英雄
     * @param <T> 英雄类型
     * @return 升级后的英雄
     */
    public static <T> T updateHero(T t){
        System.out.println("升级英雄中……");
        //TODO something
        System.out.println("英雄升级完毕（才没有）");
        return t;
    }
}
//兽人英雄
class BeastHero implements SuperPowerTag {
    private String name;
    public BeastHero(String name) {
        this.name = name;
        System.out.println("新建兽人英雄：" + name);
    }
    /*******************superPower*******************/
    public String superPower = "战争哀嚎";
    public void superPower() {
        System.out.println(name + "超能力：" + superPower);
    }
}
interface SuperPowerTag { } //标签接口：拥有超级能力的类，都有superPower方法
//测试类
class TempTest{
    public static void main(String[] args) {
        HeroStack<BeastHero> beastHeroStack = new HeroStack<>();
        BeastHero beastHero = new BeastHero("狼人");
        beastHeroStack.push(beastHero);
        beastHeroStack.pop().superPower();

        HeroStack.<BeastHero>updateHero(beastHero);
    }
    /**
     * 新建兽人英雄：狼人
     * 狼人超能力：战争哀嚎
     * 升级英雄中……
     * 英雄升级完毕（才没有）
     */
}
```
上面代码中HeroStack<T>只存一个英雄，updateHero(T t)这个泛型方法也只实现了一个空壳子，基本没什么意义，稍后会讲到，由于**类型擦除**的原因，实际在进行Java泛型编程的时候难以进行很多常规操作，使得实现一个完善的泛型类、方法很费力气。这里先知道泛型类、方法是如何声明的即可。

#### 2.2.1 命名规范

>类型变量使用大写形式，且比较短，这是很常见的。在 Java 库中，使用变量 E 表示集合的元素类型，K 和 V 分别表示表的关键字与值的类型。T ( 需要时还可以用临近的 字母 U 和 S ) 表示“ 任意类型”。  
>*《Java核心技术》 第八章泛型程序设计 8.2*


### 2.3 限定类型参数

继续讲前面构建的HeroStack，它目前什么都能存，不光拥有超能力的对象可以放进去，普通的随便一个类都可以，解决这个局面就需要对类型参数进行限制：
```java
class HeroStack<T extends SuperPowerTag>{
    //……
}
class NormalPeople{
    //……
}
class TempTest{
    public static void main(String[] args) {
        HeroStack<NormalPeople> normalPeopleHeroStack = new HeroStack<NormalPeople>();//错误
    }
}
```
class HeroStack<T extends SuperPowerTag>{}通过SuperPowerTag对T进行了限定，如此一来没有实现SuperPowerTag接口的NormalPeople类就不能作为类型参数初始化HeroStack了。

参数限制的格式为**<T extends BoundingType1 & BoundingType2\>**，无论T是继承父类还是实现接口，这里都使用extends关键字:

><T extends BoundingType> 表示 T 应该是绑定类型的子类型（subtype)。T 和绑定类型可以是类，也可以是接口。选择关键字 extends 的原因是更接近子类的概念，并且 Java 的设计者也不打算在语言中再添加一个新的关键字（如 sub)。  
>*《Java核心技术》 第八章泛型程序设计 8.2*  


## 3 理解泛型

### 3.1 类型安全

没有泛型机制之前，Java是通过类型转换实现“泛型”的：既然不能为每种特定类型写一个对应的List，那干脆只存它们的超级父类，Object类，这样就不用担心放不下某种类了，毕竟所有的类都是Object类。这种解决方案有着显而易见的弊端，类型转换本身就不方便，转换期间很容易隐含不安全的操作：
```java
//代码3-1 一个伪List，只能存一个Object
class TestList{
    private Object o;
    public Object getO() {
        return o;
    }
    public void add(Object o) {
        this.o = o;
    }
}
class Baby {
    public void cry(){
        System.out.println("Baby is crying");
    }
}
class Dog {
    public void bark(){
        System.out.println("Dog is barking");
    }
}
public class Main {
    public static void main(String[] args) {
        TestList testList = new TestList();
        Baby baby = new Baby();
        Dog dog = new Dog();
        testList.add(baby);
        ((Baby)testList.getO()).cry(); // √
        testList.add(dog);
        ((Dog)testList.getO()).bark(); // √
    }
    /**
     * Baby is crying
     * Dog is barking
     */
}
```
以上存是很好存，因为有自动向上转型，取出来的时候却很麻烦，需要强制类型转换才能正常使用，这里虽然没有报什么问题，但本身这个TestList什么都能存就是个问题，我们在多数场景下希望的是，它什么都能存，但它存一种对象的时候只存那种对象，而不是不加分辨的混合着来，如果在存Baby的时候不小心存了一条Dog进去，那么调用Baby方法的时候就会调用不到，这是在程序里隐含着的危险。

泛型很好地解决了这个问题，通过参数化类型，指定这个什么都能存的容器这次只存某一种对象，这样一来不再需要强制转换了，隐含的类型错误也能在编译阶段被检查出来，所以说**Java泛型编程某种程度上实现了类型安全**（*安全总是相对而言的*）。


### 3.2 类型擦除

#### 3.2.1 问题引入

通过前面的接触，我们似乎拥有了一个强大的泛化机制（*别急，这就将它打回原形*），回顾前面HeroStack代码：
```java
//代码3-2-1
class HeroStack<T>{
    private T hero;
    public void push(T newHero){
        this.hero = newHero;
    }
    public T pop(){
        return hero;
    }
}
```
代码3-2-1这里，与代码3-1中只能存一个对象的伪List一样，是一个伪Stack（也只能存一个对象），若想让它变成一个真正的能存多种、多个对象的Stack，是不是直接构造一个“T数组”就行了呢？像这样：
```java
//代码3-2-2
class HeroStack<T>{
    private T[] hero = new T[10]; //！
    private int index = 0;
    public void push(T newHero){
        this.hero[index++] = newHero;
    }
    public T pop(){
        return hero[--index];
    }
}
```
理想很美好，但这有点高估目前Java中泛型机制的能力了，现实是上述代码根本无法通过编译。报如下错误：
```shell
G:\REPO\AboutJava\src\com\vilaseaka\main\AboutGenericProgramming.java
    Error:(64, 24) java: 创建泛型数组
```
**Java不支持创建泛型数组**，这是相当大的一个限制，但这还不算完，Java的泛型机制还有更多的限制，具体来说，**运行时需要知道具体类型信息的操作都无法直接进行**。

所谓类型擦除，就是指在底层代码中，这些你很需要的，关于类型参数的类型信息，都被抹去了，比如说前面通过List<String>达成了类型安全，但底层存放的其实还是Object。这也是为何说**Java的泛型只是一种“伪泛型”**，因为它是在编译器以上的层面实现的语法糖，虚拟机层面是没有泛型的。通过编译器的类型擦除处理后，.class字节码文件中不再包含有关泛型的相关信息。


#### 3.2.2 类型擦除具体过程

类型擦除的具体内容：  
1. 用原始类型（raw type）替换泛型
2. 用第一个限定类型变量替换类型参数，无限定的用Object替换

##### 对【无】限定类型变量的类进行类型擦除

以代码3-2-1为例：
```java
//代码3-2-1
class HeroStack<T>{
    private T hero;
    public void push(T newHero){
        this.hero = newHero;
    }
    public T pop(){
        return hero;
    }
}
```
类型擦除之后：
```java
class HeroStack {
    private Object hero;
    public void push(Object newHero){
        this.hero = newHero;
    }
    public Object pop(){
        return hero;
    }
}
```

##### 对【有】限定类型变量的类进行类型擦除

泛型形式：
```java
class HeroStack<T extends SuperPowerTag>{
    private T hero;
    public void push(T newHero){ this.hero = newHero; }
    public T pop(){
        return hero;
    }
}
```
翻译后：
```java
class HeroStack{
    private SuperPowerTag hero;
    public void push(SuperPowerTag newHero){ this.hero = newHero; }
    public SuperPowerTag pop(){
        return hero;
    }
}
```

##### 对泛型方法进行类型擦除

对方法进行类型擦除的操作与对类是一样的，换汤不换药

泛型形式：
```java
public static <T> T updateHero(T t){
    System.out.println("升级英雄中……");
    //TODO something
    System.out.println("英雄升级完毕（才没有）");
    return t;
}
```
翻译后：
```java
public static Object updateHero(Object t){
    System.out.println("升级英雄中……");
    //TODO something
    System.out.println("英雄升级完毕（才没有）");
    return t;
}
```

#### 3.2.3 翻译执行类型擦除后的代码

前面已经说过，Java的泛型实现了类型安全，但是底层又进行了类型擦除，将限制类型的类型参数给搞没了，那么类型安全又是从何保障的呢？这里差一步翻译的过程，刚刚将泛型代码进行类型擦除，这是正向翻译，等我们调用这些翻译后的时候，不是直接调用，编译器为我们处理好了反向翻译的过程：

从翻译后的代码开始看：
```java
public static Object updateHero(Object t){
    System.out.println("升级英雄中……");
    //TODO something
    System.out.println("英雄升级完毕（才没有）");
    return t;
}
```
这个翻译后的泛型方法将会返回一个Object类型的对象，返回之后编译器在对应的地方插入了强制转换，将其变回原来声明的类型，也就是说：
```java
    BeastHero beastHeroPlus = HeroStack.<BeastHero>updateHero(beastHero);
```
相当于：
```java
    BeastHero beastHeroPlus = (BeastHero) HeroStack.updateHero((Object) beastHero);
```

有点熟悉啊！没有泛型机制之前咱们不就是这么实现“泛型”的么！没错，就是这么回事！借这个话头回顾一下Java为什么通过类型擦除来实现这么个“伪泛型”：

##### 为何通过类型擦除实现泛型

前面说过了，JavaSE5才引入泛型，到这个阶段旧有的类库以及使用旧有类库开发的项目已经有了相当的规模，大概后引入特性时最首要该考虑的就是向前兼容问题了吧，Java的设计者们决定实现这个“向前兼容”，综合考虑之下选择了类型擦除的方案。

>擦除主要的正当理由是从非泛化代码到泛化代码的转变过程，以及在不破坏现有类型的情况下，将泛型融入Java语言。
>*《Java编程思想》15.7.3*


## 4 Java泛型局限性总结

*这份总结来自《Java核心技术》8.6，书读完吸收掉了，这里就偷懒列个表概览下，不再举例子详细实践*

1. 不能用基本类型实例化类型参数
```java
    List<int> intsList1 = new ArrayList<>();     // ×
    List<Integer> intsList2 = new ArrayList<>(); // √
```
2. 运行时类型查询只适用于原始类型
```java
public static Object updateHero(Object t){
    System.out.println("升级英雄中……");
    //TODO something
    return t;
}//运行时只有Object t（或其他原始类型），而没有T t (将T替换成你传入的那个类型参数)
```
3. 不能创建参数化类型的数组
```java
    HeroStack<BeastHero>[] beastHero = new HeroStack<BeastHero>[10];  //这是无法通过编译检查滴
```
4. 不能实例化类型变量
```java
class HeroStack<T>{//英雄栈
    private T hero;
    public HeroStack(T hero) {
        this.hero = new T(); // ×  类型擦除后这里就成了new Objict();
    }
}
```
5. 不能构造泛型数组
```java
    T[] t = new T[10]; //与3一个性质，这也是无法通过编译检查滴
```
6. 泛型类的静态上下文中类型变量无效
```java
//不能在静态域或方法中引用类型变量
class HeroStack<T extends SuperPowerTag>{
    private T hero;
    static {
        T test;//这也是无法通过编译检查滴
    }
}
```
7. 不能抛出或捕获泛型类的实例
```java
//既不能抛出也不能捕获泛型类对象，甚至泛型类扩展 Throwable 都是不合法的
class HeroStack<T extends Throwable>{
    public <T> T testInStack(T t){
        try {
            //……
        }catch(T t){ //这样不行！
            throw t; //这样也不行！
        }
        return t;
    }
}
```

## 5 小结

整篇文档下来，我们似乎见识到了一个非常难用的Java泛型，当我们只想持有对象的时候还好，一旦想对具体的对象进行某些操作，就会发现因为类型擦除的缘故，处处受限很多需求难以实现，Java的设计者面对这种情况是给出了补偿机制的，很重要的两点就是**通配符**和**反射机制**，这两点本来也是这篇文档想总结完的，今天有点累了就偷懒到底吧，另开文档单独总结。



