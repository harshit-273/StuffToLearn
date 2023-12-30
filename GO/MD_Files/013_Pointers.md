# Pointers

- Pointers are something which is used to store the value of the address where the real value is stored.
- Using pointers we can change the value of something without touching it directly.

### Syntax

```golang
var someVariable *datatype = &otherVariable_ofType_datatype // assigning the value to a pointer

*someVariable = otherValue_ofType_datatype // to access the value stored at the someVariable address
```

### Example

```golang
// assigning and accessing pointer
x := 7
y := &x
fmt.Println(x, *y, y)
*y = 3
fmt.Println("After changing the value of *y")
fmt.Println(x, *y, y)
```

### Output

```
7 7 0xc000020070
After changing the value of *y
3 3 0xc000020070
```

## how passing an argument as a pointer works

### Example

```golang
func changeValueWithPointer(str *string) {
	*str = "Value is changed"
}

func changeValueWithoutPointer(str string) {
	str = "This won't work anyway"
}

// inside main function
var someStr string = "Value to be changed"
var otherStr string = "Other value to be changed"

changeValueWithPointer(&someStr)
fmt.Println(someStr)
changeValueWithoutPointer(otherStr)
fmt.Println(otherStr)
```

### Output

```
Value is changed
Other value to be changed
```