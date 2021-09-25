#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.08.31

import time

operator = ['+', '-', '*', '/', '%', '(', ')']


def generate_expression(operator, path_to_file):
    with open(path_to_file, 'w', encoding='utf8') as f:
        for op1 in operator:
            for op2 in operator:
                for op3 in operator:
                    for op4 in operator:
                        for op5 in operator:
                            for op6 in operator:
                                for op7 in operator:
                                    expression = op1 + op2 + op3 + op4 + op5 + op6 + op7
                                    # print(expression)
                                    f.write(expression + '\n')


def random_expression(length=3):
    for i in range(length):
        pass


# 运算符非法连续
def consecutive_operators():
    ops = ['+', '-', '*', '/', '%']
    _result = []
    for op1 in ops:
        if op1 != '%':
            for op2 in ops:
                print('11 ' + op1 + op2 + ' 22')
                _result.append('11 ' + op1 + op2 + ' 22')
        else:
            print('11 %%  22')
            _result.append('11 %% 22')
    return _result


# 百分号前面不为数字
def not_number_befort_per():
    ops = ['+', '-', '*', '/', '%', '(', ')', '.']
    _result = []
    for op in ops:
        print(op + '%')
        _result.append(op + '%')
    return _result


if __name__ == '__main__':
    # result = consecutive_operators()
    not_number_befort_per()

