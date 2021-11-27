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

    def __str__(self):
        return self.api_name

    def tostring(self):
        return self.api_name

