#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2021.06.25

from CaseHelper import *
from ParameterHandler import Parameter
from Handler import CaseHandler
from Handler import ShellHandler
from Handler import SQLHandler

if __name__ == '__main__':
    # for sheet in sheets:
    #     cases = read_excel(filepath, sheet)
    #     print(cases)

    # try:
    #     res = requests.post(url, headers=header, data=json.dumps(data))
    #     print(res.json())
    #     # print(res)
    # except Exception as e:
    #     print(e)
    configpath = './config.ini'
    para = Parameter(configpath)

    casehandler =CaseHandler(para)
    shellhandler = ShellHandler(para)
    sqlhandler = SQLHandler(para)
    for sheet in sheets:
        cases = read_excel(filepath, sheet)
        # print(cases)
        for case in cases:
            # print(type(case))
            # print(case)
            # print(case['Run?'][0])
            # print(case['Run?'][1])
            # print(case['Run?'][2])
            if case['Run?'][0] == '1':
                shellhandler.run(case)
            if case['Run?'][1] == '1':
                casehandler.run(case)
            if case['Run?'][2] == '1':
                sqlhandler.run(case)


    # s = 'token:2087'
    # dic = {}
    # index = s.find(':')
    # dic[s[:index]] = s[index+1:]
    # print(dic)