# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: test.py
@time: 2019/1/4
'''

import login

username = input("jAccount ID: >>> ")
password = input("jAccount Password: >>> ")

login.get_captcha(display=True, on_screen=True)
captcha = input("Input Captcha: >>> ")


log = login.Login()
print(log.attempt(username, password, captcha))

# 等会儿，喘口气
input()
print(log.logout())
