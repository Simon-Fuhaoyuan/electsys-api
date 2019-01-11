#!/usr/bin/env python
# encoding: utf-8
# package

'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /manip/__init__.py
@time: 2019/1/6
'''

from .query_course import *
from .elect_course import *
from .check_selected import *

__all__ = ['query_course', 'query_course_detail',
           'select_course', 'deselect_course', 'check_selected_course']
