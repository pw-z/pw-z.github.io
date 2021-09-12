## [P.W. Z](https://www.pwz.wiki) / [CODE](https://www.pwz.wiki/code)

以下代码均开源、归档在此博客`pwz.wiki/blog`所属仓库的二级目录`pwz.wiki/code`下，基本都是练习性质的代码，称不上项目，不单独建仓库。

|名称|简介|
|:---|:---|
|[APIAutotestTool][API_Autotest_Tool]|接口自动化测试框架，Python3实现。用Excel管理用例，参数化逐条执行。支持参数获取及验证、数据库验证、远程连接主机执行linux命令或SQL（用于准备测试环境、预埋测试数据、重置测试环境），最终生成测试报告。为了练习Python，以上包括生成测试报告的模块都是纯造轮子实现，`Pytest + Allure` 已经单拉了个目录引入，但暂时没有使用需要，待完善。<br><br>这两篇博客记录了大致的实现过程：<br>[An API Autotest Tool Part1: Basic Functions Implementation](https://www.pwz.wiki/blog/2021/07/2021071901-an-api-autotest-tool-part1-basic-functions-implementation)<br>[An API Autotest Tool Part2: Generate Test Report from Scratch](https://www.pwz.wiki/blog/2021/07/2021071902-an-api-autotest-tool-part2-generate-test-report-from-scratch)
|[Datastructure021][Datastructure_021]|基本数据结构的C++实现，覆盖的数据结构包括线性表、栈、队列、串、二叉树，另外已包含了排序算法，后续查找算法还有基本的图论内容也会补充过来。<br><br>如下博客将代码进行了梳理：<br>[Data Structure from Scratch: LinearList & Linkedlist](https://www.pwz.wiki/blog/2021/07/2021070501-data-structure-from-scratch-linearlist-and-linkedlist)<br>[Data Structure from Scratch: Stack & Queue](https://www.pwz.wiki/blog/2021/07/2021072901-data-structure-from-scratch-stack-and-queue)<br>[Data Structure from Scratch: String](https://www.pwz.wiki/blog/2021/08/2021080101-data-structure-from-scratch-string)<br>[Data Structure from Scratch: Binary Tree](https://www.pwz.wiki/blog/2021/08/2021083101-data-structure-from-scratch-tree)<br>[Data Structure from Scratch: Sorting Algorithm](https://www.pwz.wiki/blog/2021/09/20210905-data-structure-from-scratch-sort)|
|[TestlinkImporter][TestlinkImporter]|将Excel中的用例直接远程导入到testlink的指定项目中，项目及TestSuite不存在则直接创建|
|[BankCreditMS][BCMS]|银行积分管理系统。使⽤`Java + JavaFX + Derby(嵌⼊式数据库)`构建的⼀套C/S架构的信息管理系统，包含了系统本身（`./source/BCMS`*）以及系统外单独构建的证书生成小程序（`./source/BCMSLicenseGenerator`）。功能方面，除了些许界面涉及到一点稍复杂的业务逻辑，主要是增删改查。功能之外，在这个小项目里首次接触了`Java的GUI开发`、`嵌入式数据库`、`软件注册机制`等新鲜的东西。|

未整理完，待更新...


[API_Autotest_Tool]:./archived/api-autotest-tool/readme.md
[BCMS]:./ARCHIVED/bank-credit-management-system/readme.md
[Datastructure_021]:./archived/data-structure-from-scratch/readme.md
[TestlinkImporter]:./archived/excel-to-testlink/README.md