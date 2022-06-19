# 软件开发实践路线小结

- [迭代1：控制台程序提供简单的输入输出逻辑](#迭代1控制台程序提供简单的输入输出逻辑)
- [迭代2：提供本地客户端（GUI开发）并引入数据库](#迭代2提供本地客户端gui开发并引入数据库)
- [迭代3：提供网页客户端（Web开发）（不使用框架，造轮子）](#迭代3提供网页客户端web开发不使用框架造轮子)
- [迭代4：提供网页客户端（Web开发）（使用并理解框架的能力）](#迭代4提供网页客户端web开发使用并理解框架的能力)
- [迭代5：高并发高可用场景与解决方案](#迭代5高并发高可用场景与解决方案)

## 迭代1：控制台程序提供简单的输入输出逻辑

迭代1实现最原始形式的本地控制台程序，通过控制台接收用户输入，提供相应服务或者在未命中服务场景下给出通用回复。

迭代1完全使用java实现，最终交付物汇总如下:

* PRD：[OraKit Sprint 1 PRD](./sprint1_console_style/prd)
* JAVA：[迭代用到的Java内容代码实践](。/sprint1_console_style/a_review_java_basic/readme)
* OraKit2.0：[本次迭代正式代码及说明文档](./sprint1_console_style/b_orakit_sprint_1/readme)
* Reference：[本次迭代参考资料汇总](./sprint1_console_style/reference)


## 迭代2：提供本地客户端（GUI开发）并引入数据库

迭代2从迭代1的控制台程序升级到有图形界面的版本，实现了界面框架以及若干功能点，引入数据库支持用户管理功能。

迭代2完全使用python实现，最终交付物汇总如下:

* PRD：[OraKit Sprint 2 PRD](./sprint2_gui_and_db/prd)
* GUI：
  * [Python内置GUI模块~Tkinter学习材料整理](./sprint2_gui_and_db/a_try_python_gui_lib_tkinter/0-reference)
  * Tkinter快速上手的代码实践若干
    1. [快速实现一个文本编辑器对tkinter的使用有个初步印象](./sprint2_gui_and_db/a_try_python_gui_lib_tkinter/1-tkinter-demo-text-editor.py)
    2. [Tkinter乃至更多的GUI库如何学习、应用（思路整理+代码实践）](./sprint2_gui_and_db/a_try_python_gui_lib_tkinter/2-tkinter-brief-and-gui-dev-roadmap-summary.py)
    3. [对Tkinter的菜单组件进一步学习](./sprint2_gui_and_db/a_try_python_gui_lib_tkinter/3-tkinter-more-about-munu.py)
    4. [Tkinter按键映射检查（键盘事件绑定需要提供对应按键的编码，查表没有想象中方便，不如直接敲下键盘）](./sprint2_gui_and_db/a_try_python_gui_lib_tkinter/4-tkinpter-keysym-tester.py)
* DB：[Python内置数据库模块~sqlite3相关操作代码实践](./sprint2_gui_and_db/b_try_python_buildin_database_sqlite3/try-sqlite3.py)
* OraKit2.0：[本次迭代正式代码及说明文档](./sprint2_gui_and_db/c_orakit_sprint_2/readme)


## 迭代3：提供网页客户端（Web开发）（不使用框架，造轮子）

迭代3从迭代2的C/S架构（Client/Server）客户端“升级”为B/S架构（Browser/Server）架构的网页端程序，  
通过造轮子实现了从前端页面发出请求、http请求处理、路由到服务代码给出响应，最终反显前端整套流程。

迭代3使用Html、JavaScript、Java实现，最终交付物汇总如下:
* PRD：[OraKit Sprint 3 PRD](./sprint3_webapp_without_framework/prd)
* OraKit3.0：
  1. [本次迭代说明文档](./sprint3_webapp_without_framework/orakit_sprint_3/readme)
  2. [Code~ 应用主页html及js代码](./sprint3_webapp_without_framework/orakit_sprint_3/static_site/index.html)
  3. [Code~ Http服务器及路由函数](./sprint3_webapp_without_framework/orakit_sprint_3/http_server/HttpServer.java)
  4. [Code~ 后台服务代码（Mock）](./sprint3_webapp_without_framework/orakit_sprint_3/service_impl/ChatBot.java)


## 迭代4：提供网页客户端（Web开发）（使用并理解框架的能力）

迭代4通过框架实现了从前端页面发出请求、http请求处理、路由到服务代码给出响应，最终反显前端整套流程。

迭代4使用Html、JavaScript、Java（with SpringBoot）实现，最终交付物汇总如下:
* PRD：[OraKit Sprint 4 PRD](./sprint4_webapp_with_framework/prd)
* OraKit4.0：
  1. [本次迭代说明文档](./sprint4_webapp_with_framework/orakit4/readme)
  2. [本次迭代参考资料汇总](./sprint4_webapp_with_framework/orakit4/reference)
  3. [本次迭代框架与业务代码](./sprint4_webapp_with_framework/orakit4/src/main/java/com/pwz/orakit4/Orakit4Application.java)


## 迭代5：高并发高可用场景与解决方案

项目执行到此，最初希望对整个软件工程领域相关认知进行整合梳理的目标已经实现，  
实际代码没有按照最初规划的迭代严格执行，迭代5不再有继续设计实现相关内容的必要。  
杀青，收工。