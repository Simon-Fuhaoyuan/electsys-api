#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /manip/check_selected.py
@time: 2019/1/11
'''

import json
import requests
from lxml import etree
from interface.interface import ElectCourse, CourseDetail
from shared.exception import RequestError, ParseError


elect_url = 'http://i.sjtu.edu.cn/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su='

check_url = 'http://i.sjtu.edu.cn/xsxk/zzxkyzb_cxZzxkYzbChoosedDisplay.html?gnmkdm=N253512&su='

hidden_params = ['xh_id', 'jg_id', 'zyh_id', 'zyfx_id', 'njdm_id',
                 'bh_id', 'xkxnm', 'xkxqm']


def check_selected_course(s):

    # html_object
    # args:
    # keywords: 任意长，检索关键字参数
    # school: 开课院系列表
    # request_left: Boolean, 只接受有余量的课程 = True

    s.update_origin()

    if s.is_ok():
        raw_html = (s.get(elect_url + s.student_id).content.decode())
    else:
        return None

    ele_htm = etree.HTML(raw_html)

    params = {
    }

    for par in hidden_params:

        if par == 'jg_id':
            fix_par = 'jg_id_1'
        else:
            fix_par = par

        try:
            value = ele_htm.xpath('//*[@id="%s"]/@value' % fix_par)[0]
            params[par] = value
            # print("Parsed param %s as %s" % (par, value))
        except IndexError:
            raise ParseError("Failed to parse website element %s." % fix_par)

    resp = s.post(check_url + s.student_id, params)
    if resp.status_code == 200:
        resource = json.loads(resp.content.decode())
        data_list = []
        # 如果有数据
        try:
            for item in resource:
                data_list.append(ElectCourse(**item))
        except ParseError:
            # 抛异常结束
            raise ParseError("Failed to check selected course data.")
        else:
            return data_list
    raise RequestError("Failed to query elect system.")
