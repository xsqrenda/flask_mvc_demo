"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: view1.py
@time: 2017/12/26 16:32
@describe:
"""
from web import app
from python.control.file_handle import read_json_file
from flask import render_template, jsonify

print('control comment')

dirname = 'C:/Users/Administrator/AppData/Roaming/IQIYI Video/LStyle/vmPage/download/search/zipCache'
filename = ['index.json']


@app.route('/api/v1/get')
def get():
    newfilename = dirname+'/'+filename[0]
    jl = read_json_file(newfilename)
    # print(jl)
    # with 的用法：with jl['data']不可用
    # with jl['data'] as jldata:
    # with jl['data']:
    #     for jd in jl['data']:
    #         print(jd['query'])
    if 'data' in jl.keys():
        for jd in jl['data']:
            if 'query' in jl['data'][0].keys():
                print(jd['query'])
    # print(len(jl))
    # for

    # print(jl['data'][0].keys())
    # print(jl['data'][0]['query'])
    return jsonify(jl)


@app.route('/comment/add')
def comment_add():
    return 'add comment'


@app.route('/comment/delete')
def comment_delete():
    return 'delete comment'
