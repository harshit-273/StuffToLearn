'''
----------------------------------------------- break and continue -----------------------------------------------

- "break" keyword is used to break out of the loops.
- "continue" keyword is used to continue over the other loop statements without executing the statements after "continue" statement.

Synatax:

	while condition:
		# some statements
		if other_condition:
			break
		# some other statements

	while condition:
		# some statements
		if other_condition:
			continue
		# some other statements

'''

num = 0

while num < 10:
	num += 1
	if num == 5:
		break
	print(num, end = " ")

print()
num = 0

while num < 10:
	num += 1
	if num == 5:
		continue
	print(num, end = " ")



