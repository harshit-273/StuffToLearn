# while loop

exit = False

while False == exit:
	exit = True if "y" == input("Do you want to exit? Press \"y\" to exit:") else False

print("Thank you, you care good to go.")

"""
Output:
Do you want to exit? Press "y" to exit:n
Do you want to exit? Press "y" to exit:no
Do you want to exit? Press "y" to exit:yes
Do you want to exit? Press "y" to exit:y
Thank you, you are good to go.
"""

# for loop

for i in range(1, 11, 1):
	print(i, end=" ")

"""
Output:
1 2 3 4 5 6 7 8 9 10
"""

# break

while True:
	if "y" == input("Do you want to exit this loop?(Press y to exit):"):
		break

print("You have exitted the loop")

# continue
# printing multiples of 3 or 5 but not of 3 and 5.

for i in range(0, 50, 1):
	if (i%3 == 0) and (i%5 == 0):
		continue
	elif i%3 == 0:
		print(i, end=" ")
	elif i%5 == 0:
		print(i, end=" ")

"""
Output:
3 5 6 9 10 12 18 20 21 24 25 27 33 35 36 39 40 42 48
"""