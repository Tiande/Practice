#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json

url = 'http://apis.baidu.com/apistore/idservice/id?id=420984198704207896'
req = urllib.request.Request(url)
req.add_header("apikey", "3f45225d3dd0b2307758bf505a4606e0")
resp = urllib.request.urlopen(req)
content = json.loads(resp.read().decode('utf-8', 'ignore'))
if (content):
    print(content)
