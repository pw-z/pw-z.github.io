import xlrd
import time

"""
0224更新：summary字段对换行符进行转义
"""

"""参数区"""
file_name = "测试用例.20210401"
excel_path = "./input/" + file_name + ".xlsx"  # 用例文件路径
testsuite_name = "日终清算"  # 用例集名称
sheet_number = 1  # 只处理前多少个sheet页面
# step_mode = 0  # 0=多步骤（需要执行步骤与期望结果一一对应） 1=单步骤

workbook = xlrd.open_workbook(excel_path)
print("DocInfo sheets number = " + str(workbook.nsheets) + "\n")

date_stamp = time.strftime("%Y%m%d-%H%M%S", time.localtime())
output_file_path = "./output/TestCase-" + file_name + "-Export@" + date_stamp + ".xml"
all_sheet = workbook.sheets()
xml_file = open(output_file_path, "w", encoding="utf8")

print("<testsuite name = \"{0}\">".format(testsuite_name))  # 用例集一级标题
xml_file.write("<testsuite name = \"{0}\">\n".format(testsuite_name))

for sheet in all_sheet[:sheet_number]:  # 暂时只处理第一个sheet
    sheet_row_mount = sheet.nrows
    sheet_col_mount = sheet.ncols
    # print("该excel表的行列数为（{0},{1}）\n".format(sheet_row_mount,sheet_col_mount))

    """打印sheet层级suite标签"""
    print("\t<testsuite name = \"{0}\">".format(sheet.name))  # 用例集二级标题：sheet页名称
    xml_file.write("\t<testsuite name = \"{0}\">\n".format(sheet.name))

    """打印case"""
    def print_case():
        tempString1 = sheet.cell_value(x, 4)  # 处理【摘要】字段中”<“与”&“的转义问题
        tempString1 = tempString1.replace("&", "&amp;")
        tempString1 = tempString1.replace("<", "&lt;")
        print("\n\t\t\t\t<testcase name = \"{0}\">".format(sheet.cell_value(x, 3)))
        print("\t\t\t\t<summary>{0}</summary>".format(tempString1))
        xml_file.write("\n\t\t\t\t<testcase name = \"{0}\">\n".format(sheet.cell_value(x, 3)))
        xml_file.write("\t\t\t\t<summary>{0}</summary>\n".format(tempString1))

        tempString2 = sheet.cell_value(x, 5)  # 处理【前提条件】字段中”<“与”&“的转义问题
        tempString2 = tempString2.replace("&", "&amp;")
        tempString2 = tempString2.replace("<", "&lt;")
        print("\t\t\t\t<preconditions>{0}</preconditions>".format(tempString2))
        xml_file.write("\t\t\t\t<preconditions>{0}</preconditions>\n".format(tempString2))
        print("\t\t\t\t<steps>\n")
        xml_file.write("\t\t\t\t<steps>\n\n")

        # print("\t\t\t\t# -----------------------------------------------------------------打印具体操作步骤")
        actions = sheet.cell_value(x, 6) + "\n"  # 末尾+换行符方便后面统一处理
        results = sheet.cell_value(x, 7) + "\n"

        actions = actions.replace("&", "&amp;")  # 处理”<“与”&“的转义问题
        actions = actions.replace("<", "&lt;")
        results = results.replace("&", "&amp;")
        results = results.replace("<", "&lt;")

        n1 = actions.count("\n")
        n2 = results.count("\n")
        if n1 != n2:
            print("步骤动作与期望结果的条数对应不上")
            print("总共有{0}个步骤，{1}个结果".format(n1, n2))
        else:
            for i in range(n1):
                print("\t\t\t\t<step>")
                print("\t\t\t\t<step_number>{0}</step_number>".format(i + 1))
                print("\t\t\t\t<actions>{0}</actions>".format(actions[:actions.find("\n")]))
                print("\t\t\t\t<expectedresults>{0}</expectedresults>".format(results[:results.find("\n")]))

                xml_file.write("\t\t\t\t<step>\n")
                xml_file.write("\t\t\t\t<step_number>{0}</step_number>\n".format(i + 1))
                xml_file.write("\t\t\t\t<actions>{0}</actions>\n".format(actions[:actions.find("\n")]))
                xml_file.write("\t\t\t\t<expectedresults>{0}</expectedresults>\n".format(results[:results.find("\n")]))

                actions = actions[actions.find("\n") + 1:]
                results = results[results.find("\n") + 1:]
                print("\t\t\t\t</step>\n")
                xml_file.write("\t\t\t\t</step>\n\n")
        # print("\t\t\t\t# -----------------------------------------------------------------打印具体操作步骤")

        print("\t\t\t\t</steps>")
        print("\t\t\t\t</testcase>\n")
        xml_file.write("\t\t\t\t</steps>\n")
        xml_file.write("\t\t\t\t</testcase>\n\n")

    """sheet内按行处理"""
    for x in range(1, sheet_row_mount):  # 忽略表头

        if sheet.cell_value(x, 1) != '':  # 新的模块
            if x != 1:
                print("\t\t\t</testsuite>")
                print("\t\t</testsuite>")
                xml_file.write("\t\t\t</testsuite>\n")  # 先给功能收尾
                xml_file.write("\t\t</testsuite>\n")  # 再给模块收尾
            print("\t\t<testsuite name = \"{0}\">".format(sheet.cell_value(x, 1)))
            xml_file.write("\t\t<testsuite name = \"{0}\">\n".format(sheet.cell_value(x, 1)))

        if sheet.cell_value(x, 2) != '':  # 新的功能
            if sheet.cell_value(x, 1) == '' and x != 1:
                print("\t\t\t</testsuite>")
                xml_file.write("\t\t\t</testsuite>\n")
            print("\t\t\t<testsuite name = \"{0}\">".format(sheet.cell_value(x, 2)))
            xml_file.write("\t\t\t<testsuite name = \"{0}\">\n".format(sheet.cell_value(x, 2)))

        """处理具体一条用例"""
        print_case()

    print("\t\t\t</testsuite>")
    print("\t\t</testsuite>")  # 最后一行无论如何最终都要加上反tag进行收尾
    xml_file.write("\t\t\t</testsuite>\n")
    xml_file.write("\t\t</testsuite>\n")

    print("\t</testsuite>")  # 用例集二级标题：sheet页名称
    xml_file.write("\t</testsuite>\n")
print("</testsuite>")  # 用例集一级标题
xml_file.write("</testsuite>\n")
xml_file.close()
