#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main script of the api-autotest-tool.

Before running this script, make sure that config.ini
has been written correctly.
"""

from handler.parameter_handler import Parameter
from handler.case_handler import CaseHandler
from handler.shell_handler import ShellHandler
from handler.sql_handler import SQLHandler
from helper.case_helper import read_excel
from helper.log_helper import init_sio, init_logger, get_sio
import datetime
import helper.report_helper as r

if __name__ == '__main__':

    # initialize all the necessary parameters
    configpath = './config.ini'
    para = Parameter(configpath)
    excel_path = para.get_parameter('excel_path')
    sheets = para.get_parameter('sheet_list')
    logger = init_logger(__name__)
    allow_ssh = para.get_parameter('allow_ssh') == 'True'
    allow_SQL = para.get_parameter('allow_SQL') == 'True'
    casehandler = CaseHandler(para)
    if allow_ssh:
        shellhandler = ShellHandler(para)
    if allow_SQL:
        sqlhandler = SQLHandler(para)

    # initialize testing statistics for the final report
    test_result_detail = []
    test_result_summary = dict(
        count_all_cases=0,
        count_success_cases=0,
        count_fail_cases=0,
        test_start_time=datetime.datetime.now(),
        test_end_time='',
        test_report_title=para.get_parameter('test_report_title')
    )
    count_all_cases = 0
    count_success_cases = 0
    count_fail_cases = 0

    # process each case in each sheet configured in config.ini
    for sheet in sheets:
        cases = read_excel(excel_path, sheet)
        if not cases:
            logger.warning('Now try to process the next sheet page.')
            continue
        for case in cases:
            case_start_time = datetime.datetime.now()
            logger.info('='*100)
            logger.info('Run Case # ' + case['CaseName'])
            logger.info('='*100)

            case_run_result = True
            steps_run_detail = []
            count_all_steps = 0
            count_success_steps = 0
            count_fail_steps = 0
            for step in case['CaseSteps']:
                if step['Run?'] != 'y':
                    continue
                else:
                    try:
                        init_sio()  # clear the string io cache, start recording step running log
                        step_start_time = datetime.datetime.now()
                        logger.info('-' * 50)
                        logger.info('Run Step # ' + step['CaseStep'])
                        logger.info('-' * 50)
                        r1 = True
                        r2 = True
                        r3 = True

                        if step['HandleParameter'] != '':
                            for p in step['HandleParameter']:
                                idx = p.find(':')
                                para.add_parameter(p[:idx], p[idx+1:])
                        if allow_ssh and step['ShellScript'] != '':
                            r1 = shellhandler.run(step)
                        r2 = casehandler.run(step)
                        if allow_SQL and step['SQL'] != '':
                            r3 = sqlhandler.run(step)
                        # it will be confusing if the shell,body,sql are all empty, don't do that
                        step_run_result = r1 and r2 and r3
                        if step_run_result is False:
                            case_run_result = False

                        step_run_log = get_sio().getvalue()  # get step running log
                        step_end_time = datetime.datetime.now()
                        step_duration = step_end_time - step_start_time
                        temp_dict = {'step_name': step['CaseStep'],
                                     'start_time': step_start_time,
                                     'end_time': step_end_time,
                                     'duration': step_duration,
                                     'run_result': step_run_result,
                                     'run_log': step_run_log}
                        steps_run_detail.append(temp_dict)
                        if step_run_result:
                            count_success_steps += 1
                        else:
                            count_fail_steps += 1
                        count_all_steps += 1
                    except Exception as e:
                        logger.error(e)

            if count_all_steps == 0:  # no step run in this case
                logger.info('SKIP')
                continue

            case_end_time = datetime.datetime.now()
            case_duration = case_start_time - case_end_time
            case_temp_dict = {
                'case_name': case['CaseName'],
                'start_time': case_start_time,
                'end_time': case_end_time,
                'duration': case_duration,
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
    logger.info('No more sheet.')

    # process final testing statistics
    test_result_summary['test_end_time'] = datetime.datetime.now()
    test_result_summary['test_duration'] = test_result_summary['test_end_time'] - test_result_summary['test_start_time']
    test_result_summary['count_all_cases'] = count_all_cases
    test_result_summary['count_success_cases'] = count_success_cases
    test_result_summary['count_fail_cases'] = count_fail_cases

    # close ssh and database connections
    if allow_ssh:
        shellhandler.close()
    if allow_SQL:
        sqlhandler.close()

    # generate testing report
    try:
        r.generate_report(test_result_summary, test_result_detail)
    except Exception as e:
        logger.error('Generate report failed.')
        logger.error(e)

