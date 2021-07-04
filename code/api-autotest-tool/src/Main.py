#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pwz.wiki 2021.06.25

from CaseHelper import *
from ParameterHandler import Parameter
from Handler import CaseHandler
from Handler import ShellHandler
from Handler import SQLHandler

if __name__ == '__main__':
    configpath = './config.ini'
    para = Parameter(configpath)

    casehandler =CaseHandler(para)
    shellhandler = ShellHandler(para)
    sqlhandler = SQLHandler(para)
    for sheet in sheets:
        cases = read_excel(filepath, sheet)
        # print(cases)
        for case in cases:
            if case['Run?'][0] == '1':
                shellhandler.run(case)
            if case['Run?'][1] == '1':
                casehandler.run(case)
            if case['Run?'][2] == '1':
                print('-'*40)
                # sqlhandler.run(case)