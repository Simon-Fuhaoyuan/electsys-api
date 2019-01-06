#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /shared/session.py
@time: 2019/1/4
'''

import requests


class Session:

    # Main Page URL
    url = ""

    # 学号，需要此信息才能访问各子页面
    student_id = ""

    # requests.session 实例
    __session = None

    def __init__(self, url, suid, session):
        self.url = url
        self.student_id = suid
        self.__session = session

    def get(self, url, params=None, allow_redirects=True):
        return self.__session.get(url, params=params, allow_redirects=allow_redirects)

    def post(self, url, params=None, allow_redirects=True):
        return self.__session.post(url, params=params, allow_redirects=allow_redirects)

    def is_ok(self):
        return self.url != "" and self.student_id != "" and self.__session != None

    def get_session_id(self):
        return self.url.split('_t=')[1]

    def update_origin(self):
        self.__session.headers['Origin'] = 'http://i.sjtu.edu.cn'

    def print_headers(self):
        print(self.__session.headers)
