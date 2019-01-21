#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/shared/exception.py
@time: 2019/1/9
'''


class RequestError(BaseException):
    pass


class ParseError(BaseException):
    pass


class ParseWarning(Warning):
    pass
