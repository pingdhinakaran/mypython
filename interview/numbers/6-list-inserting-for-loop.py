###Inserting value into list using for loop

#!/usr/bin/env python3
    
###Inserting value into list using for loop

num_list=[] ### empty_list

range_value = int(input("enter the range_value\n\t"))


for i in range(range_value):
    
    value = int(input("Please enter the Value of %d Element : " %i))
    num_list.append(value)

print (num_list)
    
    