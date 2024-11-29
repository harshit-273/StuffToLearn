# Methods

- Methods are functions only specific to functions

### Syntax

```golang
type StructName struct {
    var1Name datatype1
    var2Name datatype2
}

// defination of a method
// use pointer to structure if want to change property of the structure
func (structVar *StructName) methodName (parameter datatype3)  return_datatype4 { 
    // some process
    return valueOfType_datatype4
}

// calling the method
returnValue := varOfType_StructName.methodName (valueOfType_datatype3)
```

### Example

```golang
type Bird struct {
	kind string
	fly  bool
}

func (b *Bird) canFly() {
	if b.kind == "ostrich" {
		b.fly = false
	} else {
		b.fly = true
	}
}

// inside main function
someBird := Bird{kind: "ostrich"}
someBird.canFly()
if someBird.fly {
	fmt.Println(someBird.kind, "can fly")
} else {
	fmt.Println(someBird.kind, "can't fly")
}

someBird.kind = "sparrow"
someBird.canFly()
if someBird.fly {
	fmt.Println(someBird.kind, "can fly")
} else {
	fmt.Println(someBird.kind, "can't fly")
}
```

### Output

```
ostrich can't fly
sparrow can fly
```