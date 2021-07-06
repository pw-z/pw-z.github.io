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

        case_run_result = False
        for case in cases:
            if case['Run?'][0] == '1':
                case_run_result = shellhandler.run(case)
            if case['Run?'][1] == '1':
                case_run_result = casehandler.run(case)
            if case['Run?'][2] == '1':
                case_run_result = sqlhandler.run(case)
            temp_dict = {'case_name': case['CaseStep'],
                         'run_result': str(case_run_result)}
            test_result_detail.append(temp_dict)

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

    r.generate_report(test_result_summary, test_result_detail)
