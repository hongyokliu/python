#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "Parameter does not contain numbers\n", Argument


temp_convert("xyz");# 调用函数
