#anagram python using funcation 

def ana(a,b):

	if sorted(a) == sorted(b):
		print (a, b, "anagram string")

	else:
		print (a, b, "this string is not anagram")

ana('krupa','karan')

ana('listen','silten')




