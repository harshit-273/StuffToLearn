# Variables and Datatypes

| Datatype | What it is used for? | Example |
| -------- | -------------------- | ------- |
| int | For storing non-decimal valued numbers. Numbers without ` . ` | 456 |
| float32 | For storing decimal valued numbers. Numbers with ` . ` | 456.321 |
| complex64 | For complex numbers. Real and imagenery part are ` float32 ` | 123.456 + 789.321i |
| string | For storing text like things. Use ` "" ` or ` `` ` to put a value in this one | "some text", \` some other text \` |
| bool | For storing one of the two values. Value can be either ` true ` or ` false ` | true, false |

## Syntax

```golang
var variableName dataType /************* Declaration *************/
variableName = someValue /************* Initialization *************/

var variableName dataType = someValue /************* Declaration and Initialization *************/

variableName := someValue or var variableName = someValue /************* In this case type would be automatically applied to variableName *************/
```

### Example

```golang
var number int
number = 7

var floatNumber float32 = 7.4

var complexNumber complex64 = 45 + 11.5i

stringText := `some 
text` /* string type */

var booleanValue = true /* bool type */

fmt.Println(number, floatNumber, complexNumber, stringText, booleanValue)
```

### Output

```
7 7.4 (45+11.5i) some 
text true
```

---

> rune

* Rune can be considered as a single character which has UTF-8 (more than ASCII characters), but they are integer value of Unicode.
* Rune are just like characters in ` C Language ` (if you know it), but just better.

> string

* String is just the group of runes.
* Like an array of runes.

### Example

```golang
var someRune rune = '🤪'
otherRune := "some string"[4]

fmt.Printf("%c ", someRune)
fmt.Printf("%d ", otherRune)
```

### Output

```
🤪 32
```