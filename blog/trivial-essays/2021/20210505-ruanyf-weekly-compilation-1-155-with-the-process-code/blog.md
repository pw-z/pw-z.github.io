# ~~阮一峰科技爱好者周刊1~155期合集及~~处理脚本
*2021050501-ruanyf-weekly-compilation-1-155-with-the-process-code*  
*Posted on 2021.05.05 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


- [~~阮一峰科技爱好者周刊1~155期合集及~~处理脚本](#阮一峰科技爱好者周刊1155期合集及处理脚本)
  - [1 脚本](#1-脚本)
    - [1.1 基本处理](#11-基本处理)
    - [1.2 使用爬虫获取周刊发布日期](#12-使用爬虫获取周刊发布日期)
    - [1.3 插入日期信息](#13-插入日期信息)
  - [~~阮一峰科技爱好者周刊1~155期合集~~](#阮一峰科技爱好者周刊1155期合集)

这篇依然是练习使用python的过程中整理的，涉及到的知识点包括基础语法、文件IO、爬虫（网络IO、正则表达式）。


## 1 脚本

### 1.1 基本处理

所有周刊存在`docs`目录下，首先遍历所有二级标题统计出哪些是广告，让后通过统计结果`ad_section`及`special_section`两个集合辅助将所有正文章节进行输出。

```python
# -*- coding: utf-8 -*-
ad_section = {'## 欢迎订阅\n','## 订阅\n','## 回顾\n'}   # 这些字段对应的内容不输出
special_section = {'本周','语雀','电影','周分享','科技爱好者周刊','封面','言论','图片','Big Sur','刊首图','资源','资讯'}   # 避免将这些字段识别为广告

def analyze_title():
    print(ad_section)
    '''分析周刊的文档结构以及标题数据，方便后续处理'''
    analyze_result = open('analyze_result.txt', 'wt', encoding='utf-8')
    title={}
    for i in range(1,156):
        filepath = './docs/issue-' + str(i) + '.md'
        # print("processing " + filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if  '欢迎订阅' in line:
                    break
                if line[:2] == '##' or line[:2] == '# ':
                    if line not in title:
                        title[line]=1
                    else:
                        title[line]+=1
                    # print(line, file=analyze_result, end="")
    print("====================================================================", file=analyze_result)
    print("                         标题计数", file=analyze_result)
    print("====================================================================", file=analyze_result)
    for count_result in title:
        print(count_result[:-1] + '  ' + str(title[count_result]), file=analyze_result)
    print("\n\n\n\n\n\n\n\n", file=analyze_result)
    
    print("====================================================================", file=analyze_result)
    print("                         识别出的广告字段", file=analyze_result)
    print("====================================================================", file=analyze_result)
    for count_result in title:
        # 生成广告关键字集合
        for keyword in special_section:
            if keyword in count_result:
                ad_flag = False
                # print('【' + count_result[:-1] + '】    未被识别未广告')
                break
            else:
                ad_flag = True
        if title[count_result] <= 2 and ad_flag == True:
            ad_section.add(count_result)
            print(count_result[:-1] + '  ' + str(title[count_result]), file=analyze_result)
    analyze_result.close()
    return ad_section

def process(ad_section):
    '''处理周刊数据，以每期作为一个章节的形式输入'''
    with open('ruanyf-weekly-compilation-1-155.md', 'w', encoding='utf-8') as mdfile:
        for i in range(1,156):
            filepath = './docs/issue-' + str(i) + '.md'
            print("processing " + filepath)
            with open(filepath, 'r', encoding='utf-8') as f:
                print_flag=False
                for line in f:
                    if line[:2] == '##' or line[:2] == '# ':
                        if line in ad_section:
                            print_flag = False
                        else:
                            print_flag = True
                    if print_flag == True:
                        print(line, file=mdfile, end="")


if __name__=="__main__": 
    ad_section = analyze_title()
    process(ad_section)
```

### 1.2 使用爬虫获取周刊发布日期

上一步处理完的文档中不包含日期信息，没写过爬虫，在此练习使用爬虫获取所需信息。

**爬虫的核心思路：根据url发送请求获取到对应网页之后再从网页上筛选出所需数据**，使用`requests`及`bs4`这两个包即可满足需求，`requests`包负责发请求及获取响应报文，[`bs4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)则可以将返回的html格式化，并提供了方便的检索方法。

具体代码如下：

```python
import requests
import re
from bs4 import BeautifulSoup
import json


def get_html(url):
    print('GET %s' % url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
    except Exception:
        pass


def get_ruanyf_weekly_urls(parent_url):
    """
    :param parent_url:周刊根目录
    :return:所有周刊url，_urls = { number : { title:title , url:url , time:time } }
    """
    _urls = {}
    _html = get_html(parent_url)
    _html_soup = BeautifulSoup(_html, 'html.parser')
    for link in _html_soup.find_all(href=re.compile('http://www.ruanyifeng.com/blog/20')):  # 通过正则获取所有周刊的a标签
        # print(link)  # <a href="http://www.ruanyifeng.com/blog/2018/07/weekly-issue-12.html">每周分享第 12 期</a>
        weekly_num = re.compile(r'-[0-9]{1,3}').search(str(link)).group()  # 通过正则在link中获取周刊期数
        _urls[weekly_num[1:]] = {'title': link.string, 'url': link.get('href'), 'date': ''}  # 构建_urls字典
    return _urls


def get_ruanyf_weekly_post_date(url):
    """
    根据具体的周刊url获取对应的发布日期
    :param url: 周刊url
    :return: post_date: 对应周刊的发布日期
    """
    html = get_html(url)
    html_soup = BeautifulSoup(html, 'html.parser')
    # print(html_soup.prettify())
    first_abbr = html_soup.abbr  # 分析周刊html可知第一个abbr标签保存的就是发布日期
    # print(first_abbr)
    post_date = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}').search(str(first_abbr)).group()
    # print(post_date)
    return post_date


if __name__ == '__main__':
    weekly_date = {}  # 对应期数周刊的发布日期
    urls = get_ruanyf_weekly_urls('http://www.ruanyifeng.com/blog/weekly/')
    for k, v in urls.items():
        print(k + '    ' + v.get('title') + '    ' + v.get('url'))  # 打印获取到的所有url信息
        weekly_date[k] = get_ruanyf_weekly_post_date(v.get('url'))
    json.dump(urls, open('urls_result.txt', 'w'))
    for k, v in weekly_date.items():
        print('第' + k + '期周刊发布日期为：' + v)
    json.dump(weekly_date, open('date_result.txt', 'w'))
```

### 1.3 插入日期信息

上一步代码中已经把爬虫获取到的时间信息进行了序列化，此处额外写一段代码处理之前的文件，将时间信息插入（并将标题层级进行处理），不再改动之前的代码。

```python
"""
对analyze_and_process.py生成的合集文档再处理：
读取每一行，若为标题行，则插入日期信息
日期信息通过get_post_date.py获取
"""
import json
import re

if __name__ == "__main__":
    date_result = json.load(open('date_result.txt', 'r'))
    # for k, v in date_result.items():
    #     print('第' + k + '期周刊发布日期为：' + v)
    # 用urls_result.txt可以把每一期的网址也输出出来
    # urls_result = json.load(open('urls_result.txt', 'r'))
    with open('ruanyf-weekly-compilation-1-155.md', 'r', encoding='utf-8') as f1:
        with open('ruanyf-weekly-compilation-1-155-with-post-date.md', 'w', encoding='utf-8') as f2:
            for line in f1:
                if line[:2] == '# ':  # 如果是一级标题，插入日期信息，同时将一级标题处理成三级标题
                    num = re.compile(r'[0-9]{1,3}').search(line).group()
                    # print(num)
                    line = '##' + line
                    print(line, file=f2, end="")
                    print('*Posted on %s*\n' % date_result[num], file=f2, end="")
                elif line[:2] == '##':  # 将二级标题处理成四级标题
                    line = '##' + line
                    print(line, file=f2, end="")
                else:
                    print(line, file=f2, end="")
    
```

## ~~阮一峰科技爱好者周刊1~155期合集~~

原文`禁止演绎`，此处就不粘贴处理结果了。

~~./final-result~~