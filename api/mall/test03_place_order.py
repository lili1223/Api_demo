"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/19 20:03
@Project:py_Api
@Author : RainBow
@File : test.py
"""
import jsonpath
import requests
import time
from api.mall.test02_login import Login

""""
下单流程
获取秒杀商品流程
Request URL: http://mall.lemonban.com:8107/p/seckill/orderPath
Request Method: GET
Status Code: 200 
param = 3C6cKqDKzNG

确认订单
Request URL: http://mall.lemonban.com:8107/p/seckill/3C6bM1JB6Y0/confirm
Request Method: POST
Status Code: 200 
data = {"addrId":0,"prodCount":1,"seckillSkuId":136}

提交订单
Request URL: http://mall.lemonban.com:8107/p/seckill/3C6bM1JB6Y0/submit
{"orderShopParam":{"remarks":"","shopId":1},"orderPath":"3C6cKqDKzNG"}

下单
Request URL: http://mall.lemonban.com:8107/p/order/pay
Request Method: POST
{"payType":2,"orderNumbers":"1560605420194893824",
"returnUrl":"http://mall.lemonban.com:3344/user-center/uc-order"}

"""
from api.mall.data import Data
class PlacsOrde:
    def __init__(self):
        self.order_path_url = 'http://mall.lemonban.com:8107/p/seckill/orderPath'
        self.headers = Login().login()

    # 获取秒杀商品订单的地址
    def get_order_path(self):
        url = 'http://mall.lemonban.com:8107/p/seckill/orderPath'
        resp = requests.get(url=url,headers=self.headers)
        jsonpath.jsonpath(resp.text,'$..')
        setattr(self,'orderpath',resp.text)

    # 确认订单
    def confirm_product(self):
        self.get_order_path()
        confirm_url = f'http://mall.lemonban.com:8107/p/seckill/{getattr(self,"orderpath")}/confirm'
        data = {"addrId": 0,
                "prodCount": 1,
                "seckillSkuId": 165}
        resp = requests.post(url=confirm_url,json=data,headers=self.headers)
        # print(resp.text)

    # 提交订单
    def submit_product(self):
        self.confirm_product()
        submit_url = f"http://mall.lemonban.com:8107/p/seckill/{getattr(self,'orderpath')}/submit"
        data = {"orderShopParam":{"remarks":"","shopId":1},"orderPath":getattr(self,'orderpath')}
        resp = requests.post(url=submit_url,json=data,headers=self.headers)
        # print(resp.json())
        # print(jsonpath.jsonpath(resp.json(), '$..orderNumbers')[0])
        setattr(self,'orderNumbers',jsonpath.jsonpath(resp.json(), '$..orderNumbers')[0])

    # 支付
    def pay(self):
        self.submit_product()
        pay_url = 'http://mall.lemonban.com:8107/p/order/pay'
        data = {"payType":3,"orderNumbers":getattr(self,'orderNumbers')}
        resp = requests.post(url=pay_url,json=data,headers=self.headers)
        print(resp.text)

    # 模拟支付回调
    def call_back(self):
        self.pay()
        call_back_url = 'http://mall.lemonban.com:8107/notice/pay/3'
        data = {"payNo": getattr(self,'orderNumbers'),  # 商城支付订单号
                "bizPayNo":"str(int(time.time()*1000))" ,  # 微信官方订单号
                "isPaySuccess": True   # True成功，False失败
                }
        resp = requests.post(url=call_back_url, json=data, headers=self.headers)
if __name__ == '__main__':
    cl = PlacsOrde()
    cl.call_back()