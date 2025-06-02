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


class TestAPI:

    configpath = './config.ini'
    para = Parameter(configpath)
    excel_path = para.get_parameter('excel_path')
    sheets = para.get_parameter('sheet_list')

    logger = init_logger(__name__)

    for sheet in sheets:
        cases = read_excel(excel_path, sheet)
        print(cases)

        for case in cases:
            # logger.info('\n' + '=' * 100 + '\n Run Case # ' + case['CaseName'] + '\n' + '=' * 100)

            @allure.story(case['CaseName'])
            @pytest.mark.parametrize("step", case['CaseSteps'])
            def test_case(self, step):
                allure.dynamic.story(self.case['CaseSteps'])
                allure.dynamic.title(step['CaseStep'])
                assert 1 == 2


if __name__ == '__main__':
    pytest.main(["-sq", "--alluredir=allure-results"])
    os.system(r"allure generate allure-results -o allure-report --clean")