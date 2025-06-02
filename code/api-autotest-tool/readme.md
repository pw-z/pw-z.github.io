# 接口自动化测试工具


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [接口自动化测试工具](#接口自动化测试工具)
  - [文件描述](#文件描述)
  - [核心依赖](#核心依赖)
  - [运行说明](#运行说明)
  - [版本记录](#版本记录)

<!-- /code_chunk_output -->



此工具为接口自动化测试框架，使用Python3编写，使用Excel管理用例，参数化自动执行后生成测试报告。

## 文件描述

* ./src/mock-api-server 测试用虚拟接口服务
* ./src/lightweight_version 接口自动化测试框架@轻量化版本
* ./src/pytest_allure_version 接口自动化测试框架@引入pytest及allure版本
* ./case/case_template.xlsx 测试用例模板，需要与虚拟接口服务配合使用
* [./doc/20210719-an-api-autotest-tool.md](doc/20210719-an-api-autotest-tool.md) 设计实现过程

## 核心依赖

如下为本项目所使用到的核心依赖，版本号为测试环境下使用的具体版本。

* [Python3][Python3]，3.8.8，整个项目建立在python3的基础上，未在python2下测试过
* [Django][Django]，3.2.7，mock-api-server的web服务是依赖Django构建起来的
* [paramiko][paramiko]，2.8.0，ssh功能需要此依赖
* [cx_Oracle][cx_Oracle]，8.3，操控Oracle数据库需要的官方依赖，根据数据库版本下载对应版本
* [matplotlib][matplotlib]，3.5.0，用于在生成轻量版测试报告过程中绘制饼图
* [numpy][numpy]，1.21.4，用于在生成轻量版测试报告过程中绘制饼图
* [pytest][pytest]，6.2.4，第三方测试脚手架，方便进行额外的devops整合，且可与Allure结合生成更漂亮的报告
* [allure-pytest][allure-pytest]，2.9.45，测试报告框架，可生成非常漂亮的报告，在本项目中与pytest结合使用

## 运行说明

由于Pytest版本长久没有更新暂时无法运行，以轻量化版本为例，整体上的使用流程如下：
1. 安装所有必须依赖
2. 写测试用例，具体请参考测试用例模板文件（./case/case_template.xlsx），里面有具体的编写说明
3. 填写配置文件（./src/lightweight_version/config.ini），文件中有具体说明
4. 运行run_test.py即可，如没有问题，可在相应report目录下查看测试报告

如果需要运行虚拟接口服务（mock-api-server），请查看其对应目录下的`readme.md`文档。

## 版本记录
    
    v0.9 @2021.11.29
    新增参数处理环节，所有列均可以进行参数置换操作，配置文件中有总开关
    补充完善相关文档，添加测试用例模板说明
    修复若干微小问题
    整理项目文件，添加.gitignore文件，初始化git仓库

    v0.8 @2021.11.26
    整理、补充大量注释（覆盖到每一个模块、类、方法和函数及重要代码块儿）

    v0.7 @2021.11.25
    优化 参数获取方式及规则优化
    新增 数据操控列可以自定义参数
    新增 总的SQL、SSH开关

    v0.6 @2021.11.24
    新增 header列可以添加任意参数
    新增 Get请求方式的支持
    完善参数校验方式至稳定的三种（简单键值对、json路径键值对、字符串包含）

    v0.5 @2021.11.23
    add mock-api-server
    add https support
    
    v0.4
    pytest + allure support
    add DML support
    add more annotation
    optimize testing log

    v0.3
    generate clean testing log
    generate clean testing report

    v0.2
    generate test report
    improve the code

    v0.1
    handle cases with excel 
    handle config.ini
    handle http/https request & response
    handle ssh and execution result
    handle SQL and execution result
    testing log output




[Python3]:https://www.python.org/
[Django]:https://www.djangoproject.com/start/overview/
[paramiko]:https://www.paramiko.org/
[cx_Oracle]:https://oracle.github.io/python-cx_Oracle/
[matplotlib]:https://matplotlib.org/
[numpy]:https://numpy.org/
[pytest]:https://docs.pytest.org/en/6.2.x/
[allure-pytest]:http://allure.qatools.ru/
    



