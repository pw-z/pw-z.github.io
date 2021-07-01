#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2021.06.25

import configparser
import re
import logging


class Parameter:
    __global_configs = {}
    __parameter_pool = {}

    def __init__(self, configpath):
        self.logger = logging.getLogger()
        cnf = configparser.ConfigParser()
        cnf.read(configpath)

        uri = cnf.get('http', 'URI')
        port = cnf.get('http', 'Port')
        content_type = cnf.get('http', 'content_type')
        print(uri + '/' + port)
        print('content type: ' + content_type)

        self.__global_configs['uri'] = uri
        self.__global_configs['port'] = port
        self.__global_configs['content_type'] = content_type

    def get_parameter(self, p_name):
        if p_name in self.__global_configs:
            return self.__global_configs[p_name]
        elif p_name in self.__parameter_pool:
            return self.__parameter_pool[p_name]
        else:
            return False

    def add_parameter(self, p_name, p_value):
        self.__parameter_pool[p_name] = p_value
        return True

    def flush_parameter_pool(self, parameters, response):
        fail_count = 0
        # print(parameters)
        # print(len(parameters))
        # print(response)
        if len(parameters) == 0:
            return True
        else:
            for p in parameters:
                print('P: ' + p)
                if p in response:
                    print('hit')
                    finds = re.finditer(r'\"{0}\" *: *\"\w*\"'.format(p), response)
                    for _p in finds:
                        print('find: ' + _p.group())
                        s = _p.group().split(':')
                        s = s[1]
                        print(s)
                        print(s[1:-1])
                        self.__parameter_pool[p] = s[1:-1]  # TODO
                        return True
                else:
                    fail_count += 1
                    self.logger.error("fail to get parameter in response -> {0}".format(p))

    def flush_body_parameter(self, body):
        """
        replace '${A}' with 'A' in __parameter_pool
        :param body:
        :return: 
        """
        paras = re.finditer(r'\$\{\w*\}', body)
        fail_count = 0

        for p in paras:
            # re.sub(r'\$\{\w*\}', self.get_parameter(p.group()[2:-1]), request_body)
            # print(p.group())
            _p = self.get_parameter(p.group()[2:-1])
            if _p:
                body = body.replace(p.group(), _p)
            else:
                fail_count += 1
                self.logger.error("fail to replace parameter for request -> {0}".format(p.group()[2:-1]))
                pass

        # if fail_count:
        #     self.logger.error("fail to replace parameter * {0}".format(fail_count))

        return body






