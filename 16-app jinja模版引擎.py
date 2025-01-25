#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""

from flask import Flask, render_template, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    title = "我的页面"
    content = "网页内容"
    # 引入jinja引擎模版
    return render_template("test.html", **locals())


@app.route('/tmp')
def tmp():
    title = "临时页面"
    content = "网页内容"
    # 引入jinja引擎模版
    temp = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <title>{{title}}</title>
        </head>
        <body>
            <h1>{{title}}</h1>
            <br />
            <h1>{{content}}</h1>
            <br />
        </body>
        </html>
    """
    return render_template_string(temp, **locals())


if '__main__':
    app.run(host="0.0.0.0", port=5050)
