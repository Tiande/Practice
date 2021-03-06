#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Tiande'

import logging
logging.basicConfig(level=logging.INFO)

import asyncio
import os
import json
import time
from datetime import datetime

from aiohttp import web


def index(request):
    """docstring for index"""
    return web.Response(body=b'<h1>Awesome</h1>')


@asyncio.coroutine
def init(loop):
    """docstring for init"""
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    # 'loop.create_server()'利用 asyncio 创建 TCP 服务
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
