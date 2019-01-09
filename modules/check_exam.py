#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /modules/check_exam.py
@time: 2019/1/4
'''

import json
from interface import PersonalExam
from shared.exception import ParseError, RequestError

exam_check_url = 'http://i.sjtu.edu.cn/kwgl/kscx_cxXsksxxIndex.html?doType=query&gnmkdm=N358105&su='


def get_exam_dict(s, year, term, course_name="", exam_location="", course_date="", max_limit=15):
    if term == 1:
        term_code = '3'
    elif term == 2:
        term_code = '12'
    elif term == 3:
        term_code = '16'
    else:
        return None
    params = {
        'xnm': str(year),
        'xqm': term_code,
        'ksmcdmb_id': course_name,
        'kch': course_name,
        'kc': exam_location,
        'ksrq': course_date,
        '_search': 'false',
        'nd': s.get_session_id(),
        'queryModel.showCount': str(max_limit),
        'queryModel.currentPage': '1',
        'queryModel.sortName': '',
        'queryModel.sortOrder': 'asc',
        'time': '0'
    }

    resp = s.post(exam_check_url, params)
    if resp.status_code == 200:
        resource = json.loads(resp.content.decode())
        if 'items' in resource:
            data_list = []
            # 如果有数据
            try:
                for item in resource['items']:
                    data_list.append(PersonalExam(**item))
            except ParseError:
                # 抛异常结束
                raise ParseError("Failed to parse exam dictionary.")
            else:
                return data_list
    raise RequestError("Failed to request exam arrangement.")
