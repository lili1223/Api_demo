"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/15 20:07
@Project:py_Api
@Author : RainBow
@File : demo02.py
"""
#  登录接口
url_logi = 'http://mall.lemonban.com:8107/login'
headers = {"Content-Type": "application/json; charset=UTF-8"}
data = {"principal":"18820992515","credentials":"123456","appType":3,"loginType":"0"}

url2_orderPath = 'http://mall.lemonban.com:8107/p/seckill/orderPath'
data2 = '3BURYsVST4c'

# 创建订单
URL = 'Request URL: http://mall.lemonban.com:8107/p/seckill/3BURYsVST4c/confirm'
data3 = {"addrId":0,"prodCount":1,"seckillSkuId":129}

# 提交订单
url_submit = 'http://mall.lemonban.com:8107/p/seckill/3BUSmieJkiL/submit'
# 支付
url_pay = 'http://mall.lemonban.com:8107/p/order/pay'
data_pay = {"payType":3,"orderNumbers":"1559151189378207744"}

#支付回调接口（用来模拟支付，开发写的）
'http://mall.lemonban.com:8107/notice/pay/3'
