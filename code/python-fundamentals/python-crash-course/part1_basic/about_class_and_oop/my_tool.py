#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""my_tool which inherited tool"""

from tool import Tool


class MyTool(Tool):
    def show_name(self):
        print('This is a my_tool named %s.' % self.name.title())


if __name__ == '__main__':
    tool = Tool('tool', 'low', '500')
    tool.show_name()
    tool.show_price()
    my_tool = MyTool('my_tool', 'high', '900')
    my_tool.show_name()
    my_tool.show_price()
"""
This is a tool named Tool.
This is a tool of low quality, priced at 500$.
This is a my_tool named My_Tool.
This is a tool of high quality, priced at 900$.
"""