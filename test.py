#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: /test.py
@time: 2019/1/4
'''

import login
import modules

log = login.Login()

username = input("jAccount ID: >>> ")
password = input("jAccount Password: >>> ")

log.get_captcha(display=True, on_screen=True)
captcha = input("Input Captcha: >>> ")


print("Login Response: ")
s = log.attempt(username, password, captcha)

if s == None:
    print("服务器提了一个问题")
    exit(1)

# s 要不是 None，就是我们的内容 Session 了

# 等会儿，喘口气
# input()

print("本学期的第一天：(月, 日)")
print(modules.get_start_day(s))

print("2018 年秋季学期的课表：")
print(modules.get_course_json(s, 2018, 1))


print("2017 年春季学期的课表：")
print(modules.get_course_json(s, 2017, 2))

print("2017 年春季学期的考试成绩：")
print(modules.get_score_json(s, 2017, 2))
input()

print("2017 年春季学期的考试安排：")
print(modules.get_exam_json(s, 2017, 2))
input()

# 尝试登出
print("Logout Response: ")
print(log.logout())
