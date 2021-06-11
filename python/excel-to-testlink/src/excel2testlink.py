#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Pengwei Zhang

"""
把Excel管理的测试用例通过API导入到Testlink中，需要使用指定的Excel模板，见input目录testcase_template2.xlsx。
Testlink测试用例的结构：唯一的根suite下面可以循环嵌套子suite，叶子节点为测试用例。
"""

# TODO : python3.9使用xlrd会报错【AttributeError: 'ElementTree' object has no attribute 'getiterator'】
import testlink as tl

import xlrd
import logging

import testlink.testlinkerrors as tl_error

filepath = r"../input/testcase_template2.xlsx"
sheets = ['suitename1']
logger = logging.getLogger()

TESTLINK_SERVER_URL = "http://xxxx:8089/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_KEY = "xxx"
PROJECT_NAME = "TEST-PROJECT"
TESTCASE_PREFIX = "PWZ-auto-"
TESTPLAN_NAME = "TEST-TESTPLAN"


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


def main(testlink_api):

    # TODO 1 : get the testprojectid or create one if not exist
    # def get_projectid_by_name(tlapi, name):
    #     projects = tlapi.getProjects()
    #     for project in projects:
    #         if project["name"] == name:
    #             return project["id"]
    #     return -1

    def get_projectid_by_name(tlapi, name):
        try:
            project_id = tlapi.getTestProjectByName(name)
        except tl_error.TLResponseError as e:
            print(e)
            return -1
        else:
            return project_id

    project_id = get_projectid_by_name(testlink_api, PROJECT_NAME)
    if project_id == -1:  # project not exist, create one
        print("no project found, creating...")
        try:
            testlink_api.createTestProject(PROJECT_NAME, TESTCASE_PREFIX)
        except Exception as e:
            print("create fail : ")
            print(e)
        else:
            project_id = get_projectid_by_name(testlink_api, PROJECT_NAME)
            print("create project {0} (ID = {1}) successful.".format(PROJECT_NAME, project_id))
    else:
        print(project_id)

    # TODO 2 :
    #  1.get test suites structure (it is a Tree)
    #  2.create test suites
    #  3.return suite_name_id_dic

    def print_all_top_testsuites_by_projectid(tlapi, projectid):
        suites = tlapi.getFirstLevelTestSuitesForTestProject(projectid)
        for suite in suites:
            print(suite)


if __name__ == '__main__':
    tlapi = tl.TestlinkAPIGeneric(TESTLINK_SERVER_URL, TESTLINK_API_KEY)
    # main(tlapi)

    project = tlapi.getTestProjectByName(PROJECT_NAME)
    project_id = project['id']
    print(project_id)

    for sheet in sheets:
        cases = read_excel(filepath, sheet)
        # print(cases)
        for case in cases:
            # print("-----------------" + case["suite_path"])
            suite_path = case["suite_path"]
            for i in range(0, suite_path.count("/")+1):
                _index = suite_path.find("/")

                if _index != -1:
                    _suite_name = suite_path[:_index]
                    suite_path = suite_path[_index + 1:]
                else:
                    _suite_name = suite_path
                # print(_suite_name)

                if i == 0:
                    parent_suite = ""
                if parent_suite == "":
                    print(_suite_name + " is the top level suite")
                    # TODO : GET SUITE OR CREATE ON IF NOT EXIST WITH SUITE NAME
                else:
                    print(_suite_name + " will be create with parent " + parent_suite)
                    # TODO : GET SUITE OR CREATE ON IF NOT EXIST WITH SUITE NAME AND PARENT SUITE(ID)
                parent_suite = _suite_name
                # suite_path = suite_path[_index + 1:]





    # TODO : get suite id or create one if suite not exist
    # suite_name = "手续费核算"
    # try:
    #     suite = tlapi.getTestSuite(suite_name, TESTCASE_PREFIX)
    # except Exception as e:
    #     print(e)
    #     try:
    #         print("creating suite...")
    #         suite = tlapi.createTestSuite(project_id, suite_name, "test_detail")
    #     except Exception as e:
    #         print(e)
    #     else:
    #         print("create suite successful, suite_id = {0}".format(suite))
    # else:
    #     print("got {0}' = {1}".format(suite_name, suite))

