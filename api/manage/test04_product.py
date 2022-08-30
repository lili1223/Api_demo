"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/21 16:27
@Project:py_Api
@Author : RainBow
@File : test04_product.py
"""
from api.manage.test01_login import Login
import requests
import time
class AddProduct:
    def __init__(self):
        self.url = 'http://mall.lemonban.com:8108/prod/prod'
        self.headers = Login().login()
    def addpro(self):
        data = {
                  "t": int(time.time()*1000),
                  "prodName": "彩虹专属商品001",
                  "brief": "",
                  "video": "",
                  "prodNameEn": "彩虹专属商品001",
                  "prodNameCn": "彩虹专属商品001",
                  "contentEn": "",
                  "contentCn": "<p><img src=\"https://img10.360buyimg.com/imgzone/jfs/t1/132877/28/24956/751711/62302c2eE6d572a08/c7e3c0c1148be4fc.jpg.avif\" alt=\"\" /><img src=\"https://img10.360buyimg.com/imgzone/jfs/t1/104330/20/25837/1481454/62302c33Eac57b4c1/c6cb2fdf30e6be6a.jpg.avif\" alt=\"\" /></p>",
                  "briefEn": "",
                  "briefCn": "",
                  "pic": "2022/08/f4bf0368c137499ba33ee299ec1c4fff.png",
                  "imgs": "2022/08/f4bf0368c137499ba33ee299ec1c4fff.png",
                  "preSellStatus": 1,
                  "preSellTime": "2022-08-28 00:00:00",
                  "categoryId": 289,
                  "skuList": [
                    {
                      "price": 0.01,
                      "oriPrice": 0.01,
                      "stocks": 0,
                      "skuScore": 1,
                      "properties": "",
                      "skuName": "",
                      "prodName": "",
                      "weight": 0,
                      "volume": 0,
                      "status": 1,
                      "prodNameCn": "彩虹专属商品001",
                      "prodNameEn": "彩虹专属商品001"
                    }
                  ],
                  "tagList": [
                    1,
                    2,
                    3
                  ],
                  "content": "",
                  "deliveryTemplateId": 1,
                  "totalStocks": 0,
                  "price": 0.01,
                  "oriPrice": 0.01,
                  "deliveryModeVo": {
                    "hasShopDelivery": True,
                    "hasUserPickUp": False,
                    "hasCityDelivery": False
                  }}
        resp = requests.post(url=self.url,json=data,headers=self.headers)
        print(resp.text)

if __name__ == '__main__':

    AddProduct().addpro()

