# Functions

## Function declaration and calling a function

- More than one value can be returned from a function in golang.

### Syntax for function declaration

```golang
// function declaration
func functionName(parameterVariable1 dataType1, parameterVariable2 dataType2, ...) (returnDataType, returnDataType2, ...) {
    // some processing
    return valueOfType_returnDataType, valueOfType_returnDataType2
}

// another way of function declaration
func functionName(parameterVariable1 dataType1, parameterVariable2 dataType2, ...) (returnVariable returnDataType, returnVariable2 returnDataType2, ...) {
    // some processing 
    // assigning the value to returnVariable and returnVariable2
    return
}

// calling a function
functionName(argumentVariable, argumentVariable2, ...) // if nothing is returned
someVar, otherVar, ... := functionName(argumentVariable, argumentVariable2, ...) // if there are some return values
```

### Example

```golang
// declaring functions
func someThing(x int, y int) (int, int) {
	return x + y, x - y
}

func otherThing(x int, y int) (z1 int, z2 int) {
	z1 = x + y
	z2 = x - y
	return
}

// calling the functions
returnedValue1, returnedValue2 := someThing(4, 6)
fmt.Println(returnedValue1, returnedValue2)

returnedValue3, returnedValue4 := otherThing(5, 3)
fmt.Println(returnedValue3, returnedValue4)
```

### Output

```
10 -2
8 2
```

## Variadic function

- This function can accept any number of argumets of type datatype.

### Syntax

```golang
func functionName(parameterVariable ...datatype) returnDataType {
    // some process
    return valueOfType_returnDataType
}
```

### Example

```golang
func variadicFunction(para ...string) {
	for _, param := range para {
		fmt.Println(param)
	}
}

variadicFunction("one", "two", "three")
```

### Output

```
one
two
three
```

## `init()` function

- main purpose of init() is to initialize the global variables that cannot be initialized in the global context

### Syntax

```golang
func init(){
    // executes at the time when package is initialized, so it executes before main function
}
```

## Use of `defer` keyword

- Doing something immediately before returning the function or finishing the function.

### Syntax

```golang
defer // some statement which should be executed exactly before function ends. Inside the function
```

### Example

```golang
func deferExample() {
	defer fmt.Println("Just before closing the function")
	fmt.Println("Other statements")
	fmt.Println("Another statement")
}

deferExample()
```

### Output

```
Other statements
Another statement
Just before closing the function
```

# Advanced function concepts

- Function is just like a variable, we can pass it as parameter, return it from a function, called directly

## Defining a function and assigning it to a variable

### Example

```golang
func test() {
	fmt.Println("assigning function to a variable")
}

x := test
x()
```
### Output

```
assigning function to a variable
```

## Calling a function and assigning it's value to variable

### Example

```golang
test := func(x int) int {
		return x * -1
}(8)

fmt.Println("calling a function directly and assigning it to a variable", test)
```

### Output

```
calling a function directly and assigning it to a variable -8
```

## Passing the function as a parameter

### Example

```golang
func test(test2 func(int) int) {
	fmt.Println("passing a function as parameter", test2(7))
}

test3 := func(x int) int {
	return x * 3
}

/*
	- first test3 is passed to test4
	- test3 is passed the value "7" in the function test
	- processing the test
*/

test(test3)
```

### Output

```
passing a function as parameter 21
```

## Returning a function

### Example

```golang
func test(x string) func() {
	return func() { fmt.Println(x) }
}

someFunc := test("calling a function that returns a function and assigning it to a variable")
someFunc()
```

### Output

```
calling a function that returns a function and assigning it to a variable
```

## Directly calling a function that returns a function

### Example

```golang
func test(x string) func() {
	return func() { fmt.Println(x) }
}

/*
Here test("...") would return a function and that function is called directly.
*/
test("directly calling a function that returns a function")()
```

### Output

```
directly calling a function that returns a function
```
