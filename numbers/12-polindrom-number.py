###!/usr/bin/env python3

def check_palindrome(number):
    if str(number)[::-1] == str(number):
        return 1
    return 0

def sum_reverse(number):
    reverse = str(number)[::-1]
    return number + int(reverse)

number = int(input())
while True:
    reversed_sum = sum_reverse(number)
    if check_palindrome(reversed_sum):
        break
    else:
        number = reversed_sum
print(reversed_sum)