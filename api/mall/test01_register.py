"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/19 20:02
@Project:py_Api
@Author : RainBow
@File : test_login.py
"""
"""
发送验证码
Request URL: http://mall.lemonban.com:8107/user/sendRegisterSms
Request Method: PUT
Status Code: 200 

{"mobile":"13099999999"}

校验验证吗

Request URL: http://mall.lemonban.com:8107/user/checkRegisterSms
Request Method: OPTIONS
Status Code: 200 

{"mobile":"13099999999","validCode":"123456"}

注册
数据库
IP地址：47.113.180.81
账号：lemon
端口：3306
密码：lemon123
数据库：yami_shops
"""
from api.mall.data import Data
import requests
from faker import Faker
import pymysql
class Register:
    def __init__(self):
        self.send_msg_url = 'http://mall.lemonban.com:8107/user/sendRegisterSms'
        self.check_msg_url = 'http://mall.lemonban.com:8107/user/checkRegisterSms'
        self.register_url = "http://mall.lemonban.com:8107/user/registerOrBindUser"
        self.fk = Faker(locale='zh_cn')
        self.phone = self.fk.phone_number()
        self.db = pymysql.connect(
                                    user='lemon',
                                    password="lemon123",
                                    host='47.113.180.81',
                                    database='yami_shops',
                                    port=3306,
                                    autocommit=True
                                    )
        self.cur = self.db.cursor()
    # 获取手机号-校验手机号是否注册
    def get_phone(self):
        while True:
            phone = self.fk.phone_number()
            print('手机号:', phone)
            # sql = f"SELECT COUNT(*) FROM `tz_user` WHERE user_mobile={phone}"
            sql = f"SELECT COUNT(*) FROM `tz_user` WHERE user_mobile={phone}"
            self.cur.execute(sql)
            result = self.cur.fetchall()
            if result[0][0] > 0:
                continue
            else:
                setattr(self,'phone',phone)
                setattr(Data,'phone',phone)
                # print(Data.__dict__)
                break
    # 发送短信验证码
    def send_msg(self):
        data = {"mobile": getattr(self, 'phone')}
        resp = requests.put(url=self.send_msg_url, json=data)
    # 校验短信验证码
    def check_msg(self):
        sql = f"SELECT mobile_code FROM `tz_sms_log` WHERE user_phone={getattr(self,'phone')} " \
              f"ORDER BY id LIMIT 1"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        code = result[0][0]
        data = {
                      "mobile": getattr(self,'phone'),
                      "validCode": code
                    }
        resp = requests.put(url=self.check_msg_url,json=data)
        setattr(self,'sms_flag',resp.text)
    def register(self):
        data = {
            "appType": 3,
            "checkRegisterSmsFlag": getattr(self,'sms_flag'),  # 短信校验接口返回值
            "mobile": getattr(self,'phone'),
            "userName": getattr(self,'phone'),
            "password": "123456",
            "registerOrBind": 1,
            "validateType": 1
        }
        resp = requests.put(url=self.register_url,json=data)
        print(resp.text)
    def close_db(self):
        self.cur.close()
        self.db.close()
    def statr(self):
        self.get_phone()
        self.send_msg()
        self.check_msg()
        self.register()
        self.close_db()
if __name__ == '__main__':
    cl = Register()
    cl.statr()

