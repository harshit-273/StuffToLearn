# If Else

### Syntax

```
if condtion {
    // some procedure if "condition" is satisfied
} else if other_condition {
    // some procedure if "other_condition" is satisfied
} else {
    // some procedure if no conditions are satisfied
}
```

### Example

```golang
var condition bool = false
var other_condition bool = false

if condition == true && other_condition == false {
	fmt.Printf("condition is %t, but other_condition is %t so \"if\" block is executed", condition, other_condition)
} else if condition == false && other_condition == true {
	fmt.Printf("condition is %t, but other_condition is %t so \"else if\" block is executed", condition, other_condition)
} else {
	fmt.Printf("condition is %t and other_condition is also %t so \"else\" block is executed", condition, other_condition)
}
```

### Output

```
condition is false and other_condition is also false so "else" block is executed
```