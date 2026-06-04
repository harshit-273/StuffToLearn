# Python

> Comments
```python
# Single line comment

"""
Multiline
comment
"""

'''
Also a
multiline
comment
'''
```



## [First Program](./00_first_program.py "First Python Program with it's output")

- File extension for python is `.py`.
- To run a python program use command:
``` 
python file_name.py
```

## [Variables](./01_variables.py "Variables in python.")

- A container for a value.

### `string`

- Can be stored in `''(Single Quotes)` or `""(Double Quotes)`
- For a better format of the variables to be printed:

```python
some_variable = "some value"
print(some_variable)
print(f"Printing the value \"{some_variable}\" for variable \"some_variable\"")
```

Output:
``` 
some value
Printing the value "some value" for variable "some_variable"
```

### `integer`

- If you store numbers without any decimal points then those are integers.

```python
some_integer = 5
print(some_integer)
```

Output:
``` 
5
```

### `float`

- If you are storing a number with a decimal point then those numbers are called floating point numbers.

```python
some_float = 10.00
print(f"My package is {some_float} LPA")
```

Output:
``` 
My package is 10.0 LPA
```

### `boolean`

- Mostly used for true or false like storing options.
- Uses keywords **True** and **False**.

```python
is_true = True
is_false = False
print(f"Is the variable \"is_true\" true? \"{is_true}\"")
```

Output:
``` 
Is the variable "is_true" true? "True"
```

## [Type Casting](./02_type_casting.py "Type Casting in python")

- The process of converting one data type to another.

### `type()` - Used to get the type of the varaible passed in the brackets.

```python
name = "Harshit"
age = 26
is_male = True
gpa = 7.1

print(type(name))
print(type(age))
print(type(is_male))
print(type(gpa))
```

Output:
``` 
<class 'str'>
<class 'int'>
<class 'bool'>
<class 'float'>
```

### `str()` - Used to convert any data within the brackets to string.

```python
house_no = 1
print(type(house_no))

house_no = str(house_no)
print(type(house_no))
```

Output:
``` 
<class 'int'>
<class 'str'>
```

### `int()` - Used to convert any data within the bracets to integer if possible.

### `float()` - Used to convert any data within the brackets to floating point number if possible.

### `bool()` - Used to convert any data within the brackets to f=boolean value.

- When any string is converted to a boolean value, the empty(`""`) string will give `False` and non-empty string will give `True`.

## [User input](./03_user_input.py "User input in python")

### `input()` - Get the input from the user in string.

```python
name = input("What is your name? ")
age = int(input("What is your age? "))

next_age = age + 1

print(f"Your name is {name}.")
print(f"On your next birthday, you will be {next_age} years old.")
```

Output:
```
What is your name? Harshit
What is your age? 26
Your name is Harshit.
On your next birthday, you will be 27 years old.
```

## [Operators](./04_operators.py "Operators")

### Arithmetic Operators

| Operators | Usage | Example | Output |
| --------- | ----- | ------- | ------ |
| + | For adding two numbers or for concating two strings. | `1+2`, `"ab"+"yz"` | `3`, `"abyz"` |
| - | For subtracting one number from another. | `5-2` | `3` |
| * | For multiplying two numbers. | `3*4` | `12` |
| / | For dividing one number from another. Always gives a float. | `5/2` | `2.5` |
| // | For dividing one number from another. Always gives an int. | `5//2` | `2` |
| ** | For one number powered to another number. | `5**2` | `25` |
| % | For finding the remainder when one number divides another. | `5%2` | `1` |

### Comparison Operators

- Always results in boolean value.

