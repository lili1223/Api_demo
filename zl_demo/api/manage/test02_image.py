"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/21 12:08
@Project:py_Api
@Author : RainBow
@File : test02_image.py
"""
"""
Request URL: http://mall.lemonban.com:8108/captcha.jpg?uuid=a43899a7-93ec-462f-8193-b2dbd918b7ac
Request Method: GET

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

if __name__ == "__main__":
    img_path = "C:/Users/Administrator/Desktop/file.jpg"
    result = base64_api(uname='你的账号', pwd='你的密码', img=img_path, typeid=3)
    print(result)
"""

import requests
import json
import base64
class ImageCode:
    def __init__(self):
        self.image_url = 'http://mall.lemonban.com:8108/captcha.jpg'
        self.image_code_url = "http://api.ttshitu.com/predict"

    def image_code(self,uuid):
        data = {"uuid":uuid}
        resp = requests.get(url=self.image_url,params=data)
        image = resp.content    # 获取图片二进制地址
        base64_data = base64.b64encode(image)
        b64 = base64_data.decode()
        return b64

    def get_image_code(self, uuid):
        b64 = self.image_code(uuid=uuid)
        data = {"username": "haili", "password": "QINHAILI", "typeid": 3, "image": b64}
        result = json.loads(requests.post(url=self.image_code_url, json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]
