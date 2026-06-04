# static method

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	@staticmethod
	def is_adult(age): # static method
		return age >= 18
	
	def intro(self): # instance method
		print(f"I am {self.name} and I am {self.age} year/s old.")
	
some_person = Person("Kong", 18)
some_person.intro()
is_person_adult = "an Adult" if Person.is_adult(some_person.age) else "a Child"
print(f"{some_person.name} is {is_person_adult}")

"""
Output:
I am Kong and I am 18 year/s old.
Kong is an Adult
"""