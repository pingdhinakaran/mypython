###counting the charater in the string...

#!/usr/bin/env python3

inp_str = input("Enter the string\n\t")
x=set()
result = ''
for i in inp_str:
    if i not in x:
        x.add(i)
        result=result+str(inp_str.count(i))+i
        print(result)
    