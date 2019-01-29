import json
def dict():
    search = input("Enter a word for get to know about meaning: ")
    data = json.load(open("/home/supriyo/Python3_BasicPrograms/PythonPojects/PythonDictoinary/data.json"))
    for i in data.keys():
        if search == i:
            return (data[i])
dict()
