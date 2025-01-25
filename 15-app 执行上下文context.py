#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
from flask import Flask, current_app, jsonify, g

app = Flask(__name__)
config = {
    "DEBUG": True,
    "SECRET_KEY": "db05d70b-c3e2-43eb-af69-c7efa080a345"
}
app.config.update(config)


@app.route('/')
def index():
    print(app.url_map)
    print(current_app.url_map)
    print(id(app))  # current_app和app不是同一个对象
    print(id(current_app))
    print(app == current_app)  # current_app是app应用实例对象在视图中的本地代理对象
    print(current_app)
    d1()
    d2()
    # g为globals全局数据存储对象，用于服务端保存全局变量数据
    print(g)  # 用户级别全局变量
    return jsonify(message="Hello, Flask 3.0.3!")


def d1():
    g.user_id = 109


def d2():
    print(g.user_id)


if '__main__':
    print(app)
    # print(current_app)  #该对象还不存在 # RuntimeError: Working outside of application context.
    with app.app_context():
        print("--app启动上下文中代理对象: \n", current_app)
    app.run(host="0.0.0.0", port=5050)