| Operators | Usage | Example | Output |
| --------- | ----- | ------- | ------ |
| < | For finding if the number on left is less than the number on right. | `5<2` | `False` |
| > | For finding if the number on left is greater than the number on right. | `5>2` | `True` |
| <= | For finding if the number on left is less than or equal to the number on right. | `5<=5` | `True` |
| >= | For finding if the number on left is greater than or equal to the number on right. | `5>=5` | `True` |
| == | For comparing two values. | `2==4` | `False` |
| != | For comparing inequality of two values. | `2!=4` | `True` |
| is [not] | For comparing two objects. | `["apple", "banana", "cherry"] is ["apple", "banana", "cherry"]` | `False` |
| [not] in | For testing the membership or iterating. | `2 in [1, 2, 3]` | `True` |

### Bitwise Operators

- Performs arthmetic operations on bits.

| Operators | Usage | Example | Output |
| --------- | ----- | ------- | ------ |
| & | For bitwise and operation. | `1&0` | `0` |
| \| | For bitwise or operation. | `1\|0` | `1` |
| ~ | For bitwise not operation. | `~0` | `-1` |
| ^ | For bitwise XOR operation. | `3^1` | *11*^*01* = `2` |
| << | For moving the bits of number a few times to left. | `1<<2` | 1 * (2**2) = `4` |
| >> | For moving the bits of number a few times to right. | `4>>2` | 4 // (2**2) = `1` |

### Logical Operators

| Operators | Usage | Example | Output |
| --------- | ----- | ------- | ------ |
| and | For checking if both the conditions are true. | `1<2 and 3>2` | `True` |
| or | For checking if both the conditions are false. | `1>2 or 3<2` | `False` |
| not | For checking if a condition is false. | `not True` | `False` |

### Assignment Operators

- For assigning the value to a variable.

| Operators | Usage | Example |
| --------- | ----- | ------- | 
| = | For assigning the value of right side to left side variable. | `a = 45` |
| += | For adding the value on right to the left side variable. | `b += 2` |
| -= | For subtracting the value on right from the left side variable. | `c -= 3` |
| *= | For multiplying the value on the right to the left side variable. | `m *= 4` |
| /= | For dividing the value of left side variable with right side value. | `d /= 2` |
| //= | For dividing the value on left side varaible wth the right side value to obtain a integer result. | `e //= 4` |
| %= | For getting the remainder of the value on left side variable with the right side value and assign it to the left side varaible. | `a %= b` |
| **= | For assigning the value of left side varaible to left side varaible's to the power of right side. | `a **= b` |
| &= | For assigning the left side variable by performing bitwise `&` with right side. | `a &= b` |
| \|= | For assigning the left side variable by performing bitwise `\|` with right side. | `a \|= b` |
| ^= | For assigning the left side variable by performing bitwise `^` with right side. | `a ^= b` |
| <<= | For assigning the left side variable by performing bitwise `<<` with right side. | `a <<= b` |
| >>= | For assigning the left side variable by performing bitwise `>>` with right side. | `a >>= b` |

## [Maths operations](./05_maths_operation.py "Maths Operations") 

- Few of the function will require `math` to be imported.

```python
import math
```

### `round()` - Used to round a number to it's nearest integer(if round off is not defined).

```python
print(round(3.14), round(3.14, 1))
```

Output:
```
3 3.1
```

### `abs()` - Used to get the absolute distance from 0 on the numer line.

```python
print(abs(-4))
```

Output:
```
4
```

### `max()` - Used to get the maximum of the given numbers.

```python
print(max(4, 3, 7))
```

Output:
```
7
```

### `min()` - Used to get the minimum of the given numbers. 

```python
print(min(2, 0, -1))
```

Output:
```
-1
```

### `math.ceil()` - Used to get the largest integer smaller than or equal to the number.

```python
print(math.ceil(4.01), math.ceil(-4.01))
```

Output:
```
5 -4
```

### `math.floor()` - Used to get the smallest integer larger than or equal to the number.

```python
print(math.floor(4.9), math.floor(-4.9))
```

Output:
```
4 -5
```

