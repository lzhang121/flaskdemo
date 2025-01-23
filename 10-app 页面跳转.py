#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""


from flask import Flask, request, Response, redirect, url_for


app = Flask(__name__)
config = {
    "DEBUG": True
}
app.config.update(config)


@app.route('/user')
def index():
    """判断请求是否还有token, 没有的话跳转到登录页面"""
    if request.args.get("token"):
        return "<h1>个人中心</h1>"
    else:
        # 跳转至登录页面
        url = url_for("login")
        print(app.url_map)
        print(url)
        return redirect("/login")


@app.route("/login")
def login():
    """模拟登录"""
    return "<h1>登录视图</h1>"


@app.route("/jump")
def jump():
    """站外跳转"""
    # return redirect("https://www.google.com", 302)
    response = Response("", 302, {"Location": "https://www.google.com"})
    return response


@app.route("/sms/<int:mobile>")
def sms(mobile):
    """发送短信"""
    return f"发送短信给{mobile}"


@app.route("/info")
def info():
    """跳转到sms页面"""
    # return redirect("/sms/13452617821")

    # 跳转到url_for的url上
    url = url_for("sms", mobile=12124121212)
    return redirect(url)


@app.route("/header")
def header():
    """自定义响应头"""
    response = Response("<h1>welcome to my website</h1>",
                        201, {"Company": "IBM"})
    return response


if '__main__':
    app.run(host="0.0.0.0", port=5050)
