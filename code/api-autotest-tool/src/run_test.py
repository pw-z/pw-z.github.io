#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handler.ParameterHandler import Parameter
from handler.Handler import CaseHandler
from handler.Handler import ShellHandler
from handler.Handler import SQLHandler
from helper.CaseHelper import *
from helper.Log import *
import datetime
import report.report as r

if __name__ == '__main__':

    configpath = './config.ini'
    para = Parameter(configpath)

    # print(para.get_parameter('excel_path'))
    # print(para.get_parameter('sheet_list'))
    excel_path = para.get_parameter('excel_path')
    print(excel_path)
    sheets = para.get_parameter('sheet_list')

    logger = init_logger(__name__)
    print(logger.level)

    casehandler = CaseHandler(para)
    shellhandler = ShellHandler(para)
    sqlhandler = SQLHandler(para)

    test_result_detail = []
    test_result_summary = dict(
        count_all_cases=0,
        count_success_cases=0,
        count_fail_cases=0,
        test_start_time=datetime.datetime.now(),
        test_end_time=''
    )

    count_all_cases = 0
    count_success_cases = 0
    count_fail_cases = 0

    for sheet in sheets:
        cases = read_excel(excel_path, sheet)
        # print(cases)

        for case in cases:
            logger.info('\n' + '='*50 + '\n Run Case # ' + case['CaseName'] + '\n' + '='*50)

            case_run_result = True
            steps_run_detail = []
            count_all_steps = 0
            count_success_steps = 0
            count_fail_steps = 0
            for step in case['CaseSteps']:
                if step['Run?']:
                    r1 = True
                    r2 = True
                    r3 = True

                    if step['ShellScript'] != '':
                        r1 = shellhandler.run(step)
                    if step['Body'] != '':
                        r2 = casehandler.run(step)
                    if step['DQL'] != '':
                        r3 = sqlhandler.run(step)
                    step_run_result = r1 and r2 and r3
                    if step_run_result is False:
                        case_run_result = False

                    temp_dict = {'step_name': step['CaseStep'],
                                 'run_result': step_run_result}
                    steps_run_detail.append(temp_dict)
                    if step_run_result:
                        count_success_steps += 1
                    else:
                        count_fail_steps += 1
                    count_all_steps += 1

            case_temp_dict = {
                'case_name': case['CaseName'],
                'run_result': case_run_result,
                'count_all_steps': count_all_steps,
                'count_success_steps': count_success_steps,
                'count_fail_steps': count_fail_steps,
                'step_detail': steps_run_detail
            }
            test_result_detail.append(case_temp_dict)

            if case_run_result:
                count_success_cases += 1
            else:
                count_fail_cases += 1
            count_all_cases += 1

    test_result_summary['test_end_time'] = datetime.datetime.now()
    test_result_summary['test_duration'] = test_result_summary['test_end_time'] - test_result_summary['test_start_time']
    test_result_summary['count_all_cases'] = count_all_cases
    test_result_summary['count_success_cases'] = count_success_cases
    test_result_summary['count_fail_cases'] = count_fail_cases

    # print(test_result_summary)
    # print("#"*100 + "\n\n" + "#"*100)
    # for case in test_result_detail:
    #     print(case)

    r.generate_report(test_result_summary, test_result_detail)
