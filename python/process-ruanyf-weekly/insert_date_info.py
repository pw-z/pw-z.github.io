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
    with open('ruanyf-weekly-compilation-1-155.md', 'r', encoding='utf-8') as f1:
        with open('ruanyf-weekly-compilation-1-155-with-post-date.md', 'w', encoding='utf-8') as f2:
            for line in f1:
                if line[:2] == '# ':  # 如果是一级标题，准备插入日期
                    num = re.compile(r'[0-9]{1,3}').search(line).group()
                    # print(num)
                    print(line, file=f2, end="")
                    print('*Posted on %s by [阮一峰](http://www.ruanyifeng.com/blog/) under the '
                          '[CC BY-NC-ND 3.0](https://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh) license*\n' % date_result[num], file=f2, end="")
                else:
                    print(line, file=f2, end="")
