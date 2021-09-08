# 用Python和正则表达式校验数学运算式的合法性

*check-the-validity-of-mathematical-expressions-with-python-and-regular-expression*  
*Posted on 2021.09.08 by [Zhang Pengwei](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


## 问题描述

本文场景下，合法的运算式由数字（正负整数、正负小数）、加减乘除、括号、百分号构成，该运算式除了需要满足基本的四则运算规则，还需要满足如下规则：

* 百分号仅可置于数字后面
* 两组括号相乘时乘号不可省略
* 正数前面不可以加正号

假设输入为一数学运算式，求该运算式是否合法，若非法需要给出非法原因。例如，运算式`123*(3.5%+1)/12`合法，可以正常运算出结果，运算式`345*+23*(34-1))`非法，`*`与`+`连写且多了一个右括号。



## 运算式非法情况列举

以下列举的情况仅适用于上述规定的场景，存在交叉覆盖的情况（同一个场景会触发多条非法规则）。

|分组|非法情况|字典字段|正则表达式|备注|
|---|---|---|---|---|
|基本错误
||含有非法字符|contains_illegal_characters|[^0-9\\+\\-\\*\\/\\%\\(\\)\\.]
||空括号|empty_bracket|\\(\\)
||显式除零|literal_divided_by_zero|~~\\/0(?!\\.)~~待定|注意排除`除以零点几`的情况|
||运算符（加减乘除百分号）连续|consecutive_operators|[\\+\\-\\*\\/\\%]{2,}|形如+-5的情况，认为是非法，同理*-3、/-3、--4|
||%前面不为数字|non_number_with_percentage_symbol|[^0-9%]%
||括号不匹配|brackets_mismatch||无法用正则匹配判断
|括号相关
||左括号与乘、除、加、%连续|left_bracket_with_wrong_operators|\\([\\*\\/\\+\\%]{2,}
||加减乘除与右括号连续|wrong_operators_with_right_bracket|[\\+\\-\\*\\/]\\)
||右括号之后不为运算符或右括号|right_bracket_with_wrong_stuff|\\)[^\\)\\+\\-\\*\\/]
||左括号之前不为运算符或左括号|wrong_stuff_with_left_bracket|[^\\(\\+\\-\\*\\/]\\(
|其它补充
||整个公式以运算符开始|start_with_wrong_stuff|从头匹配r"[\\+\\*\\/].?"|以负号开始是合法的
||整个公式以运算符结束|end_with_wrong_stuff|字符串转置::从头匹配r"[+\\-\\*\\/].?"|以百分号结束是合法的



## 代码实现
```python
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
        "literal_divided_by_zero": r"\/0(?!\.)",  # 这里有问题的
        "consecutive_operators": r"[\+\-\*\/\%]{2,}",
        "non_number_with_percentage_symbol": "[^0-9%]%",
        # bracket related
        "left_bracket_with_wrong_operators": r"\([\*\/\+\%]{2,}",
        "wrong_operators_with_right_bracket": r"[\+\-\*\/]\)",
        "right_bracket_with_wrong_stuff": r"\)[^\)\+\-\*\/]",
        "wrong_stuff_with_left_bracket": r"[^\(\+\-\*\/]\(",
        # others
        # "end_with_wrong_stuff": r"[+\-\*\/].?",  # 需要用re.march配合，后面单独处理
        # "start_with_wrong_stuff": r"[\+\*\/].?",  # 需要用re.march配合，后面单独处理
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


def run_formula_check():
    
    while True:
        formula = input()
        if formula != "bey":
            # print("your input: " + formula)
            result = formula_check(formula)
            print("="*51 + "\n" + "FORMULA TESTING RESULT:\n" + "- "*26)
            print(result)
            print("=" * 51 + "\n")
        else:
            print("bey!")
            break


if __name__ == '__main__':
    run_formula_check()

```


## 测试

TODO