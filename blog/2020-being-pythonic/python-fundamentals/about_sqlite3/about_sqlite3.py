#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3 as sq3


def create_table(db_name):
    conn = sq3.connect(db_name)
    cur = conn.cursor()
    table_creation_sql = '''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);'''
    cur.execute(table_creation_sql)
    print("Table created successfully")
    conn.commit()
    conn.close()


def insert_data(conn):
    cur = conn.cursor()
    s1 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )"
    s2 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )"
    s3 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )"
    s4 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )"
    cur.execute(s1)
    cur.execute(s2)
    cur.execute(s3)
    cur.execute(s4)
    conn.commit()


def query_data(conn):
    cur = conn.cursor()
    print(cur.execute("select * from company"))


if __name__ == '__main__':
    db_name = 'test.db'
    # create_table(db_name)
    conn = sq3.connect(db_name)
    # insert_data(conn)
    # query_data(conn)
    cur = conn.cursor()
    res = cur.execute("select * from company")
    print(res.fetchall())

    # cur.execute("delete from company where id=1")
    # conn.commit()
    print(conn.total_changes)

