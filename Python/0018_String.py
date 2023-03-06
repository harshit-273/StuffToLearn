'''
----------------------------------------------- String -----------------------------------------------

- Strings are the sequence of the characters.
- Strings are immutable.
- Any characters in the string can accessed in the same way as in tuple

Syntax:

	s1 = "string1"
    s2 = 'string2'
    
- Even multiline strings can be created, use triple single quotes or triple double quotes(""") 

Syntax:

	s =  """Some
    string
    value"""
'''

'''UNCOMMENTABLE BLOCK OF CODE
multiline_string = """
some 
multiline
string
"""
print(multiline_string)
'''

'''
Comparing strings: ----------------------------------------------------------------------------------------------

- string can be compared in the same way the numbers are compared.
'''

'''UNCOMMENTABLE BLOCK OF CODE
s1 = "h1"
s2 = "h1"
s3 = "g2"

print(s1 == s2, s1 > s3)
'''

'''
Join strings: ----------------------------------------------------------------------------------------------

Syntax:

	s1 = "Hello, " + "World"
'''

'''UNCOMMENTABLE BLOCK OF CODE
s1 = "Hello, " + "and " + "welcome to my world."
print(s1)
'''

'''
String Functions: ----------------------------------------------------------------------------------------------

len(value)	- this function will return the length of the value passed

upper()		- this method will convert all the string characters to uppercase

lower()		- this method will convert all the string characters to lowercase

replace(old, new [, count])	- this method will replace the matching old substring with the new string count number of times, if the number of counts is not specified then it replaces all the old substrings

find(search_string[, start[, end]])	- this method will search the substring passed between the start and the end value.

split([separator, maxsplit)	- this method will spilt the string based on the separator and maxsplit, by default separator would be whitespace and maxsplit would not have limit.

index(sub_str [, start[, end]])	- this method is same as find method, but here if the substring is not present then it throws error
'''

s1 = "harshit kalavadia"

print(len(s1))
print(s1.upper())
print(s1.lower())
print(s1.replace("t", "l"))
print(s1.find("hi"))
print(s1.split(" "))
print(s1.index("k"))


