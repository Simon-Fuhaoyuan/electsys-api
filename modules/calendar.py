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

from lxml import etree
import requests

calendar_url = 'http://i.sjtu.edu.cn/xtgl/index_cxshjdAreaFive.html?localeKey=zh_CN&gnmkdm=index&su='


def get_calendar_table(s):
    if s.is_ok():
        url = calendar_url + s.student_id
        cont = (s.get(url).content.decode())
        return cont

    return None


def get_start_day(s):

    cont = get_calendar_table(s)

    cal_htm = etree.HTML(cont)
    # input(cont)

    for mon in cal_htm.xpath('//*[@id="sch-xq"]/table/thead/tr[2]/th[2]'):
        month = int(mon.text.replace('月', ''))

    for day in cal_htm.xpath('//*[@id="sch-xq"]/table/tbody/tr[1]/td[2]'):
        day = int(day.text)

    if month != None and day != None:
        return month, day
    return None, None
