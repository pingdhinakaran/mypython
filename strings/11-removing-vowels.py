#Write a program to print the given input string by removing vowels and padding zeros equivalent to the number of vowels

#eg: 
#input: apple
#output: ppl00
#"""

string = input()
vowels = ['a','e','i','o','u']
new_string = ""
vowels_num = 0
for each in string:
    if each not in vowels:
        new_string += each
    else:
        vowels_num += 1
for i in range(vowels_num):
    new_string += "0"
print(new_string)