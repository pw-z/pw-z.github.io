#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2021

import xlrd
import logging
import requests
from Handler import CaseHandler


filepath = r"../case/case.xlsx"
sheets = ['test']
logger = logging.getLogger()


def get_column_index(sheet, column_name):
    column_index = None
    for i in range(sheet.ncols):
        if sheet.cell_value(0, i) == column_name:
            column_index = i
            break
    return column_index


def read_excel(file_path, sheet_name):
    case_list_dic = []
    try:
        book = xlrd.open_workbook(file_path)  # 打开excel
    except Exception as error:
        logger.error(r'can not open the excel file  ' + str(error))
        return error
    else:
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows  # 取这个sheet页的所有行数
        for i in range(1, rows):  # 忽略第一行表头
            case_dic = {
                # 'suite_path': sheet.row_values(i)[get_column_index(sheet, 'suite_path')],
                'CaseStep': sheet.row_values(i)[get_column_index(sheet, 'CaseStep')],
                'Method': sheet.row_values(i)[get_column_index(sheet, 'Method')],
                'URI': sheet.row_values(i)[get_column_index(sheet, 'URI')],
                'Port': sheet.row_values(i)[get_column_index(sheet, 'Port')],
                'Address': sheet.row_values(i)[get_column_index(sheet, 'Address')],
                'Body': sheet.row_values(i)[get_column_index(sheet, 'Body')],
                'ContentType': sheet.row_values(i)[get_column_index(sheet, 'ContentType')],
                'ResponseParameter': sheet.row_values(i)[get_column_index(sheet, 'ResponseParameter')]
            }
            case_list_dic.append(case_dic)
    return case_list_dic


if __name__ == '__main__':
    # for sheet in sheets:
    #     cases = read_excel(filepath, sheet)
    #     print(cases)

    # url = 'http://10.243.141.100:9192/secu'
    # header = {'content-type': 'text/html;charset=UTF-8'}
    # data = {
    #     "userId": "143374",
    #     "PASSWORD": "qwer1234",
    #     "f": "SECU_Login"
    # }

    # try:
    #     res = requests.post(url, headers=header, data=json.dumps(data))
    #     print(res.json())
    #     # print(res)
    # except Exception as e:
    #     print(e)
    casehandler =CaseHandler()
    for sheet in sheets:
        cases = read_excel(filepath, sheet)
        # print(cases)
        for case in cases:
            # print(case)
            casehandler.run(case)



