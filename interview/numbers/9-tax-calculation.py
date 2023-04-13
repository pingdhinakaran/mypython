#!/usr/bin/env python3

def totalTax(amount_array):
    tax = 0
    for each in amount_array:
        if each > 1000:
            tax += (each - 1000) * 0.10
    return int(tax)

num = int(input())
amounts = list(map(int, input().split()))

tax = totalTax(amounts)
print(tax)