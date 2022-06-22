## [P.W. Z](https://www.pwz.wiki) / [CODE](https://www.pwz.wiki/code)

以下代码归档在此博客所属仓库的二级目录`pwz.wiki/code`下，该目录下每一个类似`api-autotest-tool`、`expression-check`这种用纯小写单词加短横线风格命名的文件夹都是一个独立的带有`readme.md`的子工程，基本都是练习代码，不单独建仓库。

|名称| 简介|
|---:|:-----------|
|[APIAutotestTool][API_Autotest_Tool]| 接口自动化测试框架，Python3实现。用Excel管理用例，参数化逐条执行。支持参数获取及验证、数据库验证、远程连接主机执行linux命令或SQL（用于准备测试环境、预埋测试数据、重置测试环境），最终生成测试报告。为了练习Python，以上包括生成测试报告的模块都是纯造轮子实现，`Pytest + Allure` 已经单拉了个目录引入，但暂时没有使用需要，待完善。<br><br>*See > [An API Autotest Tool](../blog/2021-an-api-autotest-tool/20210719-an-api-autotest-tool)* |
|[BankCreditMS][BCMS]| 银行积分管理系统。使⽤`Java + JavaFX + Derby(嵌⼊式数据库)`构建的⼀套C/S架构的信息管理系统，包含了系统本身（`./source/BCMS`*）以及系统外单独构建的证书生成小程序（`./source/BCMSLicenseGenerator`）。功能方面，除了些许界面涉及到一点稍复杂的业务逻辑，主要是增删改查。功能之外，在这个小项目里首次接触了`Java的GUI开发`、`嵌入式数据库`、`软件注册机制`等新鲜的东西。|
|[StudentAchievementMS][SAMS]|学生成绩管理系统，C语言大作业，关于软件开发最古早的回忆。|


[API_Autotest_Tool]:./archived/api-autotest-tool/
[BCMS]:./archived/bank-credit-management-system/
[SAMS]:./archived/c-programming-homework/