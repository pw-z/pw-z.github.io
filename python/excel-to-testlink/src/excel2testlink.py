#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2021

"""
把Excel管理的测试用例通过API导入到Testlink中，需要使用指定的Excel模板，见input目录testcase_template2.xlsx。
Testlink测试用例的结构：唯一的根suite下面可以循环嵌套子suite，叶子节点为测试用例。

!NOTE: python3.9使用xlrd会报错 --> AttributeError: 'ElementTree' object has no attribute 'getiterator'
"""

import testlink as tl
import xlrd
import logging

filepath = r"../input/testcase_template_2.xlsx"
sheets = ['suitename1']
logger = logging.getLogger()

TESTLINK_SERVER_URL = "http://xxxx:xxx/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_KEY = "xxxxxxxxxxxxxxxxxxxx"
PROJECT_NAME = "TEST-PROJECT"
TESTCASE_PREFIX = "PWZ-auto-"


# TESTPLAN_NAME = "TEST-TESTPLAN"


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


# TODO 1 : get the test project or create one if not exist √
def init_test_project(testlink_api):
    # def get_projectid_by_name(tlapi, name):
    #     projects = tlapi.getProjects()
    #     for project in projects:
    #         if project["name"] == name:
    #             return project["id"]
    #     return -1

    def get_project_by_name(tlapi, name):
        try:
            project = tlapi.getTestProjectByName(name)
        except Exception as e:
            print(e)
            return -1
        else:
            return project

    project = get_project_by_name(testlink_api, PROJECT_NAME)
    if project == -1:  # project not exist, create one
        print("no project found, creating...")
        try:
            testlink_api.createTestProject(PROJECT_NAME, TESTCASE_PREFIX)
        except Exception as e:
            print("create fail : ")
            print(e)
        else:
            project = get_project_by_name(testlink_api, PROJECT_NAME)
            print("create project {0} (ID = {1}) successful.".format(PROJECT_NAME, project['id']))
            return project
    else:
        print(project)
        return project


# TODO 2 :
#  1.get test suites structure (it is a Tree)
#  2.create test suites
#  3.create test cases under current suite
# def get_or_create_suite_by_name(suite_name, project_id, TESTCASE_PREFIX):
#     try:
#         suite = tlapi.getTestSuite(suite_name, TESTCASE_PREFIX)
#     except Exception as e:
#         print(e)
#         try:
#             print("creating suite...")
#             suite = tlapi.createTestSuite(project_id, suite_name, "test_detail")
#         except Exception as e:
#             print(e)
#         else:
#             print("create suite successful, suite_id = {0}".format(suite))
#             return suite
#     else:
#         print("got {0}' = {1}".format(suite_name, suite))
#         return suite

def get_or_create_suite_by_name_and_parentid(suite_name, project_id, parent_suite_id, TESTCASE_PREFIX):
    def find_suite_in_all_suites():
        all_suites = tlapi.getTestSuite(suite_name, TESTCASE_PREFIX)
        # print(all_top_suites)
        for suite in all_suites:
            if suite['name'] == suite_name and suite['parent_id'] == parent_suite_id:
                return suite
        return -1

    if parent_suite_id == '':  # meet a top suite
        all_top_suites = tlapi.getFirstLevelTestSuitesForTestProject(project_id)
        print(all_top_suites)
        for suite in all_top_suites:
            if suite['name'] == suite_name:
                return suite
        # find none, create one
        try:
            print("creating top suite ({0}) ...".format(suite_name))
            suite_add_info = tlapi.createTestSuite(project_id, suite_name, "test_detail")[0]
        except Exception as e:
            print(e)
        else:
            print("create suite successful, suite = {0}".format(suite_add_info))
            all_top_suites = tlapi.getFirstLevelTestSuitesForTestProject(project_id)
            print(all_top_suites)
            for suite in all_top_suites:
                if suite['name'] == suite_name:
                    return suite
    else:  # not a top suite
        try:
            all_suites_with_the_name = tlapi.getTestSuite(suite_name, TESTCASE_PREFIX)
        except Exception as e:  # nothing found, just create it
            print("no suite found")
            print(e)
            try:
                print("creating suite...")
                tlapi.createTestSuite(project_id, suite_name, "test_detail", parentid=parent_suite_id)
            except Exception as e:
                print(e)
            else:
                suite = find_suite_in_all_suites()
                if suite != -1:
                    print("create suite successful, suite = {0}".format(suite))
                    return suite
                else:
                    raise Exception("fail to create the suite!!")
        else:  # found something, but may not what we want
            for suite in all_suites_with_the_name:
                if suite["parent_id"] == parent_suite_id:
                    print("got {0} = {1}".format(suite_name, suite))
                    return suite  # suite found
            # oops
            try:
                print("creating suite {0} with parent id {1} ...".format(suite_name, parent_suite_id))
                tlapi.createTestSuite(project_id, suite_name, "test_detail", parentid=parent_suite_id)
            except Exception as e:
                print(e)
            else:
                suite = find_suite_in_all_suites()
                if suite != -1:
                    print("create suite successful, suite = {0}".format(suite))
                    return suite
                else:
                    raise Exception("fail to create the suite!!")


