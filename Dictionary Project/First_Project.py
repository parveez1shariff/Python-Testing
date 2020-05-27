# This is the simple first project of creating Dictionary

import json
import difflib
from difflib import SequenceMatcher
from  difflib import get_close_matches
data = json.load(open("data.json"))

def translate(wd):
    wd1 = wd.lower()
    #x = SequenceMatcher(None,wd1,data.keys()).ratio()
    if wd1 in data:
        return data[wd1]
    elif len(get_close_matches(wd1, data.keys()))>0:
        print("Did you mean %s instead?" %get_close_matches(wd1,data.keys())[0])
        check = input("Enter Y or N: ")
        if check == "Y":
            wd2 = get_close_matches(wd1, data.keys())[0]
            return data[wd2] 
        else:
            return "The word doesnot exist, kindly do check"
    else:
        return "The word doesnot exist, kindly do check"

word = input("Enter the word:")
print(translate(word))