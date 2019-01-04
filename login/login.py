#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /login/login.py
@time: 2019/1/4
'''

import os
import re
import json
import urllib
import argparse
import requests

from PIL import Image
from lxml import etree
from .misc.const import headers, login_url, logout_url, captcha_url, post_url, captcha_cache
from shared.session import *


class Login:

    __req = None

    __sid = ""
    __client = ""
    __returl = ""
    __se = ""

    def __init__(self):
        self.__req = requests.session()
        self.__req.headers.update(headers)

        jump_url = self.__req.get(login_url).url
        unquoted_jump_url = urllib.parse.unquote(str(jump_url))

        _, self.__sid, self.__client, self.__returl, self.__se = re.split(
            r"sid=|&client=|&returl=|&se=", unquoted_jump_url)

    def __del__(self):
        self.logout()

    def attempt(self, username, password, captcha):

        post_params = {
            'sid': self.__sid,
            'returl': self.__returl,
            'se': self.__se,
            # 'v': "",
            'client': self.__client,
            'user': username,
            'pass': password,
            'captcha': captcha
        }

        resp = self.__req.post(
            post_url, data=post_params)

        # 如果最后有个 err=1 就是报错了
        if '&err=1' in resp.url:
            # Error Sign
            return None

        html = etree.HTML(resp.content.decode())

        student_id = html.xpath('//*[@id="sessionUserKey"]/@value')

        # fin_resp = self.__req.get(resp.url)
        return Session(resp.url, str(student_id), self.__req), resp

    def logout(self):
        return self.__req.get(logout_url)

    def get_captcha(self, display=False, on_screen=False):
        cap_img = self.__req.get(captcha_url).content
        with open(captcha_cache, 'wb') as f:
            f.write(cap_img)
        if display:
            img = Image.open(captcha_cache)
            if on_screen:
                draw_captcha(img)
            else:
                img.show()


def get_proper_image_width():
    ratio = 0.3
    width = os.get_terminal_size().columns
    return (width, int(width * ratio))


def draw_captcha(img):
    resize_limit = get_proper_image_width()
    img = img.resize(resize_limit)

    # 礼貌性给一个 padding，打一个空行
    print()
    for i in range(resize_limit[1]):
        line_str = ""
        for j in range(resize_limit[0]):
            pixel_color = img.getpixel((j, i))
            # 计算 RGB 色值，全白理论上等于 765， 这里以 600 为阈值
            if pixel_color[0] + pixel_color[1] + pixel_color[2] > 600:
                # 输出一块白色
                line_str += ' '
            else:
                line_str += '*'
        if len(line_str.replace(' ', '')) != 0:
            # 空行不给打
            print(line_str)
    # 礼貌性给一个 padding，打一个空行
    print()
