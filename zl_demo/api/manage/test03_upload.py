"""
!/usr/bin/python3
 -*- coding: utf-8 -*-
@Time : 2022/8/21 12:45
@Project:py_Api
@Author : RainBow
@File : test03_upload.py
"""
"""
requests-toolbelt(作用：构造数据，设置请求头)
"http://api.ttshitu.com/predict"
"""
from requests_toolbelt import MultipartEncoder
from zl_demo.api.manage.test01_login import Login
data = MultipartEncoder(fields={"file":("图片路径",'图片二进制','图片类型')

})
class Upload:
    def __init__(self):
        self_url = ''

    def upload(self):
        """
        ------WebKitFormBoundarytP4DlIFDlPVCDGVC
        Content-Disposition: form-data; name="file"; filename="bb.png"
        Content-Type: image/png
        :return:
        """
        Login().login()
        data = MultipartEncoder(fields={""})

