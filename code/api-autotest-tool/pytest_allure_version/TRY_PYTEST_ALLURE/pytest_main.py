#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.07.20
import os
import pytest

if __name__ == '__main__':
    pytest.main(["-sq", "--alluredir=allure-results"])
    os.system(r"allure generate allure-results -o allure-report --clean")

