#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json
import re

url = 'http://2.zaizaiwx.sinaapp.com/data.html'
ret = urllib.request.urlopen(url).read().decode('utf8', 'ignore')

pattern = re.compile(r'.*(?=<script)')
info = pattern.findall(ret)
print(info[0])