## [if elif else](./06_if_else_elif.py "If Elif Else")
- `if` - When someting is true for the given condition, block inside it will be executed.
- `elif` - When something is true for the given condition, block inside this will be executed.
- `else` - When none of the previously mentioned blocks gets executed it will be the default block to be executed.

```python
x = 4
if x < 0:
	print(f"{x} is less than 0.")
elif x > 0:
	print(f"{x} is greater than 0.")
else:
	print(f"{x} is 0.")
```

Output:
```
0 is 0.

-3 is less than 0.

4 is greater than 0.
```

### [Conditional Expression](./07_conditional_expression.py "Conditional Expression")

Syntax:
```python
X if condition else Y
```

```python
x = 2
print("Even" if x%2 == 0 else "Odd")
```

Output:
```
Even
```

## [String Methods](./08_string_methods.py "String Methods")

### `len()` - Used to get the length of the object passed as parameter.

```python
len("Harsh it")
```

Output:
```
8
```

### `find()` - Used to find the 1st occurrence of string passed as parameter.

```python
print("abc".find("b"))
```

Output:
```
1
```

### `rfind()` - Used to find the last occurrence of string passed as parameter.

```python
print("aabbc".rfind("b"))
```

Output:
```
3
```

### `capitalize()` - Used to capitalize the first letter of the string.

```python
print("aabbc".capitalize())
```

Output:
```
Aabbc
```

### `upper()` - Used to convert the entire string to uppercase.

```python
print("aabbc".upper())
```

Output:
```
AABBC
```

### `lower()` - Used to convert the entire string to lowercase.

```python
print("AaBbC".lower())
```

Output:
```
aabbc
```

### `isalpha()` - Used to check if it is alphanumeric string.

```python
print("H27".isalpha())
```

Output:
```
True
```

### `isdigit()` - Used to check if the entire is a number.

```python
print("27".isdigit())
```

Output:
```
True
```

### `count()` - Used to count the occurrence of the parameter in the string.

```python
print("abc aa".count("a"))
```

Output:
```
3
```

### `replace()` - Used to replace the all the occurrence of the substring with the given string.

```python
print("abc aa".replace("a", "b"))
```

Output:
```
bbc bb
```

## [Indexing](./09_indexing.py "Indexing")

Syntax:
```python
var_name[start:end:difference]
```

- If __start__ is not provided, the string will start from the 1st index.
- If __end__ is not provided, the string will end at last index.
- __difference__ is the differnce between the indexes, by default is considered `1`, meaning all the characters in string will be considered in normal sequential order.
- We can also use negative indexing in python, where `-1` is considered as the last index.

Example:
```python
print(f"The string - \"{some_str}\"")
print(f"First element of the string - {some_str[0]}")
print(f"Last element of the string - {some_str[-1]}")
print(f"Entire string starting from 2nd character - \"{some_str[1:]}\"")
print(f"Entire string ending before last character - \"{some_str[:-1]}\"")
print(f"Entire string without and even position elements - \"{some_str[::2]}\"")
print(f"Entire string but backwards - \"{some_str[::-1]}\"")
```

Output:
```
The string - "Harshit Kalavadia"
First element of the string - H
Last element of the string - a
Entire string starting from 2nd character - "arshit Kalavadia"
Entire string ending before last character - "Harshit Kalavadi"
Entire string without and even position elements - "HrhtKlvda"
Entire string but backwards - "aidavalaK tihsraH"
```

## [Format Specifiers](./10_format_specifiers.py "Format Specifiers")

- To format the number format specifiers are used.

Syntax:

### `{num:<}` - Left Justified
### `{num:>}` - Right Justified
### `{num:.decimal_places_numf}` - __decimal_places_num__ is used to specify the number of positions after the decimal point, __f__ at the end is for the floating point.
### `{num:padding_num}` - number is padded with __padding_num__ spaces.
### `{num:0padding_num}` - number is padded with __0__ __padding_num__ times.

