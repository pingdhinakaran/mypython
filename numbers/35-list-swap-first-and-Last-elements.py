###Swap the first elements and last elements 

###method : 1

#### Using Temp veriable

mylist = [2,45,66,88,90,34]

sizes = len(mylist)

temp = mylist[0] ### Assigning "0" th position to temp 

mylist[0] = mylist[sizes-1] 

mylist[sizes-1] = temp

print ("list after swapping",mylist)

### method 2 :

mylist[0],mylist[-1]=mylist[-1],mylist[0]

print ("list after swapping",mylist)







