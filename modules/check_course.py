#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /modules/check_course.py
@time: 2019/1/4
'''

import json
import logging
from interface import PersonalCourse
from shared.exception import ParseError, RequestError

course_table_url = 'http://i.sjtu.edu.cn/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151'


def get_course_list(s, year, term):
    if s.is_ok():
        if term == 1:
            xqm = '3'
        elif term == 2:
            xqm = '12'
        elif term == 3:
            xqm = '16'
        params = {
            'xnm': str(year),
            'xqm': xqm
        }
        resp = s.post(course_table_url, params)
        if resp.status_code == 200:
            resource = json.loads(resp.content.decode())
        if 'kbList' in resource:
            data_list = []
            # 如果有数据
            success = 0
            fail = 0
            for item in resource['kbList']:
                try:
                    data_list.append(PersonalCourse(**item))
                except ParseError:
                    # 抛异常结束
                    fail += 1
                else:
                    success += 1
            logging.info(
                "Course Parsing complete. %d success, %d fail." % (success, fail))
            return data_list

        raise RequestError("Failed to request course schedule.")
