import xlrd

excel_path = "C:/Users/pengwei.zhang/OneDrive/work/tttt.xlsx"


workbook = xlrd.open_workbook(excel_path)
print("DocInfo sheets number = " + str(workbook.nsheets) + "\n")

all_sheet = workbook.sheets()

print("<testsuite name = \"债券\">")

for sheet in all_sheet:
    sheet_row_mount = sheet.nrows
    sheet_col_mount = sheet.ncols
    # print("该excel表的行列数为（{0},{1}）\n".format(sheet_row_mount,sheet_col_mount))

    """打印sheet层级suite标签"""
    print("<testsuite name = \"{0}\">".format(sheet.name))

    """sheet内按行处理"""
    sub_sys = ""
    sub_function = ""
    for x in range(1, sheet_row_mount):  # 忽略表头

        # 打印case（单步骤）
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
            """step"""
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
            """step"""
            print("</step>")
            print("</steps>")
            print("</testcase>\n")


        # 内部判断
        def inner_judge(sub_function, flag):
            if x < sheet_row_mount - 1:

                if (flag == 1 or sheet.cell_value(x, 2) != sub_function ) and sheet.cell_value(x, 2) == sheet.cell_value(x + 1, 2):
                    """功能序列头"""
                    print("<testsuite name = \"{0}\">".format(sheet.cell_value(x, 2)))
                    sub_function = sheet.cell_value(x, 2)

                    # 打印整个case
                    print_case()
                elif flag == 2 or (sheet.cell_value(x, 2) == sub_function  and sheet.cell_value(x, 2) != sheet.cell_value(x + 1, 2)):
                    """功能序列尾"""

                    # 打印整个case
                    print_case()

                    print("</testsuite>")
                    sub_function = sheet.cell_value(x, 2)
                elif flag == 3 or (sheet.cell_value(x, 2) != sub_function and sheet.cell_value(x, 2) != sheet.cell_value(x + 1, 2)):
                    """功能序列头+尾"""
                    print("<testsuite name = \"{0}\">".format(sheet.cell_value(x, 2)))

                    # 打印整个case
                    print_case()

                    print("</testsuite>")
                    sub_function = sheet.cell_value(x, 2)
                else:
                    """功能序列中"""
                    # 打印整个case
                    print_case()
            else:
                if sheet.cell_value(x, 2) != sub_function:
                    print("<testsuite name = \"{0}\">".format(sheet.cell_value(x, 2)))

                # 打印整个case
                print_case()

                print("</testsuite>")


        # 外部判断（主干）
        if x < sheet_row_mount - 1:
            if sheet.cell_value(x, 1) != sub_sys and sheet.cell_value(x, 1) == sheet.cell_value(x + 1, 1):
                """模块序列头"""
                print("<testsuite name = \"{0}\">".format(sheet.cell_value(x, 1)))
                # 内部判断
                flag = 1
                inner_judge(sub_function, flag)
                sub_function = sheet.cell_value(x, 2)
                sub_sys = sheet.cell_value(x, 1)
            elif sheet.cell_value(x, 1) == sub_sys and sheet.cell_value(x, 1) != sheet.cell_value(x + 1, 1):
                """模块序列尾"""
                # 内部判断
                flag = 2
                inner_judge(sub_function, flag)
                sub_function = sheet.cell_value(x, 2)
                print("</testsuite>")
                sub_sys = sheet.cell_value(x, 1)
            elif sheet.cell_value(x, 1) != sub_sys and sheet.cell_value(x, 1) != sheet.cell_value(x + 1, 1):
                """模块序列头+尾"""
                print("<testsuite name = \"{0}\">".format(sheet.cell_value(x, 1)))
                # 内部判断
                flag = 3
                inner_judge(sub_function, flag)
                sub_function = sheet.cell_value(x, 2)
                print("</testsuite>")
                sub_sys = sheet.cell_value(x, 1)
            else:
                """模块序列中"""
                # 内部判断
                flag = 0
                inner_judge(sub_function, flag)
                sub_function = sheet.cell_value(x, 2)
                sub_sys = sheet.cell_value(x, 1)
        else:
            if sheet.cell_value(x, 1) != sub_sys:
                print("<testsuite name = \"{0}\">".format(sheet.cell_value(x, 1)))
            # 内部判断
            flag = 0
            inner_judge(sub_function, flag)
            sub_function = sheet.cell_value(x, 2)
            sub_sys = sheet.cell_value(x, 1)
            print("</testsuite>")

    print("</testsuite>")

print("</testsuite>")
