#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.07.28
import os
import pytest
import allure


cases = [
    {"case":"case1", "step":"step1"},
    {"case":"case1", "step":"step2"},
    {"case":"case2", "step":"step1"},
    {"case":"case2", "step":"step2"},
]


@pytest.mark.parametrize("case", cases)
class TestClass:
    def test_run(self, case):
        allure.dynamic.story(case["case"])
        allure.dynamic.title(case["step"])
        # print(case["case"])
        # print(case["step"])
        assert 1 == 2


if __name__ == '__main__':
    pytest.main(["-sq", "--alluredir=allure-results"])
    os.system(r"allure generate allure-results -o allure-report --clean")

