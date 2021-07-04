#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


def init_logger(__name__):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('test.log', encoding='utf-8')
    ch = logging.StreamHandler()

    formatter = logging.Formatter('%(levelname)s [%(asctime)s] %(message)s')

    fh.setLevel(logging.DEBUG)
    ch.setLevel(logging.INFO)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger