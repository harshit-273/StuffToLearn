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

