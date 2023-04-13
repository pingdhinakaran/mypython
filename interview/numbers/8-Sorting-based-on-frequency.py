###Inserting value into list using for loop

#!/usr/bin/env python3
    
###Inserting value into list using for loop

num_list=[] ### empty_list

range_value = int(input("enter the range_value\n\t"))


for i in range(range_value):
    
    value = int(input("Please enter the Value of %d Element : " %i))
    num_list.append(value)

print (num_list)

#li = list(map(int, input().split()))
num_list.sort()
final = sorted(num_list, key=num_list.count, reverse=True)
for each in final:
    print(each, end=" ")