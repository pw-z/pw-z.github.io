#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_para_order(para1, para2, para3='para3'):
    """ this won't work
    def test_para_order(para1, para2='para2', para3):
        print(para1)
        print(para2)
        print(para3)
    """
    print(para1)
    print(para2)
    print(para3)


def parameterize_copy_of_list():
    def _test(a_list):
        for i in range(len(a_list)):
            a_list[i] = 0;
        return a_list

    nums = list(range(1, 11))
    print(nums)
    _test(nums[:])
    print(nums)
    _test(nums)
    print(nums)


def pass_many_paras(*paras):
    print(paras)
    for para in paras:
        print(para)


def pass_many_key_value_paras(pos_para, **paras):
    print(pos_para)
    print(paras)
    for key, val in paras.items():
        print(key + ': ' + val)


if __name__ == '__main__':
    # test_para_order(1, 2)
    # parameterize_copy_of_list()
    # pass_many_paras('para1', 'para2', ['x', 'y'])
    pass_many_key_value_paras('hi', name='python', whatever='whatever')

