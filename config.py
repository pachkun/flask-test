# -*- coding: utf-8 -*-
__author__ = 'pachkun'

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
