#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
from helper.log_helper import *

logger = init_logger(__name__)


def get_column_index(sheet, column_name):
    column_index = None
    for i in range(sheet.ncols):
        if sheet.cell_value(0, i) == column_name:
            column_index = i
            break
    return column_index


def get_case_step(sheet_object, row_number):
    case_step = {
        'CaseStep': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'CaseStep')],
        'Method': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Method')],
        'URI': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'URI')],
        'Port': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Port')],  # 9192.0
        'Address': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Address')],
        'Body': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Body')],
        'Header': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Header')],  # multiple lines
        'ResponseParameter': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ResponseParameter')],
        'ExpectedData': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ExpectedData')],  # multiple lines
        'ShellScript': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ShellScript')],
        # 'Run?': str(sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Run?')])[:-2],   # 111.0
        'Run?': str(sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Run?')]),  # '111
        'SQL': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'SQL')],
        'ExpectedSQLData': str(
            sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ExpectedSQLData')]).upper().splitlines(),
        'HandleParameter': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'HandleParameter')]
    }
    case_step['ResponseParameter'] = str(case_step['ResponseParameter']).splitlines()
    case_step['ExpectedData'] = str(case_step['ExpectedData']).splitlines()
    case_step['HandleParameter'] = str(case_step['HandleParameter']).splitlines()

    header_paras = {}
    lines = str(case_step['Header']).splitlines()
    for line in lines:
        i = line.find(':')
        header_paras[line[:i]] = line[i + 1:]
    case_step['Header'] = header_paras

    return case_step


def read_excel(file_path, sheet_name):
    case_list_dic = []
    case_step_list = []
    try:
        book = xlrd.open_workbook(file_path)
    except Exception as error:
        logger.error(r'can not open the excel file  ' + str(error))
        return error
    else:
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows

        case_name = sheet.row_values(1)[get_column_index(sheet, 'CaseName')]  # when i==1, case name must exist
        case_step = get_case_step(sheet, 1)
        case_step_list.append(case_step)
        last_case_name = case_name
        for i in range(2, rows):  # ignore table header

            case_name = sheet.row_values(i)[get_column_index(sheet, 'CaseName')]
            if case_name == '':  # the same case
                case_step = get_case_step(sheet, i)
                case_step_list.append(case_step)
            else:  # new case
                case_dict = {
                    'CaseName': last_case_name,
                    'CaseSteps': case_step_list
                }
                case_list_dic.append(case_dict)

                case_step_list = []
                last_case_name = case_name

                case_step = get_case_step(sheet, i)
                case_step_list.append(case_step)
            if i == rows - 1:  # if the last row, no more case or step, append the case_dict to the case_list_dic
                case_dict = {
                    'CaseName': last_case_name,
                    'CaseSteps': case_step_list
                }
                case_list_dic.append(case_dict)

        # 特殊处理：只有一行用例的情况下不会进入上面的for循环导致没有录入
        if rows == 2:
            case_dict = {
                'CaseName': last_case_name,
                'CaseSteps': case_step_list
            }
            case_list_dic.append(case_dict)

    return case_list_dic
