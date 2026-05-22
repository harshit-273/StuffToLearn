"""
With the help of format specifiers we can format the numbers
"""
num = -123.45678
print(f"Number:{num}")
print(f"Number is rounded for \"3\" decimal places:{num:.3f}")
print(f"Number is allocated \"10\" spaces:{num:10}")
print(f"Number is allocated \"20\" spaces and padded with \"0\":{num:020}")
print(f"Number is allocated \"20\" spaces and is right justified:{num:>20}")
print(f"Number is allocated \"20\" spaces, padded with \"0\" and is left justified:{num:<020}")
print(f"Number is rounded for \"3\" decimal places, allocated \"20\" spaces with padded \"0\", right justified:{num:>020.3f}")


"""
Output:
Number:-123.45678
Number is rounded for "3" decimal places:-123.457
Number is allocated "10" spaces:-123.45678
Number is allocated "20" spaces and padded with "0":-0000000000123.45678
Number is allocated "20" spaces and is right justified:          -123.45678
Number is allocated "20" spaces, padded with "0" and is left justified:-123.456780000000000
Number is rounded for "3" decimal places, allocated "20" spaces with padded "0", right justified:000000000000-123.457
"""