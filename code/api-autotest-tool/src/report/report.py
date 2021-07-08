#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from helper.Log import *

REPORT_TEMPLATE = r"""
<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8"> 
<title>%(title)s</title>
<link rel="stylesheet" type="text/css" href="template.css">
</head>

<body>
    <div class="report_body">
        <h1 class="report_title">%(title)s</h1>
        %(body_summary)s
        <div class="report_detail">
            <h2>Detail</h2>
            <table>
            %(body_detail)s
            </table>
        </div>
    </div>
</body>

</html>
"""

BODY_SUMMARY_TEMPLATE = """
<div class="report_summary">
        <h2>Summary</h2>
        <div class="summary_text">
            <p>Start Time: %(test_start_time)s<br/>End Time: %(test_end_time)s<br/>Duration: %(test_duration)s</p>
            <p>Total: %(count_all_cases)s<br/>Success: %(count_success_cases)s<br/>Fail: %(count_fail_cases)s</p>
        </div>
        <div class="summary_chart">
            <img id="pie_chart" alt="" src="data:image/png;base64,%(pie_chart)s"/>
        </div>
</div>
"""


"""
{0} = run_result (pass_case, fail_case)
{1} = case_name
{2} = count_all_steps
{3} = count_success_steps
{4} = count_fail_steps
"""
CASE_TR_TEMPLATE = """
        <tr class="{0}">
            <td>{1}</td>
            <td>{2}/{3}/{4}</td>
            <td><a href="">detail</a> </td>
        </tr>
"""

STEP_TR_TEMPLATE = """
                <tr class="{0}">
                    <td>{1}</td>
                    <td><a href="">detail</a> </td>
                </tr>
"""


logger = init_logger(__name__)


def generate_report(test_summary_dict, case_detail_list):

    logger.info("=" * 70)
    logger.info("=" * 24 + " Generate Test Report " + "=" * 24)
    logger.info("=" * 70)

    logger.debug(test_summary_dict)
    logger.debug(case_detail_list)

    title = 'Test Test Report Title'
    style = generate_html_style()
    body_summary, body_detail = generate_html_body(test_summary_dict, case_detail_list)

    html_dict = dict(
        title=title,
        style=style,
        body_summary=body_summary,
        body_detail=body_detail
    )

    date = time.strftime('%Y%m%d-%H%M%S')
    report_name = 'report/TestReport-{0}.html'.format(date)
    with open(report_name, 'w', encoding='utf8') as f:
        report_html = REPORT_TEMPLATE % html_dict
        f.write(report_html)


def generate_html_summary(test_summary_dict):
    import matplotlib.pyplot as plt
    from io import BytesIO
    import base64

    # total = test_summary_dict['count_all_cases']
    success = test_summary_dict['count_success_cases']
    fail = test_summary_dict['count_fail_cases']
    x = [success, fail]
    labels = ['Success = {0}'.format(success), 'Fail = {0}'.format(fail)]
    explode = [0.01, 0]
    colors = ['#8CD790', 'coral']

    # plt.rcParams['figure.figsize'] = [3, 3]
    plt.axes(aspect='equal')
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
            textprops={'fontsize': 14, 'color': 'k'},  # 设置文本标签的属性值
            # center=(2, 2),  # 设置饼图的原点
            # frame=1,  # 是否显示饼图的图框，这里设置显示
            labels=labels,  # 添加教育水平标签
            colors=colors  # 设置饼图的自定义填充色
            )
    # 删除x轴和y轴的刻度
    plt.xticks(())
    plt.yticks(())
    png_buffer = BytesIO()
    plt.savefig(png_buffer, transparent=True, format='png')
    png_base64 = base64.b64encode(png_buffer.getvalue())
    png_base64_str_utf8 = str(png_base64, 'utf-8')
    test_summary_dict['pie_chart'] = png_base64_str_utf8

    # print("#"*100)
    # print(test_summary_dict)

    summary = BODY_SUMMARY_TEMPLATE % test_summary_dict
    return summary


def generate_html_style():
    return ' '


def generate_html_body(test_summary_dict, case_detail_list):
    """
    case_detail_list = [
        case_dict1={
            'case_name': case['CaseName'],
            'run_result': case_run_result,
            'step_detail': steps_run_detail
        },
        case_dict2={
            'case_name': case['CaseName'],
            'run_result': case_run_result,
            'step_detail': [

                step_detail_dict1 = {
                    'step_name': step['CaseStep'],
                    'run_result': step_run_result
                },
                step_detail_dict2 = {
                    'step_name': step['CaseStep'],
                    'run_result': step_run_result
                }
            ]

        }
    ]


    :param test_summary_dict:
    :param case_detail_list:
    :return:
    """
    body_summary = generate_html_summary(test_summary_dict)

    body_detail = ''
    for case_detail in case_detail_list:
        # print(case_detail)
        if case_detail['run_result'] is True:
            body_detail += CASE_TR_TEMPLATE.format('pass_case', case_detail['case_name'],
                                                   case_detail['count_all_steps'],
                                                   case_detail['count_success_steps'],
                                                   case_detail['count_fail_steps'])

            for step_detail in case_detail['step_detail']:
                if step_detail['run_result']:
                    body_detail += STEP_TR_TEMPLATE.format('pass_step', step_detail['step_name'])
                else:
                    body_detail += STEP_TR_TEMPLATE.format('fail_step', step_detail['step_name'])
        else:
            body_detail += CASE_TR_TEMPLATE.format('fail_case', case_detail['case_name'],
                                                   case_detail['count_all_steps'],
                                                   case_detail['count_success_steps'],
                                                   case_detail['count_fail_steps'])

            for step_detail in case_detail['step_detail']:
                if step_detail['run_result']:
                    body_detail += STEP_TR_TEMPLATE.format('pass_step', step_detail['step_name'])
                else:
                    body_detail += STEP_TR_TEMPLATE.format('fail_step', step_detail['step_name'])

    return body_summary, body_detail


if __name__ == '__main__':
    generate_report('1', '1')
