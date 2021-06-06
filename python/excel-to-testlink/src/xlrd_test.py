#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Excel2Xml tiny tool By 2087 @20210108

注意xlrd需要1.2.0版本，2.0.1版本不支持xlsx，
pip install xlrd==1.2.0
"""

import xlrd
 
excel_path = "../input/testcase_template.xls"

# 打开文件方式1：
workbook = xlrd.open_workbook(excel_path)

# 获取工作簿中sheet表数量
print("INFO~ sheets number = " + str(workbook.nsheets))

#返回所有Sheet对象的list
all_sheet = workbook.sheets()#Book(工作簿)对象方法
print(all_sheet)

#遍历返回的Sheet对象的list
for each_sheet in all_sheet:
    print(each_sheet)
    print("sheet名称为：",each_sheet.name)#sheet对象方法


#循环遍历每个sheet对象
sheet_name = []
sheet_row = []
sheet_col = []
for sheet in all_sheet:
    sheet_name.append(sheet.name)
    print("该Excel共有{0}个sheet,当前sheet名称为{1},该sheet共有{2}行,{3}列"
          .format(len(all_sheet),sheet.name,sheet.nrows,sheet.ncols))
    sheet_row.append(sheet.nrows)
    sheet_col.append(sheet.ncols)
 
print(sheet_name)#获取sheet的名称
print(sheet_row )#获取sheet对象的行数
print(sheet_col)#获取sheet对象的列数





print("hello 2087\n******************************\n\n\n")


for sheet in all_sheet:
    sheet_name.append(sheet.name)
    print("该Excel共有{0}个sheet,当前sheet名称为{1},该sheet共有{2}行,{3}列\n\n"
          .format(len(all_sheet),sheet.name,sheet.nrows,sheet.ncols))
    for each_row in range(sheet.nrows):#循环打印每一行
        print("当前为%s行："% each_row,type(each_row))
        print(sheet.row_values(each_row),type(sheet.row_values(each_row)))
        
        

print("hello 2087\n******************************\n\n\n\n\n")

first_row_value = sheet.row_values(0)#打印指定的某一行
print("第一行的数据为:%s" % first_row_value)

"""
xmlfile = open("./xml-file.xml","x")
xmlfile.write("hello")
xmlfile.close()
"""

for sheet in all_sheet:
    sheet_row_mount = sheet.nrows
    sheet_col_mount = sheet.ncols
    print("该excel表的行列数为（{0},{1}）\n\n\n".format(sheet_row_mount,sheet_col_mount))

    suite = set()
    for x in range(1,sheet.nrows):
        if sheet.cell_value(x,1) not in suite:
            suite.add(sheet.cell_value(x,1))
            print("new suite")
        
            
            
            
    """
    for x in range(sheet_row_mount):
        y = 0
        while y < sheet_col_mount:
            if sheet.cell_value(x,y):
            	print(sheet.cell_value(x,y))
            else:
                print("####")
            y += 1
        print("\n")
    
    flag = ""
    for x in range(sheet_row_mount):
        if flag == "":
            flag = sheet.cell_value(x,1)
            print("<testsuite name = \"{0}\">".format(sheet.cell_value(x,1)))
        elif sheet.cell_value(x,1)!=flag:
            print("</testsuite>\n")
            print("<testsuite name = \"{0}\">".format(sheet.cell_value(x,1)))
            flag = sheet.cell_value(x,1)
        else:
            pass
        y = 2
        while y < sheet_col_mount:
            if sheet.cell_value(x,y):
            	print(sheet.cell_value(x,y))
            else:
                print("####")
            y += 1
    print("</testsuite>\n")
    """

