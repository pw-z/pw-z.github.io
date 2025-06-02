#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import MemoryHandler
import io


def test1():
    logger = logging.getLogger()

    sio = io.StringIO()
    sh = logging.StreamHandler(sio)

    formatter = logging.Formatter('%(levelname)s [%(asctime)s] %(message)s')
    sh.setFormatter(formatter)

    sh.setLevel(logging.DEBUG)
    logger.setLevel(logging.DEBUG)

    logger.addHandler(sh)

    logger.error('hi')

    # sio.write('world')
    result = sio.getvalue()
    print(result)

    result2 = sio.getvalue()
    print(result2)

    sio.truncate(0)
    sio.seek(0)
    r3 = sio.getvalue()
    print(r3)


from helper.log_helper import *
def test2():
    logger = init_logger(__name__)

    print('#'*80)
    logger.error('test11111111111111111')
    s = get_sio()
    r = s.getvalue()
    print(r)

    print('#' * 80)
    logger.error('test22222222222222222')
    s = get_sio()
    r = s.getvalue()
    print(r)

    print('#' * 80)
    init_sio()
    logger.error('test333333333333333333')
    r = get_sio().getvalue()
    print(r)



if __name__ == '__main__':
    # test1()
    test2()

