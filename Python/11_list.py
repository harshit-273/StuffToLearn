# List  - []

l = [] # empty list
print(l)
some_list = ["apple", 45, False] # defination and declaration of a non-empty list
other_list = [4, 5, 65, -25, 0, 2]
print(some_list) # printing the entire list
print(some_list[1]) # printing one of the element of the list
print(some_list[0][-1]) # treating the element as normal variable
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

"""
Output:
[]
['apple', 45, False]
45
e
['apple', 45, False, 45]
2
['apple', 45, False, 45, 1, 'two', 3.0]
['apple', 45, False, 45, 'two', 3.0]
2
['zero', 'apple', 45, False, 45, 'two', 3.0]
['apple', 45, False, 45, 'two', 3.0]
[3.0, 'two', 45, False, 45, 'apple']
[-25, 0, 2, 4, 5, 65]
"""