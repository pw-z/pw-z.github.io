#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Pengwei Zhang

"""
使用pandas库对Excel进行读写

pandas官网：https://pandas.pydata.org/
"""

import pandas as pd
import logging

excel_path = "testcase_template.xlsx"
sheet_names = ['手续费核算']


def read_excel(path_to_excel, sheet_name):
    try:
        excel_dateframe = pd.read_excel(path_to_excel, sheet_name)
        logging.log("get excel data successful")
        return excel_dateframe
    except Exception:
        logging.error("something went wrong when getting the excel")


def main():
    for sheet in sheet_names:
        print(sheet)
        excel_data = read_excel(excel_path, sheet)
        print(excel_data)


if __name__ == '__main__':
    main()
