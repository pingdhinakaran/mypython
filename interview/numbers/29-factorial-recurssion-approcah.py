# Python 3 program to find  
# factorial of given number  
def fact(n):  
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
        
    #return 1 if (n==1 or n==0) else n * fact(n - 1);  

num = 3
print("Factorial of",num,"is",fact(num))