```python
num = -123.45678
print(f"Number:{num}")
print(f"Number is rounded for \"3\" decimal places:{num:.3f}")
print(f"Number is allocated \"10\" spaces:{num:10}")
print(f"Number is allocated \"20\" spaces and padded with \"0\":{num:020}")
print(f"Number is allocated \"20\" spaces and is right justified:{num:>20}")
print(f"Number is allocated \"20\" spaces, padded with \"0\" and is left justified:{num:<020}")
print(f"Number is rounded for \"3\" decimal places, allocated \"20\" spaces with padded \"0\", right justified:{num:>020.3f}")
```

Output:
```
Number:-123.45678
Number is rounded for "3" decimal places:-123.457
Number is allocated "10" spaces:-123.45678
Number is allocated "20" spaces and padded with "0":-0000000000123.45678
Number is allocated "20" spaces and is right justified:          -123.45678
Number is allocated "20" spaces, padded with "0" and is left justified:-123.456780000000000
Number is rounded for "3" decimal places, allocated "20" spaces with padded "0", right justified:000000000000-123.457
```

## [List](./11_list.py "List")

- Lists are ordered and changeable group of objects.
- Duplicates are allowed.

```python
l = [] # empty list
print(l)
some_list = ["apple", 45, False] # defination and declaration of a non-empty list
other_list = [4, 5, 65, -25, 0, 2]
print(some_list) # printing the entire list
print(some_list[1]) # printing one of the element of the list
print(some_list[0][-1]) # treating the element as normal variable
print(len(some_list)) # gives the length of the current list
print("apple" in some_list) # gives a boolean if the object is present in the list
# print(dir(some_list)) # getting all the things related to the type of list
# print(help(some_list)) # detailed help on all the things related to the type of the list
some_list.append(45) # adding an element at the end of the list
print(some_list)
print(some_list.count(45)) # counting the number of occurrences of value
some_list.extend([1, "two", 3.0]) # adding a few elements to the list
print(some_list)
some_list.remove(1) # removing an element of the given value from the list
print(some_list)
print(some_list.index(False)) # getting first index of the value
some_list.insert(0, "zero") # insert a object at an index
print(some_list)
some_list.pop(0) # by default removes last element from the list if index is not specified
print(some_list)
some_list.reverse() # reversing the list
print(some_list)
other_list.sort() # sorting a list
print(other_list)
```

Output:
```
[]
['apple', 45, False]
45
e
3
True
['apple', 45, False, 45]
2
['apple', 45, False, 45, 1, 'two', 3.0]
['apple', 45, False, 45, 'two', 3.0]
2
['zero', 'apple', 45, False, 45, 'two', 3.0]
['apple', 45, False, 45, 'two', 3.0]
[3.0, 'two', 45, False, 45, 'apple']
[-25, 0, 2, 4, 5, 65]
[[0, 1, 2, 3, 4], ['zero', 'one', 'two', 'three']]
[[0, 1, 2, 3, 4], ['zero', 'one', 'two', 'three'], [0.0, 1.0, 2.0]]
two
```

## [Set](./12_set.py "Set")

- Set is unordered.
- Set values cannot be changed.
- We can just add or remove the objects in a set.

```python
set_of_things = {"zero", 1, 2.0}
print(set_of_things)
set_of_things.add(True) # True is not added to set as it is already present as 1. Booleans are a subtype of integers.
print(set_of_things)
set_of_things.add(False)
print(set_of_things)
set_of_things.remove(2.0)
print(set_of_things)
```

Output:
```
{1, 2.0, 'zero'}
{1, 2.0, 'zero'}
{False, 1, 2.0, 'zero'}
{False, 1, 'zero'}
```

## [Tuple](./13_tuple.py "Tuple")

- Tuple is ordered.
- Tuple cannot be changes, we can't even add or remove values.
- Tuple is faster.

```python
tup = (1, True, 0, False)
print(tup)
print(tup.index(True)) # gives 0 as, True is treated same a integer is treated
print(tup.count(0)) # 0 and False both are counted as same so gives 2.
```

