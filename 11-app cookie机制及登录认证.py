#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""


from flask import Flask, make_response, request, redirect


app = Flask(__name__)
config = {
    "DEBUG": True
}
app.config.update(config)


@app.route('/set_cookie')
def set_cookie():
    """cookie的设置"""
    # cookie是保存在客户端浏览器中，所以必须跟着响应对象返回给客户端
    response = make_response("set_cookie")
    # 格式 response.set_cookie("变量名", "变量值", max_age="过期时间秒")
    response.set_cookie("user_name", "ray", max_age=3600)  # 设置max_age, 以秒为单位
    response.set_cookie("number", "01", max_age=3600)  # 设置max_age, 以秒为单位
    return response


@app.route('/get_cookie')
def get_cookie():
    """cookie的读取"""
    # 通过request获取返回的user_id 和user_name
    user_name = request.cookies.get("user_name")
    print("user_name: ", user_name)
    return f"<h1>user_name: {user_name}</h>"


@app.route('/del_cookie')
def del_cookie():
    """cookie的设置"""
    # cookie保存在客户端浏览器中，所以服务端无法删除cookie,
    # 只能让服务端告诉客户端cookie已经过期
    response = make_response("del_cookie")
    response.set_cookie("user_name", "", max_age=0)  # 设置max_age, 以秒为单位
    return response


@app.route('/login', methods=["get", "post"])
def login():
    """基于cookie的登录"""

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
    # 登录成功记录cookie
    if password == "1234" and user_name == "root":
        response = make_response("登录成功")
        response.set_cookie("user_name", user_name, max_age=3600)
        response.set_cookie("password", password, max_age=3600)
        return response
    else:
        # 登录失败重定向到login
        response = redirect('/login')
        response.status_code = 400
        return response


@app.route('/user')
def user():
    """查看一登录用户的cookie"""
    user_name = request.cookies.get("user_name")
    if not user_name:
        response = redirect('/login')
        return response
    else:
        return f"<h1>user_name: {user_name}</h>"


if '__main__':
    app.run(host="0.0.0.0", port=5050)
