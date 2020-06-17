import json

parsed_string = json.load(open('./database/data.json'))


def translate(word):
    if word in parsed_string:
        return parsed_string[word]
    else:
        return "The word doesn't exist.Please double check it"

while(True):
    word = input('Enter Word:')

    print(translate(word))
