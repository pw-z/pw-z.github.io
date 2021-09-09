#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.09.06

import re


def formula_check(formula_string):
    f = formula_string
    f = f.replace(" ", "")
    # print("formula_test::print_formula: " + f)

    # 基本正则校验
    pattern_dict = {
        # basic errors
        "contains_illegal_characters": r"[^a-zA-Z0-9\+\-\*\/\%\(\)\._]",
        "empty_bracket": r"\(\)",
        "literal_divided_by_zero": r"\/0(?!\.)|\/0\.0+(?![1-9])",
        "consecutive_operators": r"[\+\-\*\/]{2,}|[\+\-×÷%]+?%",
        "non_number_with_percentage_symbol": "[^0-9%]%",
        # bracket related
        "wrong_operators_after_left_bracket": r"\([\*\/\+\%]",
        "wrong_operators_before_right_bracket": r"[\+\-\*\/]\)",
        "wrong_character_after_right_bracket": r"\)[^\)\+\-\*\/]",
        "wrong_operators_before_left_bracket": r"[^\(\+\-\*\/]\(",
        # others
        "start_with_wrong_character": r"^[\+\*\/]",
        "end_with_wrong_character": r"[+\-\*\/]$",
        "extra_prefix_0": r"[^0-9\.]0+[0-9]+",
        "illegal_floating_point_number": r"(?<!\d)\.[\d]+|[\d]+\.[^\d]*(?!\d)|(?<!\d)[^\d]*\.[^\d]*(?!\d)",
        "too_many_decimal_points": r"[\d]+\.[\d]+\.[\d]+"
    }
    test_result = ""
    for pattern_key in pattern_dict.keys():
        pattern = pattern_dict[pattern_key]
        re_results = re.findall(pattern, f)
        if re_results:
            test_result += "Error: " + pattern_key
            # print(re_results.groups())
            for re_result in re_results:
                # print(re_result)
                test_result += "\n" + re_result
            test_result += "\n"

    # 括号匹配校验
    brackets_stack = []
    for char in f:
        if char == "(":
            # print(r"meet '(', stack.push '('")
            brackets_stack.append(1)
        elif char == ")":
            if brackets_stack:
                # print(r"meet ')', stack.pop '(' ")
                brackets_stack.pop()
            else:
                test_result += "Error: brackets_mismatch\n"
                break
    if brackets_stack:
        test_result += "Error: brackets_mismatch\n"

    # 头尾字符校验
    # start_with_wrong_stuff = r"[\+\*\/].?"
    # end_with_wrong_stuff = r"[+\-\*\/].?"
    # if re.match(start_with_wrong_stuff, f):
    #     # print("start_with_wrong_stuff")
    #     test_result += "Error: start_with_wrong_stuff\n"
    # if re.match(end_with_wrong_stuff, f[::-1]):
    #     # print("end_with_wrong_stuff")
    #     test_result += "Error: end_with_wrong_stuff\n"

    # TODO 特殊校验

    # 最终结果处理
    if test_result == "":
        test_result = "PASS, NO ERROR FOUND"
    else:
        test_result = test_result[:-1]  # remove unnecessary "\n"
    return test_result


def run_formula_check():
    while True:
        formula = input()
        if formula != "bey":
            # print("your input: " + formula)
            result = formula_check(formula)
            print("=" * 51 + "\n" + "FORMULA TESTING RESULT:\n" + "- " * 26)
            print(result)
            print("=" * 51 + "\n")
        else:
            print("bey!")
            break


def unit_test():
    formula_test_data = [
        # 正例
        "1*3+(4-5%)/6",  # 全符号覆盖
        "(45)",  # 运算符仅括号
        "-4.3/(-0.1)",  # 负数
        "",
        "",

        # 反例

    ]


if __name__ == '__main__':
    run_formula_check()