Output:
```
(1, True, 0, False)
0
2
```

## [Dictionary](./14_dictionary.py "Dictionary")

- Can store key:value pair.
- It is ordered.
- It can be modified.

```python
numbers_spellings = {
	0: "zero",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five"
}

print(numbers_spellings)
print(numbers_spellings[2]) # getting specific value of the key.
# print(numbers_spellings[6]) 
# Will give an error as below:
# KeyError: 6
print(numbers_spellings.get(6)) # if Key does not exist, it gives None
numbers_spellings.update({-1: "minus one"}) # adds to the current dictionary if does not exist
print(numbers_spellings)
numbers_spellings.update({-1: "negative one"}) # updates, if already exists
print(numbers_spellings)
numbers_spellings.pop(-1) # removes an key:value pair when key is given as argument
print(numbers_spellings)
keys = numbers_spellings.keys() # will give all the keys
print(keys)
values = numbers_spellings.values() # will give all the values
print(values)
items = numbers_spellings.items() # will give list of tuples of entire dictionary
print(items)
```

Output:
```
{0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
two
None
{0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', -1: 'minus one'}
{0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', -1: 'negative one'}
{0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
dict_keys([0, 1, 2, 3, 4, 5])
dict_values(['zero', 'one', 'two', 'three', 'four', 'five'])
dict_items([(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])
```

## [Loops](./15_loops.py "Loops")

### `while` loop - Used when we want to execute a same code until a condition is false.

Syntax:
```python
while condition:
	# This block will be executed until the condition is false.
```

```python
exit = False

while False == exit:
	exit = True if "y" == input("Do you want to exit? Press \"y\" to exit:") else False

print("Thank you, you care good to go.")
```

Output:
```
Do you want to exit? Press "y" to exit:n
Do you want to exit? Press "y" to exit:no
Do you want to exit? Press "y" to exit:yes
Do you want to exit? Press "y" to exit:y
Thank you, you are good to go.
```

### `for` loop - Used when we want to execute a same code for a specific number of times.

- Iterable is group of things.

Syntax:
```python
for i in iterable:
	# This code will be executed for all the i's in the iterable
```

- `range()` function is used to get a sequence of numbers.
	- __start__ is the number we want to start at, __end__ is the we want to end before and __difference__ is the gap of numbers in the sequence.

Syntax:
```python
range(start, end, difference)
```

Example:
```python
for i in range(1, 11, 1):
	print(i, end=" ")
```

Output:
```
1 2 3 4 5 6 7 8 9 10
```

### for loop for dictionaries

```python
numbers_spellings = {
	0: "zero",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five"
}

for key, value in numbers_spellings.items():
	print(f"{key}: {value}")
```

Output:
```
0: zero
1: one
2: two
3: three
4: four
5: five
```

### `break` - Used to break out of the loop.

Example:
```python
while True:
	if "y" == input("Do you want to exit this loop?(Press y to exit):"):
		break

print("You have exitted the loop")
```
Do you want to exit this loop?(Press y to exit)
Output:
```
Do you want to exit this loop?(Press y to exit):n
Do you want to exit this loop?(Press y to exit):no
Do you want to exit this loop?(Press y to exit):yes
Do you want to exit this loop?(Press y to exit):y
You have exitted the loop
```

### `continue` - Used to continue the block of code by just skipping the current iteration after the keyword.

Example:
```python
# printing multiples of 3 or 5 but not of 3 and 5.

for i in range(0, 50, 1):
	if (i%3 == 0) and (i%5 == 0):
		continue
	elif i%3 == 0:
		print(i, end=" ")
	elif i%5 == 0:
		print(i, end=" ")
```

Output:
```
3 5 6 9 10 12 18 20 21 24 25 27 33 35 36 39 40 42 48
```

- A list`[]`, set`{}`, tuple`()`, dictionary and many other such thing are iterables.

