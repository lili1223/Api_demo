"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/29 16:29
@Project:py_Api
@Author : RainBow
@File : test02_upload.py
"""
import unittest
import requests

from tools.handle_extract_data import HandleExtractData
from tools.handle_path import *
from ddt import ddt,data
from tools.handle_excel import ReadExcel
from tools.handle_replace import HandleRplace
from tools.handle_request import HandleRequest
from tools.handle_response import HandleResponse

# 从excel中的login页拿到测试数据
cases_list = ReadExcel(file_name=case_data_dir, sheet_name='upload').get_data()
# print(cases_list)
@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.replace = HandleRplace()
        cls.headers = {"locale": "zh_CN"}
        cls.response = HandleResponse()
        cls.extract = HandleExtractData()
        cls.request = HandleRequest()

    @data(*cases_list)
    def test_login(self,case):
        data = self.replace.replace_data(case['data'])
        print('请求参数',data)
        self.request.send_request(method=case["method"],url=case['url'],json=data,headers=self.headers)
        # res = requests.request(method=case["method"],url=case['url'],json=data,headers=self.headers)
        # print('响应结果：',res.text)
        new_response = self.response.handle_response(res)
        print(new_response)
        # 接口断言
        self.response.assert_response(response=new_response,expected_data=case['expected_data'])
        self.extract.extract_data(new_response,case['extract_data'])

if __name__ == '__main__':
    unittest.main()
