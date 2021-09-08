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
        "literal_divided_by_zero": r"\/0(?!\.)",
        "consecutive_operators": r"[\+\-\*\/\%]{2,}",
        "non_number_with_percentage_symbol": "[^0-9%]%",
        # bracket related
        "left_bracket_with_wrong_operators": r"\([\*\/\+\%]{2,}",
        "wrong_operators_with_right_bracket": r"[\+\-\*\/]\)",
        "right_bracket_with_wrong_stuff": r"\)[^\)\+\-\*\/]",
        "wrong_stuff_with_left_bracket": r"[^\(\+\-\*\/]\(",
        # others
        # "end_with_wrong_stuff": r"[+\-\*\/].?",  # 需要用march配合
        # "start_with_wrong_stuff": r"[\+\*\/].?",  # 需要用march配合
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
    start_with_wrong_stuff = r"[\+\*\/].?"
    end_with_wrong_stuff = r"[+\-\*\/].?"
    if re.match(start_with_wrong_stuff, f):
        # print("start_with_wrong_stuff")
        test_result += "Error: start_with_wrong_stuff\n"
    if re.match(end_with_wrong_stuff, f[::-1]):
        # print("end_with_wrong_stuff")
        test_result += "Error: end_with_wrong_stuff\n"

    # TODO 特殊校验

    # 最终结果处理
    if test_result == "":
        test_result = "PASS, NO ERROR FOUND"
    else:
        test_result = test_result[:-1]  # remove unnecessary "\n"
    return test_result


if __name__ == '__main__':
    while True:
        formula = input()
        # print("your input: " + formula)
        result = formula_check(formula)
        print("="*51 + "\n" + "FORMULA TESTING RESULT:\n" + "- "*26)
        print(result)
        print("=" * 51)
