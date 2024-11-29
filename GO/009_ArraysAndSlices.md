# Arrays

### Syntax

```golang
var arrayName [size_of_outer_array_in_int][size_of_inner_array_in_int]...datatype /************* Declaration *************/
arrayName[index_of_outer_array][index_of_inner_array]...  = someValue // index is of type "int" ranging between 0-(length - 1) value 

otherArray := [size_in_int]datatype {some_value, other_value, ...}

len(arrayName) // gives the length of array for which it is asked
```

### Example

```golang
arr := [4]string{"zero", "one", "two", "three"}
fmt.Printf("%q\n", arr[2])

var arr2 [2][3]int
fmt.Printf("Before the assignment of any value to array - %v\n", arr2)

arr2[1][1] = 4
fmt.Printf("after the assignment of any value to array - %v\n", arr2)

fmt.Printf("length of outer array - %d\n", len(arr2))
fmt.Printf("length of inner array - %d", len(arr2[0]))
```

### Output

```
"two"
Before the assignment of any value to array - [[0 0 0] [0 0 0]]
after the assignment of any value to array - [[0 0 0] [0 4 0]]
length of outer array - 2
length of inner array - 3
```

# Slices

## From the Array

### Syntax

```golang
var sliArrName [size_in_int]datatype = [size_in_int]datatype{some_value, other_value, ...} // declaration of array for making slice

var sliFullCapacity []datatype = sliArrName[:] // this would give full array to a slice 

var sliName []datatype = sliArrName[startingIndex:endingIndex] // this would give the part of array which starts with "startingIndex" and ends before "endingIndex"
```

### Example

```golang
var sliceArr [5]int = [5]int{0, 1, 2, 3, 4}

var sliFullCapacity []int = sliceArr[:] // it would give the full array to this slice
fmt.Println(sliFullCapacity)

var sli []int = sliceArr[1:4] // this would give sli = {1,2,3} as we started from index 1 and we would end before the index given after ":"
fmt.Println(sli)
fmt.Println(cap(sli), len(sli)) // cap function would give how much this slice can store, although the length maybe smaller than or equal to capacity
```

### Output

```
[0 1 2 3 4]
[1 2 3]
4 3
```

## Using `make()` for creation of Slices

### Syntax

```golang
otherSli := make([]datatype, sliceCapacity_in_int) // other way to declare a slice without using array

otherSli = append(otherSli, some_value) // this would add the element "some_value" at the end of this slice
```

### Example

```golang
otherSli := make([]int, 0) // other way to create a slice without the array
fmt.Println(otherSli)

otherSli = append(otherSli, 1) // this would append the element "1" at the end of the slice
fmt.Println(otherSli)
```

### Output

```
[]
[1]
```

## Two Dimensional Slices

### Example

```golang
sliOfSlices := make([][]int, 0) // make a 2D slice of length 0

fmt.Println(sliOfSlices) // printing the initial slice of slices

sliOfSlices = append(sliOfSlices, []int{5, 6, 7}) // appending the slice in slice of slices
sliOfSlices = append(sliOfSlices, []int{1, 2})
sliOfSlices = append(sliOfSlices, []int{3, 4, 8, 9})

fmt.Printf("%v", sliOfSlices)
```

### Output

```
[]
[[5 6 7] [1 2] [3 4 8 9]]
```