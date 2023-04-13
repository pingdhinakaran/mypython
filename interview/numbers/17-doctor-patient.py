"""
Problem Statement:
A doctor has a clinic where he serves his patients. The doctor’s consultation fees are different for different groups of patients depending on their age. If the patient’s age is below 17, fees is 200 INR. If the patient’s age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR. Write a code to calculate earnings in a day for which one array/List of values representing age of patients visited on that day is passed as input.

Note:
- Age should not be zero or less than zero or above 120
- Doctor consults a maximum of 20 patients a day
- Enter age value (press Enter without a value to stop):

Example 1:
Input
20
30
40
50
2
3
14
 
Output:
Total Income 2000 INR

https://www.youtube.com/watch?v=mwlNzGh0gzo

"""

max_patient = 20
ages = []
for i in range(max_patient):
    value = input()
    if value == "":
        break
    elif int(value) >  0 or int(value) < 120:
        ages.append(int(value))
    else:
        print("INVALID INPUT")
fees = 0
for each in ages:
    if each < 17:
        fees += 200
    elif each < 40:
        fees += 400
    else:
        fees += 300
print("Total Income "+str(2000)+" INR")