

import json
from difflib import get_close_matches

jsonfile = json.load(open("data1.json"))

word = input("enter the word:")


def check(d):
    d=d.lower()
    if d in jsonfile:
        return jsonfile[d]
    elif len(get_close_matches(d,jsonfile.keys()))>0:
        choice = input("Did you mean %s, Enter Y for Yes and N for No" %get_close_matches(d,jsonfile.keys())[0])
        if choice=="Y" or "y":
            return jsonfile[get_close_matches(d,jsonfile.keys())[0]]
        elif choice == "N" or "n":
            return "The value doesn't exist... Ply try with correct value"
        else:
            return "You entered the wrong choice"
    else:
        return "The value doesn't exist... Ply try with correct value"


result=(check(word))
if type(result)==list:
    for i in result:
        print(i)
else:
    print(result)