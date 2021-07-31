#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
import io

__sio = io.StringIO()


def init_sio():
    __sio.truncate(0)
    __sio.seek(0)


def get_sio():
    return __sio


def init_logger(__name__):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    today = time.strftime('%Y-%m-%d')
    log_name = today + '.log'
    log_path = 'log/' + log_name
    # log_path = log_name

    formatter = logging.Formatter('%(levelname)s [%(asctime)s] %(message)s')

    fh = logging.FileHandler(log_path, encoding='utf-8')
    ch = logging.StreamHandler()

    sh = logging.StreamHandler(__sio)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    sh.setFormatter(formatter)

    fh.setLevel(logging.DEBUG)
    ch.setLevel(logging.ERROR)
    sh.setLevel(logging.INFO)

    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.addHandler(sh)
    return logger

