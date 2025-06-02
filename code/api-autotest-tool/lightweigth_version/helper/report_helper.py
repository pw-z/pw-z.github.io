#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An all-in-one html testing report generator."""

import time
from helper.log_helper import init_logger

# for pie chart
import matplotlib.pyplot as plt
from io import BytesIO
import base64

REPORT_TEMPLATE = """
<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8"> 
<title>%(title)s</title>
<style>
    %(style)s
</style>
</head>

<body>

    <div class="report_body">
        <h1 class="report_title">%(title)s</h1>
        %(body_summary)s
        <div class="report_detail">
            <h2>Detail</h2>
            %(body_detail)s
        </div>
    </div>

    <!--script----------------------------------------------------------------------->
    <script>
        function show_or_close_case_detail(that) {
            var current_display_mode = that.parentNode.lastElementChild.style.display;
            var div_step_detail = that.parentNode.lastElementChild.getElementsByClassName('step_detail');
            if (current_display_mode != 'none') {
                that.parentNode.lastElementChild.style.display = 'none';
                for (let index = 0; index < div_step_detail.length; index++) {
                    div_step_detail[index].style.display = 'none';
                }
            } else {1
                that.parentNode.lastElementChild.style.display = 'block';
                for (let index = 0; index < div_step_detail.length; index++) {
                    div_step_detail[index].style.display = 'none';
                }
            }
        }
        function show_or_close_step_detail(that) {
            var current_display_mode = that.parentNode.lastElementChild.style.display;
            if (current_display_mode != 'none') {
                that.parentNode.lastElementChild.style.display = 'None';
            } else {
                that.parentNode.lastElementChild.style.display = 'block';
            }
        }
    </script>
    <!--script---------------------------------------------------------------end----->

</body>

</html>
"""

BODY_SUMMARY_TEMPLATE = """
<div class="report_summary">
        <h2>Summary</h2>
        <div class="summary_text">
            <p>
                <span>Start: %(test_start_time)s</span><br/>
                <span>End:  %(test_end_time)s</span><br/>
                <span>Duration: %(test_duration)s</span><br/>
            </p>
            
            <div class="summary_chart">
                <img id="pie_chart" alt="" src="data:image/png;base64,%(pie_chart)s"/>
            </div>
            
            <p>
                <span>Total: %(count_all_cases)s</span>
                <span>Success: %(count_success_cases)s</span>
                <span>Fail: %(count_fail_cases)s</span>
            </p>
        </div>
</div>
"""

"""
{0} = run_result (pass_case, fail_case)
{1} = case_name
{2} = count_all_steps
{3} = count_success_steps
{4} = count_fail_steps
{5} = step_detail
"""
CASE_TEMPLATE = """
        <div class="{0}">
            <div class="case_info" onclick="show_or_close_case_detail(this)">
                <span class="name">{1}</span>
                <span class="status">{2}/{3}/{4}</span>
            </div>
            <div class="step_list" style="display: none;">
            {5}
            </div>
        </div>
"""

"""
{0} = run_result
{1} = %(name)s
{2} = %(start)s
{3} = %(end)s
{4} = %(duration)s
{5} = step run log
"""
STEP_TEMPLATE = """
                <div class="{0}">
                    <div class="step_info" onclick="show_or_close_step_detail(this)">
                        <span class="step_name">{1}</span>
                        <span class="step_duration">Dur: {4}</span>
                        <span class="step_end_time">End: {3}</span>
                        <span class="step_start_time">Start: {2}</span>
                    </div>
                    <div class="step_detail">
                    {5}
                    </div>
                </div>
"""

CSS_TEMPLATE = """
/* --------------------------- basic setting --------------------------- */
.report_body {
    max-width: 900px;
    margin-right: auto;
    margin-left: auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-size: 16px;
    line-height: 1.2;
}

h1 {
    padding-bottom: 2px;
    border-bottom: 3px solid #eaecef;
    background-color: #ffffff;
}

h2 {
    padding-bottom: 3px;
    border-bottom: 1px solid #f5f3f3;
    background-color: #ffffff;
}
/* --------------------------- basic setting --------------------------- */

/* --------------------------- report summary -------------------------- */
.report_summary {
    width: 98%;
    margin: 20px auto;
    height: 400px;
}

.summary_text {
    width: 98%;
    text-align: center;
    height: 100%;
}

.summary_chart {
    height: 60%;
}

#pie_chart {
    max-width: 100%;
    max-height: 100%;
    display: block;
    margin: auto;
}
/* --------------------------- report summary -------------------------- */


/* --------------------------- report detail --------------------------- */
.report_detail {
    width: 98%;
    margin: 40px auto;
}

.case_info,
.step_info{
    padding: 3px;
    border: 2px solid #ffffff;
}
.case_info:hover,
.step_info:hover{
    border-bottom: 1px solid #6d6d6d;
    cursor: pointer;
}
.case_info .status {
    float: right;
}

.pass_case,
.fail_case,
.error_case {
    border: 2px;
    padding: 3px;
    margin: 8px;
}

.pass_case .case_info { background-color: #f7f7f7; }
.fail_case .case_info { background-color: #f7f7f7; color: red;}
.error_case .case_info { background-color: #d55858; }

.step_list {
    display: none;
    width: 95%;
    margin: auto;
}

.pass_step,
.fail_step,
.error_step {
    padding: 3px;
    margin: 8px;
    font-size: 16px;
}

.fail_step .step_info {
     color: #ff0032;
}

.error_step .step_info {
    color: #cc0000;
}

.step_start_time,
.step_end_time,
.step_duration{
    float: right;
    margin:auto;
    font-size: 14px;
}

.step_detail {
    font-size: 14px;
    line-height: 1.2;
    width: 98%;
    margin: 4px auto;
    padding: 4px;
    border: 1px solid rgba(138, 176, 187, 0.25);
    white-space: pre-line;
    word-wrap: break-word;
    word-break: break-all;
}
/* --------------------------- report detail --------------------------- */
"""

