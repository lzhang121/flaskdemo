#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
from flask import Flask, render_template


app = Flask(__name__)
config = {
    "DEBUG": True
}
app.config.update(config)


@app.route('/hay')
def index():
    return render_template('hello.html', person=None)


@app.route('/hay/<name>')
def hello(name):
    return render_template('hello.html', person=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
