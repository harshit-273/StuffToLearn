'''
----------------------------------------------- Class and Object -----------------------------------------------

- Object is something which has some attributes and some behavior.
- Class is the blueprint of a object.

Syntax:

	# Class implementation
	class ClassName:
		# attributes
        att1 = some_value
        att2 = other_value
        
		# behavior
        def behavior1(arg1, arg2, ...):
			#behavior implementation

	objName = ClassName()

'''

class Cl1:
	att1 = "attribute 1"
	att2 = (2,)
    
	def beh1(self):
		print("behavior 1")

	def beh2(self):
		print("behavior 2")
		return ("|./\.|")

classObject = Cl1()
print(f'{classObject.att1} and {classObject.att2} are the attributes of the class and "{classObject.beh1()}" and "{classObject.beh2()}" are the behavior of the class Cl1')
                
	
        
	
