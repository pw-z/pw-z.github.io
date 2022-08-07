#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a tool class"""


class Tool:
    """tool is tool"""

    def __init__(self, tool_name, tool_quality, tool_price):
        self.name = tool_name
        self.quality = tool_quality
        self.price = tool_price

    def show_name(self):
        print('This is a tool named %s.' % self.name.title())

    def show_price(self):
        print('This is a tool of %s quality, priced at %s$.' % (self.quality, str(self.price)))

