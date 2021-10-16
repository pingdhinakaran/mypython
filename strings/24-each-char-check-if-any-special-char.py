#!/usr/bin/env python3

text = input("enter a string to check\n\t")

special=['!','@','#','$','%','^','&','*','(',')','-','<','>','?','_','/','{','}']

for i in text:
    
    if i in special: #### if condition to check
        
        print (i,"has special characters")
        
    else:
    
        print (i, "has not special characters")