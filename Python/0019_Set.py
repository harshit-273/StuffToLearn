'''
----------------------------------------------- Set -----------------------------------------------

- Set is a collection of unique data.

Syntax:

	set1 = {"element1", element2, [element3], (element4)}
'''

'''UNCOMMENTABLE BLOCK OF CODE

set1 = set()	# empty set
# dictionary1 = {} # empty dictionary
'''

'''
Set Functions: ----------------------------------------------------------------------------------------------

add(value)	- method will add value to the set

update(collection_type_value)	- method will update the set by adding new values in the collection passed in the brackets

discard(value) - method will remove the value from the set
'''
'''UNCOMMENTABLE BLOCK OF CODE

set1 = {2, 3, 4, 5}
set1.add(0)
print(set1)

set1.remove(5)
print(set1)

set1.update([0, 1, 2, 3])
print(set1)
'''

'''
Set Operations: ----------------------------------------------------------------------------------------------

Union:- either "|" or set1.union(set2) can be used for union of the sets

Intersection:- either "&" or set1.intersection(set2) can be used for intersection of the sets

Difference:- either "-" or set1.difference(set2) can be used to get the (Set1 - Set2)

Symmetric Difference:- either "^" or set1.symmetric_difference(set2) can be used to get ((A ∪ B) - (A ∩ B)

Equality:- To compare the two sets for their equality(==) can be used.
'''

s1 = {1, 3, 5, 7, 9, 11}
s2 = {2, 3, 5, 7, 11}

print(f'{s1 | s2}, {s1 & s2}, {s1 - s2}, {s1 ^ s2}, {s1 == s2}')