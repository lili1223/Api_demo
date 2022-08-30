"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/15 21:42
@Project:py_Api
@Author : RainBow
@File : test03_upload.py
"""
import requests
from requests_toolbelt import MultipartEncoder
from api.manage.test01_login import Login
from tools.handle_extract_data import HandleExtractData


class UpLoad:
    def __init__(self):
        self.url = 'http://mall.lemonban.com:8108/admin/file/upload/img'
        self.headers = Login().login()
    def upload(self):
        """
        ------WebKitFormBoundarytP4DlIFDlPVCDGVC
        Content-Disposition: form-data; name="file"; filename="bb.png"
        Content-Type: image/png
        :return:
        """
        with open(file=r'C:\Users\MI\Pictures\Camera Roll\bb.png', mode='rb') as file:
            image = file.read()
            data = MultipartEncoder(fields={"file": ("bb.png",image,'image/png')})
            self.headers["Content-Type"] = data.content_type
            print(self.headers)
            resp = requests.post(url=self.url, data=data, headers=self.headers)
            print(resp.text)
if __name__ == '__main__':
    UpLoad().upload()



