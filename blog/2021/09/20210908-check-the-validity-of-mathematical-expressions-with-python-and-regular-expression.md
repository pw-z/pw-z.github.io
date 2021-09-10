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
||含有非法字符|contains_illegal_characters|`[^0-9\+\-\*\/%\(\)\.]`
||空括号|empty_bracket|`\(\)`
||显式除零|literal_divided_by_zero|`\/0(?!\.)\|\/0\.0+(?![1-9])\|\/0\.(?![0-9])`|注意排除`除以零点几`的情况，包括0.00这种情况|
||运算符（加减乘除百分号）连续|consecutive_operators|`[\+\-\*\/]{2,}\|[\+\-\*\/%]+?%`|形如`+-5`的情况，认为是非法，同理`*-3`、`/-3`、`--4`，另外注意百分号后面可以接运算符|
||%前面不为数字|non_number_with_percentage_symbol|`[^0-9%]%`
||括号不匹配|brackets_mismatch||无法用正则匹配判断
|括号相关
||左括号与乘、除、加、%连续|wrong_operators_after_left_bracket|`\([\*\/\+\%]`
||加减乘除与右括号连续|wrong_operators_before_right_bracket|`[\+\-\*\/]\)`
||右括号之后不为运算符或右括号|wrong_character_after_right_bracket|`\)[^\)\+\-\*\/]`
||左括号之前不为运算符或左括号|wrong_operators_before_left_bracket|`[^\(\+\-\*\/]\(`
|其它补充
||整个运算式以运算符开始|start_with_wrong_character|`^[\+\*\/]`|以负号开始是合法的<br>以%开始被前面的规则覆盖了
||整个运算式以运算符结束|end_with_wrong_character|`[+\-\*\/]$`|以百分号结束是合法的
||小数点左、右或左右均不为数字|illegal_floating_point_number|`(?<!\d)\.[\d]+\|[\d]+\.[^\d]\*(?!\d)\|(?<!\d)[^\d]\*\.[^\d]*(?!\d)`|非法数字，如`.4`、`5.`均为非法形式
||数字中夹杂两个小数点|too_many_decimal_points|`[\d]+\.[\d]+\.[\d]+`|非法数字，如`433.534.2`为非法形式
||数字包含多余前缀零|extra_prefix_0|`[^0-9\.]0+[0-9]+`|非法数字，如`0222`，`00.34`均非法



## 代码实现

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.09.06

import re


def expression_check(expression_string):
    f = expression_string
    f = f.replace(" ", "")

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
            for re_result in re_results:
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
```


## 测试

TODO