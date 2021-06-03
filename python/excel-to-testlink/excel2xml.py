import xlrd

excel_path = "./test.xlsx"

workbook = xlrd.open_workbook(excel_path)
print("DocInfo sheets number = " + str(workbook.nsheets) + "\n")

all_sheet = workbook.sheets()

print("【@ 用例集总标题】<testsuite name = \"债券\">")  # 用例集一级标题

for sheet in all_sheet[:1]:  # 暂时只处理第一个sheet
    sheet_row_mount = sheet.nrows
    sheet_col_mount = sheet.ncols
    # print("该excel表的行列数为（{0},{1}）\n".format(sheet_row_mount,sheet_col_mount))

    """打印sheet层级suite标签"""
    print("【## sheet页】<testsuite name = \"{0}\">".format(sheet.name))  # 用例集二级标题：sheet页名称

    """打印case（单步骤）"""
    def print_case():
        print("<testcase name = \"{0}\">".format(sheet.cell_value(x, 3)))
        print("<summary>{0}</summary>".format(sheet.cell_value(x, 4)))

        # 处理小于号的转义字符问题
        temp = ""
        t = sheet.cell_value(x, 5)
        while "<" in str(t):
            for index in range(len(t)):
                if t[index] == '<':
                    temp = t[0:index] + "&lt;" + t[index + 1:]
                    t = temp
        print("<preconditions>{0}</preconditions>".format(temp))
        print("<steps>")
        print("<step>")
        print("<step_number>1</step_number>")

        # 处理&的转义字符问题
        # temp2 = ""
        # t2 = sheet.cell_value(x, 6)
        # while "&" in str(t2):
        #     for index in range(len(t2)):
        #         if t2[index] == '&':
        #             temp2 = t[0:index] + "&amp;" + t[index + 1:]
        #             t2 = temp2
        print("<actions>{0}</actions>".format(sheet.cell_value(x, 6)))
        print("<expectedresults>{0}</expectedresults>".format(sheet.cell_value(x, 7)))
        print("</step>")
        print("</steps>")
        print("</testcase>\n")

    """sheet内按行处理"""
    for x in range(1, sheet_row_mount):  # 忽略表头
        if x < sheet_row_mount - 1:  # 最后一行特殊处理
            if sheet.cell_value(x, 1) != '':  # 新的功能模块
                if x != 1:
                    print("【#### 一级菜单 - 】</testsuite>")
                print("【#### 一级菜单 + 】<testsuite name = \"{0}\">".format(sheet.cell_value(x, 1)))

            if sheet.cell_value(x, 2) != '':  # 新的子功能（增删改查之类的）
                if x != 1:
                    print("【###### 二级菜单 - 】</testsuite>")
                print("【###### 二级菜单 + 】<testsuite name = \"{0}\">".format(sheet.cell_value(x, 2)))

            """处理具体一条用例"""
            print_case()
        else:
            print_case()
            print("【###### 二级菜单 - 】</testsuite>")
            print("【#### 一级菜单 - 】</testsuite>")  # 最后一行无论如何最终都要加上反tag进行收尾

    print("【## sheet页】</testsuite>")  # 用例集二级标题：sheet页名称
print("【@ 用例集总标题】</testsuite>")  # 用例集一级标题
