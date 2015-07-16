#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

print(s.recv(1024).decode('utf-8'))
for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
s.send(b'text')
s.close()
