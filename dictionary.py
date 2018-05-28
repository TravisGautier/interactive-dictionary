##Interactive Dictionary 
##Travis Gautier 2018
##
##
import json
from difflib import SequenceMatcher         # similiarity ratio library for detecting close matches
from difflib import get_close_matches       # finding the best match of a word

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()       # making user in put case-insensitive
    if w in data:       # checks if user input is a word or not
        return data[w]
    elif w.title() in data:                             # if the user entered "kansas" instead of "Kansas"
        return data[w.title()]
    elif w.upper() in data:                             # if the user enters an acronym
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:    # checks if user input is a word/spelled correctly
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]               # if suggested word is correct
        elif yn == "N":
            return "The word doesn't exist. Please double check it."        # if suggested word is incorrect
        else:
            return "We didn't understand your entry."                       # if the user did not type y or n
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")        # ask for user input

output = translate(word)
if type(output) == list:            # making sure the user input is a list, and not a string for example
    for item in output:
        print(item)
else:
    print(output)




