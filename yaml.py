import json

import yaml
def write(filename,data):
    with open(file=filename,mode="a+",encoding="utf-8") as f:
        yaml.safe_dump(data=data,stream=f)

def read(filename):
    with open(file=filename,mode="r",encoding="utf-8") as f:
        data = yaml.safe_load(stream=f)
        return data

def clear(filename):
    with open(file=filename,mode="w",encoding="utf-8") as f:
        f.truncate()

def test_01():
    # data = {
    #     "name" : "aaa",
    #     "age" : 11
    # }
    # write("1.yml",data)
    # data = read("1.yml")
    # print(data)
    # clear("1.yml")
    data = read("1.yml")
    print(json.dumps(data))