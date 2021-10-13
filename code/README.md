## [P.W. Z](https://www.pwz.wiki) / [CODE](https://www.pwz.wiki/code)

以下代码均开源、归档在此博客`pwz.wiki/blog`所属仓库的二级目录`pwz.wiki/code`下，该目录下每一个类似`api-autotest-tool`、`expression-check`这种用纯小写单词加短横线风格命名的文件夹都是一个独立的带有`readme.md`的子工程，因基本都是练习性质的代码，称不上项目，不单独建仓库。

|名称|简介|
|---:|:---|
|[APIAutotestTool][API_Autotest_Tool]|接口自动化测试框架，Python3实现。用Excel管理用例，参数化逐条执行。支持参数获取及验证、数据库验证、远程连接主机执行linux命令或SQL（用于准备测试环境、预埋测试数据、重置测试环境），最终生成测试报告。为了练习Python，以上包括生成测试报告的模块都是纯造轮子实现，`Pytest + Allure` 已经单拉了个目录引入，但暂时没有使用需要，待完善。<br><br>*如下两篇博客记录了大致的实现过程：*<br>[*An API Autotest Tool Part1: Basic Functions Implementation*](https://www.pwz.wiki/blog/2021/07/2021071901-an-api-autotest-tool-part1-basic-functions-implementation)<br>[*An API Autotest Tool Part2: Generate Test Report from Scratch*](https://www.pwz.wiki/blog/2021/07/2021071902-an-api-autotest-tool-part2-generate-test-report-from-scratch)
|[TestlinkImporter][TestlinkImporter]|Testlink导入工具，公司用testlink管理用例，平时都是用excel写完往里导入，testlink不支持直接导入excel，遂写了这个工具将excel转成支持testlink导入的xml格式，后来更新了调用testlink的api直接往里灌数据的功能。<br><br>*实现过程见这篇博客：*<br>[*Import Testcases From Excel to Testlink*](https://www.pwz.wiki/blog/2021/06/20210623-import-testcases-from-excel-to-testlink)|
|[TestStatusReporter][TestStatusReporter]|一个小爬虫，按照一定格式获取Jira以及Testlink的数据信息，通过钉钉机器人发送到项目群里，每天定时获取数据进行测试进度的报告，内容包括缺陷的情况以及用例执行的情况。<br><br>*实现过程见这篇博客：*<br>[*获取Jira与Testlink测试概况并推送消息到钉钉机器人*](https://www.pwz.wiki/blog/2021/05/2021053101-collect-test-status-of-jira-and-testlink-then-send-msg-to-dingtalkchatbot)|
|[Datastructure021][Datastructure_021]|基本数据结构的C++实现，覆盖的数据结构包括线性表、栈、队列、串、二叉树，另外已包含了排序算法，后续查找算法还有基本的图论内容也会补充过来。<br><br>*如下博客将代码进行了梳理：*<br>[*Data Structure from Scratch: LinearList & Linkedlist*](https://www.pwz.wiki/blog/2021/07/2021070501-data-structure-from-scratch-linearlist-and-linkedlist)<br>[*Data Structure from Scratch: Stack & Queue*](https://www.pwz.wiki/blog/2021/07/2021072901-data-structure-from-scratch-stack-and-queue)<br>[*Data Structure from Scratch: String*](https://www.pwz.wiki/blog/2021/08/2021080101-data-structure-from-scratch-string)<br>[*Data Structure from Scratch: Binary Tree*](https://www.pwz.wiki/blog/2021/08/2021083101-data-structure-from-scratch-tree)<br>[*Data Structure from Scratch: Sorting Algorithm*](https://www.pwz.wiki/blog/2021/09/20210905-data-structure-from-scratch-sort)|
|[BankCreditMS][BCMS]|银行积分管理系统。使⽤`Java + JavaFX + Derby(嵌⼊式数据库)`构建的⼀套C/S架构的信息管理系统，包含了系统本身（`./source/BCMS`*）以及系统外单独构建的证书生成小程序（`./source/BCMSLicenseGenerator`）。功能方面，除了些许界面涉及到一点稍复杂的业务逻辑，主要是增删改查。功能之外，在这个小项目里首次接触了`Java的GUI开发`、`嵌入式数据库`、`软件注册机制`等新鲜的东西。|


[API_Autotest_Tool]:./archived/api-autotest-tool/
[BCMS]:./archived/bank-credit-management-system/
[Datastructure_021]:./archived/data-structure-from-scratch/
[TestlinkImporter]:./archived/excel-to-testlink/
[TestStatusReporter]:./archived/jira-testlink-dingtalk/