logger = init_logger(__name__)


def generate_html_style():
    return CSS_TEMPLATE


def generate_html_summary(test_summary_dict):
    """Handle summary statistics and draw a pie chart of case result.

    Fill all statistics into BODY_SUMMARY_TEMPLATE;
    Embed a pie chart picture in HTML with the help of Base64 encoding.

    :param test_summary_dict: see generate_report()
    :return: long string, part of the html report, with a pie chart picture in it
    """
    # total = test_summary_dict['count_all_cases']
    success = test_summary_dict['count_success_cases']
    fail = test_summary_dict['count_fail_cases']
    x = [success, fail]
    labels = ['Success = {0}'.format(success), 'Fail = {0}'.format(fail)]
    explode = [0.01, 0]
    colors = ['#8CD790', 'coral']

    plt.axes(aspect='equal')
    plt.xlim(0, 4)
    plt.ylim(0, 4)
    plt.pie(x,
            explode=explode,
            autopct='%1.1f%%',
            startangle=70,
            radius=1,
            counterclock=False,
            textprops={'fontsize': 14, 'color': 'k'},
            labels=labels,
            colors=colors
            )
    plt.xticks(())
    plt.yticks(())
    png_buffer = BytesIO()
    plt.savefig(png_buffer, transparent=True, format='png')
    png_base64 = base64.b64encode(png_buffer.getvalue())
    png_base64_str_utf8 = str(png_base64, 'utf-8')
    test_summary_dict['pie_chart'] = png_base64_str_utf8

    summary = BODY_SUMMARY_TEMPLATE % test_summary_dict
    return summary


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
                    'run_result': step_run_result,
                    'run_log': step_run_log
                },
                step_detail_dict2 = {
                    'step_name': step['CaseStep'],
                    'run_result': step_run_result,
                    'run_log': step_run_log
                }
            ]
        }
    ]
    :param test_summary_dict: refer generate_report()
    :param case_detail_list: refer generate_report()
    :return: (body_summary, body_detail), both html string
    """

    def get_step_list(steps):
        """
        steps = [
                step_detail_dict1 = {
                    'step_name': step['CaseStep'],
                    'run_result': step_run_result,
                    'run_log': step_run_log
                },
                step_detail_dict2 = {
                    'step_name': step['CaseStep'],
                    'run_result': step_run_result,
                    'run_log': step_run_log
                }
            ]
        """
        _step_list = ''
        for step in steps:
            if step['run_result']:  # pass step
                _step_list += STEP_TEMPLATE.format('pass_step',
                                                   step['step_name'],
                                                   step['start_time'],
                                                   step['end_time'],
                                                   step['duration'],
                                                   step['run_log'])
            else:  # fail step
                _step_list += STEP_TEMPLATE.format('fail_step',
                                                   step['step_name'],
                                                   step['start_time'],
                                                   step['end_time'],
                                                   step['duration'],
                                                   step['run_log'])
        return _step_list

    body_summary = generate_html_summary(test_summary_dict)

    body_detail = ''
    for case_detail in case_detail_list:
        # print(case_detail)
        step_list = get_step_list(case_detail['step_detail'])
        if case_detail['run_result'] is True:
            body_detail += CASE_TEMPLATE.format('pass_case',
                                                case_detail['case_name'],
                                                case_detail['count_all_steps'],
                                                case_detail[
                                                    'count_success_steps'],
                                                case_detail['count_fail_steps'],
                                                step_list)
        else:
            body_detail += CASE_TEMPLATE.format('fail_case',
                                                case_detail['case_name'],
                                                case_detail['count_all_steps'],
                                                case_detail[
                                                    'count_success_steps'],
                                                case_detail['count_fail_steps'],
                                                step_list)
    return body_summary, body_detail


def generate_report(test_summary_dict: dict, case_detail_list: list):
    """The main method used to generate test report.

    :param test_summary_dict:
        test_summary_dict = dict(
            count_all_cases=XXX,
            count_success_cases=XXX,
            count_fail_cases=XXX,
            test_start_time=datetime.datetime.now(),
            test_end_time=datetime.datetime.now(),
            test_report_title=para.get_parameter('test_report_title')
        )
    :param case_detail_list:
        [
            case_detail_dict = {
                    'case_name': case['CaseName'],
                    'start_time': case_start_time,
                    'end_time': case_end_time,
                    'duration': case_duration,
                    'run_result': case_run_result,
                    'count_all_steps': count_all_steps,
                    'count_success_steps': count_success_steps,
                    'count_fail_steps': count_fail_steps,
                    'step_detail': steps_run_detail
            },
        ]
    """
    logger.info("=" * 100)
    logger.info("=" * 39 + " Generate Test Report " + "=" * 39)
    logger.info("=" * 100)

    # logger.debug("test_summary_dict is: \n\n" + test_summary_dict + "\n\n")
    # logger.debug("case_detail_list is: \n\n" + case_detail_list + "\n\n")

    try:
        title = test_summary_dict['test_report_title']
        if title == '':
            title = 'API AutoTest Report ' + time.strftime('%Y.%m.%d')
        else:
            title = title + ' ' + time.strftime('%Y.%m.%d')
        style = generate_html_style()
        body_summary, body_detail = generate_html_body(test_summary_dict,
                                                       case_detail_list)

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

    except Exception as e:
        logger.error('Error while generating test report.')
        logger.error(e)
    else:
        logger.info('Testing done, please check the report --> ' + report_name)

