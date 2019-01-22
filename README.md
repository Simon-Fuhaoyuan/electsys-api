# electsys-api
上海交通大学新版教学信息服务网 API。


![](https://img.shields.io/badge/python-3.x-blue.svg)
[![](https://img.shields.io/pypi/v/electsysApi.svg)](https://pypi.org/project/electsysApi/)
![](https://travis-ci.org/yuxiqian/electsys-api.svg?branch=master)
[![](https://img.shields.io/github/last-commit/google/skia.svg)](https://github.com/yuxiqian/electsys-api/)


<div align=center>
    <img src="https://raw.githubusercontent.com/yuxiqian/electsys-api/master/screenshots/login_captcha.png"/>
</div>

> jAccount 登录接口


# 安装

``` shell
pip[3] install electsysApi
```

# 功能
 - [x] `jAccount` 登录
 - [x] 查询校历
 - [x] 查询课程表
 - [x] 查询考试安排
 - [x] 查询考试成绩
 
 > 以下操作仅开放选课时段可用
 - [x] 模糊／精确搜索课程库
 - [x] 查询已选课程
 - [x] 选课
 - [x] 退课

# 文档
* [Wiki Home](https://github.com/yuxiqian/electsys-api/wiki)

| 类目 | 链接 |
| ------ | ------ |
| 模块 | [![](https://img.shields.io/badge/模块-登录-1265FF.svg)](https://github.com/yuxiqian/electsys-api/wiki/login-模块) [![](https://img.shields.io/badge/模块-会话-2F4B7F.svg)](https://github.com/yuxiqian/electsys-api/wiki/session-模块) [![](https://img.shields.io/badge/模块-功能-0E51CC.svg)](https://github.com/yuxiqian/electsys-api/wiki/功能模块)|
| 操作 | [![](https://img.shields.io/badge/操作-查询已选-E889B4.svg)](https://github.com/yuxiqian/electsys-api/wiki/CheckSelected-方法) [![](https://img.shields.io/badge/操作-检索可选-F075FF.svg)](https://github.com/yuxiqian/electsys-api/wiki/QueryCourse-方法) [![](https://img.shields.io/badge/操作-选课-A05FE8.svg)](https://github.com/yuxiqian/electsys-api/wiki/SelectCourse-方法) [![](https://img.shields.io/badge/操作-退课-918AFF.svg)](https://github.com/yuxiqian/electsys-api/wiki/DeselectCourse-方法)|
| 结构 | [![](https://img.shields.io/badge/结构-课程表-FF724C.svg)](https://github.com/yuxiqian/electsys-api/wiki/PersonalCourse-结构) [![](https://img.shields.io/badge/结构-考试安排-FF3600.svg)](https://github.com/yuxiqian/electsys-api/wiki/PersonalExam-结构) [![](https://img.shields.io/badge/结构-待选课程-CC2B00.svg)](https://github.com/yuxiqian/electsys-api/wiki/ElectCourse-结构)  [![](https://img.shields.io/badge/结构-考试成绩-7F3926.svg)](https://github.com/yuxiqian/electsys-api/wiki/PersonalScore-结构) |


# 测试

``` shell
python[3] unit_test.py
```

# 致谢

* [SJTU NIC](https://net.sjtu.edu.cn)

* [lxml](https://github.com/lxml/lxml), under the BSD License

* [requests](https://github.com/requests/requests), under the Apache License

* [Shields](https://github.com/badges/shields/), under the CC0 1.0 Universal License

* [Pillow](https://github.com/python-pillow/Pillow), under the open source PIL Software License

# 协议

[MIT License](https://github.com/yuxiqian/electsys-api/blob/master/LICENSE)
