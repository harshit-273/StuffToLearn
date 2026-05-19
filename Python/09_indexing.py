"""
How to access any elements based on their index ? We will answering this question here.
"""

some_str = "Harshit Kalavadia"

print(f"The string - \"{some_str}\"")
print(f"First element of the string - {some_str[0]}")
print(f"Last element of the string - {some_str[-1]}")
print(f"Entire string starting from 2nd character - \"{some_str[1:]}\"")
print(f"Entire string ending before last character - \"{some_str[:-1]}\"")
print(f"Entire string without and even position elements - \"{some_str[::2]}\"")
print(f"Entire string but backwards - \"{some_str[::-1]}\"")

"""
Output:
The string - "Harshit Kalavadia"
First element of the string - H
Last element of the string - a
Entire string starting from 2nd character - "arshit Kalavadia"
Entire string ending before last character - "Harshit Kalavadi"
Entire string without and even position elements - "HrhtKlvda"
Entire string but backwards - "aidavalaK tihsraH"
"""