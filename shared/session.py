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


class RequestError(BaseException):
    pass


class Session:

    # Main Page URL
    url = ""

    # 学号，需要此信息才能访问各子页面
    student_id = ""

    # 上次请求的返回代码
    __last_response_code = 0

    # requests.session 实例
    __session = None

    def __init__(self, url, suid, session):
        self.url = url
        self.student_id = suid
        self.__session = session

    def get(self, url, params=None, allow_redirects=True):
        try:
            resp = self.__session.get(
                url, params=params, allow_redirects=allow_redirects)
            self.__last_response_code = resp.status_code
            return resp
        except:
            raise RequestError("Failed to perform GET request to %s." % url)

    def post(self, url, params=None, allow_redirects=True):
        try:
            resp = self.__session.post(
                url, params=params, allow_redirects=allow_redirects)
            self.__last_response_code = resp.status_code
            return resp
        except:
            raise RequestError("Failed to perform POST request to %s." % url)

    def is_ok(self):
        return self.url != "" and self.student_id != "" and self.__session != None

    def get_session_id(self):
        return self.url.split('_t=')[1]

    def update_origin(self):
        self.__session.headers['Origin'] = 'http://i.sjtu.edu.cn'

    def last_status(self):
        if self.__last_response_code != 0:
            return self.__last_response_code
        return None
