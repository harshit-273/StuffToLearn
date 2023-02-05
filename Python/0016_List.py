'''
----------------------------------------------- List -----------------------------------------------

- The datatypes which can store 0 or more other datatypes.
- List can contain different types of the datatypes in a same list.
- List are mutable(which can be changed) datatypes

Syntax:

	# empty list
	l1 = []

	# list with few elements
	l2 = [1, "two", 3.0]

	# accessing any element in a list
	print(l2[1])

'''

'''UNCOMMENTABLE BLOCK OF CODE
l1 = []

l2 = [1, "two", 3.0]

print(l1, l2)

print(l2[1])

l2[2] = 3 + 0j
print(l2[2])
'''

'''
Output:

[] [1, 'two', 3.0]
two
(3+0j)
'''

'''
Indexing in Python: ----------------------------------------------------------------------------------------------

- Indexes are used to access a specific element of some iterator(list, tuple, string)
- Python has two types of indexing Non-negative indexing(starts like 0, 1, ...) and negative indexing(ends like ..., -2, -1)

l =["1st element",	"2nd element", 	"3rd element", "4th element"]
		0				1				2				3				# non-negative indexing
		-4				-3				-2				-1				# negative indexing

'''

'''UNCOMMENTABLE BLOCK OF CODE
l = ["1st element or last 3rd element", "2nd element or 2nd last element", "3rd element or last element"]

print(l[2])
print(l[-2])
'''

'''
Outut:

3rd element or last element
2nd element or 2nd last element
'''

'''
Slicing in Python: --------------------------------------------------------------------------------------------------

- it means to get continous portion of the Iterator(list, string, tuple)

Syntax:

	i[index_to_start_with:index_to_end_before]

'''


l = [0, 1, 2, 3, 4]
print(l[:])
print(l[1:])
print(l[:3])
print(l[1:4])