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
"C:\Program Files\Python38\python.exe" C:/Users/pengwei.zhang/Desktop/paper/code-filling/pwz.kit/formula-check/expression_check_test.py
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
