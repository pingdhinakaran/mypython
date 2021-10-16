####Method 1

#text = input("enter a charater to check")

#vowel=['a','e','i','o','u','A','E','I','O','U']

#if text in vowel: #### if condition to check 
#    print(text," is vowel")
#else:
#    print (text,"is not vowel")

### Method 2
text = input("enter a charater to check")

if (text == 'a' or text =='e' or text =='i' or text =='0' or text =='u' or text == 'A' or text =='E' or text =='I' or text =='O' or text =='U'):
     
    print (text,"is vowel")
    
else:
    
    print (text, "is not vowel")
