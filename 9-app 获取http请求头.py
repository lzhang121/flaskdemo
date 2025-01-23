#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
from flask import Flask, request


app = Flask(__name__)
config = {"DEBUG": True}
app.config.update(config)


@app.route("/header", methods=["get", "post", "put", "delete"])
def header():
    # 获取请求头
    print(request.headers)

    # 获取User-Agent
    print(request.headers["User-Agent"])

    # 获取User-Agent
    print(request.user_agent)

    # 获取远程地址
    print(request.remote_user)

    # 获取服务器
    print(request.server)

    # 获取请求方法
    print(request.method)

    # 获取请求url
    print(request.url)

    # 获取环境变量
    print(request.environ)

    return "hello header"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
