###To check the check the string charachter check the
### asked in ctrix 06/07/2021 - due to that i am failed 

###get the string charachter

##### to get counter i am importing counter moudule

from collections import Counter

i=input('enter the string')

####### which charachter frequency do you want to check 

j=input("enter the charachter frequency")

count = Counter(i)

print("checking the counting of charachter frequency" + str(count[j]))