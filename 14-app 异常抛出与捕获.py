#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
from flask import Flask, jsonify, request, abort

app = Flask(__name__)


class NetworkError(Exception):
    pass


@app.route('/')
def index():
    password = request.args.get("password")
    if password != "123456":
        # 主动抛出异常
        # abort参数为抛出的http异常状态码
        # abort(400, "密码错误！")
        raise Exception("网络异常!!!")
        # print(hello)

    return jsonify(message="Hello, Flask 3.0.3!")


# 参数为异常的类型
@app.errorhandler(NameError)
def NameErrorFunc(exc):
    """
    针对变量名异常处理
    :params exc:
    :returns:
    """
    print(exc.args)
    print(exc.__traceback__)
    return {"错误提示": f"{exc}"}


@app.errorhandler(400)
def HttpError400(exc):
    print(exc.__traceback__)
    print("error:", exc.code)
    print("info:", exc.description)
    return {"错误提示": f"{exc}"}


@app.errorhandler(404)
def HttpError404(exc):
    print(exc.__traceback__)
    print("error:", exc.code)
    print("info:", exc.description)
    return {"错误提示": f"{exc}"}


@app.errorhandler(Exception)
def network_error_func(exc):
    return {"错误提示": f"{exc}"}


if '__main__':
    app.run(host="0.0.0.0", port=5050)
