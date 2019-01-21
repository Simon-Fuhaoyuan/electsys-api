#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/login/misc/const.py
@time: 2019/1/4
'''

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Origin': 'https://jaccount.sjtu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15',
    'Accept-Language': 'zh-cn,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}


login_url = 'http://i.sjtu.edu.cn/jaccountlogin'
logout_url = 'http://i.sjtu.edu.cn/xtgl/login_slogin.html'
captcha_url = 'https://jaccount.sjtu.edu.cn/jaccount/captcha'
post_url = 'https://jaccount.sjtu.edu.cn/jaccount/ulogin'

captcha_cache = '__captcha.png'
