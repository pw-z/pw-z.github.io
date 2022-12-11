#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from helper.log_helper import *
logger = init_logger(__name__)


class CaseHandler:
    """Handler test case.

    run(): post or get the request through requests.\n
    __before_run(): flush body parameter\n
    __after_run(): flush global parameter pool, verify parameter in response
    """

    def __init__(self, parameter_handler):
        self.para = parameter_handler

    def __before_run(self, body):
        new_body = self.para.flush_data_parameter(body)
        return new_body

    def __after_run(self, case, response):
        # 1. flush the parameter pool
        self.para.flush_parameter_pool(case['ResponseParameter'], response)
        # 2. verify the wanted response values
        flag = self.para.verify_parameter_in_response(case['ExpectedData'], response)
        return flag

    def run(self, case):
        __uri = case['URI'] if case['URI'] != '' else self.para.get_parameter('uri')
        __port = case['Port'] if case['Port'] != '' else self.para.get_parameter('port')
        __header = case['Header'] if case['Header'] != '' else self.para.get_parameter('Header')

        if __uri != '' and __port != '' and case['Address'] != '' and __header != '':
            url = __uri + ":" + __port + case['Address']
            header = __header
            logger.info('Request url: ' + url)
            logger.info('Request header:\n' + str(__header))
        else:
            return False

        try:
            # send requests based on method type
            if str(case['Method']).lower() == 'post':
                body = case['Body']
                body = self.__before_run(body)
                logger.info('Request body:\n' + body)
                res = requests.post(url, headers=header, data=body.encode('utf-8'), verify=False)
            elif str(case['Method']).lower() == 'get':
                res = requests.get(url, headers=header, verify=False)
            else:
                raise Exception('Request method not in ["post", "get"].')
        except Exception as e:
            logger.error(e)
            return False
        else:
            logger.info('Response:\n' + res.text)
            return self.__after_run(case, res)

