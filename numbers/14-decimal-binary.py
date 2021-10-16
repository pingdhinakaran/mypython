#"""
#Convert Decimal to Binary using Python
#"""
num = int(input())
string = ""
while num > 1:
    string += str(num%2)
    num = num//2
else:
    string += str(num)
binary = string[::-1]
print(binary)