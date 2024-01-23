# Operators

## Arithmetic 

Operator       | Symbol | Usage
-------------- | ------ | -----
Addition       | +      | 15 + 2
Subtraction    | -      | 12 - 7
Multiplication | *      | 4 * 3
Division       | /      | 8 / 2

## Comparison

Operator                 | Symbol | Usage
------------------------ | ------ | -----
Equal to                 | =      | 15 = 3
Not equal to             | <>     | 23 <> 6
Greater than             | >      | 12 > 4
Greater than or equal to | >=     | 5 >= 2
Less than                | <      | 2 < 6
Less than or equal to    | <=     | 7 <= 10

## Other comparison

Operator | Symbol | Usage 
-------- | ------ | -----
Range    | `BETWEEN <lower limit> AND <upper limit>` | Matches values between a range of values(both inclusive)
List | `IN (List of values)` | Matches any of the list items
Pattern matching | `LIKE '<pattern>'` | Matches a pattern
NULL test | `<value> IS NULL` | Is a null value

## Logical 

Operartor | Symbol | Usage
--------- | ------ | -----
And | AND | If both the conditions are true then returns TRUE
Or | OR | If both the conditions are false then retuns FALSE
Not | NOT | If TRUE returns FALSE
