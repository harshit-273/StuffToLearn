# Loops

## Infinite loop

### Syntax

```golang
for {
	/*
		some stuff to be executed again and again infinite times

		Note: Don't ever forget to have an terminating conditions, or else your program would fail. To terminate the loop use a "break" keyword based on a condition.
	*/
}
```

### Example to use the `break` keyword

> Printing 1 to 5 using an infinite loop

```golang
x := 1
for {
	if x > 5 {
		break
	}
	fmt.Printf("%03d ", x)
	x++
}
```

### Output

```
001 002 003 004 005 
```

## `while` loop

### Syntax

```golang
for condition {
        // some stuff to be executed till condition is satisfied
        // change in condition when required
}
```

### Example to use `continue` keyword in a loop

> Printing 1 to 5, but not 3

```golang
x := 1
for x < 5 {
	x++
	if x == 3 {
		continue
	}
	fmt.Printf("%03d ", x)
}
```

### Output

```
001 002 004 005
```

## The `for` loop

### Syntax

```golang
for initializing_value; terminating_condition; changes_made_in__initialized_value {
        // some stuff to be executed again and till changes_made would terminate the loop
}
```

### Example

```golang
for i := 1; i <= 10; i++ {
	fmt.Printf("%03d ", i)
}
```

### Output

```
001 002 003 004 005 006 007 008 009 010
```

## Loop using `range`

### Syntax

```golang
for index, element := range array_or_slice_maybe {
        /* some stuff to be executed again and again till in range,
            index is the index of array_or_slice_maybe and
            element is that element having that index */
}
```

### Example

```golang
arr := [5]int{123, 231, 1232, 12333, 2314}
for index, element := range arr { // if index is not required then use "_" instead of it
		fmt.Printf("%5d: %5d\n", index, element)
}
```

### Output

```
    0:   123
    1:   231
    2:  1232
    3: 12333
    4:  2314
```