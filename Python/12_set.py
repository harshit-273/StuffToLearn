# Set - {}

set_of_things = {"zero", 1, 2.0}
print(set_of_things)
set_of_things.add(True) # True is not added to set as it is already present as 1. Booleans are a subtype of integers.
print(set_of_things)
set_of_things.add(False)
print(set_of_things)
set_of_things.remove(2.0)
print(set_of_things)

"""
{1, 2.0, 'zero'}
{1, 2.0, 'zero'}
{False, 1, 2.0, 'zero'}
{False, 1, 'zero'}
"""
