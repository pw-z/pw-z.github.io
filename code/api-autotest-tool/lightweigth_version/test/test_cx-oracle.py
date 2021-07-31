#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cx_Oracle as oracle


def test1():
    db_uri = '10.243.141.118:1521/cmbirs2'
    db_username = 'cmbirs'
    db_password = 'cmbirs'
    oracle.init_oracle_client('C:\oracle\instantclient_19_11')
    conn = oracle.connect(db_username, db_password, db_uri)
    print("connect to Oracle success, Oracle version is" + conn.version)

    sql = r"SELECT * FROM BASE_PARAM"
    cur = conn.cursor()
    cur.execute(sql)  # here return a tuple
    print(cur.description)
    # for col in cur.description:
    #     print(col)
    for col in cur.description:
        # print(col)
        col_1ist = list(col)
        # print(col_1ist)
        # print(col_1ist.index(''))
        if 'PARAM_NAME' in col_1ist:
            print(cur.description.index(col))
    # for row in cur.execute(sql):
    #     print(row)


def test2():
    db_uri = '10.243.141.118:1521/cmbirs2'
    db_username = 'cmbirs'
    db_password = 'cmbirs'
    oracle.init_oracle_client('C:\oracle\instantclient_19_11')
    conn = oracle.connect(db_username, db_password, db_uri)
    print("connect to Oracle success, Oracle version is" + conn.version)
    cur = conn.cursor()

    sql = r"SELECT * FROM BASE_PARAM"
    cur.execute(sql)  # here return a tuple

    WANTED_PARA = 'PARAM_NAME:上清所代理保证金户'
    PARA_COL_NUMBER = -1

    # for col in cur.description:
    #     print(col)
    print(cur.description)
    for col in cur.description:
        # print(col)
        col_description = list(col)
        # print(col_1ist)
        # print(col_1ist.index(''))
        if 'PARAM_NAME' in col_description:
            print(cur.description.index(col))
            PARA_COL_NUMBER = cur.description.index(col)

    for row in cur.execute(sql):
        # print(row)
        row_list = list(row)
        print(row_list)
        print(row_list[PARA_COL_NUMBER])
        if row_list[PARA_COL_NUMBER] == WANTED_PARA[WANTED_PARA.index(':')+1:]:
            print('#'*30 + 'The wanted parameter is Correct!')
        else:
            print('*'*30 + 'Bad Value!')


if __name__ == '__main__':
    # test1()
    test2()
