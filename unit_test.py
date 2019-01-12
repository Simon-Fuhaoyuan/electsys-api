#!/usr/bin/env python
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /unit_test.py
@time: 2019/1/12
'''

import unittest
import testcase

suite = unittest.TestSuite()

# PersonalCourse Unittest
suite.addTest(testcase.course_unittest.PersonalCourseUnitTest("test_normal"))
suite.addTest(testcase.course_unittest.PersonalCourseUnitTest("test_error"))

# PersonalExam Unittest
suite.addTest(testcase.exam_unittest.PersonalExamUnitTest("test_normal"))
suite.addTest(testcase.exam_unittest.PersonalExamUnitTest("test_error"))

# PersonalScore Unittest
suite.addTest(testcase.score_unittest.PersonalScoreUnitTest("test_normal"))
suite.addTest(testcase.score_unittest.PersonalScoreUnitTest("test_error"))

# ElectCourse Unittest
suite.addTest(
    testcase.elect_course_unittest.ElectCourseUnitTest("test_normal"))
suite.addTest(testcase.elect_course_unittest.ElectCourseUnitTest("test_error"))

runner = unittest.TextTestRunner()
runner.run(suite)
