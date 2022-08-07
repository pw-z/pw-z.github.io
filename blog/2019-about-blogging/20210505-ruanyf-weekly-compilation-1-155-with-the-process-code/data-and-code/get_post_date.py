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
        weekly_num = re.compile(r'-[0-9]{1,3}').search(str(link)).group()  # 通过正则在link结果中获取周刊期数
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

