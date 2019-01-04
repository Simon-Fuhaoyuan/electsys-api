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


course_table_url = 'http://i.sjtu.edu.cn/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151'


def get_course_json(s, year, term):
    if s.is_ok():
        params = {
            'xnm': str(year),
            'xqm': str(term)
        }
        resp = s.post(course_table_url, params)
        if resp.status_code == 200:
            return resp.content.decode()
        return None
