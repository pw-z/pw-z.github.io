#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fetch test cases from a Excel file.

Make sure the case file is in `.xlsx` format and the xlrd package
version == 1.2.0, using `pip install xlrd==1.2.0`to install it.
"""

import xlrd

from helper.log_helper import init_logger

logger = init_logger(__name__)


def get_column_index(sheet, column_name: str):
    """Locate the column index number by column name.

    :param sheet: xlrd.open_workbook().sheet_by_name()
    :param column_name: column name string
    :return: column index if column exists or None if not
    """
    column_index = None
    for i in range(sheet.ncols):
        if sheet.cell_value(0, i) == column_name:
            column_index = i
            break
    return column_index


def get_case_step(sheet, row_number: int):
    """Fetch case step detail by row number.

    :param sheet: object xlrd.open_workbook().sheet_by_name()
    :param row_number: a case may contain multiple steps, each row represents one step
    :return: case step detail dict
    """
    case_step = {
        'CaseStep': sheet.row_values(row_number)[get_column_index(sheet, 'CaseStep')],
        'Method': sheet.row_values(row_number)[get_column_index(sheet, 'Method')],
        'URI': sheet.row_values(row_number)[get_column_index(sheet, 'URI')],
        'Port': sheet.row_values(row_number)[get_column_index(sheet, 'Port')],  # 9192.0
        'Address': sheet.row_values(row_number)[get_column_index(sheet, 'Address')],
        'Body': sheet.row_values(row_number)[get_column_index(sheet, 'Body')],
        'Header': sheet.row_values(row_number)[get_column_index(sheet, 'Header')],  # multiple lines --> dict
        'ResponseParameter': sheet.row_values(row_number)[get_column_index(sheet, 'ResponseParameter')],  # multiple lines --> list
        'ExpectedData': sheet.row_values(row_number)[get_column_index(sheet, 'ExpectedData')],  # multiple lines --> list
        'ShellScript': sheet.row_values(row_number)[get_column_index(sheet, 'ShellScript')],
        'Run?': sheet.row_values(row_number)[get_column_index(sheet, 'Run?')],
        'Delay': sheet.row_values(row_number)[get_column_index(sheet, 'Delay')],  # unit: second, support float, 0.5==500ms
        'SQL': sheet.row_values(row_number)[get_column_index(sheet, 'SQL')],
        'ExpectedSQLData': sheet.row_values(row_number)[get_column_index(sheet, 'ExpectedSQLData')],  # multiple lines --> list
        'HandleParameter': sheet.row_values(row_number)[get_column_index(sheet, 'HandleParameter')]  # multiple lines --> list
    }
    # List type columns
    case_step['ExpectedSQLData'] = str(case_step['ExpectedSQLData']).splitlines()
    case_step['ResponseParameter'] = str(case_step['ResponseParameter']).splitlines()
    case_step['ExpectedData'] = str(case_step['ExpectedData']).splitlines()
    case_step['HandleParameter'] = str(case_step['HandleParameter']).splitlines()

    # Column Header is of type dict
    header_paras = {}
    lines = str(case_step['Header']).splitlines()
    for line in lines:
        i = line.find(':')
        header_paras[line[:i]] = line[i + 1:]
    case_step['Header'] = header_paras

    # special process
    if case_step['Port'] != '':
        case_step['Port'] = str(int(case_step['Port']))
    if case_step['Delay'] != '':
        case_step['Delay'] = float(case_step['Delay'])

    return case_step


def read_excel(file_path: str, sheet_name: str):
    """Fetch test cases from the sheet_name page in the Excel file.

    :param file_path: "base_dir/path/to/case.xlsx"
    :param sheet_name: just sheet name
    :return: case_dict_list if every is ok, or False if meet Exception
    """
    case_dict_list = []
    case_step_list = []
    try:
        book = xlrd.open_workbook(file_path)
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows
        if rows == 1:
            logger.warning('Empty sheet!')
            return False

        # when i==1, case name must exist
        case_name = sheet.row_values(1)[get_column_index(sheet,'CaseName')]
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
                case_dict_list.append(case_dict)
                case_step_list = []
                last_case_name = case_name
                case_step = get_case_step(sheet, i)
                case_step_list.append(case_step)

            # if the last row, no more case or step, append the case_dict to the case_dict_list
            if i == rows - 1:
                case_dict = {
                    'CaseName': last_case_name,
                    'CaseSteps': case_step_list
                }
                case_dict_list.append(case_dict)

        # bug fixed：handle the situation that only two rows (one case) exist
        if rows == 2:
            case_dict = {
                'CaseName': last_case_name,
                'CaseSteps': case_step_list
            }
            case_dict_list.append(case_dict)
    except FileNotFoundError as error:
        logger.error('Can\'t open the excel file:  ' + str(error))
        return False
    except xlrd.XLRDError as error:
        logger.error('Error while reading excel file:  ' + str(error))
        return False
    except Exception as error:
        logger.error('Error while dealing with case detail:  ' + str(error))
        return False

    return case_dict_list
