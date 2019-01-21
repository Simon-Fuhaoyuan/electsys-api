#!/usr/bin/env python
#
# Abbreviation Interpreter
#
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/utils/interpreter.py
@time: 2019/1/14
'''

abbr_dict = {

    'teacher': '教师',
    'locked': '锁定',
    'outexcel': '输出EXCEL',
    'outpdf': '输出PDF',
    'table': '表格',
    'list': '列表',
    'select': '选择',
    'xn': '学年',
    'xnmmc': '学年',
    'xq': '学期',
    'xqmmc': '学期',
    'njmc': '年级',
    'xymc': '学院',
    'kkbmmc': '开课部门',
    'kkxymc': '管理学院',
    'jgmc': '学院',
    'zymc': '专业',
    'bj': '班级',
    'xh': '学号',
    'xm': '姓名',
    'xb': '性别',
    'kcmc': '课程',
    'jxbmc': '教学班名称',
    'rs': '人数',
    'sksj': '上课时间',
    'jxdd': '上课地点',
    'jxbzc': '教学班组成',
    'kcxx': '课程信息',
    'jxbxx': '教学班信息',
    'xsxx': '学生信息',
    'btn_colse': '关 闭',
    'btn_bccg': '保存草稿',
    'btn_tjsq': '提交申请',
    'needCondition': '请选择筛选条件!',
    'emptyRecord': '没有符合条件记录!',
    'unauthorized': '当前功能您没有按钮操作权限!',
    'atleastone': '请选定一条记录!',
    'cz': '操作',
    'xqmc ': '校区',
    'tklxmc': '调课类型',
    'yylb': '原因类别',
    'tkyy': '调动原因',
    'tksm': '备注说明',
    'ctzt ': '冲突情况',
    'yjsxm': '原教师',
    'ycdmc': '原教室',
    'yzcd': '原周次',
    'yxqj': '原星期',
    'yjc': '原节次',
    'xjsxm': '现教师',
    'xcdmc': '现教室',
    'xzcd': '现周次',
    'xxqj': '现星期',
    'xjc': '现节次 ',
    'kkxy': '开课学院',
    'jsxm': '教师 ',
    'zc': '起始/结束周',
    'zxs': '总学时',
    'rlzt': '状态',
    'lcgz': '流程跟踪',
    'czmc': '操作',
    'szx': '设置项',
    'sqjg': '申请结果',
    'shzt': '审核状态',
    'sqzt': '申请状态',
    'sqtjsj': '申请时间',
}

if __name__ == '__main__':
    abbr_value = input("Input the abbreviation >>> ").lower()
    try:
        print(abbr_dict[abbr_value])
    except KeyError:
        pass
