#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: electsysApi/shared/school_id.py
@time: 2019/1/6
'''


school_id_map = {"01000": '船舶海洋与建筑工程学院',
                 "02000": '机械与动力工程学院',
                 "03000": '电子信息与电气工程学院',
                 "03600": '信息安全工程学院',
                 "03700": '软件学院',
                 "04000": '电力学院（原）',
                 "05000": '材料科学与工程学院',
                 "06000": '机械工程学院（原）',
                 "07000": '理学院',
                 "07100": '数学系',
                 "07200": '物理系',
                 "08000": '生命科学技术学院',
                 "08200": '生物医学工程学院',
                 "09000": '人文学院',
                 "09600": '科学史与科学文化研究院',
                 "10000": '建筑工程与力学学院(原)',
                 "11000": '化学化工学院',
                 "12000": '安泰经济与管理学院',
                 "13000": '国际与公共事务学院',
                 "14000": '外国语学院',
                 "15000": '农业与生物学院',
                 "16000": '环境科学与工程学院',
                 "17000": '药学院',
                 "18000": '医学院（并校前）',
                 "19000": '凯原法学院',
                 "20000": '媒体与设计学院',
                 "21000": '微电子学院',
                 "22000": '继续教育学院',
                 "23000": '马克思主义学院',
                 "24000": '致远学院',
                 "25100": '体育系',
                 "26000": '巴黎高科卓越工程师学院',
                 "29000": '塑性成形系（原）',
                 "29100": '塑性成形技术与装备研究院',
                 "30000": '医学院(原二医大)',
                 "31000": '技术学院',
                 "32000": '成人教育部',
                 "33000": '图书馆',
                 "34000": '微纳米科学技术研究院',
                 "35000": '高等教育研究院',
                 "36000": '国际教育学院',
                 "37000": '密西根学院',
                 "38000": '上海高级金融学院',
                 "39000": '创业学院',
                 "40000": '上海中医药大学',
                 "40001": '华东师范大学',
                 "41000": '工程训练中心',
                 "41300": '航空航天学院',
                 "50400": '党委宣传部',
                 "50500": '学指委、团委(含学生处、人武部)',
                 "50501": '军事教研室',
                 "60200": '教务处',
                 "70000": '医学院'
                 }

school_map = [{'jg_id': '01000', 'jgmc': '船舶海洋与建筑工程学院', 'jgywmc': 'School of Naval Architecture Ocean and Civil Engineering'}, {'jg_id': '02000', 'jgmc': '机械与动力工程学院', 'jgywmc': 'School of Mechanical Engineering'}, {'jg_id': '03000', 'jgmc': '电子信息与电气工程学院', 'jgywmc': 'School of Electronic Information and Electrical Engineering'}, {'jg_id': '21000', 'jgmc': '微电子学院', 'jgywmc': 'School of Microelectronics'}, {'jg_id': '05000', 'jgmc': '材料科学与工程学院', 'jgywmc': 'School of Materials Science & Engineering'}, {'jg_id': '07100', 'jgmc': '数学科学学院', 'jgywmc': 'School of Mathematical Sciences'}, {'jg_id': '07200', 'jgmc': '物理与天文学院', 'jgywmc': 'School of Physics and Astronomy'}, {'jg_id': '08000', 'jgmc': '生命科学技术学院', 'jgywmc': 'School of Life Science & Biotechnology'}, {'jg_id': '08200', 'jgmc': '生物医学工程学院', 'jgywmc': 'School of Biomedical Engineering'}, {'jg_id': '09000', 'jgmc': '人文学院', 'jgywmc': 'School of Humanity'}, {'jg_id': '36000', 'jgmc': '国际教育学院', 'jgywmc': 'School of International Education'}, {'jg_id': '11000', 'jgmc': '化学化工学院', 'jgywmc': 'School of Chemistry & Chemical Engineering'}, {'jg_id': '12000', 'jgmc': '安泰经济与管理学院', 'jgywmc': 'Antai College of Economics and Management'}, {'jg_id': '13000', 'jgmc': '国际与公共事务学院', 'jgywmc': 'School of International and Public Affairs'}, {'jg_id': '14000', 'jgmc': '外国语学院', 'jgywmc': 'School of Foreign Languages'}, {'jg_id': '15000', 'jgmc': '农业与生物学院', 'jgywmc': 'School of Agriculture and Biology'}, {'jg_id': '16000', 'jgmc': '环境科学与工程学院', 'jgywmc': 'School of Environmental Science and Engineering'}, {'jg_id': '17000', 'jgmc': '药学院', 'jgywmc': 'School of Pharmacy'}, {'jg_id': '19000', 'jgmc': '凯原法学院', 'jgywmc': 'School of Law'}, {'jg_id': '20000', 'jgmc': '媒体与传播学院', 'jgywmc': 'School of Media and Design'}, {'jg_id': '01000', 'jgmc': '船舶海洋与建筑工程学院', 'jgywmc': 'School of Naval Architecture Ocean and Civil Engineering'}, {'jg_id': '02000', 'jgmc': '机械与动力工程学院', 'jgywmc': 'School of Mechanical Engineering'}, {'jg_id': '03000', 'jgmc': '电子信息与电气工程学院', 'jgywmc': 'School of Electronic Information and Electrical Engineering'}, {'jg_id': '21000', 'jgmc': '微电子学院', 'jgywmc': 'School of Microelectronics'}, {'jg_id': '05000', 'jgmc': '材料科学与工程学院', 'jgywmc': 'School of Materials Science & Engineering'}, {'jg_id': '07100', 'jgmc': '数学科学学院', 'jgywmc': 'School of Mathematical Sciences'}, {'jg_id': '07200', 'jgmc': '物理与天文学院', 'jgywmc': 'School of Physics and Astronomy'}, {'jg_id': '08000', 'jgmc': '生命科学技术学院', 'jgywmc': 'School of Life Science & Biotechnology'}, {'jg_id': '08200', 'jgmc': '生物医学工程学院', 'jgywmc': 'School of Biomedical Engineering'}, {'jg_id': '09000', 'jgmc': '人文学院', 'jgywmc': 'School of Humanity'}, {'jg_id': '36000', 'jgmc': '国际教育学院', 'jgywmc': 'School of International Education'}, {'jg_id': '11000', 'jgmc': '化学化工学院', 'jgywmc': 'School of Chemistry & Chemical Engineering'}, {'jg_id': '12000', 'jgmc': '安泰经济与管理学院', 'jgywmc': 'Antai College of Economics and Management'}, {'jg_id': '13000', 'jgmc': '国际与公共事务学院', 'jgywmc': 'School of International and Public Affairs'}, {'jg_id': '14000', 'jgmc': '外国语学院', 'jgywmc': 'School of Foreign Languages'}, {'jg_id': '15000', 'jgmc': '农业与生物学院', 'jgywmc': 'School of Agriculture and Biology'}, {'jg_id': '16000', 'jgmc': '环境科学与工程学院', 'jgywmc': 'School of Environmental Science and Engineering'}, {'jg_id': '17000', 'jgmc': '药学院', 'jgywmc': 'School of Pharmacy'}, {'jg_id': '19000', 'jgmc': '凯原法学院', 'jgywmc': 'School of Law'}, {'jg_id': '20000', 'jgmc': '媒体与传播学院', 'jgywmc': 'School of Media and Design'}, {'jg_id': '01000', 'jgmc': '船舶海洋与建筑工程学院', 'jgywmc': 'School of Naval Architecture Ocean and Civil Engineering'}, {'jg_id': '02000', 'jgmc': '机械与动力工程学院', 'jgywmc': 'School of Mechanical Engineering'}, {'jg_id': '03000', 'jgmc': '电子信息与电气工程学院', 'jgywmc': 'School of Electronic Information and Electrical Engineering'}, {'jg_id': '21000', 'jgmc': '微电子学院', 'jgywmc': 'School of Microelectronics'}, {'jg_id': '05000', 'jgmc': '材料科学与工程学院', 'jgywmc': 'School of Materials Science & Engineering'}, {'jg_id': '07100', 'jgmc': '数学科学学院', 'jgywmc': 'School of Mathematical Sciences'}, {'jg_id': '07200', 'jgmc': '物理与天文学院', 'jgywmc': 'School of Physics and Astronomy'}, {'jg_id': '08000', 'jgmc': '生命科学技术学院', 'jgywmc': 'School of Life Science & Biotechnology'}, {'jg_id': '08200', 'jgmc': '生物医学工程学院', 'jgywmc': 'School of Biomedical Engineering'}, {'jg_id': '09000', 'jgmc': '人文学院', 'jgywmc': 'School of Humanity'}, {'jg_id': '36000', 'jgmc': '国际教育学院', 'jgywmc': 'School of International Education'}, {'jg_id': '11000', 'jgmc': '化学化工学院', 'jgywmc': 'School of Chemistry & Chemical Engineering'}, {'jg_id': '12000', 'jgmc': '安泰经济与管理学院', 'jgywmc': 'Antai College of Economics and Management'}, {'jg_id': '13000', 'jgmc': '国际与公共事务学院', 'jgywmc': 'School of International and Public Affairs'}, {'jg_id': '14000', 'jgmc': '外国语学院', 'jgywmc': 'School of Foreign Languages'}, {'jg_id': '15000', 'jgmc': '农业与生物学院', 'jgywmc': 'School of Agriculture and Biology'}, {'jg_id': '16000', 'jgmc': '环境科学与工程学院', 'jgywmc': 'School of Environmental Science and Engineering'}, {'jg_id': '17000', 'jgmc': '药学院', 'jgywmc': 'School of Pharmacy'}, {'jg_id': '19000', 'jgmc': '凯原法学院', 'jgywmc': 'School of Law'}, {'jg_id': '20000', 'jgmc': '媒体与传播学院', 'jgywmc': 'School of Media and Design'}, {'jg_id': '01000', 'jgmc': '船舶海洋与建筑工程学院', 'jgywmc': 'School of Naval Architecture Ocean and Civil Engineering'}, {'jg_id': '02000', 'jgmc': '机械与动力工程学院', 'jgywmc': 'School of Mechanical Engineering'}, {'jg_id': '03000', 'jgmc': '电子信息与电气工程学院', 'jgywmc': 'School of Electronic Information and Electrical Engineering'}, {'jg_id': '21000', 'jgmc': '微电子学院', 'jgywmc': 'School of Microelectronics'}, {'jg_id': '05000', 'jgmc': '材料科学与工程学院', 'jgywmc': 'School of Materials Science & Engineering'}, {'jg_id': '07100', 'jgmc': '数学科学学院', 'jgywmc': 'School of Mathematical Sciences'}, {'jg_id': '07200', 'jgmc': '物理与天文学院', 'jgywmc': 'School of Physics and Astronomy'}, {'jg_id': '08000', 'jgmc': '生命科学技术学院', 'jgywmc': 'School of Life Science & Biotechnology'}, {'jg_id': '08200', 'jgmc': '生物医学工程学院', 'jgywmc': 'School of Biomedical Engineering'}, {'jg_id': '09000', 'jgmc': '人文学院', 'jgywmc': 'School of Humanity'}, {'jg_id': '36000', 'jgmc': '国际教育学院', 'jgywmc': 'School of International Education'}, {'jg_id': '11000', 'jgmc': '化学化工学院', 'jgywmc': 'School of Chemistry & Chemical Engineering'}, {'jg_id': '12000', 'jgmc': '安泰经济与管理学院', 'jgywmc': 'Antai College of Economics and Management'}, {'jg_id': '13000', 'jgmc': '国际与公共事务学院', 'jgywmc': 'School of International and Public Affairs'}, {'jg_id': '14000', 'jgmc': '外国语学院', 'jgywmc': 'School of Foreign Languages'}, {'jg_id': '15000', 'jgmc': '农业与生物学院', 'jgywmc': 'School of Agriculture and Biology'}, {'jg_id': '16000', 'jgmc': '环境科学与工程学院', 'jgywmc': 'School of Environmental Science and Engineering'}, {'jg_id': '17000', 'jgmc': '药学院', 'jgywmc': 'School of Pharmacy'}, {'jg_id': '19000', 'jgmc': '凯原法学院', 'jgywmc': 'School of Law'}, {'jg_id': '20000', 'jgmc': '媒体与传播学院', 'jgywmc': 'School of Media and Design'}, {'jg_id': '22000', 'jgmc': '继续教育学院'}, {'jg_id': '23000', 'jgmc': '马克思主义学院'}, {'jg_id': '24000', 'jgmc': '致远学院', 'jgywmc': 'Zhiyuan College'}, {'jg_id': '25100', 'jgmc': '体育系'}, {'jg_id': '26000', 'jgmc': '巴黎高科卓越工程师学院', 'jgywmc': 'ParisTech Elite Institute of Technology'}, {'jg_id': '37000', 'jgmc': '密西根学院', 'jgywmc': 'UM-SJTU Joint Institute'}, {'jg_id': '40001', 'jgmc': '华东师范大学'}, {'jg_id': '41300', 'jgmc': '航空航天学院', 'jgywmc': 'School of Aeronautics and Astronautics'}, {'jg_id': '43000', 'jgmc': '设计学院', 'jgywmc': 'School of Design'}, {'jg_id': '50501', 'jgmc': '军事教研室'}, {'jg_id': '60200', 'jgmc': '教务处', 'jgywmc': 'Academic Affairs Division'}, {'jg_id': '70000', 'jgmc': '医学院', 'jgywmc': 'Medical School'}]

def holder_school_packer(*schools):
    packs = set()
    for sc_n in schools:
        if sc_n.isdigit():
            if school_id_map[sc_n] != None:
                packs.add(sc_n)
        else:
            for key, value in school_id_map.items():
                if sc_n in value:
                    packs.add(key)
                    break
    return packs
