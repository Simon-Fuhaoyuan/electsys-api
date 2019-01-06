#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /manip/query_course.py
@time: 2019/1/6
'''

import json
import requests
from lxml import etree


query_url = 'http://i.sjtu.edu.cn/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su='

post_url = 'http://i.sjtu.edu.cn/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512&su='

hidden_params = ['xh_id', 'xqh_id', 'jg_id', 'zyh_id', 'zyfx_id', 'njdm_id',
                 'bh_id', 'xbm', 'xslbdm', 'ccdm', 'xsbj', 'xkxnm', 'xkxqm']


def query_course(s, *keywords, **args):

    # html_object
    # args:
    # keywords: 任意长，检索关键字参数
    # school: 开课院系列表
    # request_left: Boolean, 只接受有余量的课程 = True

    s.update_origin()

    if s.is_ok():
        raw_html = (s.get(query_url + s.student_id).content.decode())

    else:
        return None

    input(raw_html)
    ele_htm = etree.HTML(raw_html)

    params = {
        'rwlx': '1',
        'xkly': '0',
        'bklx_id': '0',
        'sfkknj': '0',
        'sfkkzy': '0',
        'sfznkx': '0',
        'zdkxms': '0',
        'sfkxq': '1',
        'sfkcfx': '0',
        'kkbk': '0',
        'kklxdm': '0',
        'sfkgbcx': '1',
        'sfrxtgkcxd': '0',
        'tykczgxdcs': '0',
        'rlkz': '0',
        'kspage': '1',
        'jspage': '10'
    }

    for par in hidden_params:

        # 有一项不一致的情况
        if par == 'jg_id':
            fix_par = 'jg_id_1'
        else:
            fix_par = par

        value = ele_htm.xpath('//*[@id="%s"]/@value' % fix_par)[0]
        params[par] = value
        print("Parsed param %s as %s" % (par, value))

    xkkz_id = ele_htm.xpath('//*[@id="firstXkkzId"]/@value')[0]

    if 'request_left' in args:
        if args['request_left']:
            params['yl_list[0]'] = 1

    count = 0
    for kw in keywords:
        params["filter_list[%d]" % count] = str(kw)
        count += 1

    if 'school' in args:
        count = 0
        for school in args['school']:
            params["kkbm_id_list[%d]" % count] = school
            count += 1

    print(params)
    print(post_url + s.student_id)
    s.print_headers()
    print(s.post(post_url + s.student_id, params).content.decode())
