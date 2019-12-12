import re
import json

def add_all_numbers(string):
    numbers=re.compile('-?[0-9]+')
    total=sum(map(int,numbers.findall(string)))
    return total
def add_all(filename):
    f=open(filename)
    s=f.read()
    f.close
    return add_all_numbers(s)
def ignore_red(obj):
    if 'red' in obj.values():
        return None
    else:
        return obj
def read_json(filename):
    f=open(filename)
    jsonstring=json.dumps(json.load(f,object_hook=ignore_red))
    f.close()
    return add_all_numbers(jsonstring)
