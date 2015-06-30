#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://fanyi.youdao.com/openapi?path=data-mode
# API key：242349121
# keyfrom：Tiandechi

import urllib.request
import urllib.parse
import json
import sys

def getDic(args):
    """getDic"""
    dic = ''
    for item in sys.argv[1:slen+1]:
        dic += item + ' '
    return dic

slen = len(sys.argv)
dic = getDic(sys.argv) if slen>1 else input('请键入要查询的参数： \n')

uri =  'http://fanyi.youdao.com/openapi.do?keyfrom=Tiandechi&key=242349121&type=data&doctype=json&version=1.1&q=' + urllib.parse.quote(dic)
content = json.loads(urllib.request.urlopen(uri).read().decode('utf-8', 'ignore'))

for key in content:
    print(key, ' : ', content[key])
