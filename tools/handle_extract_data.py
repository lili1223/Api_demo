"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/29 16:50
@Project:py_Api
@Author : RainBow
@File : handle_extract_data.py
"""
import json

from tools.handle_attribute import HandleAttr


from jsonpath import jsonpath
class HandleExtractData:
    def __init__(self):
        pass
    def extract_data(self,response:dict,extract_data:str):
        # extract_data = {'access_token','$..access_token'}
        extract_data = extract_data if isinstance(extract_data,dict) else json.loads(extract_data)
        for k,v in extract_data.items():
            # 将token提取出来
            value = jsonpath(response,v)[0]
            # 设置为类属性
            setattr(HandleAttr,k,value)
        else:
            print('字段为空不需要提取')

