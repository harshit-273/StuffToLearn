# Arithmetic Operators
print(1+2)
print("ab"+"yz")
print(5-2)
print(3*4)
print(5/2)
print(5//2)
print(5**2)
print(5%2)

"""
Output:
3
abyz
3
12
2.5
2
25
1
"""

# Comparison Operators

print(5<2)
print(5>2)
print(5<=5)
print(5>=5)
print(2==4)
print(2!=4)
print(["apple", "banana", "cherry"] is ["apple", "banana", "cherry"])
print(2 in [1, 2, 3])

"""
Output:
False
True
True
True
False
True
False
True
"""

# Bitwise Operators

print(1&0)
print(1|0)
print(~0)
print(3^1)
print(1<<2)
print(4>>2)

"""
Output:
0
1
-1
2
4
1
"""

# Logical Operators

print(1<2 and 3>2)
print(1>2 or 3<2)
print(not True)

"""
Output:
True
False
False
"""

# Assignment Operators

a = 5
print(a)
a += 5
print(a)
a -= 4
print(a)
a *= 3
print(a)
a /= 4
print(a)
a //= 2
print(a)
a %= 3
print(a)
a **= 4
print(a)

a = int(a) # Converting to int as bitwise operations can only be performed on the integers

a &= 19
print(a)
a |= 4
print(a)
a ^= 2
print(a)
a <<= 2
print(a)
a >>= 1
print(a)

