#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import re
from Log import *

logger = init_logger(__name__)


class Parameter:
    __global_configs = {}
    __parameter_pool = {}

    def __init__(self, configpath):
        cnf = configparser.ConfigParser()
        cnf.read(configpath)

        uri = cnf.get('http', 'URI')
        port = cnf.get('http', 'Port')
        content_type = cnf.get('http', 'content_type')

        ssh_hostname = cnf.get('shell', 'ssh_hostname')
        ssh_username = cnf.get('shell', 'ssh_username')
        ssh_password = cnf.get('shell', 'ssh_password')

        db_uri = cnf.get('database', 'db_uri')
        db_username = cnf.get('database', 'db_username')
        db_password = cnf.get('database', 'db_password')
        db_oracle_lib_dir = cnf.get('database', 'db_oracle_lib_dir')

        self.__global_configs['uri'] = uri
        self.__global_configs['port'] = port
        self.__global_configs['content_type'] = content_type
        self.__global_configs['ssh_hostname'] = ssh_hostname
        self.__global_configs['ssh_username'] = ssh_username
        self.__global_configs['ssh_password'] = ssh_password
        self.__global_configs['db_uri'] = db_uri
        self.__global_configs['db_username'] = db_username
        self.__global_configs['db_password'] = db_password
        self.__global_configs['db_oracle_lib_dir'] = db_oracle_lib_dir

        logger.debug("config object initialize success # " + str(self.__global_configs))

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
                if ':' not in p:
                    logger.debug('flush_parameter_pool: ' + p)
                    if p in response:
                        finds = re.finditer(r'\"{0}\" *: *\"\w*\"'.format(p), response)
                        for _p in finds:
                            # print('find: ' + _p.group())
                            s = _p.group().split(':')
                            s = s[1]
                            # print(s)
                            # print(s[1:-1])
                            self.__parameter_pool[p] = s[1:-1]  # TODO
                            return True
                    else:
                        fail_count += 1
                        logger.error("fail to get parameter in response -> {0}".format(p))
                else:
                    # rename parameter with string after ':'
                    p_origin = p[:p.find(':')]
                    p_rename = p[p.find(':')+1:]
                    logger.debug('flush_parameter_pool: ' + p_origin)
                    if p_origin in response:
                        finds = re.finditer(r'\"{0}\" *: *\"\w*\"'.format(p_origin), response)
                        for _p in finds:
                            # print('find: ' + _p.group())
                            s = _p.group().split(':')
                            s = s[1]
                            # print(s)
                            # print(s[1:-1])
                            self.__parameter_pool[p_rename] = s[1:-1]  # TODO
                            return True
                    else:
                        fail_count += 1
                        logger.error("fail to get parameter in response -> {0}".format(p_origin))


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
                logger.error("fail to replace parameter for request -> {0}".format(p.group()[2:-1]))
                pass

        # if fail_count:
        #     self.logger.error("fail to replace parameter * {0}".format(fail_count))
        return body

    # def verify_parameter_in_response(self, paras_dict, response):
    #     for key in paras_dict:
    #         logger.debug("verify_parameter_in_response: " + key + " ?= " + paras_dict[key])
    #         if key in response:
    #             finds = re.finditer(r'\"{0}\" *: *\"\w*\"'.format(key), response)
    #             for _p in finds:
    #                 s = _p.group().split(':')
    #                 s = s[1]
    #                 # print(s)
    #                 # print(s[1:-1])
    #                 if paras_dict[key] == s[1:-1]:
    #                     logger.info("wanted value of [{0}] is [{1}], correct!".format(key, paras_dict[key]))
    #                 else:
    #                     logger.error("wanted value of [{0}] is [{1}] but found [{2}]".format(key, paras_dict[key], s[1:-1]))
    #         else:
    #             logger.error("could not find the parameter [{0}] in response".format(key))

    def verify_parameter_in_response(self, paras_dict, response):
        for key in paras_dict:
            logger.debug("verify_parameter_in_response: " + key + " ?= " + paras_dict[key])
            if key in response:
                finds = re.finditer(r'\"{0}\" *: *\"\w*\"'.format(key), response)
                for _p in finds:
                    s = _p.group().split(':')
                    para_value = s[1]
                    print(s)
                    # print(s[1:-1])
                    if paras_dict[key] == para_value:
                        logger.info("wanted value of [{0}] is [{1}], correct!".format(key, paras_dict[key]))
                    else:
                        logger.error("wanted value of [{0}] is [{1}] but found [{2}]".format(key, paras_dict[key], para_value))
            else:
                logger.error("could not find the parameter [{0}] in response".format(key))

    def verify_parameter_in_sql_result(self, paras, result):
        logger.info("verify_parameter_in_sql_result... ")
        if paras == result:
            logger.info("wanted value of SQL is [{1}], correct!".format(paras, result))
        else:
            logger.error("wanted value of SQL is [{0}] but found [{1}]".format(paras, result))






