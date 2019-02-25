#!/usr/bin/env python
# encoding: utf-8
'''
@author: yuxiqian
@license: MIT
@contact: akaza_akari@sjtu.edu.cn
@software: electsys-api
@file: setup.py
@time: 2019/1/21
'''

from setuptools import setup, find_packages

setup(
    name='electsysApi',
    version='0.0.7',
    description=(
        'Next generation of SJTU elect system API.'
    ),
    long_description=open('README.rst').read(),
    python_requires='>=3.4',
    author='yuxiqian',
    author_email='akaza_akari@sjtu.edu.cn',
    maintainer='yuxiqian',
    maintainer_email='akaza_akari@sjtu.edu.cn',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/yuxiqian/electsys-api',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'requests~=2.20',
        'lxml~=4.2',
        'Pillow~=5.4'
    ]
)
