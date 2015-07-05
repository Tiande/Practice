#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 感谢 网易有道翻译 ;)
# Date:2015-07-02 09:04
# 重写 youdao_TD_old.py
# 参考了 http://www.cnblogs.com/BeginMan/p/3644283.html

__author__ = 'Tiande ( https://github.com/Tiande ) '

import urllib.request
import urllib.parse
import json
import sys

class youdao(object):
    def __init__(self):
        # 从下面的地址申请 APIkey && keyfrom
        # http://fanyi.youdao.com/openapi?path=data-mode
        self._APIkey = '242349121' # 你的 APIkey
        self._keyfrom = 'Tiandechi' # 你的 keyfrom
        self._content = ''
        # 格式化的空格
        self._space = '      '

    # 获取由命令行传入的字符串
    def getDic(self):
        dic = ''
        for item in sys.argv[1:len(sys.argv)+1]:
            dic += item + ' '
        return dic

    # 赋值请求结果的函数
    def getResult(self):
        uri =  'http://fanyi.youdao.com/openapi.do'
        # 生成查询字符串
        dic = self.getDic() if len(sys.argv)>1 else input('请键入要查询的参数： \n')
        data = {
                'keyfrom': self._keyfrom,
                'key': self._APIkey,
                'type': 'data',
                'doctype': 'json',
                'version': '1.1',
                'q': 'Please input words!' if len(dic)==0 else dic
                }
        data = urllib.parse.urlencode(data)
        req = urllib.request.Request(uri + '?' + data)
        response = urllib.request.urlopen(req)
        self._content = json.loads(response.read().decode('utf-8', 'ignore'))

    # 打印翻译的方法
    def printTrans(self):
        # 获取翻译 list
        translation = self._content['translation'] if len(self._content['translation'])>0 else []
        print('翻译：')
        for value in translation :
            print('  ', value)

    # 打印基本词典的方法
    def printBasic(self):
        # 获取基本词典 dict
        dic = self._content['basic'] if 'basic' in self._content else {}
        print('\n基本词典：')
        seq = ''
        for (key, value) in sorted(dic.items(), key=lambda dic: dic[0]): # .items() 转为元组数组 tuple; sorted 排序
            seq += '  「' + key + '」\n'
            if isinstance(value, list):
                for item in value:
                    seq += self._space  + item + '\n'
            else:
                seq += self._space + value + '\n'
        print(seq)

    # 打印网络释义的方法
    def printWebValue(self):
        # 获取网络释义 list
        webValue = self._content['web'] if 'web' in self._content else ''
        print('网络释义：')
        for dic in webValue:
            dic = dic.items()
            seq = ''
            for (key, value) in sorted(dic, key=lambda dic: dic[0]):
                if key=='key':
                    seq += '  「' + value + '」\n'
                elif key=='value':
                    seq += self._space
                    for item in value:
                        seq += item + ' '
            print(seq)

    def whetherContinue(self):
        yn = input('\n是否继续查询？\n(q 退出, 回车 继续)\n')
        if yn=='q':
            sys.exit(0)
        else:
            sys.argv = sys.argv[0:1]
            self.main()


    def main(self):
        """print all"""
        self.getResult()
        self.printTrans()
        self.printBasic()
        self.printWebValue()
        self.whetherContinue()

if __name__ == "__main__":
    yd = youdao()
    yd.main()

