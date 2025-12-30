"""
str(), int(), float(), bool(), type()
"""

name = "Harshit"
age = 26
is_male = True
gpa = 7.1

print(type(name))
print(type(age))
print(type(is_male))
print(type(gpa))

"""
Output:
<class 'str'>
<class 'int'>
<class 'bool'>
<class 'float'>
"""

house_no = 1
print(type(house_no))

"""
Output:
<class 'int'>
"""

house_no = str(house_no)
print(type(house_no))

"""
Output:
<class 'str'>
"""
