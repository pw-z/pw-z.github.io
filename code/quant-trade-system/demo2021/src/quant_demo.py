#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2021
import time
import requests
import datetime as dt
from dateutil import parser  # 用于处理时间，注意安装时包的名字 pip install python-dateutil


def get_sina_tick_by_code(code='sh600519'):
    sina_url = 'http://hq.sinajs.cn/?format=text&list={}'.format(code)
    res = requests.get(sina_url)
    info_list = res.text.split(',')
    # print(info_list)
    stock_info = {
        'code': info_list[0].split('=')[0],
        'name': info_list[0].split('=')[1],
        'last_price': float(info_list[1]),
        'timestamp': info_list[30] + ' ' + info_list[31]
    }
    # print(stock_info)

    # 时间信息的数据格式转换
    # dt = parser.parse(tick[1])
    # print(dt)
    # print(dt.date())
    # print(dt.time())

    _tick = (stock_info['last_price'], stock_info['timestamp'])
    return _tick


def strategy(_tick):
    """交易策略
    1. last < 某项指标如ma20*0.95 买入， last > ma20*1.05 卖出
    2. 假设已经拥有历史数据
    具体步骤：
    1. 更新指标
    2. 判断策略条件，得出交易信号（buy or sell or pass）
    """
    pass


if __name__ == '__main__':
    weekday = dt.date.today().weekday()  # 星期一为0，星期日为6
    # print(weekday)
    trade_time = dt.time(9, 30)  # 初始化交易时间为九点半
    while dt.time(9) < trade_time < dt.time(15) and weekday < 5:
        print('-' * 30)
        tick = get_sina_tick_by_code()
        trade_time = parser.parse(tick[1]).time()
        print(tick)
        print(trade_time)
        time.sleep(2)