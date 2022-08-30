"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/12 20:56
@Project:py_Api
@Author : RainBow
@File : demo01.py
"""
import json

import requests
import jsonpath
# 用户登录
# url ='http://mall.lemonban.com:8108/adminLogin'
# data = {"t":1660310892561,"principal":"student","credentials":"123456a","sessionUUID":"cef560fc-c722-4996-866d-b37aada38a20","imageCode":"lemon"}
# res = requests.post(url=url,json=data)
# print(res.json())
# token = jsonpath.jsonpath(res.json(),'$..access_token')[0]
# url2 ='http://mall.lemonban.com:8108/admin/file/upload/img'
# headers = {
# "Content-Disposition": 'form-data; name="file"; filename="1.png"',
# "Content-Type": "image/png",
#     "Authorization": "bearerf2977f51-d0d4-488b-b29f-8d518e6e8f92"
# }
# # Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryCeKHGOsaOkOTmbnk
# res1 = requests.post(url=url2,headers=headers)
# headers = {"Authorization":token}
url2 = 'http://mall.lemonban.com:8108/prod/prod'
data = {"t":1660313819957,"prodName":"夏日必囤好物","brief":"","video":"",
        "prodNameEn":"夏日必囤好物","prodNameCn":"夏日必囤好物","contentEn":"",
        "contentCn":"<p><img src=\"https://img30.360buyimg.com/jgsq-productsoa/jfs/t1/208920/12/25106/121266/62f3273dE538c154c/7c5d2f594b37e411.jpg\" alt=\"图一\" width=\"640\" height=\"300\" /></p>",
        "briefEn":"","briefCn":"就是好看","pic":"2022/08/ccdcddde760a4b229c82e3ae82784b3d.png",
        "imgs":"2022/08/ccdcddde760a4b229c82e3ae82784b3d.png","preSellStatus":1,
        "preSellTime":"2022-08-13 00:00:00","categoryId":155,
        "skuList":[{"price":0.01,"oriPrice":0.01,"stocks":10000,"skuScore":1,"properties":"","skuName":"",
                    "prodName":"","weight":0.01,"volume":0,"status":1,"partyCode":"202208122209","prodNameCn":"夏日必囤好物",
                    "prodNameEn":"夏日必囤好物"}],"tagList":[1],"content":"","deliveryTemplateId":1,"totalStocks":10000,"price":0.01,"oriPrice":0.01,
        "deliveryModeVo":{"hasShopDelivery":true,"hasUserPickUp":false,"hasCityDelivery":false}}

res1 = json.loads(requests.post(url=url2,json=data).text)