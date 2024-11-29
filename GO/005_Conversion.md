# Conversion

Method/Function | Purpose
--------------- | -------
strconv.Atoi(s string) returns (int) | string to int
strconv.ParseInt(s string, base int, bitSize int) returns (i int64, err error) | string to int
strconv.ParseFloat(s string, bitSize int) returns (float64, error) | string to float
strconv.Itoa(i int) returns (string) | int to string
strconv.FormatFloat(float64, fmt byte, prec int, bitSize int) returns (string) | float to string
float64(int) returns (float64) | int to float
int64(float) returns (int64) | float to int
int(float) returns (int) | float to int
[]rune(string) returns (array of rune) | string to array of rune
string([]rune) returns (string) | array of rune to string

## Example

```golang
intString, _ := strconv.ParseInt("25", 10, 64)
fmt.Printf("from string to int : %d\n", intString)

floatString, _ := strconv.ParseFloat("25.52", 64)
fmt.Printf("from string to float : %f\n", floatString)

stringInt := strconv.Itoa(12)
fmt.Printf("from int to string : %q\n", stringInt)

stringFloat := strconv.FormatFloat(556.54, 'f', 2, 64)
fmt.Printf("from float to string : %q\n", stringFloat)

floatInt := float64(65)
fmt.Printf("from int to float : %f\n", floatInt)

var someFloat float64 = 56.65
intFloat := int64(someFloat)
fmt.Printf("from float to int : %d\n", intFloat)

var str string = "some😁string"
runeString := []rune(str)
fmt.Print("from string to array of runes : ")
fmt.Printf("%v\n", runeString)

stringRune := string(runeString)
fmt.Printf("from array of runes to string : %q\n", stringRune)
```

## Output

```
from string to int : 25
from string to float : 25.520000
from int to string : "12"
from float to string : "556.54"
from int to float : 65.000000
from float to int : 56
from string to array of runes : [115 111 109 101 128513 115 116 114 105 110 103]
from array of runes to string : "some😁string"
```