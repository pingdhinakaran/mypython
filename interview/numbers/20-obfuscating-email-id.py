""""
#Obfuscating Email ID program using python.

#Information like email id and other contact details need to be handled in a way so that the privacy of the user is safeguarded way to do this is to hide or partially hide such information also called obfuscating the information give me the email ID is input the program should of obfuscated the ID as follows:
# -*- coding: utf-8 -*-- For the given mail ID the part that comes before at the rate is referred to as the first part is there is no correct know @ collector mail ID is invalid

- If the first part of the email is less than or equal to 5 characters in length replace all characters in the first part with star.
- If the first of the email ID is greater than 5 characters in length print first 3 character as is and replace the remaining characters of the first part with star 

- If the email is invalid print invalid input


Sample:
input:
abcd@gmail.com
output:
****@gmail.com

Sample:
input:
abcdefghi@gmail.com
output:
abc******@gmail.com
"""

def process_mail(mailid):
    # Write Code here
    if "@" not in mailid:
        return "Invalid Input"
    mail_splitted = mailid.split("@")
    if len(mail_splitted[0])>5:
        return mailid[0:3] + ("*"*(len(mail_splitted[0])-3)) + "@"+mail_splitted[1]
    elif len(mail_splitted[0])<=5:
        return ("*"*(len(mail_splitted[0]))) + "@"+ mail_splitted[1]
    else:
        return "Invalid Input"
    

mailid = input()
print(process_mail(mailid))