#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/testcase/elect_course_unittest.py
@time: 2019/1/12
'''

import json
import electsysApi.shared as shared
import logging
import unittest
import electsysApi.interface as interface


class ElectCourseUnitTest(unittest.TestCase):

    __testcase_loc = 'electsysApi/testcase/elect_course_testcase.txt'

    __error_testcase_loc = 'electsysApi/testcase/elect_course_testcase_error.txt'

    __case_count = 0

    @classmethod
    def tearDownClass(self):
        logging.info("Starting Elect Course Unit Test.")
        self.__case_count = 0

    @classmethod
    def setUpClass(self):
        logging.info("Completed %d Elect Course Unit Test." %
                     (self.__case_count))

    def test_normal(self):
        """
        Tests that should return Object but not None
        """
        testcase_f = open(self.__testcase_loc, 'r')
        case_list = testcase_f.readlines()

        for case in case_list:
            # 保证每个构造成功
            self.assertIsNotNone(interface.ElectCourse(**json.loads(case)))
            self.__case_count += 1

    def test_error(self):
        """
        Tests that should raise Exception
        """
        testcase_f = open(self.__error_testcase_loc, 'r')
        case_list = testcase_f.readlines()

        for case in case_list:
            # 保证每个构造抛异常

            self.assertRaises(shared.ParseError,
                              interface.ElectCourse, **json.loads(case))
            self.__case_count += 1
