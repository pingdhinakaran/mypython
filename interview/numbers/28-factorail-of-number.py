#!/usr/bin/env python3

# Python program to find the factorial of a number provided by the user.
#factorial of 5 is the number
#1 * 2 * 3 * 4 * 5 = 120 
# change the value for a different result
#num = 7

# To take input from the user

num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero

if num < 0:
    
   print("Sorry, factorial does not exist for negative numbers")
   
elif num == 0:
    
   print("The factorial of 0 is 1")
   
else:
    
#now we are trying to get range from 1 to range , num , always it will come -1 ,
#if 5 then 4 will come , thats why we are giving num+1

   for i in range(1,num + 1):
       
       factorial = factorial*i
       
   print("The factorial of",num,"is",factorial)