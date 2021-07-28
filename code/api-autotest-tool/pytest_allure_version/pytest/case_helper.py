#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
from log_helper import *

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
        'ContentType': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ContentType')],
        'ResponseParameter': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ResponseParameter')],
        'ExpectedData': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ExpectedData')],
        'ShellScript': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ShellScript')],
        # 'Run?': str(sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Run?')])[:-2],   # 111.0
        'Run?': str(sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Run?')]),  # '111
        'DQL': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'DQL')],
        'ExpectedDQLData': str(
            sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ExpectedDQLData')]).upper().splitlines()
    }
    case_step['ResponseParameter'] = str(case_step['ResponseParameter']).splitlines()

    wanted_paras = {}
    lines = str(case_step['ExpectedData']).splitlines()
    for line in lines:
        i = line.find(':')
        wanted_paras[line[:i]] = line[i + 1:]
    case_step['ExpectedData'] = wanted_paras

    return case_step


def read_excel(file_path, sheet_name):
    case_list_dic = []
    case_step_list = []
    try:
        book = xlrd.open_workbook(file_path)  # 打开excel
    except Exception as error:
        logger.error(r'can not open the excel file  ' + str(error))
        return error
    else:
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows  # 取这个sheet页的所有行数

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
            if i == rows - 1:
                case_dict = {
                    'CaseName': last_case_name,
                    'CaseSteps': case_step_list
                }
                case_list_dic.append(case_dict)

    return case_list_dic
