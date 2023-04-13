#Odd Even Difference
#Write a program to return the difference between the sum of odd and even numbers 
# from an array of positive integers.

n = int(input())
num_list = list(map(int, input().split()))

even_sum = 0
odd_sum = 0

for each in num_list:
    if each % 2 == 0:
        even_sum += each
    else:
        odd_sum += each

print(odd_sum - even_sum)