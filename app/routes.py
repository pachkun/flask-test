# -*- coding: utf-8 -*-
__author__ = 'pachkun'

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
