#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on 2021.07.20

class TestClass:
    def is_equal(self, a, b):
        assert a == b

    def test_is_equal1(self):
        self.is_equal(2, 2)

    def test_is_equal2(self):
        self.is_equal(7, 7)

    def test_is_equal3(self):
        raise Exception('6 equal 6')
