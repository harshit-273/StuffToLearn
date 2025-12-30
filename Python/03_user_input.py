"""
input()
"""
print("Hello!")
input()

name = input("What is your name? ")
age = int(input("What is your age? ")) # type casting the age to int as by default the input() returns string of the input.

next_age = age + 1

print(f"Your name is {name}.")
print(f"On your next birthday, you will be {next_age} years old.")

"""
Output:
Hello!
hello
What is your name? Harshit
What is your age? 26
Your name is Harshit.
On your next birthday, you will be 27 years old.
"""