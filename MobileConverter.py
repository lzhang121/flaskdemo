# -*- coding: utf-8 -*-
"""
@Name:        MobileConverter.py
@Describe:    XXX
@Time:        2025/01/21 20:12:53
@Author:      Ray
@Version:     1.0
"""
from werkzeug.routing.converters import BaseConverter


class MobileConverter(BaseConverter):
    regex = r"1[3-9]\d{9}"


if __name__ == '__main__':
    MobileConverter()