## [Functions](./16_function.py "Functions")

- A function is a block of code which can be re-used.
- Parameters are in the defination of the function which can be processed to perform some action
- Arguments are the values we pass to the function which will be processed to perform some action

Syntax for defination of a function:
```python
def func(parameters):
	# some code block for process and result to return something
	return something # If the function returns something, this can be used
```

Syntax for calling a function:
```python
func(arguments)
```

### function without parameters

```python
def without_param():
	print("This is a function without any parameters")

without_param()
```
Output:
```
This is a function without any parameters
```

### function with a parameters
- Arguments we pass are positional, i.e. first argument will be processed for first parameter, second argument will be processed for second parameter and thus further.

```python
def with_param(some_param, some_other_param):
	print(f"This is a function with parameters: \"{some_param}\" and \"{some_other_param}\"")

with_param("The argument", "other argument")
```

Output:
```
This is a function with parameter: "The argument" and "other argument"
```

### function with a return value

```python
def with_return():
	return "some return value"

print(with_return())
```

Output:
```
some return value
```

### function with default parameters

- Default parameters( or arguments) are always at the end.
- When non-default and default arguments are passed together, all the non-default parameter will be assigned the values first and then default parameters will be assigned at last.
- If we want to assign a value to specific default parameter then we can use keyword arguments and for the keyword arguments, the order does not matter and should be assigned at last or else will result in error.

```python
def default_params(zero, one="default_1", two="default_2"):
	print(f"{zero} {one} {two}")

default_params("non-default", "modified_default_1", "modified_default_2") # passing all the arguments
default_params("non-default") # passing only non default arguments
default_params("non-default", "set_to_default_1") # passing one non-default and one default argument.
default_params("non-default", two="set_to_default_2") # using keywords to pass a specific argument, here the order will not matter as well
# default_params(one="set_to_default_1", "non-default") # gives error as any positional argument should be passed first and then the default arguments:- SyntaxError: positional argument follows keyword argument
```

Output:
```
non-default modified_default_1 modified_default_2
non-default default_1 default_2
non-default set_to_default_1 default_2
non-default default_1 set_to_default_2
```

### function with variable number of positional parameter and variable number of keyword parameters

- `*` is used for variable number of positional parameters.
- `**` is used for variable number of keyword parameters.
- All the positional parameters will be stored in a tuple.
- All the keyword parameters will be stored in a dictionary.

```python
def var_params(*params, **keyword_params):
	# print(type(params), type(keyword_params)) # gives: <class 'tuple'> <class 'dict'>
	print(params, keyword_params)

var_params()
var_params("var_param_1", "var_param_2", "var_param_3", keyword_parameter_1="keyword_param_1", keyword_parameter_2="keyword_param_2")
```

Output:
```
() {}
('var_param_1', 'var_param_2', 'var_param_3') {'keyword_parameter_1': 'keyword_param_1', 'keyword_parameter_2': 'keyword_param_2'}
```

### function which is not implemented but which will not cause any issue if code is run

```python
def pass_function():
	pass
```

## [try except else finally](./17_try_except_else_finally.py "try except else finally")
- `try` - a block of code where there is a chance of getting an `Exception`.
- `except` - a block of code where we process the get and process that specific exception unless it is `Exception` itself.
- `else` - a block of code executed if there are no exceptions.
- `finally` - a block of code executed no matter if an exception occurs or not

Syntax:
```python
try:
	# code where the exception might occur
except SomeError as e:
	# code to prevent the stopping of execution of the program if some error "e" occurs
except Exception as e:
	# code to prevent the stopping of execution of the program if any error occurs
else:
	# code to be executed if no exception occurs
finally:
	# code to be executed no matter if a exception occurs or not
```

### When no try-except is used
```python
print("Performing a division opeartion")
num1 = int(input("Enter a number to be divided: "))
num2 = int(input("Enter a number to divide: "))
print(f"division is {num1 / num2}")
```

