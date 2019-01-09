#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /interface/elect_course.py
@time: 2019/1/9
'''

import warnings
from shared.exception import ParseError


class ElectCourse:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            raise ParseError(
                "Missing key %s in elect information." % self.__missed_keys)

    __personal_keys = ['']

    __missed_keys = []

    def __check_valid(self):
        self.__missed_keys = []
        flag = True
        for key in self.__personal_keys:
            if not key in self.__dict__:
                self.__missed_keys.append(key)
                flag = False
        return flag

    def print_raw(self):
        print(self.__dict__)


class PersonalCourse:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            for critical in self.__critical_keys:
                if critical in self.__missed_keys:
                    # 如果丢失必须 key，就抛异常
                    raise ParseError(
                        "Missed necessary key %s in personal course schedule." % critical)

            # 否则只是打警告
            warnings.warn(
                "Missing key %s in personal course schedule." % self.__missed_keys, RuntimeWarning)

    __personal_keys = ['cdmc', 'cd_id', 'jc', 'jcor',
                       'jcs', 'jgh_id', 'jgpxzd', 'jxb_id', 'jxbmc', 'kch_id', 'kcmc', 'khfsmc', 'xm',
                       'xnm', 'xqj', 'xqjmc']

    __missed_keys = []

    __critical_keys = ['cdmc', 'kcmc', 'xqj', 'jc', 'zcd', 'kch_id', 'xm']

    def __check_valid(self):
        self.__missed_keys = []
        flag = True
        for key in self.__personal_keys:
            if not key in self.__dict__:
                self.__missed_keys.append(key)
                flag = False
        return flag

    def print_raw(self):
        print(self.__dict__)


class PersonalExam:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            for critical in self.__critical_keys:
                if critical in self.__missed_keys:
                    # 如果丢失必须 key，就抛异常
                    raise ParseError(
                        "Missed necessary key %s in personal exam arrangements." % critical)

            # 否则只是打警告
            warnings.warn(
                "Missing key %s in personal exam arrangements." % self.__missed_keys, RuntimeWarning)

    __personal_keys = ['ksmc', 'kssj', 'cdxqmc', 'cdmc', 'xh',
                       'xm', 'xb', 'njmc', 'jgmc', 'zymc', 'bj',
                       'ksmc', 'kch', 'jxbmc', 'xf', 'jxbzc']

    __missed_keys = []

    __critical_keys = ['ksmc', 'kssj']

    def __check_valid(self):
        self.__missed_keys = []
        flag = True
        for key in self.__personal_keys:
            if not key in self.__dict__:
                self.__missed_keys.append(key)
                flag = False
        return flag

    def print_raw(self):
        print(self.__dict__)


class PersonalScore:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            for critical in self.__critical_keys:
                if critical in self.__missed_keys:
                    # 如果丢失必须 key，就抛异常
                    raise ParseError(
                        "Missed necessary key %s in personal score information." % critical)

            # 否则只是打警告
            warnings.warn(
                "Missing key %s in personal score information." % self.__missed_keys, RuntimeWarning)

    __personal_keys = ['kcmc', 'kkbmmc', 'jsxm', 'bfzcj',
                       'jd', 'kch', 'jxbmc', 'xh', 'xm', 'xb', 'njmc', 'jgmc', 'zymc', 'bh_id', 'bj']

    __missed_keys = []

    __critical_keys = ['kcmc', 'bfzcj']

    def __check_valid(self):
        self.__missed_keys = []
        flag = True
        for key in self.__personal_keys:
            if not key in self.__dict__:
                self.__missed_keys.append(key)
                flag = False
        return flag

    def print_raw(self):
        print(self.__dict__)
