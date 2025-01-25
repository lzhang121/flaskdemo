#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.before_request
def before_request():
    """before_request在每个请求处理之前运行"""
    print("=在每个请求处理之前运行=")
    print(f"----Before request: {request.method} {request.path}----")


@app.after_request
def after_request(response):
    """after_request在每个请求处理之后运行"""
    print("=在每个请求处理之后运行=")
    response.headers['X-Custom-Header'] = 'FlaskHook'
    print("----After request executed----")
    return response


@app.teardown_request
def teardown_request(exception):
    """teardown_request在每个请求的上下文销毁时运行"""
    print("=在每个请求的上下文销毁时运行（无论是否抛出异常）=")
    if exception:
        print(f"----Request ended with exception: {exception}----")
    else:
        print("----Request ended successfully----")


@app.teardown_appcontext
def teardown_appcontext(exception):
    """teardown_appcontext在应用上下文销毁时运行"""
    print("=在应用上下文销毁时运行=")
    print("----Application context is being torn down----")
    if exception:
        print(f"----Exception: {exception}----")


@app.route('/')
def index():
    return jsonify(message="Hello, Flask 3.0.3!")


if '__main__':
    app.run(host="0.0.0.0", port=5050)
