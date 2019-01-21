#!/usr/bin/env python
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: unit_test.py
@time: 2019/1/12
'''

import unittest
import electsysApi.testcase as tc

suite = unittest.TestSuite()

# PersonalCourse Unittest
suite.addTest(tc.course_unittest.PersonalCourseUnitTest("test_normal"))
suite.addTest(tc.course_unittest.PersonalCourseUnitTest("test_error"))

# PersonalExam Unittest
suite.addTest(tc.exam_unittest.PersonalExamUnitTest("test_normal"))
suite.addTest(tc.exam_unittest.PersonalExamUnitTest("test_error"))

# PersonalScore Unittest
suite.addTest(tc.score_unittest.PersonalScoreUnitTest("test_normal"))
suite.addTest(tc.score_unittest.PersonalScoreUnitTest("test_error"))

# ElectCourse Unittest
suite.addTest(
    tc.elect_course_unittest.ElectCourseUnitTest("test_normal"))
suite.addTest(tc.elect_course_unittest.ElectCourseUnitTest("test_error"))

runner = unittest.TextTestRunner()
runner.run(suite)
