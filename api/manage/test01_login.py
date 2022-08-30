"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/15 20:34
@Project:py_Api
@Author : RainBow
@File : test01_login.py
"""
import time

"""
#  登录接口
url_logi = 'http://mall.lemonban.com:8107/login'
headers = {"Content-Type": "application/json; charset=UTF-8"}
data = {"principal":"18820992515","credentials":"123456","appType":3,"loginType":"0"}
"""
import requests
import uuid
import jsonpath
from test02_image import ImageCode
class Login:
    def __init__(self):
        self.url_logi = 'http://mall.lemonban.com:8108/adminLogin'
        self.headers = {"locale": "zh_CN"}
    def login(self):
        my_uuid = str(uuid.uuid4())
        imageCode = ImageCode().get_code_image(my_uuid)
        data = {
            "t": int(time.time()*1000),
             "principal": "student",
             "credentials": "123456a",
             "sessionUUID": my_uuid,  # 会话uuid不能重复每次都是唯一的
             # "imageCode": imageCode   # 万能验证码，一般情况下最好通过万能验证码去解决，通过第三方平台图片识别平台去处理
            "imageCode": "lemon"
        }
        resp = requests.post(url=self.url_logi, json=data)
        # print(resp.json())
        token = jsonpath.jsonpath(resp.json(), '$..access_token')[0]
        self.headers['Authorization'] = f"bearer{token}"
        # print(resp.json())
        return self.headers


if __name__ == '__main__':
    cl = Login()
    print(cl.login())




