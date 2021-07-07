#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time


def init_logger(__name__):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    today = time.strftime('%Y-%m-%d')
    log_name = today + '.log'
    # log_path = 'log/' + log_name
    log_path = log_name

    fh = logging.FileHandler(log_path, encoding='utf-8')
    ch = logging.StreamHandler()

    formatter = logging.Formatter('%(levelname)s [%(asctime)s] %(message)s')

    fh.setLevel(logging.DEBUG)
    ch.setLevel(logging.INFO)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger