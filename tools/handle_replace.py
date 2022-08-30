"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/19 21:26
@Project:py_Api
@Author : RainBow
@File : handle_replace.py
"""

import json
import requests
import re
import time
import uuid
import json
from tools.handle_path import *
from tools.handle_attribute import HandleAttr
from uuid import uuid4
from tools.handle_excel import ReadExcel
class HandleRplace:
    def replace_data(self, data: str):
        """
        1、获取需要替换的数据
        2、遍历需要提替换的数据，根据对应的数据生成对应的值
        :param data:
        :return:
        """
        if data:
            key_list = re.findall("#(\w.+?)#", data)
            if len(key_list) > 0:
                for key in key_list:
                    if key == 'time':
                        times = str(int(time.time() * 1000))
                        setattr(HandleAttr, key, times)
                    elif key == 'sessionUUID':
                        UUID = str(uuid4())
                        setattr(HandleAttr, key, UUID)
                for key in key_list:
                    data = data.replace(f"#{key}#", getattr(HandleAttr, key))
                data = json.loads(data)
                return data
            else:
                print('不需要替换请求参数，直接返回json数据')
                data = json.loads(data)
                return data
        else:
            print('参数为空，不需要替换参数')
            return {}

if __name__ == '__main__':
    cases_list = ReadExcel(file_name=case_data_dir, sheet_name='login').get_data()
    for case in cases_list:
        cl = HandleRplace()
        data = cl.replace_data(case['data'])
        print(type(data),data)
        headers = {"locale": "zh_CN"}
        res = requests.request(method=case["method"],url=case['url'],json=data,headers=headers)
        print(res.text)


