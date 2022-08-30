"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/19 20:54
@Project:py_Api
@Author : RainBow
@File : handle_path.py
"""
import os

# 项目根路径
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据的路径
case_data_dir = os.path.join(base_path,'test_datas','case_data.xlsx')
# print(case_data_dir)

# 测试用例路径
case_dir = os.path.join(base_path,'test_cases')
# 日志路径


