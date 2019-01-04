#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /modules/calendar.py
@time: 2019/1/4
'''

import requests

calendar_url = 'http://i.sjtu.edu.cn/xtgl/index_cxshjdAreaFive.html?localeKey=zh_CN&gnmkdm=index&su='


def get_calendar(s):
    if s.is_ok():
        url = calendar_url + s.student_id
        return s.GET(url).content.decode()
    return None
