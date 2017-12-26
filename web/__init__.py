"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: __init.py
@time: 2017/12/26 16:29
@describe:
"""
from flask import Flask

print('app __name__')
app = Flask(__name__)

from python import control