Output:
```
Performing a division opeartion
Enter a number to be divided: 2
Enter a number to divide: zero
Traceback (most recent call last):
  File "...File/path...", line number, in <module>
    num2 = int(input("Enter a number to divide: "))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'zero'
```

### When try-except is used

```python
try:
	num1 = int(input("Enter a number to be divided: "))
	num2 = int(input("Enter a number to divide: "))
	print(f"division is {num1 / num2}")
except ValueError as e:
	print(f"a non-number cannot be converted to number: {e}")
```

Output:
```
Performing a division opeartion
Enter a number to be divided: 3
Enter a number to divide: zero
a non-number cannot be converted to number: invalid literal for int() with base 10: 'zero'
```

### When try-except-else is used and no exceptions occur

```python
try:
	num1 = int(input("Enter a number to be divided: "))
	num2 = int(input("Enter a number to divide: "))
	print(f"division is {num1 / num2}")
except ValueError as e:
	print(f"a non-number cannot be converted to number: {e}")
except ZeroDivisionError as e:
	print(f"Cannot divide by 0: {e}")
else:
	print("No errors occurred")
```

Output:
```
Performing a division opeartion
Enter a number to be divided: 3
Enter a number to divide: 2
division is 1.5
No errors occurred
```

### When try-except-else-finally is used and exception occurs

```python
try:
	num1 = int(input("Enter a number to be divided: "))
	num2 = int(input("Enter a number to divide: "))
	print(f"division is {num1 / num2}")
except ValueError as e:
	print(f"a non-number cannot be converted to number: {e}")
except ZeroDivisionError as e:
	print(f"Cannot divide by 0: {e}")
else:
	print("No errors occurred")
finally:
	print("This will always be executed, doesn't matter if an exception occurs or not")
```

Output:
```
Performing a division opeartion
Enter a number to be divided: 4
Enter a number to divide: 0
Cannot divide by 0: division by zero
This will always be executed, doesn't matter if a exception occurs or not
```

## Module

- It is a file which we can import into the current program file of python and then use it.
- `import` is the keyword used to import the module.
- `from` is the keyword used to when we don't need entire module it's part to be imported.
- `as` is the keyword to give a different name.

Syntax when using a specific module part:
```python
from some_module import some_data

some_data() # if some_data is a function
somedata # if some_data is not a function and some object
```

Syntax when using the entire module:
```python
import some_module

some_module.some_data() # using a function inside the module
some_module.somedata # using the object or variable inside the module
```

- path of the module we are importing and program file are same then we can directly import it.

Syntax to import a file:
```python
import file_name # Give the file_name without extension of ".py" while importing the file
```

## [Class](./18_object_oriented_python.py "class")

- A `class` is a blueprint of some kind of object, which is used to create a object, or perform some action for object.
- A class variable is shared among all the objects created with this class.
- A method is a function for a class.
- A constructor is a special method used to create the object of a specific class.

### Syntax:
```python
class Some_class: # defining a class
	class_var = "shared variable across all the created objects"

	def __init__(self, property1, property2, property3): # defining a constructor
		self.property1 = property1
		self.property2 = property2
		self.property3 = property3
	
	def some_method(self): # defining class method
		# perform something
		print(f"Performing \"some_method\" of class \"Some_class\". There is a property - \"{self.property1}\" inside it. The class variable is - \"{Some_class.class_var}\"")

some_object = Some_class("prop1", "prop2", "prop3") # creating an object from a class

print(some_object.property1) # getting a value of the property
some_object.some_method() # executing a class method
```

Output:
```
prop1
Performing "some_method" of class "Some_class". There is a property - "prop1" inside it. The class variable is - "shared variable across all the created objects"
```

## [Inheritance](./19_inheritance.py "Inheritance")

- Inheritance allows to reuse the code and extending the code.
- There can be multiple inheritance meaning there can be multiple parents of a child class.
- There can also be multi level inheritance allowing code to be extended to grand child class.

