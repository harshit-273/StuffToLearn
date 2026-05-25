# Dictionary - {key:value}

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

"""
Output:
{0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
two
None
{0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', -1: 'minus one'}
{0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', -1: 'negative one'}
{0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
dict_keys([0, 1, 2, 3, 4, 5])
dict_values(['zero', 'one', 'two', 'three', 'four', 'five'])
dict_items([(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])
"""