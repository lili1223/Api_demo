"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/15 20:56
@Project:py_Api
@Author : RainBow
@File : test02_image.py
"""
import json
import base64
import requests
"""
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
"""
url_image = 'http://mall.lemonban.com:8108/captcha.jpg?uuid=ff779e99-6c07-409b-8f32-d661427066e2'
class ImageCode:
    def __init__(self):
        # 获取图片验证码的地址
        self.url_image = 'http://mall.lemonban.com:8108/captcha.jpg?'
        # 解析图片验证码的地址
        self.image_code_url = "http://api.ttshitu.com/predict"
    def __get_image(self,uuid):
        data = {"uuid": uuid}
        res = requests.get(url=self.url_image, params=data)
        image_byte = res.content    # 获取响应结果的二进制
        base64_data = base64.b64encode(image_byte)
        b64 = base64_data.decode()  # 图片验证码base64编码
        return b64
    def get_code_image(self,uuid):
        b64 = self.__get_image(uuid)
        data = {"username": "haili", "password": "QINHAILI", "typeid": 3, "image": b64}
        result = json.loads(requests.post(url=self.image_code_url, json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]

if __name__ == '__main__':
    ImageCode().get_code_image(uuid)





