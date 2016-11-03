# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Pu hanhui'

'''
async web application.
'''

import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web



def index(request):
    logging.info("Tcp Server running")
    return web.Response(content_type='text/html', body=b'<h1>Awesome</h1>')


async def init(loop):
    app = web.Application(loop=loop)  # 设置该web的消息机制
    app.router.add_route('GET', '/', index)  # 添加路由
    # 创建TCP服务器,建立连接,协程等待连接完成
    logging.info("Tcp Server before")
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    logging.info(srv)
    return srv


loop = asyncio.get_event_loop()  # 获得消息机制
loop.run_until_complete(init(loop))  # 循环处理init任务
loop.run_forever()
