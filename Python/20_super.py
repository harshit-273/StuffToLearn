# super()

class Parent:
	def __init__(self, attribute1):
		self.attribute1 = attribute1
		print(f"Attribute - {self.attribute1}")

class Child(Parent):
	def __init__(self, attribute1, attribute2):
		super().__init__(attribute1)
		self.attribute2 = attribute2
		print(f"Attribute - {self.attribute2}")

ch = Child("one", "two")

"""
Output:
Attribute - one
Attribute - two
"""