# BMI = weight(in kg)/height(in m) ** 2

weight = int(input("Enter weight in Kg"))
height = int(input("Enter height in cms"))/100

bmi = weight/(height**2)
print("Your BMI is ", bmi)