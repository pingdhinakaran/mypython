#"""
#Write a program to find the sum of cubes of natural numbers up to n.
#"""
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += (i*i*i)
print(sum)