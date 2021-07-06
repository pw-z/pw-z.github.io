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

<style type="text/css">
%(style)s
</style>

</head>

<body>

<h1>%(title)s</h1>

%(body_summary)s

<br>
<br>
<br>

%(body_detail)s

</body>

</html>
"""

BODY_SUMMARY = """
Start Time: %(test_start_time)s <br>
End Time: %(test_end_time)s <br>
Duration: %(test_duration)s <br>
Total: %(count_all_cases)s <br>
Success: %(count_success_cases)s <br>
Fail: %(count_fail_cases)s <br>
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


def generate_html_head(html_file):
    pass


def generate_html_style():
    return ' '


def generate_html_body(test_summary_dict, case_detail_list):
    body_summary = BODY_SUMMARY % test_summary_dict
    body_detail = ''
    for case_detail in case_detail_list:
        # print(case_detail)
        body_detail += case_detail['case_name'] + "    " + case_detail['run_result'] + " <br>\n"
    return body_summary, body_detail


if __name__ == '__main__':
    generate_report('1', '1')
