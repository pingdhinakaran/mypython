#Here is the python program to find the total execution time of a process.
#Code - 
import time # Import the time module
def process(number):
    sum = 0
    for i in range(number):
        sum += i
    return sum

start_time = time.time()
process(10) # Increase the number passed to increase the number of iteration in For Loop
end_time = time.time()

print(end_time - start_time, "seconds") # Let's test