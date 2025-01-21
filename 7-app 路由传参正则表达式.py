#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
from flask import Flask
from werkzeug.routing.converters import BaseConverter


class MobileConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.regex = args[0]


app = Flask(__name__)
# 开启Debug模式
app.config["DEBUG"] = True
app.url_map.converters["regex"] = MobileConverter


@app.route("/sms/<regex('1[3-9]\d{9}'):mobile>")
# 路由传参
def good(mobile):
    return f"发送给手机号： {mobile}的用户"


@app.route("/user/<regex('\d{5}'):id>")
# 路由传参
def user(id):
    return f"用户id为{id}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
