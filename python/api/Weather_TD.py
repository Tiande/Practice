#!usr/bin/env python3
# -*- coding: utf-8 -*-
# Tiande's weather api practice.
# https://github.com/Tiande
# http://apistore.baidu.com/apiworks/servicedetail/112.html

__author__ = 'Tiande'

import urllib.request
import urllib.parse
import json
import re
import os

class Weather(object):

    def __init__(self):
        """__init__"""
        self._city = urllib.parse.quote(input('输入你想查询天气的城市:\n'))
        self._my_headers = {
                'apikey' : '3f45225d3dd0b2307758bf505a4606e0'
                }

    def yn_pinyin(self, city):
        """wheather pinyin or 汉子"""
        pattern = re.compile(r'^[a-zA-Z]')
        if pattern.match(city):
            return 'http://apis.baidu.com/apistore/weatherservice/weather?citypinyin=' + city
        else:
            return 'http://apis.baidu.com/apistore/weatherservice/cityname?cityname=' + city

    def get_data(self, url):
        request = urllib.request.Request(url, headers=self._my_headers)
        response = urllib.request.urlopen(request)
        data = json.loads(response.read().decode('utf8'))
        if data['errMsg']!='success':
            print('\n  ʕ •ᴥ•ʔ  竟然让我出错了，好好反思下再运行吧！阿西巴! \n')
            os._exit(0)
        return data['retData']

    def show_out(self, retData):
        """show me the weather"""
        # output == op
        op = '城市名： ' + retData['city'] + '\n'
        op += '日期： ' + retData['date'] + '\n'
        op += '当前气温： ' + retData['temp'] + '\n'
        op += '天气状况： ' + retData['weather'] + '\n'
        op += '今日趋势： ' + retData['l_tmp'] + ' ==> ' + retData['h_tmp'] + '\n'
        print(op)

    def doit(self):
        return self.show_out(self.get_data(self.yn_pinyin(self._city)))

if __name__ == '__main__':
       weather = Weather()
       weather.doit()

