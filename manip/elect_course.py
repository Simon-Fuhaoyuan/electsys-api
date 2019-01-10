#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /manip/elect_course.py
@time: 2019/1/6
'''

import requests
from lxml import etree
from shared.exception import ParseError
from interface.interface import ElectCourse, CourseDetail

elect_url = 'http://i.sjtu.edu.cn/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su='

select_url = 'http://i.sjtu.edu.cn/xsxk/zzxkyzb_xkBcZyZzxkYzb.html?gnmkdm=N253512&su='

deselect_url = 'http://i.sjtu.edu.cn/xsxk/zzxkyzb_tuikBcZzxkYzb.html?gnmkdm=N253512&su='

select_hidden_params = ['xkkz_id', 'xkxnm', 'xkxqm',
                        'njdm_id', 'zyh_id', 'kklxdm', 'xklc']

deselect_hidden_params = ['xkxnm', 'xkxqm', 'xklc']

success_flag = '{"flag":"1"}'

success_desel_flag = "1"


def select_course(s, course_piece):

    if type(course_piece) != ElectCourse:
        return False

    s.update_origin()

    if s.is_ok():
        raw_html = (s.get(elect_url + s.student_id).content.decode())
    else:
        return False

    ele_htm = etree.HTML(raw_html)
    params = {
        'jxb_ids': course_piece.jxb_id,
        'kch_id': course_piece.kch_id,
        'kcmc': "(%s)%s - %s 学分" % (course_piece.kch_id, course_piece.kcmc, course_piece.xf),
        'rwlx': '1',
        'rlkz': '0',
        'rlzlkz': '0',
        'sxbj': '0',
        'xxkbj': '0',
        'qz': '0',
    }

    for par in select_hidden_params:

        # 有一项不一致的情况
        if par == 'xkkz_id':
            fix_par = 'firstXkkzId'
        elif par == 'xklc':
            fix_par = 'zkcs'
        else:
            fix_par = par
        try:
            value = ele_htm.xpath('//*[@id="%s"]/@value' % fix_par)[0]
            params[par] = value
        except IndexError:
            raise ParseError("Failed to parse website element %s." % fix_par)

    if (s.post(select_url + s.student_id, params).content.decode()) == success_flag:
        return True
    return False


def deselect_course(s, course_piece):

    if type(course_piece) != ElectCourse:
        return False

    s.update_origin()

    if s.is_ok():
        raw_html = (s.get(elect_url + s.student_id).content.decode())
    else:
        return False

    ele_htm = etree.HTML(raw_html)
    params = {
        'jxb_ids': course_piece.jxb_id,
        'kch_id': course_piece.kch_id,
        'kcmc': '',
        'rwlx': '1',
        'rlkz': '0',
        'txbsfrl': '0'
    }

    for par in deselect_hidden_params:

        # 有一项不一致的情况
        if par == 'xkkz_id':
            fix_par = 'firstXkkzId'
        elif par == 'xklc':
            fix_par = 'zkcs'
        else:
            fix_par = par
        try:
            value = ele_htm.xpath('//*[@id="%s"]/@value' % fix_par)[0]
            params[par] = value
        except IndexError:
            raise ParseError("Failed to parse website element %s." % fix_par)

    if (s.post(deselect_url + s.student_id, params).content.decode()) == success_desel_flag:
        return True
    return False
