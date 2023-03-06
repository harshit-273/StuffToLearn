'''
----------------------------------------------- Tuple -----------------------------------------------

- Tuple is same as List, just that Lists are mutable(changable) while Tuples are immutable.
- Anything can not be added or removed from the tuple, just the entire tule can be changed
- Tuples have slightly better performance for iterating as compared to lists as tuples are immutable.
- Tuples that contain immutable elements can be used as the key for a dictionary(another datatype, coming soon...)

Syntax:

	t1 = ()
'''

'''UNCOMMENTABLE BLOCK OF CODE
t1 = ()
print(t1)

t1 = ("some value")		# this is a string
print("type of t1 is", type(t1))	
t2 = ("some other value", )		# to declare a tuple with one value `,` needs to be used
print("type of t2 is", type(t2))
'''

'''
Functions for Tuple: ----------------------------------------------------------------------------------------------

Syntax:

	t1.count(some_element)	- would return the count of the element passed as the argument
    t1.index(some_element)	- would return the first occurring index of the value passed in the the parameter.
'''


t1 = ('h', 'a', 'r', 's', 'h', 'i', 't')
print(t1.count('h'), "'h' in", t1)
print(t1.index('i'), "is the index of 'i' in", t1)