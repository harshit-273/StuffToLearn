import functools

# lambda parameter:expression

add = lambda x, y, z: x+y+z
print(add(4, 5, 6))
print(add(1, 2, 3))

is_adult = lambda age: True if age >= 18 else False
print(is_adult(19))

"""
Output:
15
6
True
"""

# map(function, iterator)

squared = lambda x: x*x
nums = list(range(1, 11, 1))
squared_nums = list(map(squared, nums))
print(f"{nums} => {squared_nums}")

"""
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

# filter(function, iterator)

l1 = list(range(1, 31, 1))
multiple_of_3 = lambda x: x%3 == 0
multiples_of_three = list(filter(multiple_of_3, l1))
print(f"{l1} => {multiples_of_three}")

"""
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30] => [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
"""

# reduce(function, iterator)

l = list(range(1, 11, 1))
sum_l = functools.reduce(lambda x, y,: x+y, l)
print(f"{l} => {sum_l}")

"""
Outut:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => 55
"""