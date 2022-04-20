# Alternative Repo Source

## PIP

| name     | link                                     |
|----------|------------------------------------------|
| 清华大学     | https://pypi.tuna.tsinghua.edu.cn/simple |
| 中国科学技术大学 | http://pypi.mirrors.ustc.edu.cn/simple   |
| 阿里云      | http://mirrors.aliyun.com/pypi/simple    |
| 中国科技大学   | https://pypi.mirrors.ustc.edu.cn/simple  |
| 豆瓣       | http://pypi.douban.com/simple            |


```shell
# 安装时临时指定下载源
pip3 install sweetest  -i https://pypi.tuna.tsinghua.edu.cn/simple

# 变更配置文件默认下载源（linux/mac）
mkdir ~/.pip    
vim ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```