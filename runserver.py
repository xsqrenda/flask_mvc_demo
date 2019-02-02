"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: runserver.py
@time: 2017/12/26 16:31
@describe:
"""
from web import app


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
