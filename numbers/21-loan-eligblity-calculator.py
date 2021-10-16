
"""
Loan Eligiblity Calculator - IBM Coding April 2021
1. Type of employement can be salaried or self-employed.
2. Age limit for the Individuals: 21 to 58 years 
3. Minimum salary for Salaried employee: 
   Rs10,000 per month ie 1,20,000 per annum 
4. Minimum salary for Self-Employed:
   200,000 per annum
5. Maximum loan term: 30 years 
6. Present age plus Loan term should be less than or equat to his retirement age pf 58.

If above case fulfilled, return "Eligible", else "Not eligible"

For example:
a person in age 32 and applies for home loan for a term of 30 years, 
then he is not eligible because his present age + loan term is 62 years 
which is greater than the retirement age of 58. 


Input Format:
empType: a String
age: an Integer
salary: an Integer
loanTerm: an Integer


Ex - 
Input-
salaried
29
300000
25
Output-
Eligible


Ex - 
    Input-
    salaried
    29
    300000
    25
    Output-
    Eligible
"""

def check_eligiblity(empType, age, salary, loanTerm):
    # Your Code inside a function
    eligible = True
    if not(empType=="self-employed" or empType=="salaried"):
        eligible = False
    if not(age>=21 or age<=58):
        eligible = False
    if empType=="self-employed":
        if salary < 200000:
            eligible = False
    if empType=="salaried":
        if salary < 120000:
            eligible = False
    if loanTerm > 30:
        eligible = False
    if (age + loanTerm) > 58:
        eligible = False
    
    if eligible == False:
        return "Not eligible"
    return "Eligible"
    



empType = input()
age = int(input())
salary = int(input())
loanTerm = int(input())
print(check_eligiblity(empType, age, salary, loanTerm))