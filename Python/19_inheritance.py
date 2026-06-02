# Inheritance

class Grand_Father:
	def grand_father_method(self):
		print("Inherited from Grand Father")

class Father(Grand_Father): # Class from which other classes will be inherited
	def __init__(self, name):
		self.name = name
	
	def father_method(self):
		print("Inherited from Father")

class Mother:
	def mother_method(self):
		print("Inherited from Mother")


class Son(Father): # Inherited class
	def own_method(self): # Own method
		print(f"Comes from the {type(self)}")

class Daughter(Father, Mother):
	pass

son1 = Son("name of son")
son1.father_method()
son1.own_method()
son1.grand_father_method()

daughter1 = Daughter("name of daughter")
daughter1.father_method()
daughter1.mother_method()
daughter1.grand_father_method()

"""
Output:
Inherited from Father
Comes from the <class '__main__.Son'>
Inherited from Grand Father
Inherited from Father
Inherited from Mother
Inherited from Grand Father
"""