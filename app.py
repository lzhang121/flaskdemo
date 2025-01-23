#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
import json
from flask import Flask, Response, jsonify


app = Flask(__name__)
config = {
    "DEBUG": True
}
app.config.update(config)


@app.route('/')
def hello():
    # # 返回html内容和状态码
    # return "<h>Hello world!</h>", 201

    # # 通过make_response返回
    # response = make_response("<h>Hello world!</h>", 201)
    # return response

    # 通过Response返回
    response = Response("<h>Hello Ray!</h>", 201)
    return response


@app.route("/jsonapi")
def jsonapi():
    """响应json数据"""
    # data = {"name": "xiaoming", "age": 16}
    # return json.dumps(data), 200, {"Content-Type": "application/json"}

    data = {"name": "xiaoming", "age": 16}
    return jsonify(data)


@app.route("/img")
def img():
    """响应图片格式给客户端"""
    with open("static/images/flask-logo.png", "rb") as f:
        data = f.read()

    return data, 200, {"Content-Type": "image/png"}


if '__main__':
    app.run(host="0.0.0.0", port=5050)