```python
class Grand_Father:
	def grand_father_method(self):
		print("Inherited from Grand Father")

class Father(Grand_Father): # Class from which other classes will be inherited
	def __init__(self, name):
		self.name = name
	
	def father_method(self):
		print("Inherited from Father")

class Mother:
	def mother_method(self):
		print("Inherited from Mother")


class Son(Father): # Inherited class
	def own_method(self): # Own method
		print(f"Comes from the {type(self)}")

class Daughter(Father, Mother):
	pass

son1 = Son("name of son")
son1.father_method()
son1.own_method()
son1.grand_father_method()

daughter1 = Daughter("name of daughter")
daughter1.father_method()
daughter1.mother_method()
daughter1.grand_father_method()
```

Output:
```
Inherited from Father
Comes from the <class '__main__.Son'>
Inherited from Grand Father
Inherited from Father
Inherited from Mother
Inherited from Grand Father
```

## [`super()`](./20_super.py "super()")

- `super()` allows to use the method from the parent class to be extended in the child class.

```python
class Parent:
	def __init__(self, attribute1):
		self.attribute1 = attribute1
		print(f"Attribute - {self.attribute1}")

class Child(Parent):
	def __init__(self, attribute1, attribute2):
		super().__init__(attribute1)
		self.attribute2 = attribute2
		print(f"Attribute - {self.attribute2}")

ch = Child("one", "two")
```

Output:
```
Attribute - one
Attribute - two
```

## [lambda](./21_lambda.py "Lambda")

- Functions which can be written in a line.

Syntax:
```python
lambda parameters:expression
```

```python
add = lambda x, y, z: x+y+z
print(add(4, 5, 6))
print(add(1, 2, 3))

is_adult = lambda age: True if age >= 18 else False
print(is_adult(19))
```

Output:
```
15
6
True
```

### map

- A function which performs a expression on all the elements of the iterator.

Syntax:
```python
map(function, iterator)
```

```python
squared = lambda x: x*x
nums = list(range(1, 11, 1))
squared_nums = list(map(squared, nums))
print(f"{nums} => {squared_nums}")
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### filter

- A function which will filter the values which answered with True when passed to a function.

Syntax:
```python
filter(function, iterator)
```

```python
l1 = list(range(1, 31, 1))
multiple_of_3 = lambda x: x%3 == 0
multiples_of_three = list(filter(multiple_of_3, l1))
print(f"{l1} => {multiples_of_three}")
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30] => [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

### reduce

- A function which turns a iterator to a single value by performing the action on first two values continuesly repeating it.

Syntax:
```python
import functools

functools.reduce(function, iterator)
```

```python
l = list(range(1, 11, 1))
sum_l = functools.reduce(lambda x, y,: x+y, l)
print(f"{l} => {sum_l}")
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => 55
```

## [Static method](./22_static.py "Static method")

- A method that belongs to a class rather than the object(instance)

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	@staticmethod
	def is_adult(age): # static method
		return age >= 18
	
	def intro(self): # instance method
		print(f"I am {self.name} and I am {self.age} year/s old.")
	
some_person = Person("Kong", 18)
some_person.intro()
is_person_adult = "an Adult" if Person.is_adult(some_person.age) else "a Child"
print(f"{some_person.name} is {is_person_adult}")
```

Output:
```
I am Kong and I am 18 year/s old.
Kong is an Adult
```

## [`cls` method](./23_class_method.py "Class Method")

- A method used with the Class data.

```python
class Someclass:

	some_value = "some value"

	def __init__(self, data):
		self.data = data
	
	@classmethod
	def get_some_value(cls):
		return f"Class methods value is {cls.some_value}"
	
sc = Someclass("some data")
print(Someclass.get_some_value())
print(f"Instance data is {sc.data}")
```

Output:
```
Class methods value is some value
Instance data is some data
```