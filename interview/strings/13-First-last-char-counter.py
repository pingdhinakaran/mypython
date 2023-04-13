#Expanation:
#In Example 1,
#Str = "school"
#starting character of Str is "s" and ending character is "l".  So they both are not the same. Hence the output is zero.

#In Example 2,
#Str = "noon"
#Both the start and end character of Str is 'n' that's why we have to find the occurrence of the given character 'o'.  'o' is two times in noon hence the output is 2.
#"""
#///

str = input()
char = input()
if len(str)<2:
    print(-1)
elif str[0] == str[-1]:
    print(str.count(char)) # It will print the occurence of the char
else:
    print(0)