"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/29 14:26
@Project:py_Api
@Author : RainBow
@File : handle_response.py
"""
import json
from unittest import TestCase
import jsonpath


class HandleResponse:
    def __init__(self):
        self.my_assert = TestCase()
    # 相应结果的处理
    def handle_response(self,response):
        """
        1、参数接收相应结果
        2、根据数据类型判断是否需要二次封装
        :return:
        """
        try:
            if isinstance(response.json(), dict):
                return {"response": response.json()}
        except Exception as e:
            # 执行报错了，response.text，需要二次封装
            return {"response": response.text}

    def assert_response(self,response,expected_data):
        # new_response = self.__handle_response(response=response)
        # 期望结果=={"token_type":"bearer"}
        # 实际结果==接口执行的结果
        # 1、从excel读取期望结果
        # 2、遍历期望结果的key，通过key从相应结果中提取对应的key
        # 3、断言期望结果和实际结果
        if expected_data:
            actual_data = {}
            expected_data = expected_data if isinstance(expected_data, dict) else json.loads(expected_data)
            for key in expected_data:
                actual_data[key] = jsonpath.jsonpath(response, f"$..{key}")[0]
            self.my_assert.assertEqual(expected_data, actual_data)


