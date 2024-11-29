# Interface

- Interfaces are used when we want to use a same method for two or more than two object(struct).

### Syntax

```golang
// interface defination
type interfaceName interface {
	methodName(parameterType, ...) (returnType, ...)
}

// some structs
type anything struct {
	varName varType
}

type something struct {
	varName varType
}

// implementing the interface method
func (a *anything) methodName(p parameterType, ...) (r returnType, ...) {
	// processing parameterType
	// returning returnType
}

func someFunction(i interfaceName) (someReturnType) {
	// here the "i" can have both the structs and process something here for both
}
```

### Example

```golang
type Computer interface {
	whatsTheProperty() string
}

type Desktop struct {
	property string
}

type Laptop struct {
	property string
}

func (d *Desktop) whatsTheProperty() string {
	return d.property
}

func (l *Laptop) whatsTheProperty() string {
	return l.property
}

func whatPropertyDoesThisComputerHas(c Computer) {
	fmt.Println("It can be", c.whatsTheProperty())
}

// inside main
d := &Desktop{property: "plugged and played"}
l := &Laptop{property: "moved anywhere"}

whatPropertyDoesThisComputerHas(d)
whatPropertyDoesThisComputerHas(l)
```

### Output

```
It can be plugged and played
It can be moved anywhere
```