def import_test_cases(tlapi, project_id, cases):
    count = {'succeed': 0, 'failed': 0}
    for case in cases:
        # print("-----------------" + case["suite_path"])
        suite_path = case["suite_path"]
        parent_suite = {}
        for i in range(0, suite_path.count("/") + 1):
            _index = suite_path.find("/")

            if _index != -1:
                _suite_name = suite_path[:_index]
                suite_path = suite_path[_index + 1:]
            else:
                _suite_name = suite_path
            # print(_suite_name)

            if i == 0:
                parent_suite["id"] = ""
            if parent_suite["id"] == "":
                print(_suite_name + " is the top level suite")
                # TODO : GET SUITE OR CREATE ON IF NOT EXIST WITH SUITE NAME
                try:
                    suite = get_or_create_suite_by_name_and_parentid(_suite_name, project_id, "", TESTCASE_PREFIX)
                    print(suite)
                except Exception as e:
                    print("*" * 50)
                    print(e)
            else:
                print(_suite_name + " is the subsuite under parent " + parent_suite["name"])
                # TODO : GET SUITE OR CREATE ON IF NOT EXIST WITH SUITE NAME AND PARENT SUITE(ID)
                try:
                    suite = get_or_create_suite_by_name_and_parentid(_suite_name, project_id, parent_suite["id"], TESTCASE_PREFIX)
                    print(suite)
                except Exception as e:
                    print("#" * 80)
                    print(e)
            parent_suite = suite

        # create suite done, now create test case
        print('under the path {}'.format(case["suite_path"]))
        print('!!!!! create test case under {}'.format(parent_suite['name']))

        """
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
        
        createTestCase: Create a test case
        positional args: testcasename, testsuiteid, testprojectid, authorlogin,
                         summary
        optional args : steps, preconditions, importance, executiontype, order,
                        internalid, checkduplicatedname, actiononduplicatedname,
                        status, estimatedexecduration
                        
        argument 'steps' will be set with values from .stepsList, 
        - when argsOptional does not include a 'steps' item
        - .stepsList can be filled before call via .initStep() and .appendStep()
        
        otherwise, optional arg 'steps' must be defined as a list with 
        dictionaries , example
            [{'step_number' : 1, 'actions' : "action A" , 
                'expected_results' : "result A", 'execution_type' : 0},
                 {'step_number' : 2, 'actions' : "action B" , 
                'expected_results' : "result B", 'execution_type' : 1},
                 {'step_number' : 3, 'actions' : "action C" , 
                'expected_results' : "result C", 'execution_type' : 0}]
            
        possible values for optional arguments testlink/cfg/const.inc.php
        importance:    1 (low)    2 (medium) 3 (high)   
        status:        1 (draft)             2 (readyForReview)
                       3 (reviewInProgress)  4 (rework) 
                       5 (obsolete)          6 (future)
                       7 (final)
        executiontype: 1 (Manual)            2 (Automated)
        """
        switcher = {
            "low": 1,
            "medium": 2,
            "high": 3,
            "manual": 1,
            "automated": 2
        }
        c_name = case['casename']
        c_precondition = case['precondition']
        c_step = case['step']
        c_excepted = case['excepted']
        c_author = case['author']
        c_summary = case['summary']
        # c_steps = list(zip(case['step'].split('\n'), case['excepted'].split('\n')))
        c_steps = [{'step_number': 1, 'actions': c_step.replace("\n", "<br>"),
                    'expected_results': c_excepted.replace("\n", "<br>"), 'execution_type': 0}]  # ONLY ONE STEP
        c_importance = switcher.get(case['priority'])
        c_execution_type = switcher.get(case['execution_type'])
        try:
            tlapi.createTestCase(c_name, parent_suite['id'], project_id, c_author, c_summary, c_steps,
                                 preconditions=c_precondition, importance=c_importance, executiontype=c_execution_type)
        except Exception as e:
            print(e)
            count['failed'] += 1
        else:
            count['succeed'] += 1
    return count


if __name__ == '__main__':
    tlapi = tl.TestlinkAPIGeneric(TESTLINK_SERVER_URL, TESTLINK_API_KEY)

    project = init_test_project(tlapi)
    project_id = project['id']
    print("INIT PROJECT DONE, GOT PROJECT ID : " + project_id)

    for sheet in sheets:
        cases = read_excel(filepath, sheet)
        # print(cases)
        count = import_test_cases(tlapi, project_id, cases)
        print('import done, {0} succeed, {1} failed.'.format(count['succeed'], count['failed']))
