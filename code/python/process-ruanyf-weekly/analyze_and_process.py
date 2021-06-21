# -*- coding: utf-8 -*-
ad_section = {'## 欢迎订阅\n', '## 订阅\n', '## 回顾\n', '## 历史上的本周\n'}  # 这些字段对应的内容不输出
special_section = {'本周', '语雀', '电影', '周分享', '科技爱好者周刊', '封面', '言论', '图片', 'Big Sur', '刊首图', '资源', '资讯'}  # 避免将这些字段识别为广告


def analyze_title():
    """分析周刊的文档结构以及标题数据，方便后续处理"""
    analyze_result = open('analyze_result.txt', 'wt', encoding='utf-8')
    title = {}
    for i in range(1, 156):
        filepath = './docs/issue-' + str(i) + '.md'
        # print("processing " + filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if '欢迎订阅' in line:
                    break
                if line[:2] == '##' or line[:2] == '# ':
                    if line not in title:
                        title[line] = 1
                    else:
                        title[line] += 1
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
    """处理周刊数据，以每期作为一个章节的形式输入"""
    with open('ruanyf-weekly-compilation-1-155.md', 'w', encoding='utf-8') as mdfile:
        for i in range(1, 156):
            filepath = './docs/issue-' + str(i) + '.md'
            print("processing " + filepath)
            with open(filepath, 'r', encoding='utf-8') as f:
                print_flag = False
                for line in f:
                    if line[:2] == '##' or line[:2] == '# ':
                        if line in ad_section:
                            print_flag = False
                        else:
                            print_flag = True
                    if print_flag:
                        print(line, file=mdfile, end="")


if __name__ == "__main__":
    ad_section = analyze_title()
    process(ad_section)
