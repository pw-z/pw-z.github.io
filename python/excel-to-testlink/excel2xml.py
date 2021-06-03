import xlrd

excel_path = "./test.xlsx"

workbook = xlrd.open_workbook(excel_path)
print("DocInfo sheets number = " + str(workbook.nsheets) + "\n")

all_sheet = workbook.sheets()
xml_file = open("./test.xml", "w", encoding="utf8")

print("<testsuite name = \"债券\">")  # 用例集一级标题
xml_file.write("<testsuite name = \"债券\">\n")
for sheet in all_sheet[:1]:  # 暂时只处理第一个sheet
    sheet_row_mount = sheet.nrows
    sheet_col_mount = sheet.ncols
    # print("该excel表的行列数为（{0},{1}）\n".format(sheet_row_mount,sheet_col_mount))

    """打印sheet层级suite标签"""
    print("\t<testsuite name = \"{0}\">".format(sheet.name))  # 用例集二级标题：sheet页名称
    xml_file.write("\t<testsuite name = \"{0}\">\n".format(sheet.name))

    """打印case（单步骤）"""
    def print_case():
        print("\n\t\t\t\t<testcase name = \"{0}\">".format(sheet.cell_value(x, 3)))
        print("\t\t\t\t<summary>{0}</summary>".format(sheet.cell_value(x, 4)))
        xml_file.write("\n\t\t\t\t<testcase name = \"{0}\">\n".format(sheet.cell_value(x, 3)))
        xml_file.write("\t\t\t\t<summary>{0}</summary>\n".format(sheet.cell_value(x, 4)))

        # 处理小于号"<"的转义问题
        temp = ""
        t = sheet.cell_value(x, 5)
        while "<" in str(t):
            for index in range(len(t)):
                if t[index] == '<':
                    temp = t[0:index] + "&lt;" + t[index + 1:]
                    t = temp
        print("\t\t\t\t<preconditions>{0}</preconditions>".format(temp))
        xml_file.write("\t\t\t\t<preconditions>{0}</preconditions>\n".format(temp))

        print("\t\t\t\t<steps>")
        print("\t\t\t\t<step>")
        print("\t\t\t\t<step_number>1</step_number>")
        xml_file.write("\t\t\t\t<steps>\n")
        xml_file.write("\t\t\t\t<step>\n")
        xml_file.write("\t\t\t\t<step_number>1</step_number>\n")

        # 处理&的转义问题
        # temp2 = ""
        # t2 = sheet.cell_value(x, 6)
        # while "&" in str(t2):
        #     for index in range(len(t2)):
        #         if t2[index] == '&':
        #             temp2 = t[0:index] + "&amp;" + t[index + 1:]
        #             t2 = temp2
        print("\t\t\t\t<actions>{0}</actions>".format(sheet.cell_value(x, 6)))
        print("\t\t\t\t<expectedresults>{0}</expectedresults>".format(sheet.cell_value(x, 7)))
        xml_file.write("\t\t\t\t<actions>{0}</actions>\n".format(sheet.cell_value(x, 6)))
        xml_file.write("\t\t\t\t<expectedresults>{0}</expectedresults>\n".format(sheet.cell_value(x, 7)))

        print("\t\t\t\t</step>")
        print("\t\t\t\t</steps>")
        print("\t\t\t\t</testcase>\n")
        xml_file.write("\t\t\t\t</step>\n")
        xml_file.write("\t\t\t\t</steps>\n")
        xml_file.write("\t\t\t\t</testcase>\n\n")

    """sheet内按行处理"""
    for x in range(1, sheet_row_mount):  # 忽略表头
        if x < sheet_row_mount - 1:  # 最后一行特殊处理
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
        else:
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