#Convert Binary to Decimal using Python
#"""
binary = int(input())
binary_str = str(binary)
decimal = 0
for i in range(len(binary_str)):
    decimal += int(binary_str[i]) * (2**(len(binary_str)-i-1))
print(decimal)