text = input("enter a charater to check")

vowel=['a','e','i','o','u','A','E','I','O','U']

for i in text:
    
    if i in vowel: #### if condition to check
        
        print (text,i,"is vowel")
        
    else:
    
        print (text,i, "its not vowel")
