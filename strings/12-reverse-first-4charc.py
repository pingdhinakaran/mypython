#"""
#Write a program to print reverse substring of first four letters of the given input.

#eg:
#input: Indianocean 
#output: idnI
#"""
string = input()
trimmed = string[0:4] # Trimmed text
reversed = trimmed[::-1] # Reversed Text

print(reversed)