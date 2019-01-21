#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/modules/calendar.py
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


def get_start_date(s):

    cont = get_calendar_table(s)

    cal_htm = etree.HTML(cont)

    for mon in cal_htm.xpath('//*[@id="sch-xq"]/table/thead/tr[2]/th[2]'):
        month = int(mon.text.replace('月', ''))

    for day in cal_htm.xpath('//*[@id="sch-xq"]/table/tbody/tr[1]/td[2]'):
        day = int(day.text)

    for title in cal_htm.xpath('//*[@id="sch-xq"]/table/thead/tr[1]/th'):
        year_term = title.text.replace('上海交通大学', '').replace('校历', '')

    if '秋冬' in year_term:
        year = int(year_term.split('-')[0])
    else:
        year = int(year_term.split('-')[0]) + 1

    if month != None and day != None:
        return "%s-%02d-%02d" % (year, month, day)
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
