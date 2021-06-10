#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Pengwei Zhang

"""
把Excel管理的测试用例通过API导入到Testlink中，需要使用指定的Excel模板，见input目录testcase_template2.xlsx。
Testlink测试用例的结构：唯一的根suite下面可以循环嵌套子suite，叶子节点为测试用例。
"""

# TODO : python3.9使用xlrd会报错【AttributeError: 'ElementTree' object has no attribute 'getiterator'】
import testlink

import xlrd
import logging

filepath = r"../input/testcase_template_new.xlsx"
sheets = ['suitename1']
logger = logging.getLogger()

TESTLINK_SERVER_URL = "http://xxxx:8089/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_KEY = "bdfabc36949xxxxb0"
PROJECT_NAME = "TEST-PROJECT"
TESTPLAN_NAME = "TEST-TESTPLAN"


def get_projectid_by_name(tlapi, name):
    projects = tlapi.getProjects()
    for project in projects:
        if project["name"] == name:
            return project["id"]
    return -1


def get_column_index(sheet, column_name):
    """
    获取列名所在的下标
    :param sheet: excel的sheet页
    :param column_name: 列名
    :return: int
    """
    column_index = None
    for i in range(sheet.ncols):
        if sheet.cell_value(0, i) == column_name:
            column_index = i
            break
    return column_index


def read_excel(file_path, sheet_name):
    """
    读取用例数据
    :param file_path: Excel路径
    :param sheet_name: 要读取的sheet页名称
    :return: case_list_dic
    """
    case_list_dic = []
    try:
        book = xlrd.open_workbook(file_path)  # 打开excel
    except Exception as error:
        logger.error('路径不在或者excel不正确 : ' + str(error))
        return error
    else:
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows  # 取这个sheet页的所有行数
        for i in range(1, rows):  # 忽略第一行表头
            case_dic = {
                'suite_path': sheet.row_values(i)[get_column_index(sheet, 'suite_path')],
                'casename': sheet.row_values(i)[get_column_index(sheet, 'casename')],
                'precondition': sheet.row_values(i)[get_column_index(sheet, 'precondition')],
                'step': sheet.row_values(i)[get_column_index(sheet, 'step')],
                'excepted': sheet.row_values(i)[get_column_index(sheet, 'excepted')],
                'execution_type': sheet.row_values(i)[get_column_index(sheet, 'execution_type')],
                'author': sheet.row_values(i)[get_column_index(sheet, 'author')],
                'priority': sheet.row_values(i)[get_column_index(sheet, 'priority')],
                'summary': sheet.row_values(i)[get_column_index(sheet, 'summary')]
            }
            case_list_dic.append(case_dic)
    return case_list_dic


def main():
    for sheet in sheets:
        cases = read_excel(filepath, sheet)
        print(cases)
    project_id = get_projectid_by_name(PROJECT_NAME)
    if project_id == -1:  # project not exist, create one
        # TODO create project.
        print("hi")


if __name__ == '__main__':
    # main()
    tlapi = testlink.TestlinkAPIGeneric(TESTLINK_SERVER_URL, TESTLINK_API_KEY)
    tlapi.createTestCase

