# -*- coding: utf-8 -*-
# $ pip install mysql-connector-python --allow-external mysql-connector-python
import mysql.connector as mycon

conn = mycon.connect(user=input('输入用户名： '), password=input'输入密码： ')
