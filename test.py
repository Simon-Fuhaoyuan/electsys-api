#!/usr/bin/env python
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


log = login.Login()

username = input("jAccount ID: >>> ")
password = input("jAccount Password: >>> ")

log.get_captcha(display=True, on_screen=True)
captcha = input("Input Captcha: >>> ")


print("Login Response: ")
print(log.attempt(username, password, captcha).url)

# 等会儿，喘口气
input()

print("Logout Response: ")
print(log.logout())
