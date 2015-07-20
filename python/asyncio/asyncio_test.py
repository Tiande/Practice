#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import threading

@asyncio.coroutine
def hello():
    """docstring for hello"""
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
@asyncio.coroutine
def hello():
    """hello use asyncio"""
    print("Hello world!")
    # 异步调用 asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取 EventLoop:
loop = asyncio.get_event_loop()
# 执行 coroutine
loop.run_until_complete(hello())
loop.close()


# 协程
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
'''


