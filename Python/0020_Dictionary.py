'''
----------------------------------------------- Dictionary -----------------------------------------------

- Dictionary are the set of ordered key-value pairs.

Syntax:

	dic1 = {key1: value1, key2: value2, ...}
'''

'''UNCOMMENTABLE BLOCK OF CODE

dic1 = {1: "one", 2: "two", 3: "three"}
print(dic1)
'''

'''
Adding/Updating items in Dictionary: ----------------------------------------------------------------------------------------------

Syntax:

	dic1[key1] = value1
'''

'''UNCOMMENTABLE BLOCK OF CODE

dic1 = {}
dic1[0] = "zero"
dic1[1] = "one"
print(dic1)
'''

'''
Removing from Dictionary: ----------------------------------------------------------------------------------------------

Syntax:

	del dic1[key1]	# this will remove key-value pair where key is key1
'''

'''UNCOMMETABLE BLOCK OF CODE

dic1 = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}
print(dic1)

del dic1[4]
print(dic1)
'''

'''
Iterating through Dictionary: ----------------------------------------------------------------------------------------------

Syntax:

	for key in dic:
		print(key, dic[key])
'''

dic1 = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}

for ky in dic1:
    print(f'{ky}: {dic1[ky]}')
