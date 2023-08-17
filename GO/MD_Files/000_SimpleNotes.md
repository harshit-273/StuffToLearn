# Simple Notes

> How to import in Golang
1. Method 1
```golang
import "module_name"
```
2. Method 2
```golang
import(
    "someThing",
    "otherThing",
    "anyThing"
)
```

* Variable declared in `GO` should be used, or else it will throw an error.
* To store an value in variable which will not be used later on, use `_` as variable name, it is an anonymous variable.
* For printing something import `fmt`.
* For working with input/output import `bufio`.
* For working with standard input/output from OS import `os`.
* For conversion of string to some other datatype import `strconv`.
* Arithematic operations only occurs between same datatypes.
* Arithematic operations between two operands of same datatype would give output in same datatype.
* Arithematic operator `/`, when using divisor as 0(zero) throws an runtime error.
* Conditional operators can also be used with string datatypes, string values would be compared on the basis of the ASCII values.
* `break` keyword used to leave the loop without executing lines next to `break` in the loop.
* `continue` keyword is used to proceed in the loop without executing the lines next to `continue` in the loop.
* For the arrays the size of the array should be defined.
* When an array is declared all it's elements are assigned the default value of the datatype.
* Maps do not retain order, they can just be used to store the key-value pairs.
* Slices and Maps are actually pointers to address where the real thing is stored.
	* When we assign one value to slice/map variable to another variable the values of those are copied to another variable i.e., address stored in the variable is assigned to another variable.
	* You can pass the slice or map to a function and process them but it is not required to retuen them.