#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import re
from helper.log_helper import *

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
        """
        刷新参数池，根据用例的ResponseParameter字段从响应中获取参数存放到参数池中
        :param parameters:测试用例的ResponseParameter字段，按行拆分成的list
        :param response:接口的响应结果
        :return:
        """

        def flush_by_re(_fail_count, _pattern):
            _response = response.text
            if ':' not in _pattern:
                logger.info('Flush parameter: ' + _pattern)
                if _pattern in _response:
                    re_string = r'("{0}" *: *.*?)'.format(_pattern) + '[,|)|}]'
                    finds = re.finditer(re_string, _response)
                    for find in finds:
                        s = find.group(1).split(':')
                        find_value = s[1]
                        if '"' in find_value:
                            logger.info('  ' + _pattern + '-->' + find_value[1:-1])
                            self.add_parameter(_pattern, find_value[
                                                  1:-1])  # deal with "key":"value"
                        else:
                            logger.info('  ' + _pattern + '-->' + find_value)
                            self.add_parameter(_pattern, find_value)
                else:
                    _fail_count[0] += 1
                    logger.warning("No parameter in response -> {0}".format(_pattern))
            else:
                # rename parameter with string after ':'
                p_origin = _pattern[:_pattern.find(':')]
                p_rename = _pattern[_pattern.find(':') + 1:]
                logger.info('Flush parameter: ' + p_origin)
                if p_origin in _response:
                    re_string = r'("{0}" *: *.*?)'.format(p_origin) + '[,|)|}]'
                    finds = re.finditer(re_string, _response)
                    for _p in finds:
                        s = _p.group(1).split(':')
                        find_value = s[1]
                        if '"' in find_value:
                            logger.info('  ' + _pattern + '-->' + find_value[1:-1])
                            self.add_parameter(p_rename, find_value[
                                                         1:-1])  # deal with "key":"value"
                        else:
                            logger.info('  ' + _pattern + '-->' + find_value)
                            self.add_parameter(p_rename, find_value)
                else:
                    _fail_count[0] += 1
                    logger.error(
                        "No parameter in response -> {0}".format(p_origin))

        def flush_by_json_dict(_fail_count, _pattern):
            # 先将response转换成json格式
            try:
                logger.info('>> transforming response into json format..')
                _response = response.json()
            except Exception as e:
                logger.error(
                    '>> transform failed, please check the content-type of the response.')
                logger.error(e)
                _fail_count[0] += 1
                return

            # 层层递进按照路径获取json中的节点
            path = str(_pattern[2:]).split('::')
            key = path
            for idx in range(len(path) - 1):
                try:
                    key = path[idx]
                    if key.startswith('#'):
                        key = int(key[1:])
                    _response = _response[key]
                except Exception as e:
                    logger.error(
                        '>> can\'t deal with {} in response.json()'.format(key))
                    logger.error(e)
                    _fail_count[0] += 1
                    return

            # 准备获取最后一个节点（目标节点，不一定是叶子节点）的值，但需要处理参数重命名
            final = path[-1]
            if ':' in final:
                try:
                    p_origin = final[:final.find(':')]
                    p_rename = final[final.find(':') + 1:]
                    if p_origin.startswith('#'):
                        p_origin = int(p_origin[1:])
                    p_value = _response[p_origin]
                except Exception as e:
                    logger.error('>> can\'t deal with {} in response.json()'.format(final))
                    logger.error(e)
                    _fail_count[0] += 1
                    return
                else:
                    logger.info('  ' + _pattern + '-->' + p_value)
                    self.add_parameter(p_rename, p_value)
            else:
                # 不需要处理重命名，同时也不支持数字（及#开头）
                try:
                    p_value = _response[final]
                except Exception as e:
                    logger.error('>> can\'t deal with {} in response.json()'.format(final))
                    logger.error(e)
                    _fail_count[0] += 1
                    return
                else:
                    logger.info('  ' + _pattern + '-->' + p_value)
                    self.add_parameter(final, p_value)

        fail_count = [0]  # 使用可变类型，让子函数处理的时候可以改变该值
        if len(parameters) == 0:
            return True
        else:
            for p in parameters:
                if str(p).startswith('::'):
                    flush_by_json_dict(fail_count, p)
                else:
                    flush_by_re(fail_count, p)
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

    def verify_parameter_in_response(self, paras_list, response):
        """
        新的响应结果校验函数@2021年11月24日
        :param paras_list: 按行划分的期望结果list，每行校验一项内容，三种形式，简单键值对、路径键值对、字符串包含
        :param response: request请求收到的响应
        :return:
        """

        def verify_1_simple_key_value(_verification):
            logger.info('> handle verification --> ' + _verification)
            _response = response.text
            pivot = _verification.find(':')
            key = _verification[:pivot]
            value = _verification[pivot+1:]

            logger.info(">> " + key + " == " + value + " ?")
            if key in _response:
                # re_string = r'{0} *: *\".*?\"'.format(key)  # outdated
                re_string = '({0} *: *.*?)'.format(key) + '[,|)|}]'
                finds = re.finditer(re_string, _response)
                for _p in finds:
                    logger.debug(">> find {} in response".format(_p.group()))
                    s = _p.group(1).split(':')
                    _p_name = s[0]
                    _p_value = s[1]
                    if value == _p_value:
                        logger.info(">> Correct! Expected value of {0} is {1}, found {2}.".format(key, value, _p_value))
                    else:
                        logger.error(
                            "Bad Value! Expected value of {0} is {1} but found {2}".format(key, value, _p_value))
                        return False
                return True
            else:
                logger.error("Bad Parameter! No parameter named --> {0}".format(key))
                return False

        def verify_2_json_path_key_value(_verification):
            logger.info('> handle verification --> ' + _verification)

            try:
                logger.info('>> transforming response into json format..')
                _response = response.json()
            except Exception as e:
                logger.error('>> transform failed, please check the content-type of the response.')
                logger.error(e)
                return False

            logger.info('>> verifying...')
            path = str(_verification[2:]).split('::')
            key = path  # 此处给key一个初始值以防后续循环内key初始化失败
            for idx in range(len(path) - 1):
                try:
                    key = path[idx]
                    if key.startswith('#'):
                        key = int(key[1:])
                    _response = _response[key]
                except Exception as e:
                    logger.error('>> can\'t deal with {} in response.json()'.format(key))
                    logger.error(e)
                    return False

            target = path[-1]
            if target.startswith('#'):
                target = int(target[1:])

            if target == _response:
                logger.info('>> Ok. ')
                return True
            else:
                logger.error('Bad Value! Expected value of {0} is {1}({2}) but found {3}({4})'
                             .format(_verification, target, type(target), _response, type(_response)))
                return False

        def verify_3_string_contain(_verification):
            logger.info('> handle verification --> ' + _verification)
            _verification = _verification[2:]
            logger.info(">> does response contains string: " + _verification + " ?")
            if _verification in response.text:
                logger.info('>> Yes.')
                return True
            else:
                logger.error('>> No.')
                return False

        flag = True
        if len(paras_list) == 0:
            pass
        else:
            logger.info('Verify parameters in response...')
            for verification in paras_list:
                if str(verification).startswith('::'):
                    # 调用路径键值对的校验方法，要求response为json格式串
                    if not verify_2_json_path_key_value(verification):
                        flag = False
                elif str(verification).startswith(';;'):
                    # 调用字符串包含的校验方法
                    if not verify_3_string_contain(verification):
                        flag = False
                elif str(verification).count(':') == 1:
                    # 调用简单键值对的校验方法
                    if not verify_1_simple_key_value(verification):
                        flag = False
                else:
                    logger.error('Parameters verification format error: ' + verification)
                    flag = False
        return flag

    def verify_parameter_in_sql_result(self, paras, results, db_col):
        logger.info("Verify parameters in sql result... ")

        def verify_method1():
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
