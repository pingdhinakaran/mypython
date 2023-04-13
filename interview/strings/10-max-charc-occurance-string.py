###checking maxmium character in string 

###!/usr/bin/env python3 

text = input("enter the string to check\n\t")

#text = "Hello World"

char_dict = {}  #### empty disconery

for each in text:
    
    if each in char_dict.keys():
        char_dict[each] += 1
    else:
        char_dict[each] = 1
        
print(char_dict)

print("Max is", max(char_dict, key=char_dict.get))