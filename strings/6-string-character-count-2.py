#####counting the charachter in the string.

#!/usr/bin/env python3

str_input=input("enter the value")

c=input("charachter to check")

count=0

for i in str_input: 
    if i == c:
        count+=1
print (c, "occurs", count, "time(s)")
    







