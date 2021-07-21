#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.07.20
import allure


class TestClass:
    @allure.step("TEST 1")
    def is_equal(self, a, b):
        assert a == b

    @allure.step("TEST 2")
    def test_is_equal1(self):
        self.is_equal(2, 3)

    @allure.step("TEST 3")
    def test_is_equal2(self):
        self.is_equal(7, 9)