#!/usr/bin/env python3

num = int(input())
numbers = list(map(int, input().split()))
total_feet = 0
for each in numbers:
    feet = each//12
    if feet:
        total_feet += feet
print(total_feet)