# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:16:47 2020

@author: Ruslan
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'