#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.08.31

import time


operator = ['+', '-', '*', '/', '%', '(', ')']


def generate_formula(operator, path_to_file):
    with open(path_to_file, 'w', encoding='utf8') as f:
        for op1 in operator:
            for op2 in operator:
                for op3 in operator:
                    for op4 in operator:
                        for op5 in operator:
                            for op6 in operator:
                                for op7 in operator:
                                    formula = op1 + op2 + op3 + op4 + op5 + op6 + op7
                                    # print(formula)
                                    f.write(formula + '\n')


def random_formula(length):
    for i in range(length):
        # TODO:根据长度生成一定格式的随机公式
        pass

if __name__ == '__main__':
    start_time = time.time()*1000  # s
    generate_formula(operator, 'test.text')
    end_time = time.time()*1000
    duration = end_time - start_time
    print(duration)

