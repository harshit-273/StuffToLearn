# Switch

## Normal `switch`

### Syntax

```golang
switch some_variable {
	case value1, value3:
		// procedure if value of some_variable is equal to value1 or value3
	case value2:
		// procedure if value of some_variable is equal to value2
	default:
		// procedure if none of the value matches with some_variable
}
```

### Example

```golang
x := 3
switch x {
case 3, -3:
	fmt.Printf("three")
case 5:
	fmt.Printf("five")
default:
	fmt.Printf("No value")
}
```

### Output

```
three
```

## If-Else like `switch`

### Syntax

```golang
switch {
	case some_condition :
		// procedure if the some_condition satisfies
	case other_condition :
		// procedure if the other_condition satisfies
	default:
		// procedure if no conditions satisfies
}
```

### Example

```golang
y := 10
z := 10
switch {
case y < z:
	fmt.Printf("y < z")
case y > z:
	fmt.Printf("y > z")
default:
	fmt.Printf("y == z")
}
```

### Output

```
y == z
```