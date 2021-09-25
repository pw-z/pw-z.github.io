#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.09.06

import re


def expression_check(expression_string):
    f = expression_string
    f = f.replace(" ", "")
    # print("expression_test::print_expression: " + f)

    # 基本正则校验
    pattern_dict = {
        # basic errors
        "contains_illegal_characters": r"[^0-9\+\-\*\/\%\(\)\.]",
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
            test_result += "ERROR: " + pattern_key
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


def run_expression_check():
    while True:
        expression = input()
        if expression != "bey":
            # print("your input: " + expression)
            result = expression_check(expression)
            print("=" * 51 + "\n" + "EXPRESSION TESTING RESULT:\n" + "- " * 26)
            print(result)
            print("=" * 51 + "\n")
        else:
            print("bey!")
            break


if __name__ == '__main__':
    run_expression_check()