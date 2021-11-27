#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Logger Factory.

fh = logging.FileHandler()   --> file log handler
ch = logging.StreamHandler() --> console log handler
sh = logging.StreamHandler() --> using to capture all logs to generate test report
"""
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
    """Initialize and return the logger.

    :param __name__: model name
    :return: logging.getLogger(__name__)
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    today = time.strftime('%Y-%m-%d')
    log_name = today + '.log'
    log_path = 'log/' + log_name

    formatter = logging.Formatter('%(levelname)s [%(asctime)s] %(message)s')

    fh = logging.FileHandler(log_path, encoding='utf-8')
    ch = logging.StreamHandler()
    sh = logging.StreamHandler(__sio)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    sh.setFormatter(formatter)

    fh.setLevel(logging.DEBUG)
    ch.setLevel(logging.INFO)
    sh.setLevel(logging.DEBUG)

    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.addHandler(sh)
    return logger

