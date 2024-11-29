# Generics

- It is a concept used when you want to implement something for few datatypes.

### Syntax

```golang
type someGenericType interface {
	datatype1 | datatype2 | datatype3
}

// implementing a generic type function
func someFunc[G someGenericType](para G) G {
	// processing the "para"
	// returning the type G
}
```

### Example

```golang
type Number interface {
	int | float64 | complex128
}

// simple program to add two numbers
func add[G Number](a G, b G) G {
	return a + b
}

// inside main
fmt.Println(add(4, 3))
fmt.Println(add(3.5, 4.2))
fmt.Println(add(3.7 + 7i, 4 + 2.4i))
```

### Output

```
7
7.7
(7.7+9.4i)
```