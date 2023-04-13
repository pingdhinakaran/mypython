# Python Program to find the Median of a list containing numbers.
numbers = [1,2,3,4,5]
num_len = len(numbers)
if num_len%2==0:
    med1 = numbers[num_len//2]
    med2 = numbers[num_len//2 - 1]
    median = (med1 + med2)/2
else:
    median = numbers[num_len//2]
print(median)

