"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: view1.py
@time: 2017/12/26 16:32
@describe:
"""
from web import app
from flask import render_template

print('control comment')


@app.route('/comment/add')
def comment_add():
    return 'add comment'


@app.route('/comment/delete')
def comment_delete():
    return 'delete comment'

