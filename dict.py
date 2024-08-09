import json
import time
from difflib import get_close_matches

data = json.load(open("data.json"))

def translator(word):
    word = word.lower()

    if word in data:
        return data[word]
    else:
        if word not in data:
            close_words = get_close_matches(word, data, n=1)
            ask_for_close_words = input(f"Did your mean {close_words[0]} instead? Input 'y' if Yes or 'n' if No: ")
            if close_words:
                if ask_for_close_words == ask_for_close_words:
                    return data[close_words[0]]
                elif ask_for_close_words == False:
                    return "Please try with another word"
                else:
                    return "Sorry, you have inserted wrong words!"
            else:
                return "This word doesn't exits. Please try again!"
        
    
while True: 
    user_input = input("Please input a English word to know it's full meaning: ")
    if user_input == "exit":
        break
    else:
        result = translator(user_input)
        if type(result) == list:
            print(f"The full meanig of '{user_input}' is: ")
            for output in result:
                print("-", output)
            print()
        else:
            print(result)
    time.sleep(2)