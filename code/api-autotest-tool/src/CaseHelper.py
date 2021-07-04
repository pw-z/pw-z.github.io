#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2021

import xlrd
import logging


filepath = r"../case/case.xlsx"
sheets = ['test']
logger = logging.getLogger()


def read_excel(file_path, sheet_name):

    def get_column_index(sheet, column_name):
        column_index = None
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == column_name:
                column_index = i
                break
        return column_index

    case_list_dic = []
    try:
        book = xlrd.open_workbook(file_path)
    except Exception as error:
        logger.error(r'can not open the excel file  ' + str(error))
        return error
    else:
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows
        for i in range(1, rows):
            case_dic = {
                # 'suite_path': sheet.row_values(i)[get_column_index(sheet, 'suite_path')],
                'CaseStep': sheet.row_values(i)[get_column_index(sheet, 'CaseStep')],
                'Method': sheet.row_values(i)[get_column_index(sheet, 'Method')],
                'URI': sheet.row_values(i)[get_column_index(sheet, 'URI')],
                'Port': sheet.row_values(i)[get_column_index(sheet, 'Port')],   # 9192.0
                'Address': sheet.row_values(i)[get_column_index(sheet, 'Address')],
                'Body': sheet.row_values(i)[get_column_index(sheet, 'Body')],
                'ContentType': sheet.row_values(i)[get_column_index(sheet, 'ContentType')],
                'ResponseParameter': sheet.row_values(i)[get_column_index(sheet, 'ResponseParameter')],
                'ExpectedData': sheet.row_values(i)[get_column_index(sheet, 'ExpectedData')],
                'ShellScript': sheet.row_values(i)[get_column_index(sheet, 'ShellScript')],
                'Run?': str(sheet.row_values(i)[get_column_index(sheet, 'Run?')])[:-2],   # 111.0
                'DQL': sheet.row_values(i)[get_column_index(sheet, 'DQL')]
            }

            case_dic['ResponseParameter'] = str(case_dic['ResponseParameter']).splitlines()

            wanted_paras = {}
            lines = str(case_dic['ExpectedData']).splitlines()
            for line in lines:
                i = line.find(':')
                wanted_paras[line[:i]] = line[i+1:]
            case_dic['ExpectedData'] = wanted_paras

            case_list_dic.append(case_dic)
    return case_list_dic





