#!/usr/bin/env python
# encoding: utf-8
# package

'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/testcase/__init__.py
@time: 2019/1/12
'''

from .course_unittest import *
from .exam_unittest import *
from .score_unittest import *
from .elect_course_unittest import *

__all__ = ['PersonalCourseUnitTest',
           'PersonalExamUnitTest', 'PersonalScoreUnitTest', 'ElectCourseUnitTest']
