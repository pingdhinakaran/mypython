###Inserting value into list using for loop

num_list=[] ### empty_list

range_value = int(input("enter the range_value\n\t"))


for i in range(range_value):
    
    value = int(input("Please enter the Value of %d Element : " %i))
    num_list.append(value)
    
### came out from the loop

###### decending Order
num_list.sort(reverse=True)

print("Element After Sorting List in decending Order is : ", num_list)

###### Ascending Order
num_list.sort()

print("Element After Sorting List in Ascending Order is : ", num_list)



