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
import allure


# @pytest.fixture()
def init_testcase_data():
    # print("*"*100 + "init_testcase_data()")
    configpath = './config.ini'
    para = Parameter(configpath)
    excel_path = para.get_parameter('excel_path')
    sheets = para.get_parameter('sheet_list')

    test_data = []

    for sheet in sheets:
        cases = read_excel(excel_path, sheet)
        # print(cases)
        for case in cases:
            # print(case)
            for step in case['CaseSteps']:
                step["CaseName"] = case['CaseName']
                test_data.append(step)
    return test_data


test_data = init_testcase_data()


class Test:
    # test_data = init_testcase_data()

    def setup_class(self):
        print("*"*100 + "setup_class()")
        configpath = './config.ini'
        para = Parameter(configpath)

        self.logger = init_logger(__name__)
        self.casehandler = CaseHandler(para)
        self.shellhandler = ShellHandler(para)
        self.sqlhandler = SQLHandler(para)

    @pytest.mark.parametrize("step", test_data)
    def test_case(self, step):
        allure.dynamic.story(step['CaseName'])
        allure.dynamic.title(step['CaseStep'])

        if step['Run?'] != 'y':
            logger.info('SKIP CASE')
            pytest.mark.skip()
        else:
            if step['ShellScript'] != '':
                self.shellhandler.run(step)
            if step['Body'] != '':
                self.casehandler.run(step)
            if step['DQL'] != '':
                self.sqlhandler.run(step)

    def teardown_class(self):
        print("*"*100 + "teardown_class")
        self.shellhandler.close()
        self.sqlhandler.close()


if __name__ == '__main__':
    pytest.main(["-sq", "--alluredir=allure-results", "run_test.py"])
    os.system(r"allure generate allure-results -o allure-report --clean")

