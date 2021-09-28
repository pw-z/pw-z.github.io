#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.09.22

from datetime import datetime
import time


def generate_list():
    nums = list(range(1, 101, 2))
    print(nums)

    # start_time1 = datetime.now()
    start_time = time.time()
    million = list(range(1, 1000000))
    print('min of million = ' + str(min(million)))
    print('max of million = ' + str(max(million)))
    for num in million:
        # pass
        print(num)
    # end_time1 = datetime.now()
    end_time = time.time()
    duration = round((end_time - start_time) * 1000)  # ms
    # duration1 = str(end_time1 - start_time1)
    print('duration = ' + str(duration))
    # print('duration1 = ' + duration1)
    print('every print costs = ' + str(duration / 1000000))


def how_long_takes_to_sum_million_numbers():
    million = list(range(1, 1000001))
    start = time.time()
    print(sum(million))
    end = time.time()
    duration = round((end - start) * 1000)
    print("duration = %s ms" % str(duration))


def list_comprehensions():
    list_squares = [val ** 2 for val in range(1, 101)]
    print(list_squares)
    list_squares.extend([val ** 2 for val in range(200, 205)])
    print(list_squares)
    print('min = ' + str(min(list_squares)))
    print('max = ' + str(max(list_squares)))
    print('sum = ' + str(sum(list_squares)))


def copy_list():
    list1 = [1, 2, 3]
    list2 = list1
    list3 = list1[:]

    list1.append(4)
    print(list1)
    print(list2)
    print(list3)

    list2.append(5)
    print(list1)
    print(list2)
    print(list3)

    list3.append(6)
    print(list1)
    print(list2)
    print(list3)


def map_mapping():
    mymap = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    print('key:')
    for key in mymap.keys():
        print(key)
    print('val:')
    for val in mymap.values():
        print(val)
    print('key.val:')
    for key, val in mymap.items():
        print(key + '.' + str(val))



if __name__ == '__main__':
    # generate_list()
    # how_long_takes_to_sum_million_numbers()
    # list_comprehensions()
    # copy_list()
    map_mapping()