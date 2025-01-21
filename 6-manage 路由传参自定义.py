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
from MobileConverter import MobileConverter


app = Flask(__name__)
# 开启Debug模式
app.config["DEBUG"] = True

# 把自定义路由转化器注册到flask项目中
app.url_map.converters["mobile"] = MobileConverter


@app.route("/sms/<mobile:mobile>")
# 路由传参
def good(mobile):
    return f"发送给手机号： {mobile}的用户"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
