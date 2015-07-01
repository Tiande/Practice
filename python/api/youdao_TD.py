#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 感谢 网易有道翻译 ;)
# 从下面的地址申请 APIkey && keyfrom
# http://fanyi.youdao.com/openapi?path=data-mode

APIkey = '242349121' # 你的 APIkey
keyfrom = 'Tiandechi' # 你的 keyfrom
__author__ = 'Tiande ( https://github.com/Tiande ) '

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
uri =  'http://fanyi.youdao.com/openapi.do?keyfrom=' + keyfrom + '&key=' + APIkey + '&type=data&doctype=json&version=1.1&q=' + urllib.parse.quote(dic)
content = json.loads(urllib.request.urlopen(uri).read().decode('utf-8', 'ignore')) # dict

def printDict(dic):
    seq = '  '
    for (key, value) in sorted(dic.items(), key=lambda dic: dic[0]): # .items() 转为元组数组 tuple; sorted 排序
        seq += key + ' ==> '
        if isinstance(value, list):
            for item in value:
                seq += item + ' '
        else:
            seq += value
        seq += '\n  '
    print(seq)

def printList(lst):
    for value in lst:
        print('  ', value)

def printWebValue(dic):
    dic = dic.items()
    seq = '  '
    for (key, value) in sorted(dic, key=lambda dic: dic[0]):
        if key=='key':
            seq += value + ' ==> '
        elif key=='value':
            for item in value:
                seq += item + ' '
    print(seq)


translation = content['translation'] if len(content['translation'])>0 else [] # 翻译 list

def getTranslation(trans):
    print('\n翻译： ')
    printList(trans)

getTranslation(translation)

basic = content['basic'] if 'basic' in content else {} # 基本词典 dict

def getBasic(basic):
    print('\n基本词典： ')
    printDict(basic)

getBasic(basic)

webValue = content['web'] if 'web' in content else '' # 网络释义 list

def getWebValue(webValue):
    print('网络释义： ')
    for value in webValue:
        printWebValue(value)
        # print(value)

getWebValue(webValue)
