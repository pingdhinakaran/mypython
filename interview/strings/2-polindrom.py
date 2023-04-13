import pdb
def poli(s):
	if s == s[::-1]:
		print (s, "string is polidarom")
	else:
		print (s, "String is not polidarom")

poli('dhinakaran')
poli('malayalam')