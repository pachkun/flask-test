# -*- coding: utf-8 -*-
__author__ = 'pachkun'

from flask import Flask

app = Flask(__name__)

from . import routes
