#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import re
from log_helper import *

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

        excel_path = cnf.get('case', 'excel_path')
        sheet_list = cnf.get('case', 'sheet_list')

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

        self.__global_configs['excel_path'] = excel_path
        self.__global_configs['sheet_list'] = sheet_list.split(',')

        self.__global_configs['db_uri'] = db_uri
        self.__global_configs['db_username'] = db_username
        self.__global_configs['db_password'] = db_password
        self.__global_configs['db_oracle_lib_dir'] = db_oracle_lib_dir

        test_report_title = cnf.get('other', 'test_report_title')
        self.__global_configs['test_report_title'] = test_report_title

        logger.debug("parameter handler initialize success # " + str(self.__global_configs))

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
        # print(response)
        if len(parameters) == 0:
            return True
        else:
            for p in parameters:
                if ':' not in p:
                    logger.info('Flush parameter: ' + p)
                    if p in response:
                        re_string = r'("{0}" *: *.*?)'.format(p) + '[,|)|}]'
                        finds = re.finditer(re_string, response)
                        for find in finds:
                            s = find.group(1).split(':')
                            find_value = s[1]
                            if '"' in find_value:
                                # self.__parameter_pool[p] = find_value[1:-1]
                                logger.info('  ' + p + '-->' + find_value[1:-1])
                                self.add_parameter(p, find_value[1:-1])  # deal with "key":"value"
                            else:
                                # self.__parameter_pool[p] = find_value  # deal with "key":value
                                logger.info('  ' + p + '-->' + find_value)
                                self.add_parameter(p, find_value)
                    else:
                        fail_count += 1
                        logger.warning("No parameter in response -> {0}".format(p))
                else:
                    # rename parameter with string after ':'
                    p_origin = p[:p.find(':')]
                    p_rename = p[p.find(':') + 1:]
                    logger.info('Flush parameter: ' + p_origin)
                    if p_origin in response:
                        re_string = r'("{0}" *: *.*?)'.format(p_origin) + '[,|)|}]'
                        finds = re.finditer(re_string, response)
                        for _p in finds:
                            s = _p.group(1).split(':')
                            find_value = s[1]
                            if '"' in find_value:
                                # self.__parameter_pool[p_rename] = find_value[1:-1]  # deal with "key":"value"
                                logger.info('  ' + p + '-->' + find_value[1:-1])
                                self.add_parameter(p_rename, find_value[1:-1])  # deal with "key":"value"
                            else:
                                # self.__parameter_pool[p_rename] = find_value  # deal with "key":value
                                logger.info('  ' + p + '-->' + find_value)
                                self.add_parameter(p_rename, find_value)
                    else:
                        fail_count += 1
                        logger.error("No parameter in response -> {0}".format(p_origin))
            return True if fail_count == 0 else False

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
                logger.info('Replace parameter: {0} --> {1}'.format(p.group(), _p))
            else:
                fail_count += 1
                logger.error("Fail to replace parameter -> {0}".format(p.group()[2:-1]))
                pass

        # if fail_count:
        #     self.logger.error("fail to replace parameter * {0}".format(fail_count))
        return body

    def verify_parameter_in_response(self, paras_dict, response):
        # paras_dict = { 'expected_name1': 'expected_value1', 'expected_name2': 'expected_value2', ... }
        flag = True
        if len(paras_dict) == 0:
            pass
        else:
            logger.info('Verify parameters in response...')
            for key in paras_dict:
                logger.info(" does " + key + " == " + paras_dict[key] + " ?")
                if key in response:
                    # re_string = r'{0} *: *\".*?\"'.format(key)  # outdated
                    re_string = '({0} *: *.*?)'.format(key) + '[,|)|}]'
                    finds = re.finditer(re_string, response)
                    for _p in finds:
                        logger.debug("find {} in response".format(_p.group()))
                        s = _p.group(1).split(':')
                        _p_name = s[0]
                        _p_value = s[1]
                        # print(s)
                        # print(s[1:-1])
                        assert paras_dict[key] == _p_value
                        if paras_dict[key] == _p_value:
                            logger.info("Correct! Expected value of {0} is {1}, found {2}.".format(key, paras_dict[key], _p_value))
                        else:
                            logger.error(
                                "Bad Value! Expected value of {0} is {1} but found {2}".format(key, paras_dict[key], _p_value))
                            flag = False
                else:
                    logger.error("Bad Parameter! No parameter named --> {0}".format(key))
                    flag = False
        return flag

    def verify_parameter_in_sql_result(self, paras, results, db_col):
        logger.info("Verify parameters in sql result... ")

        def verify_method1():
            assert para == str(results)
            if para == str(results):
                # TODO maybe we should consider more when para=='32' but result==32,
                # TODO not just str(result) then conclude that para==result
                logger.info("Correct! Expected SQL result is {1}".format(paras, results))
                return True
            else:
                logger.warning("Bad Value! Expected SQL result is {0} but found {1}".format(paras, results))
                return False

        def verify_method2():
            colon_index = para.index(':')
            para_name = para[:colon_index]
            para_value = para[colon_index + 1:]
            para_col_number = -1
            for col in db_col:
                col_description = list(col)
                if para_name in col_description:
                    # print(db_col.index(col))
                    para_col_number = db_col.index(col)
                    break
            if para_col_number != -1:
                for row in results:
                    # if results contains more then one row, every row needs to meet the para_name:para_value
                    row_list = list(row)
                    _found_value = str(row_list[para_col_number])
                    assert para_value == _found_value
                    if para_value == _found_value:
                        # TODO maybe we should consider more when para=='32' but result==32,
                        # TODO not just str(result) then conclude that para==result
                        logger.info('Correct! Expected value of {0} is {1}, found {2}.'.format(para_name, para_value, _found_value))
                        return True
                    else:
                        logger.warning('Bad Value! Expected value of {0} is {1} BUT found {2}!'.format(para_name,
                                                                                                          para_value,
                                                                                                          _found_value))
                        return False
            else:
                logger.error('Bad Parameter! No column named --> {0}'.format(para_name))
                return False

        flag = True
        for para in paras:  # paras = ['only_one_string_without_colon'] or ['expected_name:expected_value', 'n2:v2',...]
            if ':' in para:
                r = verify_method2()
            else:
                r = verify_method1()
            if not r:
                flag = False
        return flag
