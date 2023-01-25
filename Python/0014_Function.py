'''
----------------------------------------------- function -----------------------------------------------

- Functions are used to implement a segment of a code which can be reusable.

Syntax:
	
	# function defination
	def function_name(argument1, argument2, ...):
		# statements
		return

	# calling a function
	# here parameters are passed with positional arguments
	function_name(parameter1, parameter2, ...)

'''

''' UNCOMMENTABLE BLOCK OF CODE
def fun1(message):
	print(message)
	return print(message)

return_value = fun1(input("Enter something: "))
print(return_value)
'''

'''
Output:

Enter something: example
example
example
None
'''


'''
Default arguments: ------------------------------------------------------------------------------------

- default arguments are the one which would be used by default when the parameter is not passed for that argument.

Syntax:

	def fun_arg(arg = some_value):
		print(arg)

	# passing the value of parameter here
	fun_arg(value1)

	# not passing the value here
	fun_arg()
'''

''' UNCOMMENTABLE BLOCK OF CODE
def fun_arg(arg = "some default value"):
	print(arg)

fun_arg("not default value")
fun_arg()
'''

'''
Output:

not default value
some default value
'''

'''
Keyword arguments: ------------------------------------------------------------------------------------

- Keyword arguments are used when specifically the parameter for the some particular argument is to be passed.

Syntax:

	def fun_keyword(arg1, arg2):
		print(arg1, " and ", arg2)

	# using keywords to pass the parameter for the arguments
	fun_keyword(arg2 = "arg2_value", arg1 = "arg1_value")

	# not using keywords to pass the parameter for the arguments
	fun_keyword(param1, param2)
'''

''' UNCOMMENTABLE BLOCK OF CODE
def fun_keyword(arg1, arg2):
	print(arg1, "and", arg2)

fun_keyword(arg2 = "arg2_value", arg1 = "arg1_value")

fun_keyword("param1", "param2")
'''

'''
Output:

arg1_value and arg2_value
param1 and param2
'''


'''
Arbitrary arguments: ------------------------------------------------------------------------------------

- This can be used when we don't know the number of arguments(of same type) to be passed.
- This can be used at last argument.

Syntax:

	def fun_arb(arg1, *arb_arg):
		print(arg1, end = " ")
		for val in arb_arg:
			print(val, end = " ")
		print()

	fun_arb(param1, param2, param3)
	fun_arb(param1, param2, param3, param4)
'''


def fun_arb(arg1, *arb_arg):
		print(arg1, end = " ")
		for val in arb_arg:
			print(val, end = " ")
		print()

fun_arb("param1", "param2", "param3")
fun_arb("param1", "param2", "param3", "param4")


'''
Output:

param1 param2 param3 
param1 param2 param3 param4 
'''