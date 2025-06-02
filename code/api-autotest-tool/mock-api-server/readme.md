# 测试用挡板服务

*UPDATED ON 2021.11.23 BY Pengwei.Zhang*

整个`mock-api-server`文件夹是一个Django项目，提供了供测试用的虚拟接口服务。  
其中的子文件夹：
* test_target为Django初始化项目时自动生成的基本框架内容
* polls为Django官方入门教程中的示例程序，可以忽略
* apitest为虚拟接口服务应用
* logs目录为apitest服务的运行日志，按日期划分

---

版本信息：
* Python 3.8.8
* Django 3.2.7

---

使用方法：
1. 安装好Django框架（`pip install django`）
2. 在manage.py同级目录执行`python manage.py runserver`启动服务
3. 访问`localhost:8000/admin/`管理`MockApi`
4. 访问`localhost:8000/apitest/`查看所有已经添加的`MockApi`
5. 访问`localhost:8000/apitest/mock/你所配置的虚拟接口名称`触发虚拟接口的响应

---
补充说明：  
每一个MockApi为一个虚拟接口，具体定义如下：
```python
from django.db import models
class MockApi(models.Model):
    """
    挡板接口类
    api_name: 用于界面显示
    api_request: 接口接受的请求，根据请求是否匹配来给出响应
    api_response： 返回的响应
    api_response_type： 根据type构建响应的类型（即content-type字段）

    api_response_type暂时仅支持：json,text两种
    """
    api_name = models.CharField(max_length=100, unique=True)
    api_request = models.CharField(max_length=200)
    api_response = models.CharField(max_length=2000)
    api_response_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
```
访问对应的虚拟接口时，接口名不存在则返回提示信息，接口名存在时，判断是Get请求还是Post请求，Get请求则直接给出响应，若是Post请求，则进一步判断报文中的请求体与虚拟接口设置的请求体是否一致（字符串相等判断），一致则返回响应，不一致则按照未命中处理，返回提示信息。