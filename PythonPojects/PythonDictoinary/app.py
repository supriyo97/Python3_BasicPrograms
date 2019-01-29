import json,difflib
from difflib import get_close_matches #get_close_matches helps to get the most nearest common word

data = json.load(open("/home/supriyo/Python3_BasicPrograms/PythonPojects/PythonDictoinary/data.json")) #load and open the data file using json

def dict():
    search = input("Enter a word for get to know about meaning: ").lower() #converts getting input into lower case:-)
    if search in data.keys():
        return (data[search])
    elif len(get_close_matches(search,data.keys(),cutoff=0.8))>0:
        while True:
            a = input(f"Are you looking for {get_close_matches(search,data.keys())[0]} word instead?(y/n): ").lower()
            if a == "y":
                return data[get_close_matches(search,data.keys())[0]]
            elif a == "n":
                return ("No such meaning available.")
            else:
                print( "wrong input" )
    else:
        return ("No such meaning available.Please double check your word")
d = dict()
if type(d) == list:
    for i in d:
        print(i)
else:
    print(d)
