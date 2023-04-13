#reverse the string 

def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

print (reverse('dhinakaran'))


##########

####Another way of writing ######

#getting input from keykoard 

a=input('enter the string\n')

print (a, "actual string\n")

b=a[::-1]

print (b, "this is reversed string\n")