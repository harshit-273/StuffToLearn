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
Output:

3rd element or last element
2nd element or 2nd last element
'''

'''
Slicing in Python: --------------------------------------------------------------------------------------------------

- it means to get continous portion of the Iterator(list, string, tuple)

Syntax:

	i[index_to_start_with:index_to_end_before]

'''

'''UNCOMMENTABLE BLOCK OF CODE
l = [0, 1, 2, 3, 4]
print(l[:])
print(l[1:])
print(l[:3])
print(l[1:4])
'''

'''
Output:

[0, 1, 2, 3, 4]
[1, 2, 3, 4]
[0, 1, 2]
[1, 2, 3]
'''

'''
Python List Functions: --------------------------------------------------------------------------------------------------

Syntax:

	list_l1.append(value_to_be_appended)		// this will append the value in the parameter at the last
    
    del list_l1[start_index:index_after_end]	// this will delete the value based on the index, even a single element can be deleted
    
    list_l1.remove(value_to_be_removed)			// this will remove the value
    
    list_l1.extend(iterator)					// this will add the interator at the end of the list
    
    list_l1.insert(index, value)				// this will add the value at the specified index, values from the index will move next to the index
    
    list_l1.pop(index)							// this will remove and return the value of the list at the index, default value of index here is -1
    
    list_l1.index(value)						// this will return the index of the specified value
    
    list_l1.reverse()							// this will reverse the list
    
    list_l1.count(value_to_be_counted)			// this will return the number of count of the value passed
'''

list_l1 = ["one", "two", "three", "four", "five", "six", "seven"]

list_l1.append("eight")

del list_l1[7]

list_l1.remove("seven")

list_l1.extend(["seven", "eight", "nine"])

ret_index = list_l1.index(5)

list_l1.insert(0, "zero")

list_l1.pop()

list_l1.reverse()

list_l1.count("two")

