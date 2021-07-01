#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2021.06.25
import json
import requests
from ParameterHandler import Parameter


class CaseHandler:
    configpath = './config.ini'
    para = Parameter(configpath)

    def __before_run(self, body):
        new_body = self.para.flush_body_parameter(body)
        return new_body

    def __after_run(self, parameters, response):
        self.para.flush_parameter_pool(parameters, response)
        pass

    def run(self, case):
        # __uri = (case['URI']!='') ? case['URI'] : para.get_parameter('uri')
        __uri = case['URI'] if case['URI'] != '' else self.para.get_parameter('uri')
        __port = str(case['Port'])[:4] if str(case['Port'])[:4] != '' else self.para.get_parameter('port')
        __header = case['ContentType'] if case['ContentType'] != '' else self.para.get_parameter('content_type')

        if __uri != '' and __port != '' and case['Address'] != '' and __header != '':
            url = __uri + ":" + __port + case['Address']
            header = {'content-type': __header}
        else:
            return False

        # TODO: PARAMETER REPLACE
        body = case['Body']
        body = self.__before_run(body)

        try:
            res = requests.post(url, headers=header, data=body.encode('utf-8'))
            # print(res.json())
            print(res.text)

            para = str(case['ResponseParameter']).splitlines()
            # print(para)
            self.__after_run(para, res.text)
        except Exception as e:
            print(e)


class ShellHandler:
    pass


class SQLHandler:
    pass
