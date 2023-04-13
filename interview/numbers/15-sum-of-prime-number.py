
###Write a python program to add 10 subsequent prime numbers from the given prime number.
def checkPrime(num):
    for i in range(2,num):
        if num%i==0:
            return 0
    return 1

number = int(input())
sum = 0
count = 0
while count !=10:
    if checkPrime(number):
        sum += number
        count += 1
    number += 1
print(sum)