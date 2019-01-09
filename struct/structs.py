#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /struct/elect_course.py
@time: 2019/1/9
'''


class ElectCourse:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            raise ParseError("Failed to parse course elect information.")

    __personal_keys = ['']

    def __check_valid(self):
        for key in self.__personal_keys:
            if not key in self.__dict__:
                return False
        return True

    def print_raw(self):
        print(self.__dict__)


class PersonalCourse:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            raise ParseError("Failed to parse personal course schedule.")

    __personal_keys = ['cd_id', 'cdmc', 'jc', 'jcor',
                       'jcs', 'jgh_id', 'jgpxzd', 'jxb_id', 'jxbmc', 'kch_id', 'kcmc', 'khfsmc', 'xm',
                       'xnm', 'xqj', 'xqjmc', 'xqm', 'xqmc']

    def __check_valid(self):
        for key in self.__personal_keys:
            if not key in self.__dict__:
                return False
        return True

    def print_raw(self):
        print(self.__dict__)


class PersonalExam:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            raise ParseError("Failed to parse personal exam information.")

    __personal_keys = ['ksmc', 'kssj', 'cdxqmc', 'cdmc', 'xh',
                       'xm', 'xb', 'njmc', 'jgmc', 'zymc', 'bj',
                       'ksmc', 'kch', 'jxbmc', 'xf', 'jxbzc']

    def __check_valid(self):
        for key in self.__personal_keys:
            if not key in self.__dict__:
                return False
        return True

    def print_raw(self):
        print(self.__dict__)


class PersonalScore:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            raise ParseError("Failed to parse personal score information.")

    __personal_keys = ['kcmc', 'kkbmmc', 'jsxm', 'bfzcj', 'zcj',
                       'jd', 'kch', 'jxbmc', 'xh', 'xm', 'xb', 'njmc', 'jgmc', 'zymc', 'bh_id', 'bj']

    def __check_valid(self):
        for key in self.__personal_keys:
            if not key in self.__dict__:
                return False
        return True

    def print_raw(self):
        print(self.__dict__)
