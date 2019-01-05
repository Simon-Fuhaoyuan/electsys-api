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


def get_course_dict(s, year, term):
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
            return json.loads(resp.content.decode())
        return None
