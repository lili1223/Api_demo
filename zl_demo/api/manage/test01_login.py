"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/21 12:01
@Project:py_Api
@Author : RainBow
@File : test01_login.py
"""
import jsonpath

"""
Request URL: http://mall.lemonban.com:8108/adminLogin
Request Method: POST
Status Code: 200 
Content-Type: application/json; charset=UTF-8
"""
import requests
import time
import jsonpath
import uuid
from zl_demo.api.manage.test02_image import ImageCode

class Login:
    def __init__(self):
        self.login_url = 'http://mall.lemonban.com:8108/adminLogin'
        self.headers = {'locale': 'zh_CN','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    def login(self):
        my_uuid = str(uuid.uuid4())
        image_code = ImageCode().get_image_code(uuid=my_uuid)
        data = {
                  "t": int(time.time()*1000),
                  "principal": "student",
                  "credentials": "123456a",
                  "sessionUUID": my_uuid,
                  # "imageCode": "lemon"
                  "imageCode": image_code
                }
        resp = requests.post(url=self.login_url, json=data)
        print(resp.json())
        token = jsonpath.jsonpath(resp.json(),'$..access_token')
        self.headers['Authorization']=f"bearer{token}"
        return self.headers

if __name__ == '__main__':
    print(Login().login())

