#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from io import BytesIO
import base64

# 设置绘图的主题风格
plt.style.use('ggplot')
# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = [3, 3]

x = [60, 30]
labels = ['Pass = 365', 'Fail = 4']
explode = [0.01, 0]
colors = ['#8CD790', 'coral']

# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0, 4)
plt.ylim(0, 4)

# 绘图数据
plt.pie(x,  # 绘图数据
        explode=explode,  # 突出显示大专人群
        autopct='%1.1f%%',  # 设置百分比的格式，这里保留一位小数
        # pctdistance=0.6,  # 设置百分比标签与圆心的距离
        # labeldistance=1.2,  # 设置教育水平标签与圆心的距离
        startangle=70,  # 设置饼图的初始角度
        radius=1,  # 设置饼图的半径
        counterclock=False,
        # wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 饼图内外边界的属性值
        textprops={'fontsize': 8, 'color': 'k'},  # 设置文本标签的属性值
        # center=(2, 2),  # 设置饼图的原点
        # frame=1,  # 是否显示饼图的图框，这里设置显示
        labels=labels,  # 添加教育水平标签
        colors=colors  # 设置饼图的自定义填充色
        )

# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())

# 添加图标题
# plt.title('Test Result')
# plt.legend(loc=1)
plt.show()






# png_buffer = BytesIO()
# plt.savefig(png_buffer, transparent=True, format='png')
# # png_buffer.seek(0)
# png_bytes = png_buffer.getvalue()
# print(png_bytes)
# png_base64 = base64.b64encode(png_buffer.getvalue())
# png_base64_str_utf8 = str(png_base64, 'utf-8')
# print(png_base64_str_utf8)

# html = """<img src="data:image/png;base64,{}"/>""".format(png_base64_str_utf8)
# filename = 'png.html'
# with open(filename, 'w', encoding='utf8') as f:
#     f.write(html)


