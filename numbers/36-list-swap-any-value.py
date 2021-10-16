mylist=[1,3,45,77,99,33,55,61,32]

print(mylist)

print ("length of size", len(mylist))

print("enter the position between size")

pos1=int(input("enter postion value\n\t"))

pos2=int(input("enter postion value\n\t"))

mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]

print ("after changing the position",mylist)

