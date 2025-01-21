#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Name:        manage.py
@Describe:    XXX
@Time:        2025/01/21 15:37:37
@Author:      Ray
@Version:     1.0
"""
from flask import Flask


app = Flask(__name__)
# 开启Debug模式
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    # 默认flask支持函数式视图，视图的函数名不能重复，否则报错
    # 视图的返回值将被flask包装成响应视图对象的html文档内容，返给客户端
    return "<h1>hello world</h1>"


@app.route("/good/<int:cid>/<int:gid>/<float:tid>/<uuid:uuid>")
# 路由传参
def good(cid, gid, tid, uuid):
    print("type(cid): {}, cid: {}".format(type(cid), cid))
    print("type(gid): {}, gid: {}".format(type(gid), gid))
    print("type(tid): {}, tid: {}".format(type(tid), tid))
    print("type(uuid): {}, uuid: {}".format(type(uuid), uuid))
    return f"显示cid={cid}, gid={gid}的商品信息tid={tid} \n uuid={uuid}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
