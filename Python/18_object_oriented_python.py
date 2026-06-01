# Class, Constructor, Method, class varaibles

class Some_class: # defining a class
	class_var = "shared variable across all the created objects"

	def __init__(self, property1, property2, property3): # defining a constructor
		self.property1 = property1
		self.property2 = property2
		self.property3 = property3
	
	def some_method(self): # defining class method
		# perform something
		print(f"Performing \"some_method\" of class \"Some_class\". There is a property - \"{self.property1}\" inside it. The class variable is - \"{Some_class.class_var}\"")

some_object = Some_class("prop1", "prop2", "prop3") # creating an object from a class

print(some_object.property1) # getting a value of the property
some_object.some_method() # executing a class method

"""
Output:
prop1
Performing "some_method" of class "Some_class". There is a property - "prop1" inside it. The class variable is - "shared variable across all the created objects"
"""

