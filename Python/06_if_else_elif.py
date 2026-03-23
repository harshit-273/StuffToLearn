"""
if - When someting is true for the given condition, block inside it will be executed
elif - When something is true for the given condition, block inside this will be executed
else - When none of the previously mentioned blocks gets executed it will be the default block to be executed 
"""

x = 4
if x < 0:
	print(f"{x} is less than 0.")
elif x > 0:
	print(f"{x} is greater than 0.")
else:
	print(f"{x} is 0.")

"""
Output:
0 is 0.

-3 is less than 0.

4 is greater than 0.
"""