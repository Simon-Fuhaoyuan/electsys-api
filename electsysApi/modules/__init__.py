#!/usr/bin/env python
# encoding: utf-8
# package

'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/modules/__init__.py
@time: 2019/1/4
'''

from .calendar import *
from .check_course import *
from .check_score import *
from .check_exam import *
from .query_all import *

__all__ = ['get_calendar_table', 'get_start_day',
           'get_course_list', 'get_score_list', 'get_exam_list', 'conditional_query']
