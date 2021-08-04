#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cx_Oracle as oracle  # SQLHandler
from log_helper import *
logger = init_logger(__name__)


class SQLHandler:

    def __init__(self, parameter_handler):
        self.para = parameter_handler
        oracle.init_oracle_client(parameter_handler.get_parameter('db_oracle_lib_dir'))
        self.db_uri = parameter_handler.get_parameter('db_uri')
        self.db_username = parameter_handler.get_parameter('db_username')
        self.db_password = parameter_handler.get_parameter('db_password')
        self.db_conn = oracle.connect(self.db_username, self.db_password, self.db_uri)
        self.db_cur = self.db_conn.cursor()
        logger.debug("connect to Oracle success: " + self.db_conn.version)
        print("sqlhandler init suc")

    def __after_run(self, case, results, db_col):
        if case['ExpectedDQLData'] != "":
            flag = self.para.verify_parameter_in_sql_result(case['ExpectedDQLData'], results, db_col)
        else:
            flag = True
        return flag

    def run(self, case):
        db_cur = self.db_cur
        sql = case['DQL']
        # sql = "SELECT PARAM_VALUE FROM BASE_PARAM WHERE ID='TRADE_DATE'"
        if sql[0:6] == 'SELECT' and sql[0:6] == 'select':
            if sql[-1] == ';':
                sql = sql[0:-1]  # remove ';'
            db_cur.execute(sql)
            db_col = db_cur.description
            results = db_cur.fetchall()
            logger.info("Execute SQL: " + case['DQL'])
            logger.info("SQL results: ")  # here may return too much stuff, take control of your SQL conditions
            logger.info(results)
            # TODO handle multiple SQL results  ...done.
            return self.__after_run(case, results, db_col)
        else:
            sqls = str(sql).splitlines()
            for sql in sqls:
                if sql[-1] == ';':
                    sql = sql[0:-1]  # remove ';'
                db_cur.execute(sql)
            self.db_conn.commit()
            logger.info("Execute SQL: " + case['DQL'])
            return True

    def close(self):
        self.db_cur.close()
        self.db_conn.close()
