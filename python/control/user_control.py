"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: login.py
@time: 2017/12/26 16:34
@describe:
"""
from web import app
from flask import render_template
print('control user')

@app.route('/')
def user_index():
    return render_template('index.html')


@app.route('/user/login/')
def user_login():
    return 'user login page'


@app.route('/user/logout')
def user_logout():
    return 'user logout page'

