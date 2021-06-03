import xlrd
import time

"""
2021年3月13日：该脚本是为xx发过来的测试用例专门调整的
"""

"""参数区"""
file_name = "ST未执行案例142条_20210315091526745"
excel_path = "./input/" + file_name + ".xlsx"  # 用例文件路径
testsuite_name = "ST"  # 用例集名称
sheet_number = 5  # 只处理前多少个sheet页面
# step_mode = 0  # 0=多步骤（需要执行步骤与期望结果一一对应） 1=单步骤

workbook = xlrd.open_workbook(excel_path)

date_stamp = time.strftime("%Y%m%d-%H%M%S", time.localtime())
output_file_path = "./output/TestCase-" + file_name + "-Export@" + date_stamp + ".xml"
all_sheet = workbook.sheets()
xml_file = open(output_file_path, "w", encoding="utf8")

xml_file.write("<testsuite name = \"{0}\">\n".format(testsuite_name))

for sheet in all_sheet[:sheet_number]:
    sheet_row_mount = sheet.nrows
    sheet_col_mount = sheet.ncols
    # print("该excel表的行列数为（{0},{1}）\n".format(sheet_row_mount,sheet_col_mount))

    """打印sheet层级suite标签"""
    xml_file.write("\t<testsuite name = \"{0}\">\n".format(sheet.name))

    """打印case"""
    def print_case():
        tempString1 = "<![CDATA[" \
                      + sheet.cell_value(x, 4) \
                      + "<p>用例编号：" + sheet.cell_value(x, 2) + "<p>" \
                      + "<p>执行路径：<p>" \
                      + "<p>" + sheet.cell_value(x, 1) + "<p>" \
                      + "]]>"  # 处理【摘要】字段中”<“与”&“的转义问题
        testString_testname = sheet.cell_value(x, 3)
        testString_testname = testString_testname.replace("&", "&amp;")
        testString_testname = testString_testname.replace("<", "&lt;")
        xml_file.write("\n\t\t<testcase name = \"{0}____{1}\">\n".format(testString_testname, sheet.cell_value(x, 2)))
        xml_file.write("\t\t<summary>{0}</summary>".format(tempString1))

        tempString2 = sheet.cell_value(x, 5)  # 处理【前提条件】字段中”<“与”&“的转义问题
        tempString2 = tempString2.replace("&", "&amp;")
        tempString2 = tempString2.replace("<", "&lt;")
        xml_file.write("\t\t<preconditions>{0}</preconditions>\n".format(tempString2))
        xml_file.write("\t\t<steps>\n\n")

        # 优先级提取
        importance = sheet.cell_value(x, 10)
        if importance == '高':
            importance = '[3]'
        elif importance == '中':
            importance = '[2]'
        elif importance == '低':
            importance = '[1]'
        else:
            importance = ''
        xml_file.write("\t\t<importance>{0}</importance>\n".format(importance))

        # print("\t\t# -----------------------------------------------------------------打印具体操作步骤")
        actions = sheet.cell_value(x, 6) + "\n"  # 末尾+换行符方便后面统一处理
        results = sheet.cell_value(x, 7) + "\n"

        actions = actions.replace("&", "&amp;")  # 处理”<“与”&“的转义问题
        actions = actions.replace("<", "&lt;")
        results = results.replace("&", "&amp;")
        results = results.replace("<", "&lt;")

        # print("对操作步骤、预期结果进行处理，使其正常换行---------------start")
        n1 = actions.count("\n")
        actions_process = "<![CDATA["
        for i in range(n1):
            actions_process += "<p>" + actions[:actions.find("\n")] + "</p>"
            actions = actions[actions.find("\n") + 1:]
        actions_process += "]]>"

        n2 = results.count("\n")
        results_process = "<![CDATA["
        for i in range(n2):
            results_process += "<p>" + results[:results.find("\n")] + "</p>"
            results = results[results.find("\n") + 1:]
        results_process += "]]>"
        # print("对操作步骤、预期结果进行处理，使其正常换行---------------END\n\n\n")

        xml_file.write("\t\t<step>\n")
        xml_file.write("\t\t<step_number>1</step_number>\n")
        xml_file.write("\t\t<actions>{0}</actions>\n".format(actions_process))
        xml_file.write("\t\t<expectedresults>{0}</expectedresults>\n".format(results_process))

        xml_file.write("\t\t</step>\n\n")
        # print("\t\t# -----------------------------------------------------------------打印具体操作步骤")

        xml_file.write("\t\t</steps>\n")
        xml_file.write("\t\t</testcase>\n\n")

    """sheet内按行处理"""
    for x in range(1, sheet_row_mount):  # 忽略表头

        """处理具体一条用例"""
        print_case()

    xml_file.write("\t</testsuite>\n")  # 用例集二级标题：sheet页名称
xml_file.write("</testsuite>\n")  # 用例集一级标题
xml_file.close()
