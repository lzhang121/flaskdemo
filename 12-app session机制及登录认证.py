#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""

import random
from flask import Flask, session, request, make_response, redirect


app = Flask(__name__)
config = {
    "DEBUG": True,
    # flask seesion是基于cookie加密实现的，使用前必须设置SECREY_KEY
    "SECRET_KEY": "db05d70b-c3e2-43eb-af69-c7efa080af1e"
}
app.config.update(config)


@app.route('/set_session')
def set_session():
    """session的设置"""
    session["user_name"] = "ray"
    session["user_id"] = "100"
    session["user_data"] = [1, 2, 3, 4, 5]
    return "set_session"


@app.route('/get_session')
def get_session():
    """session的读取"""
    user_name = session.get("user_name")
    user_id = session.get("user_id")
    user_data = session.get("user_data")
    return f"<h1>user_name: {user_name}<br> user_id: {user_id}<br> user_data: {user_data}<br></h>"


@app.route('/del_session')
def del_session():
    """session的设置"""
    session.pop("user_name")
    session.pop("user_id")
    session.pop("user_data")
    return "del_session"


@app.route('/login', methods=["get", "post"])
def login():
    """基于session的登录"""

    form = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
                <form action="" method="post">
                    账号:<input type="text" name="user_name"><br><br> 
                    密码:<input type="password" name="password"><br><br>
                    <input type="submit" value="登录">
                </form>
            </body>
            </html>
    """

    if request.method == "GET":
        return make_response(form)

    user_name = request.form.get("user_name")
    password = request.form.get("password")
    # 登录成功基于session保存登录信息
    if password == "1234" and user_name == "root":
        session["user_name"] = user_name
        session["password"] = password
        session["user_id"] = str(random.randint(100, 200))
        session["user_data"] = ''.join(random.choices("abcdefg123456", k=5))
        response = make_response("登录成功")
        return response
    else:
        # 登录失败重定向到login
        response = redirect('/login')
        response.status_code = 400
        return response


@app.route('/user')
def user():
    """查看一登录用户的session"""
    user_name = session.get("user_name")
    if not user_name:
        response = redirect('/login')
        return response
    else:
        return f"<h1>user_name: {user_name}</h>"


if '__main__':
    app.run(host="0.0.0.0", port=5050)
