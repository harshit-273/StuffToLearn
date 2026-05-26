# function

def without_param(): # function without any parameters
	print("This is a function without any parameters")

without_param()

"""
Output:
This is a function without any parameters
"""

def with_param(some_param, some_other_param): # function with a parameter
	print(f"This is a function with parameters: \"{some_param}\" and \"{some_other_param}\"")

with_param("The argument", "other argument")

"""
Output:
This is a function with parameter: "The argument" and "other argument"
"""

def with_return(): # function with a return value
	return "some return value"

print(with_return())

"""
Output:
some return value
"""

def default_params(zero, one="default_1", two="default_2"): # function with default parameters, default parameters are always at the end
	print(f"{zero} {one} {two}")

default_params("non-default", "modified_default_1", "modified_default_2") # passing all the arguments
default_params("non-default") # passing only non default arguments
default_params("non-default", "set_to_default_1") # passing one non-default and one default argument. It will pick the first argument which is default and will modify it as per positional parameter rule
default_params("non-default", two="set_to_default_2") # using keywords to pass a specific argument, here the order will not matter as well
# default_params(one="set_to_default_1", "non-default") # gives error as any positional argument should be passed first and then the default arguments:- SyntaxError: positional argument follows keyword argument

"""
Output:
non-default modified_default_1 modified_default_2
non-default default_1 default_2
non-default set_to_default_1 default_2
non-default default_1 set_to_default_2
"""

def var_params(*params, **keyword_params): # function with variable number of positional parameter and variable number of keyword parameters
	# print(type(params), type(keyword_params)) # gives: <class 'tuple'> <class 'dict'>
	print(params, keyword_params)

var_params()
var_params("var_param_1", "var_param_2", "var_param_3", keyword_parameter_1="keyword_param_1", keyword_parameter_2="keyword_param_2")

"""
Output:
() {}
('var_param_1', 'var_param_2', 'var_param_3') {'keyword_parameter_1': 'keyword_param_1', 'keyword_parameter_2': 'keyword_param_2'}
"""

def pass_function(): # function which is not implemented but which will not cause any issue if code is run
	pass