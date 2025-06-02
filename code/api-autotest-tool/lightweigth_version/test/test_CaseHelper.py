#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handler.ParameterHandler import Parameter
from helper.case_helper import *


def test1():
    configpath = '../config.ini'
    para = Parameter(configpath)

    excel_path = para.get_parameter('excel_path')
    print(excel_path)
    sheets = para.get_parameter('sheet_list')

    for sheet in sheets:
        cases = read_excel(excel_path, sheet)
        for case in cases:
            # print(case)
            for step in case['CaseSteps']:
                print(step)
                print()
            print("*"*100)
            print("*"*100)


if __name__ == '__main__':
    test1()
