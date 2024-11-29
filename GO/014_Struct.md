# Struct

### Syntax

```golang
// defination of structure
type StructName struct {
    var1Name datatype1
    var2Name datatype2
}

// Embedded Structure
type StructName2 struct {
    var3Name datatype3
    stVar StructName
}

type StructName3 struct {
    var4Name datatype4
    *StructName         // if you do not want to give another name to StructName variable
}

var st1 StructName = StructName{valueOfType_datatype1, valueOfType_datatype2} // if we already know both the values for the structure
st2 := StructName{var2Name: valueOfType_datatype2} // if we only know few of the values for the structure

st1.var1Name             // how to access value of one of the variable in struct

st3 := StructName2{valueOfType_datatype3, st1} // declaring and initializing embedded struct
// st3 := StructName2{valueOfType_datatype3, StructName{valueOfType_datatype1, valueOfType_datatype2}} // another way to do the same above thing

st3.stVar.var2Name      // how to access value of one of the structure in struct

st4 := StructName3{valueOfType_datatype4, &StructName{valueOfType_datatype1, valueOfType_datatype2}} 

// accessing the value of var1Name of StructName of st4 (for this to work StructName and StructName3 should have different property names)
st4.var1Name
```

### Example

```golang
type Point struct {
	x float32
	y float32
}

type Triangle struct {
	a Point
	b Point
	c Point
}

type Circle struct {
	radius float32
	*Point // you can name it center if you want
}

// inside main function
pt := Point{4, 5}
fmt.Printf("%T\n", pt)
fmt.Println(pt)
fmt.Println(pt.x)
fmt.Println()

tri := Triangle{b: pt, c: Point{6, 8}}
tri.a = Point{3, 2}
fmt.Printf("%T\n", tri)
fmt.Println(tri)
fmt.Println(tri.a)
fmt.Println(tri.b.x)
fmt.Println()

cir := Circle{6, &Point{7, 1}}
fmt.Printf("%T\n", cir)
fmt.Println(cir)
fmt.Println(cir.radius)
fmt.Println(cir.x)
```

### Output

```
main.Point
{4 5}
4

main.Triangle
{{3 2} {4 5} {6 8}}
{3 2}
4

main.Circle
{6 0xc0000200a8}
6
7
```