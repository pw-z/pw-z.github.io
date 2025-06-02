# 关于架构分层及缩写名称的主题阅读与随笔

*Posted on 2022.08.07 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 

最近做Java项目的开发，不太理解一些项目结构从何而来（为啥这样设计），也不懂怎么那么多各种缩写，写代码被“这里应该抽象个什么类（最纠结的是命名），这个类应该放在哪里才更合理”之类的问题烦扰，做一次主题阅读。

归档下还不错的阅读材料（出处 - 标题 #年份）：

* [JAVA架构师笔记 - 大型网站架构演进历程 #2022](https://zq99299.github.io/note-architect/ztc/00/01.html)
* [JAVA架构师笔记 - 架构分层：我们为什么一定要这么做 #2022](https://zq99299.github.io/note-architect/hc/01/02.html)
* [Sofastack - 蚂蚁金服的业务系统模块化之模块化隔离方案 #2018](https://www.sofastack.tech/blog/sofastack-modular-isolation/)
* [Medium - DAO, DTO, PO, SO, BO, VO… WTF..? #2021](https://colin-but.medium.com/dao-dto-po-so-bo-vo-wtf-6673c9dd5437)


做份小结收敛下底层认知：

架构的设计规划、代码的组织编排，已有太多成熟方法论可以参考，道与术均有，从底层的OOP，各种设计模式，到基本的MVC分层，DDD思想，根源上是在追求怎么在满足系统需求的情况下写出清晰易于维护的代码，需求&膨胀的项目体量不断推动着架构&项目结构的发展，结合Java在企业应用尤其是Web应用中如此大的市场占有率，催生出较多大家公认“这样写比较好”的“标准写法”。理解好各种“标准写法”的来龙去脉，编码过程场景匹配才使用，没有银弹，不要强行标准化，不要过度设计。