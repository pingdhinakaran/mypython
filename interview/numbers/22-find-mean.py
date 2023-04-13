# Python Program to find the mean of a list containing numbers.
numbers = [4, 5, 8, 9, 10, 17]
# Method 1
mean_1 = sum(numbers)/len(numbers)
print(mean_1)

# Method 2
sum_num = 0
for each in numbers:
    sum_num += each
mean_2 = sum_num/len(numbers)
print("Mean 2 is", mean_2)