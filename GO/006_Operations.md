# Operations

## Arithmetic Operators

operator | used for
-------- | --------
\+ | adding two numbers
\- | subtracting two numbers
\* | multiplying two numbers
\\ | dividing two numbers
%  | finding remainder

### Example

```golang
fmt.Printf("%03d + %03d = %03d\n", 5, 3, 5+3)
fmt.Printf("%03d - %03d = %03d\n", 5, 3, 5-3)
fmt.Printf("%03d * %03d = %03d\n", 5, 3, 5*3)
fmt.Printf("%03d / %03d = %03d\n", 5, 3, 5/3)
fmt.Printf("%03d %% %03d = %03d\n", 5, 3, 5%3)
fmt.Printf("%03.5f / %03.5f = %03.5f\n", 8.0, 7.0, 8.0/7.0)
```

### Output

```
005 + 003 = 008
005 - 003 = 002
005 * 003 = 015
005 / 003 = 001
005 % 003 = 002
8.00000 / 7.00000 = 1.14286
```

## Bitwise Operators

operator | name | used for
-------- | ---- | --------
\& | binary `and` operator | results only if both the bits are present
\| | binary `or` operator  | results if even one bit is present
\^ | binary `xor` operator | results if one bit is present and other is absent
\<\< | binary left shift operator | multiplies the left operand with two to the power of the right operand
\>\> | binary right shift operator | divides the left operand with two to the power of the right operand

### Example

```golang
fmt.Printf("%03d & %03d = %03d\n", 13, 2, (13 & 2))
fmt.Printf("%03d | %03d = %03d\n", 13, 2, (13 | 2))
fmt.Printf("%03d ^ %03d = %03d\n", 13, 2, (13 ^ 2))
fmt.Printf("%03d >> %03d = %03d\n", 13, 2, (13 >> 2))
fmt.Printf("%03d << %03d = %03d\n", 13, 2, (13 << 2))
```

### Output

```
013 & 002 = 000
013 | 002 = 015
013 ^ 002 = 015
013 >> 002 = 003
013 << 002 = 052
```

## Conditional Operators

opeartor | used for checking
-------- | --------
\< | less than
\> | greater than
== | equality
\<= | less than or equal to
\>= | greater than or equal to
!= | not equal to

### Example

```golang
fmt.Printf("%d < 5 => %t\n", 5, 5 < 5)
fmt.Printf("%d > 5 => %t\n", 5, 5 > 5)
fmt.Printf("%d <= 5 => %t\n", 5, 5 <= 5)
fmt.Printf("%d >= 5 => %t\n", 5, 5 >= 5)
fmt.Printf("%d == 5 => %t\n", 5, 5 == 5)
fmt.Printf("%d != 5 => %t\n\n", 5, 5 != 5)

fmt.Printf("%q < \"\" => %t\n", "Harshit", "Harshit" < "")
fmt.Printf("%q > \"\" => %t\n", "Harshit", "Harshit" > "")
fmt.Printf("%q <= \"\" => %t\n", "Harshit", "Harshit" <= "")
fmt.Printf("%q >= \"\" => %t\n", "Harshit", "Harshit" >= "")
fmt.Printf("%q == \"\" => %t\n", "Harshit", "Harshit" == "")
fmt.Printf("%q != \"\" => %t\n", "Harshit", "Harshit" != "")
```

### Output

```
5 < 5 => false
5 > 5 => false
5 <= 5 => true
5 >= 5 => true
5 == 5 => true
5 != 5 => false

"Harshit" < "" => false
"Harshit" > "" => true
"Harshit" <= "" => false
"Harshit" >= "" => true
"Harshit" == "" => false
"Harshit" != "" => true
```

## Logical Operators

operator | purpose
-------- | -------
\|\| | `OR` operator
\&\& | `AND` operator
! | `NOT` operator

### Example

```golang
fmt.Printf("true || true => %t\n", true || true)
fmt.Printf("true || false => %t\n", true || false)
fmt.Printf("false || true => %t\n", false || true)
fmt.Printf("false || false => %t\n\n", false || false)

fmt.Printf("true && true => %t\n", true && true)
fmt.Printf("true && false => %t\n", true && false)
fmt.Printf("false && true => %t\n", false && true)
fmt.Printf("false && false => %t\n\n", false && false)

fmt.Printf("!true => %t\n", !true)
fmt.Printf("!false => %t\n", !false)
```

### Output

```
true || true => true
true || false => true
false || true => true
false || false => false

true && true => true
true && false => false
false && true => false
false && false => false

!true => false
!false => true
```
