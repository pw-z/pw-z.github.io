# 1. 用Python和正则表达式校验数学运算式的合法性

*check-the-validity-of-mathematical-expressions-with-python-and-regular-expression*  
*Posted on 2021.09.08 by [Zhang Pengwei](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  

- [1. 问题描述](#1-问题描述)
- [2. 运算式非法情况及对应正则表达式](#2-运算式非法情况及对应正则表达式)
- [3. 代码实现](#3-代码实现)
- [4. 测试](#4-测试)
  - [4.1. 测试用例](#41-测试用例)
  - [4.2. 测试代码及结果](#42-测试代码及结果)


## 1. 问题描述

某场景下，合法的运算式由`数字（正负整数、正负小数）、加、减、乘、除、括号、百分号`构成，该运算式除了需要满足基本的四则运算规则，还需要满足如下规则：

* 百分号仅可置于数字后面，即`(A+B)%`为非法形式
* 两组括号相乘时乘号不可省略
* 正数前面不可以加正号

假设输入为一数学运算式，求该运算式是否合法，若非法需要给出非法原因。例如，运算式`123*(3.5%+1)/12`合法，可以正常运算出结果，运算式`345*+23*(34-1))`非法，`*`与`+`连写且多了一个右括号。



## 2. 运算式非法情况及对应正则表达式

以下列举的情况存在交叉覆盖的情况，即同一个场景会符合多个非法情况，对应的正则表达式也存在同样的多重命中的问题，有适当微调但未进行严格划分。

|分组|非法情况|字典字段|正则表达式|备注|
|---|---|---|---|---|
|基本错误
||含有非法字符|contains_illegal_characters|`[^0-9\+\-\*\/%\(\)\.]`
||空括号|empty_bracket|`\(\)`
||显式除零|literal_divided_by_zero|`\/0(?!\.)|\/0\.0+(?![1-9])|\/0\.(?![0-9])`|注意排除`除以零点几`的情况，包括0.00这种情况|
||运算符（加减乘除百分号）连续|consecutive_operators|`[\+\-\*\/]{2,}|[\+\-\*\/%]+?%`|形如`+-5`的情况，认为是非法，同理`*-3`、`/-3`、`--4`，另外注意百分号后面可以接运算符|
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
||小数点左、右或左右均不为数字|illegal_floating_point_number|`(?<!\d)\.[\d]+|[\d]+\.[^\d]\*(?!\d)|(?<!\d)[^\d]\*\.[^\d]*(?!\d)`|如`.4`、`5.`均为非法形式
||数字中夹杂两个小数点|too_many_decimal_points|`[\d]+\.[\d]+\.[\d]+`|如`433.534.2`为非法形式
||数字包含多余前缀零|extra_prefix_0|`[^0-9\.]0+[0-9]+`|如`0222`，`00.34`均为非法形式


上述部分正则编写过程中的注意事项、经验，在此备注：

* 为了后续编码过程可以取到非法子串作为提示信息，可以扩大命中范围，如将非法小数`5.`命中为`5.abc`
* 运算符连续不能简单写为`[\+\-\*\/\%]{2,}`，会命中合法表达式如`2.4%*10000`，需要单独处理百分号
* 正则中有`^`与`$`用于实现从头或从尾部匹配，不用在代码中额外进行转置、将`search`换成`match`等多余操作
* 要命中`/0`或`/0.0`但不命中`/0.01`，可以借助`否定预查(negative assert)`实现，同理所有条件命中的情况


## 3. 代码实现

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


## 4. 测试

### 4.1. 测试用例

按照前文非法情况对应列举如下正向、反向用例，有重复覆盖的情况未进行严格划分。

|   用例    |    运算式   |
|---|---|
|	合法运算式_空运算式	|		|
|	合法运算式_简单加法	|	1+2+3	|
|	合法运算式_简单减法	|	10-1-999	|
|	合法运算式_简单乘法	|	2\*5\*10	|
|	合法运算式_简单除法及精度校验	|	100/10/3	|
|	合法运算式_简单四则混合	|	2*2-3/3+1	|
|	合法运算式_括号引入	|	2*((2-3)/3+1)	|
|	合法运算式_括号多层嵌套	|	((((((1+1)+1)+1)+1)+1)+(1+1))+(0)	|
|	合法运算式_括号后接负数	|	(-3+(-4))-7	|
|	合法运算式_除以小数	|	10/0.025	|
|	合法运算式_除以带百分号的数字	|	10/2.5%	|
|	合法运算式_合法百分号位置覆盖	|	2%*((2%-3%)/3%+1%/2%)-0.01%	|
|	合法运算式_运算式以负号开始	|	-23+(34-123)	|
|	非法运算式_空括号	|	1+()+32	|
|	非法运算式_显式除零	|	12/0	|
|	非法运算式_除以小数零	|	12/0.00	|
|	非法运算式_运算符连续1	|	11 ++ 22	|
|	非法运算式_运算符连续2	|	11 +- 22	|
|	非法运算式_运算符连续3	|	11 +* 22	|
|	非法运算式_运算符连续4	|	11 +/ 22	|
|	非法运算式_运算符连续5	|	11 +% 22	|
|	非法运算式_运算符连续6	|	11 -+ 22	|
|	非法运算式_运算符连续7	|	11 -- 22	|
|	非法运算式_运算符连续8	|	11 -* 22	|
|	非法运算式_运算符连续9	|	11 -/ 22	|
|	非法运算式_运算符连续10	|	11 -% 22	|
|	非法运算式_运算符连续11	|	11 *+ 22	|
|	非法运算式_运算符连续12	|	11 *- 22	|
|	非法运算式_运算符连续13	|	11 ** 22	|
|	非法运算式_运算符连续14	|	11 */ 22	|
|	非法运算式_运算符连续15	|	11 *% 22	|
|	非法运算式_运算符连续16	|	11 /+ 22	|
|	非法运算式_运算符连续17	|	11 /- 22	|
|	非法运算式_运算符连续18	|	11 /* 22	|
|	非法运算式_运算符连续19	|	11 // 22	|
|	非法运算式_运算符连续20	|	11 /% 22	|
|	非法运算式_运算符连续21	|	11 %%  22	|
|	非法运算式_百分号前面不为数字1	|	+%	|
|	非法运算式_百分号前面不为数字2	|	-%	|
|	非法运算式_百分号前面不为数字3	|	*%	|
|	非法运算式_百分号前面不为数字4	|	/%	|
|	非法运算式_百分号前面不为数字5	|	%%	|
|	非法运算式_百分号前面不为数字6	|	(%)	|
|	非法运算式_百分号前面不为数字7	|	(1+1)%	|
|	非法运算式_百分号前面不为数字8	|	.%	|
|	非法运算式_左括号与乘除加及百分号连续1	|	1+(*2)	|
|	非法运算式_左括号与乘除加及百分号连续2	|	1+(/2)	|
|	非法运算式_左括号与乘除加及百分号连续3	|	1+(+2)	|
|	非法运算式_左括号与乘除加及百分号连续4	|	1+(%2)	|
|	非法运算式_加减乘除与右括号连续1	|	(1+)	|
|	非法运算式_加减乘除与右括号连续2	|	(1-)	|
|	非法运算式_加减乘除与右括号连续3	|	(1*)	|
|	非法运算式_加减乘除与右括号连续4	|	(1/)	|
|	非法运算式_右括号之后不为运算符或右括号1	|	(1+2)3	|
|	非法运算式_右括号之后不为运算符或右括号2	|	(1+2)0.3	|
|	非法运算式_右括号之后不为运算符或右括号3	|	(1+2)(1-2)	|
|	非法运算式_右括号之后不为运算符或右括号4	|	(1+2)%	|
|	非法运算式_左括号之前不为运算符或左括号1	|	5(1+2)	|
|	非法运算式_左括号之前不为运算符或左括号2	|	0.3(1-2)	|
|	非法运算式_左括号之前不为运算符或左括号3	|	(-2)(-2)	|
|	非法运算式_左括号之前不为运算符或左括号4	|	12%(-1)	|
|	非法运算式_运算式以运算符开始1	|	+(1+1)	|
|	非法运算式_运算式以运算符开始2	|	*(1+1)	|
|	非法运算式_运算式以运算符开始3	|	/(1+1)	|
|	非法运算式_运算式以运算符结束1	|	(1+1)+	|
|	非法运算式_运算式以运算符结束2	|	(1+1)-	|
|	非法运算式_运算式以运算符结束3	|	(1+1)*	|
|	非法运算式_运算式以运算符结束4	|	(1+1)/	|
|	非法运算式_非法小数格式1	|	1+3.	|
|	非法运算式_非法小数格式2	|	1+.3	|
|	非法运算式_非法小数格式3	|	1-.3	|
|	非法运算式_非法小数格式4	|	1+0..3	|
|	非法运算式_非法小数格式5	|	.	|
|	非法运算式_非法小数格式6	|	..	|
|	非法运算式_非法小数格式7	|	1-0.5 .1	|
|	非法运算式_非法小数格式8	|	1+3.3.3	|
|	非法运算式_数字含多余前缀零1	|	1+01	|
|	非法运算式_数字含多余前缀零2	|	1/001	|
|	非法运算式_数字含多余前缀零3	|	1/000.1	|
|	非法运算式_运算式含非法字符	|	~`!@#$^&_=[]{}\|:;"'<,>.?	|


### 4.2. 测试代码及结果

上述测试用例保存在CSV文件中，依次读取调用检查程序，输出结果到控制台及文件中。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.09.10

import csv
from expression_check import expression_check as check


def run_test():
    with open('expression_test_data.csv', 'r', encoding='utf8', newline='') as csv_file, \
            open('expression_test_result.text', 'w', encoding='utf8') as output_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['case'], row['expression'])
            result = check(row['expression'])
            print(result)
            output_file.write(row['case'] + row['expression'] + '\n')
            output_file.write(result + '\n')


if __name__ == '__main__':
    run_test()

"""
"C:\Program Files\Python38\python.exe" C:/pwz.kit/expression_check_test.py
合法运算式_空运算式  
PASS, NO ERROR FOUND
合法运算式_简单加法 1+2+3
PASS, NO ERROR FOUND
合法运算式_简单减法 10-1-999
PASS, NO ERROR FOUND
合法运算式_简单乘法 2*5*10
PASS, NO ERROR FOUND
合法运算式_简单除法及精度校验 100/10/3
PASS, NO ERROR FOUND
合法运算式_简单四则混合 2*2-3/3+1
PASS, NO ERROR FOUND
合法运算式_括号引入 2*((2-3)/3+1)
PASS, NO ERROR FOUND
合法运算式_括号多层嵌套 ((((((1+1)+1)+1)+1)+1)+(1+1))+(0)
PASS, NO ERROR FOUND
合法运算式_括号后接负数 (-3+(-4))-7
PASS, NO ERROR FOUND
合法运算式_除以小数 10/0.025
PASS, NO ERROR FOUND
合法运算式_除以带百分号的数字 10/2.5%
PASS, NO ERROR FOUND
合法运算式_合法百分号位置覆盖 2%*((2%-3%)/3%+1%/2%)-0.01%
PASS, NO ERROR FOUND
合法运算式_运算式以负号开始 -23+(34-123)
PASS, NO ERROR FOUND
非法运算式_空括号 1+()+32
Error: empty_bracket
()
非法运算式_显式除零 12/0
Error: literal_divided_by_zero
/0
非法运算式_除以小数零 12/0.00
Error: literal_divided_by_zero
/0.00
非法运算式_运算符连续1 11 ++ 22
Error: consecutive_operators
++
非法运算式_运算符连续2 11 +- 22
Error: consecutive_operators
+-
非法运算式_运算符连续3 11 +* 22
Error: consecutive_operators
+*
非法运算式_运算符连续4 11 +/ 22
Error: consecutive_operators
+/
非法运算式_运算符连续5 11 +% 22
Error: consecutive_operators
+%
Error: non_number_with_percentage_symbol
+%
非法运算式_运算符连续6 11 -+ 22
Error: consecutive_operators
-+
非法运算式_运算符连续7 11 -- 22
Error: consecutive_operators
--
非法运算式_运算符连续8 11 -* 22
Error: consecutive_operators
-*
非法运算式_运算符连续9 11 -/ 22
Error: consecutive_operators
-/
非法运算式_运算符连续10 11 -% 22
Error: consecutive_operators
-%
Error: non_number_with_percentage_symbol
-%
非法运算式_运算符连续11 11 *+ 22
Error: consecutive_operators
*+
非法运算式_运算符连续12 11 *- 22
Error: consecutive_operators
*-
非法运算式_运算符连续13 11 ** 22
Error: consecutive_operators
**
非法运算式_运算符连续14 11 */ 22
Error: consecutive_operators
*/
非法运算式_运算符连续15 11 *% 22
Error: non_number_with_percentage_symbol
*%
非法运算式_运算符连续16 11 /+ 22
Error: consecutive_operators
/+
非法运算式_运算符连续17 11 /- 22
Error: consecutive_operators
/-
非法运算式_运算符连续18 11 /* 22
Error: consecutive_operators
/*
非法运算式_运算符连续19 11 // 22
Error: consecutive_operators
//
非法运算式_运算符连续20 11 /% 22
Error: non_number_with_percentage_symbol
/%
非法运算式_运算符连续21 11 %%  22
Error: consecutive_operators
%%
非法运算式_百分号前面不为数字1 +%
Error: consecutive_operators
+%
Error: non_number_with_percentage_symbol
+%
Error: start_with_wrong_character
+
非法运算式_百分号前面不为数字2 -%
Error: consecutive_operators
-%
Error: non_number_with_percentage_symbol
-%
非法运算式_百分号前面不为数字3 *%
Error: non_number_with_percentage_symbol
*%
Error: start_with_wrong_character
*
非法运算式_百分号前面不为数字4 /%
Error: non_number_with_percentage_symbol
/%
Error: start_with_wrong_character
/
非法运算式_百分号前面不为数字5 %%
Error: consecutive_operators
%%
非法运算式_百分号前面不为数字6 (%)
Error: non_number_with_percentage_symbol
(%
Error: wrong_operators_after_left_bracket
(%
非法运算式_百分号前面不为数字7 (1+1)%
Error: non_number_with_percentage_symbol
)%
Error: wrong_character_after_right_bracket
)%
非法运算式_百分号前面不为数字8 .%
Error: non_number_with_percentage_symbol
.%
Error: illegal_floating_point_number
.%
非法运算式_左括号与乘除加及百分号连续1 1+(*2)
Error: wrong_operators_after_left_bracket
(*
非法运算式_左括号与乘除加及百分号连续2 1+(/2)
Error: wrong_operators_after_left_bracket
(/
非法运算式_左括号与乘除加及百分号连续3 1+(+2)
Error: wrong_operators_after_left_bracket
(+
非法运算式_左括号与乘除加及百分号连续4 1+(%2)
Error: non_number_with_percentage_symbol
(%
Error: wrong_operators_after_left_bracket
(%
非法运算式_加减乘除与右括号连续1 (1+)
Error: wrong_operators_before_right_bracket
+)
非法运算式_加减乘除与右括号连续2 (1-)
Error: wrong_operators_before_right_bracket
-)
非法运算式_加减乘除与右括号连续3 (1*)
Error: wrong_operators_before_right_bracket
*)
非法运算式_加减乘除与右括号连续4 (1/)
Error: wrong_operators_before_right_bracket
/)
非法运算式_右括号之后不为运算符或右括号1 (1+2)3
Error: wrong_character_after_right_bracket
)3
非法运算式_右括号之后不为运算符或右括号2 (1+2)0.3
Error: wrong_character_after_right_bracket
)0
非法运算式_右括号之后不为运算符或右括号3 (1+2)(1-2)
Error: wrong_character_after_right_bracket
)(
Error: wrong_operators_before_left_bracket
)(
非法运算式_右括号之后不为运算符或右括号4 (1+2)%
Error: non_number_with_percentage_symbol
)%
Error: wrong_character_after_right_bracket
)%
非法运算式_左括号之前不为运算符或左括号1 5(1+2)
Error: wrong_operators_before_left_bracket
5(
非法运算式_左括号之前不为运算符或左括号2 0.3(1-2)
Error: wrong_operators_before_left_bracket
3(
非法运算式_左括号之前不为运算符或左括号3 (-2)(-2)
Error: wrong_character_after_right_bracket
)(
Error: wrong_operators_before_left_bracket
)(
非法运算式_左括号之前不为运算符或左括号4 12%(-1)
Error: wrong_operators_before_left_bracket
%(
非法运算式_运算式以运算符开始1 +(1+1)
Error: start_with_wrong_character
+
非法运算式_运算式以运算符开始2 *(1+1)
Error: start_with_wrong_character
*
非法运算式_运算式以运算符开始3 /(1+1)
Error: start_with_wrong_character
/
非法运算式_运算式以运算符结束1 (1+1)+
Error: end_with_wrong_character
+
非法运算式_运算式以运算符结束2 (1+1)-
Error: end_with_wrong_character
-
非法运算式_运算式以运算符结束3 (1+1)*
Error: end_with_wrong_character
*
非法运算式_运算式以运算符结束4 (1+1)/
Error: end_with_wrong_character
/
非法运算式_非法小数格式1 1+3.
Error: illegal_floating_point_number
3.
非法运算式_非法小数格式2 1+.3
Error: illegal_floating_point_number
.3
非法运算式_非法小数格式3 1-.3
Error: illegal_floating_point_number
.3
非法运算式_非法小数格式4 1+0..3
Error: illegal_floating_point_number
0.
.3
非法运算式_非法小数格式5 .
Error: illegal_floating_point_number
.
非法运算式_非法小数格式6 ..
Error: illegal_floating_point_number
..
非法运算式_非法小数格式7 1-0.5 .1
Error: too_many_decimal_points
0.5.1
非法运算式_非法小数格式8 1+3.3.3
Error: too_many_decimal_points
3.3.3
非法运算式_数字含多余前缀零1 1+01
Error: extra_prefix_0
+01
非法运算式_数字含多余前缀零2 1/001
Error: literal_divided_by_zero
/0
Error: extra_prefix_0
/001
非法运算式_数字含多余前缀零3 1/000.1
Error: literal_divided_by_zero
/0
Error: extra_prefix_0
/000
非法运算式_运算式含非法字符 ~`!@#$^&_=[]{}\|:;"'<,>.?
Error: contains_illegal_characters
~
`
!
@
#
$
^
&
=
[
]
{
}
\
|
:
;
"
'
<
,
>
?
Error: illegal_floating_point_number
~`!@#$^&_=[]{}\|:;"'<,>.?

Process finished with exit code 0
"""
```