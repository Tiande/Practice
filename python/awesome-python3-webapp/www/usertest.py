#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
import asyncio
from models import User, Blog, Comment

def test(loop):
    """docstring for test"""
    yield from orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='12345', image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
