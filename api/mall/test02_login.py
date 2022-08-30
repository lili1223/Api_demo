"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/19 20:02
@Project:py_Api
@Author : RainBow
@File : test02_login.py
"""
import jsonpath

"""
Request URL: http://mall.lemonban.com:8107/login
Request Method: POST
Status Code: 200 

{"principal":"18820992515","credentials":"123456","appType":3,"loginType":0}
"""
from api.mall.data import Data
import requests
from api.mall.test01_register import Register
class Login:
    def __init__(self):
        self.url = 'http://mall.lemonban.com:8107/login'
        self.headers = {"locale": "zh_CN"}
        # self.register = Register().statr()
    def login(self):
        data = {
                    # "principal": getattr(Data,'phone'), #账号
                    "principal": "18820992515", #账号
                    "credentials": "123456", # 密码
                    "appType": 3,  #1小程序，2 微信公众号，3 pc登陆，4 h5登陆，5安卓登陆，6 ios登陆
                    "loginType": 0  #0用户名或手机，1短信验证码
                }
        resp = requests.post(url=self.url, json=data)
        access_token = jsonpath.jsonpath(resp.json(),'$..access_token')[0]
        self.headers['Authorization']=f"bearer{access_token}"
        return self.headers
if __name__ == '__main__':
    print(Login().login())

