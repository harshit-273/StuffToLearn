# Exception

print("Performing a division opeartion")
num1 = int(input("Enter a number to be divided: ")) # If a non-number is entered then it may create an exception as it cannot be converted to int
num2 = int(input("Enter a number to divide: "))
print(f"division is {num1 / num2}") # If a number is divided by 0 then exception will occur


"""
Output when no try-except is used and 2nd number is non-number:
Performing a division opeartion
Enter a number to be divided: 2
Enter a number to divide: zero
Traceback (most recent call last):
  File "...File/path...", line number, in <module>
    num2 = int(input("Enter a number to divide: "))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'zero'
"""

try: # The block in which exceptions might occur
	num1 = int(input("Enter a number to be divided: ")) # If a non-number is entered then it may create an exception as it cannot be converted to int
	num2 = int(input("Enter a number to divide: "))
	print(f"division is {num1 / num2}") # If a number is divided by 0 then exception will occur
except ValueError as e: # If this type of exception occurs then it will execute this block of code
	print(f"a non-number cannot be converted to number: {e}")

"""
Output when try-except is used and 2nd number is non-number:
Performing a division opeartion
Enter a number to be divided: 3
Enter a number to divide: zero
a non-number cannot be converted to number: invalid literal for int() with base 10: 'zero'

Output when try-except for converting non-number to number is used and is divided by 0:
Performing a division opeartion
Enter a number to be divided: 4
Enter a number to divide: 0
Traceback (most recent call last):
  File "...File/path...", line number, in <module>
    print(f"division is {num1 / num2}") # If a number is divided by 0 then exception will occur
                         ~~~~~^~~~~~
ZeroDivisionError: division by zero
"""

try: # The block in which exceptions might occur
	num1 = int(input("Enter a number to be divided: ")) # If a non-number is entered then it may create an exception as it cannot be converted to int
	num2 = int(input("Enter a number to divide: "))
	print(f"division is {num1 / num2}") # If a number is divided by 0 then exception will occur
except ValueError as e: # If this type of exception occurs then it will execute this block of code
	print(f"a non-number cannot be converted to number: {e}")
except ZeroDivisionError as e:
	print(f"Cannot divide by 0: {e}")

"""
Output when try-except for converting non-number to number is used, try-except for dividing by 0 and is divided by 0:
Performing a division opeartion
Enter a number to be divided: 9
Enter a number to divide: 0
Cannot divide by 0: division by zero

Output when try-except for converting non-number to number is used, try-except for dividing by 0 and is divided by non-zero:
Performing a division opeartion
Enter a number to be divided: 3
Enter a number to divide: 2
division is 1.5
"""

try: # The block in which exceptions might occur
	num1 = int(input("Enter a number to be divided: ")) # If a non-number is entered then it may create an exception as it cannot be converted to int
	num2 = int(input("Enter a number to divide: "))
	print(f"division is {num1 / num2}") # If a number is divided by 0 then exception will occur
except ValueError as e: # If this type of exception occurs then it will execute this block of code
	print(f"a non-number cannot be converted to number: {e}")
except ZeroDivisionError as e:
	print(f"Cannot divide by 0: {e}")
else: # If any exception does not occur then this block of code will be executed or else it will not be executed
	print("No errors occurred")

"""
Output when no exceptions occur and else block is used:
Performing a division opeartion
Enter a number to be divided: 3
Enter a number to divide: 2
division is 1.5
No errors occurred
"""

try: # The block in which exceptions might occur
	num1 = int(input("Enter a number to be divided: ")) # If a non-number is entered then it may create an exception as it cannot be converted to int
	num2 = int(input("Enter a number to divide: "))
	print(f"division is {num1 / num2}") # If a number is divided by 0 then exception will occur
except ValueError as e: # If this type of exception occurs then it will execute this block of code
	print(f"a non-number cannot be converted to number: {e}")
except ZeroDivisionError as e:
	print(f"Cannot divide by 0: {e}")
else: # If any exception does not occur then this block of code will be executed or else it will not be executed
	print("No errors occurred")
finally: # This block of code will be executed no matter if an exception occurs or not
	print("This will always be executed, doesn't matter if an exception occurs or not")

"""
Output when exception occurs:
Performing a division opeartion
Enter a number to be divided: 4
Enter a number to divide: 0
Cannot divide by 0: division by zero
This will always be executed, doesn't matter if a exception occurs or not
"""