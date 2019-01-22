#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/modules/query_all.py
@time: 2019/1/4
'''

import json
import logging
from urllib.parse import quote
from electsysApi.interface import ElectCourse
from electsysApi.shared.school_id import school_id_map
from electsysApi.shared.exception import ParseError, RequestError


index_url = 'http://i.sjtu.edu.cn/design/viewFunc_cxDesignFuncPageIndex.html?gnmkdm=N219904&layout=default&su='

post_to_url = 'http://i.sjtu.edu.cn/design/funcData_cxFuncDataList.html?func_widget_guid=FUNCWIDGETGUID&gnmkdm=N219904&su='


def conditional_query(s, year, term, name=None, weekday=None, teacher=None, max_limit=30):
    if term == 1:
        term_code = '3'
    elif term == 2:
        term_code = '12'
    elif term == 3:
        term_code = '16'
    else:
        raise TypeError("Invalid term code.")

    if weekday != None:
        if type(weekday) != int:
            raise TypeError("Weekday must be integer.")

        if weekday < 1 or weekday > 7:
            raise TypeError(
                "Weekday must lies in range(1, 8) but not %d." % weekday)

    resp = s.get(index_url + s.student_id)

    if resp.status_code == 200:
        resource = resp.content.decode()
        if not 'data-func_widget_guid="' in resource:
            raise ParseError("Failed to get functional widget GUID.")

        func_widget_guid = resource.split(
            'data-func_widget_guid="')[1].split('"')[0]

    params = {
        'xnm': str(year),
        'xqm': term_code,
        '_search': 'false',
        'nd': s.get_session_id(),
        'queryModel.showCount': max_limit,
        'queryModel.currentPage': '1',
        'queryModel.sortName': '',
        'queryModel.sortOrder': 'asc'
    }

    if name != None:
        # Must quote params before post them.
        params.update({'kch_id': quote(str(name))})

    if teacher != None:
        params.update({'js': quote(str(teacher))})

    if weekday != None:
        params.update({'xqj': str(weekday)})

    post_resp = s.post(post_to_url.replace(
        'FUNCWIDGETGUID', func_widget_guid) + s.student_id, params)

    # print("Going to %s." % (post_to_url.replace(
    # 'FUNCWIDGETGUID', func_widget_guid) + s.student_id))

    # print(params)

    if post_resp.status_code == 200:
        resource = json.loads(post_resp.content.decode())
    else:
        raise RequestError(
            "Failed to post parameters. Status Code: %d" % post_resp.status_code)

    if 'items' in resource:
        data_list = []
        # 如果有数据
        success = 0
        fail = 0
        for item in resource['items']:
            try:
                data_list.append(ElectCourse(**item))
            except ParseError:
                # 抛异常结束
                fail += 1
            else:
                success += 1
        logging.info(
            "Course Parsing complete. %d success, %d fail." % (success, fail))
        return data_list

    raise RequestError("Failed to request course schedule.")
