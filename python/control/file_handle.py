import json

def read_json_file(filename):
    with open(filename, 'r', encoding='utf8') as jf:
        jl = json.load(jf)
        return jl