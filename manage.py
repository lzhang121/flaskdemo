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


app = Flask(__name__)

# 通过实例对象app提供的route路由装饰器，绑定视图与uri地址的关系


@app.route("/")
def index():
    # 默认flask支持函数式视图，视图的函数名不能重复，否则报错
    # 视图的返回值将被flask包装成响应视图对象的html文档内容，返给客户端
    return "<h1>hello world</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
