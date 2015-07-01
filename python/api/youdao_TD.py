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

# 获取由命令行传入的字符串
def getDic(args):
    dic = ''
    for item in sys.argv[1:argvLen+1]:
        dic += item + ' '
    return dic

# 获取命令参数的长度
argvLen = len(sys.argv)
# 生成查询字符串
dic = getDic(sys.argv) if argvLen>1 else input('请键入要查询的参数： \n')
# 格式化请求地址
uri =  'http://fanyi.youdao.com/openapi.do?keyfrom=' + keyfrom + '&key=' + APIkey + '&type=data&doctype=json&version=1.1&q=' + urllib.parse.quote(dic)
# 获取返回结果 dict
content = json.loads(urllib.request.urlopen(uri).read().decode('utf-8', 'ignore'))
# 获取翻译 list
translation = content['translation'] if len(content['translation'])>0 else []
# 获取基本词典 dict
basic = content['basic'] if 'basic' in content else {}
# 获取网络释义 list
webValue = content['web'] if 'web' in content else ''

# 格式化的空格
space = '      '

# 打印翻译的方法
def printTrans(lst):
    for value in lst:
        print('  ', value)

# 打印基本词典的方法
def printBasic(dic):
    seq = ''
    for (key, value) in sorted(dic.items(), key=lambda dic: dic[0]): # .items() 转为元组数组 tuple; sorted 排序
        seq += '  「' + key + '」\n'
        if isinstance(value, list):
            for item in value:
                seq += space  + item + '\n'
        else:
            seq += space + value + '\n'
    print(seq)

# 打印网络释义的方法
def printWebValue(lst):
    for dic in lst:
        dic = dic.items()
        seq = ''
        for (key, value) in sorted(dic, key=lambda dic: dic[0]):
            if key=='key':
                seq += '  「' + value + '」\n'
            elif key=='value':
                seq += space
                for item in value:
                    seq += item + ' '
        print(seq)

# 显示结果
print('\n[[翻译]]')
printTrans(translation)

print('\n[[基本词典]]')
printBasic(basic)

print('[[网络释义]]')
printWebValue(webValue)
