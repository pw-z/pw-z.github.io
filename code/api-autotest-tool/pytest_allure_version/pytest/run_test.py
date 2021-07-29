#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from parameter_handler import Parameter
from case_handler import CaseHandler
from shell_handler import ShellHandler
from sql_handler import SQLHandler
from case_helper import *
from log_helper import *
import datetime

import pytest
import pytest_assume
import allure


# @pytest.fixture(scope="class")
def init_testcase_data():
    configpath = './config.ini'
    para = Parameter(configpath)

    # print(para.get_parameter('excel_path'))
    # print(para.get_parameter('sheet_list'))
    excel_path = para.get_parameter('excel_path')
    # print(excel_path)
    sheets = para.get_parameter('sheet_list')

    logger = init_logger(__name__)
    # print(logger.level)

    casehandler = CaseHandler(para)
    shellhandler = ShellHandler(para)
    sqlhandler = SQLHandler(para)

    test_data = []

    for sheet in sheets:
        cases = read_excel(excel_path, sheet)
        # print(cases)

        for case in cases:
            # print(case)

            for step in case['CaseSteps']:
                step["CaseName"] = case['CaseName']
                # print(step)
                # step = (step,)
                # print(type(step[0]))
                test_data.append(step)
    return test_data


class Test:

    # data = init_testcase_data()
    # print(data)

    configpath = './config.ini'
    para = Parameter(configpath)

    # print(para.get_parameter('excel_path'))
    # print(para.get_parameter('sheet_list'))
    excel_path = para.get_parameter('excel_path')
    # print(excel_path)
    sheets = para.get_parameter('sheet_list')

    logger = init_logger(__name__)
    # print(logger.level)

    casehandler = CaseHandler(para)
    shellhandler = ShellHandler(para)
    # sqlhandler = SQLHandler(para)

    test_data = []

    for sheet in sheets:
        cases = read_excel(excel_path, sheet)
        # print(cases)

        for case in cases:
            # print(case)

            for step in case['CaseSteps']:
                step["CaseName"] = case['CaseName']
                # print(step)
                # step = (step,)
                # print(type(step[0]))
                test_data.append(step)

    @pytest.mark.parametrize("step", test_data)
    def test_case(self, step):
        allure.dynamic.story(step['CaseName'])
        allure.dynamic.title(step['CaseStep'])
        # assert step['CaseName'] == '参数获取1'



        if step['Run?'] != 'y':
            # logger.info('SKIP CASE')
            pytest.mark.skip()
        else:
            if step['ShellScript'] != '':
                self.shellhandler.run(step)

            if step['Body'] != '':
                self.casehandler.run(step)
                pytest.assume(1 == 2)
                pytest.assume(3 == 2)
            # if step['DQL'] != '':
                # self.sqlhandler.run(step)

    # shellhandler.close()
    # sqlhandler.close()


if __name__ == '__main__':
    pytest.main(["-sq", "--alluredir=allure-results"])
    os.system(r"allure generate allure-results -o allure-report --clean")