'''
----------------------------------------------- Anonymous or Lambda Function -----------------------------------------------

- It is a function without a name.

Syntax:

	lambda args : expression

'''

'''UNCOMMENTABLE BLOCK OF CODE
lambda_fun = lambda something : print("printing", something)

lambda_fun("anything")
'''

'''
Output:

printing anything
'''

'''
Filter with lambda: -------------------------------------------------------------------------------------------------------

- filter() function is used to filter out the values from an iterable.
- It returns the values from the list which evaluates the values to true from the guven function

Syntax:

	filter(function, iterable)
'''

''' UNCOMMENTABLE BLOCK OF CODE
def fun(arg):
	return (arg % 2 == 0)

print(list(filter(fun, [1, 2, 3, 4])))
print(list(filter(lambda x : (x % 2 != 0), [1, 2, 3, 4, 5])))
'''

'''
Output:

[2, 4]
[1, 3, 5]
'''

'''
Map with lambda: --------------------------------------------------------------------------------------------------------------

- map() function is used for mapping each value in iterable with the exression of the function

Syntax:

	map(function, iterable)
'''

print(list(map(lambda x : x*x, [1, 2, 3, 4, 5, 6])))

