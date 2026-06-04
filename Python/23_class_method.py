# Class method

class Someclass:

	some_value = "some value"

	def __init__(self, data):
		self.data = data
	
	@classmethod
	def get_some_value(cls):
		return f"Class methods value is {cls.some_value}"
	
sc = Someclass("some data")
print(Someclass.get_some_value())
print(f"Instance data is {sc.data}")

"""
Output:
Class methods value is some value
Instance data is some data
"""