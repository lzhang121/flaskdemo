#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
from flask import Flask, render_template, request, session, g

app = Flask(__name__)
config = {
    "DEBUG": True,
    "SECRET_KEY": "db05d70b-c3e2-43eb-af69-c7efa080af1e"
}
app.config.update(config)


@app.route('/')
def index():
    title = "我的页面"
    content = "网页内容"

    # 简单类型
    num = 100
    num2 = 3.14
    is_bool = True
    title = "变量练习"

    # 复杂类型
    set_var = {1, 2, 3, 4}
    list_var = ["小明", "小白", "小花"]
    dict_var = {"name": "ray", "age": "38", "pwd": "123456"}
    tuple_var = (1, 2, 3, 4, 5)

    # 数据类型
    book_list = [
        {"id": 1, "title": "story", "description": "book"},
        {"id": 2, "title": "history", "description": "work"},
        {"id": 3, "title": "consume", "description": "flower"}
    ]

    session['uname'] = 'centos7.2'
    g.num = "12"
    # 引入jinja引擎模版
    return render_template("test.html", **locals())


@app.route('/user')
def user1():
    return "ok"


@app.route('/user/<userid>')
def user2(userid):
    return "ok"


if '__main__':
    app.run(host="0.0.0.0", port=5050)
