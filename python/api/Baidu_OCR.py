# -*- coding: utf-8 -*-
import os
import base64
import sys
import urllib.request
import urllib.parse
import json
# f = open(r'c:\tmp.jpg','rb')
f = open(input('输入jpg地址：\n'),'rb')
ls_f = base64.b64encode(f.read())
f.close()
# fw = open(r'c:\tmp.txt','w')
# fw.write(ls_f.decode('utf-8'))
# fw.close()
url = 'http://apis.baidu.com/apistore/idlocr/ocr'
data = {}
data['fromdevice'] = "pc"
data['clientip'] = "10.10.10.0"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"
data['image'] = ls_f
decoded_data = urllib.parse.urlencode(data).encode(encoding='UTF8')
req = urllib.request.Request(url, data = decoded_data)
req.add_header("Content-Type", "application/x-www-form-urlencoded")
req.add_header("apikey", "3f45225d3dd0b2307758bf505a4606e0")
resp = urllib.request.urlopen(req)
content = json.loads(resp.read().decode('utf-8', 'ignore'))
if(content):
    print(content)

