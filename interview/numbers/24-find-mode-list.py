# Python Program to find the Mode of a list containing numbers.
numbers = [11,7,5,3,15,11,9,12,11] # 11
frequency_dict = {}
for each in numbers:
    if each not in frequency_dict:
        frequency_dict[each] = 1
    else:
        frequency_dict[each] += 1
mode = [key for key,value in frequency_dict.items() if value==max(frequency_dict.values())]
print(mode) # 11