###Inserting value into array using for loop

#!/usr/bin/env python3
    
###Inserting value into array using for loop

array_list=()

range_value = int(input("enter the range_value\n\t"))

for i in range(range_value):
    
    value = int(input("Please enter the Value of %d Element : " %i))
    
    array_list.append(value)
    
print (array_list)