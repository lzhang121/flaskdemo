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
from urllib.parse import parse_qs

app = Flask(__name__)
# 开启Debug模式
app.config["DEBUG"] = True


@app.route("/user/")
# 路由传参
def user():

    # 获取单个值
    # # 获取查询字符串，返回byte格式
    # # print(request.query_string)
    # user = parse_qs(request.query_string.decode())
    # print(user["id"][0], user["age"][0])

    # # 获取查询字符串，返回ImmutableMultiDict格式
    # print(request.args)
    # print(request.args["id"], request.args["age"])

    # 获取多值
    print(request.args.get("id"))
    print(request.args.getlist("age"))
    return f"hello flask"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
