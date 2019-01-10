#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /interface/interface.py
@time: 2019/1/9
'''

import logging
from shared.exception import ParseError


class ElectCourse:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            for critical in self.__critical_keys:
                if critical in self.__missed_keys:
                    # 如果丢失必须 key，就抛异常
                    raise ParseError(
                        "Missed critical key %s in course query." % critical)

            # 否则只是打警告
            logging.warn(
                "Missing key %s in personal course query." % self.__missed_keys)

    __personal_keys = ['jxb_id', 'jxbmc', 'kch', 'kch_id',
                       'kcmc', 'xf']

    __missed_keys = []

    __critical_keys = ['jxb_id', 'kch_id', 'kcmc', 'xf']

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
                    if 'kcmc' in self.__dict__:
                        raise ParseError("Missed critical key %s in <PersonalCourse> %s." % (
                            critical, self.__dict__['kcmc']))
                    raise ParseError("Missed critical key %s in <PersonalCourse> Anonymous." %
                                     critical)

            # 否则只是打警告
            logging.warn(
                "Missing optional key[s] %s in PersonalCourse: %s. Use carefully." % (self.__missed_keys, self.__dict__['kcmc']))

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
                    if 'ksmc' in self.__dict__:
                        raise ParseError(
                            "Missed critical key %s in <PersonalExam> %s." % (critical, self.__dict__['ksmc']))
                    raise ParseError(
                        "Missed critical key %s in <PersonalExam> Anonymous." % critical)

            # 否则只是打警告
            logging.warn(
                "Missing optional key[s] %s in <PersonalExam> %s. Use carefully." % (critical, self.__dict__['ksmc']))

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
                    if 'kcmc' in self.__dict__:
                        raise ParseError(
                            "Missed critical key %s in <PersonalScore> %s." % (critical, self.__dict__['kcmc']))
                    raise ParseError(
                        "Missed critical key %s in <PersonalScore> Anonymous." % critical)

            # 否则只是打警告
            logging.warn(
                "Missing optional key %s in <PersonalScore> %s. Use carefully." % (self.__missed_keys, self.__dict__['kcmc']))

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


class CourseDetail:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        if not self.__check_valid():
            for critical in self.__critical_keys:
                if critical in self.__missed_keys:
                    # 如果丢失必须 key，就抛异常
                    if 'kcmc' in self.__dict__:
                        raise ParseError(
                            "Missed critical key %s in <CourseDetail> %s." % (critical, self.__dict__['kcmc']))
                    raise ParseError(
                        "Missed critical key %s in <CourseDetail> Anonymous." % critical)

            # 否则只是打警告
            logging.warn(
                "Missing optional key %s in <CourseDetail> %s. Use carefully." % (self.__missed_keys, self.__dict__['kcmc']))

    __personal_keys = ['jxb_id', 'jxbrl', 'jxdd', 'sksj', 'jsxx']

    __missed_keys = ['jxb_id', 'jxbrl', 'jxdd']

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
