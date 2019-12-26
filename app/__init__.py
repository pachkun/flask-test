# -*- coding: utf-8 -*-
__author__ = 'pachkun'

from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from . import routes
