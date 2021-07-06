#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests  # CaseHandler
import paramiko  # ShellHandler
import cx_Oracle as oracle  # SQLHandler
from helper.Log import *

logger = init_logger(__name__)


class CaseHandler:

    def __init__(self, parameter_handler):
        self.para = parameter_handler

    def __before_run(self, body):
        new_body = self.para.flush_body_parameter(body)
        return new_body

    def __after_run(self, case, response):
        # 1. flush the parameter pool
        self.para.flush_parameter_pool(case['ResponseParameter'], response.text)
        # 2. verify the wanted response values
        flag = self.para.verify_parameter_in_response(case['ExpectedData'], response.text)
        return flag

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
        logger.info('Request body:\n' + body)

        try:
            res = requests.post(url, headers=header, data=body.encode('utf-8'))
            # print(res.json())
            logger.debug(res.text)
        except Exception as e:
            logger.error(e)
        else:
            return self.__after_run(case, res)


class ShellHandler:

    def __init__(self, parameter_handler):
        self.ssh_hostname = parameter_handler.get_parameter('ssh_hostname')
        self.ssh_username = parameter_handler.get_parameter('ssh_username')
        self.ssh_password = parameter_handler.get_parameter('ssh_password')
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def run(self, case):
        self.ssh.connect(hostname=self.ssh_hostname, port=22, username=self.ssh_username, password=self.ssh_password)
        sh = case['ShellScript']
        logger.info("Execute command:\n" + sh)
        stdin, stdout, stderr = self.ssh.exec_command(sh)
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        logger.info("Command result:\n " + result.decode())

        self.ssh.close()
        return True


class SQLHandler:

    def __init__(self, parameter_handler):
        self.para = parameter_handler
        oracle.init_oracle_client(parameter_handler.get_parameter('db_oracle_lib_dir'))
        self.db_uri = parameter_handler.get_parameter('db_uri')
        self.db_username = parameter_handler.get_parameter('db_username')
        self.db_password = parameter_handler.get_parameter('db_password')
        self.db_conn = oracle.connect(self.db_username, self.db_password, self.db_uri)
        logger.debug("connect to Oracle success: " + self.db_conn.version)

    def __after_run(self, case, results):
        flag = self.para.verify_parameter_in_sql_result(case['ExpectedDQLData'], results)
        return flag

    def run(self, case):
        db_conn = self.db_conn
        db_cur = db_conn.cursor()
        sql = case['DQL']
        # sql = "SELECT PARAM_VALUE FROM BASE_PARAM WHERE ID='TRADE_DATE'"
        db_cur.execute(sql)
        results = db_cur.fetchall()
        logger.info("Execute SQL: " + case['DQL'])
        logger.info("SQL results:")
        # logger.debug(results)
        for row in results:
            logger.info(row[0])
            return self.__after_run(case, row[0])

        # db_cur.close()
        # db_conn.close()
