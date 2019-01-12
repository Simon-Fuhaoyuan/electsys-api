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
import manip
import modules
import shared

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

try:
    print("已选的课程：")
    selected_course = manip.check_selected_course(s)

    print(selected_course)

    input()

    print("搜索关键字 03000 结果：")
    school_pack = shared.holder_school_packer('03000')

    ele_cs = manip.query_course(s, '', school='03000', request_left=True)

    print(ele_cs)
    input()

    # 选完就退 刺激
    print("试图选上：")
    print(ele_cs[0])
    manip.select_course(s, ele_cs[0])
    input()

    # 选完就退 刺激
    print("试图退掉：")
    print(ele_cs[0])
    manip.deselect_course(s, ele_cs[0])
    input()

except shared.RequestError:
    print("大概现在不是选课的时候...")
except shared.ParseError:
    print("解析请求数据出了毛病...")

print("本学期的第一天：")
print(modules.get_start_date(s))


print("2018 年秋季学期的课表：")
print(modules.get_course_list(s, 2018, 1))

input()


print("2017 年春季学期的课表：")
print(modules.get_course_list(s, 2017, 2))

input()

print("2017 年春季学期的考试成绩：")
print(modules.get_score_list(s, 2017, 2))
input()

print("2017 年春季学期的考试安排：")
print(modules.get_exam_list(s, 2017, 2))
input()

# 尝试登出
print("Logout Response: ")
print(log.logout())
