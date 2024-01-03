# Formatting with Printf and Sprintf of fmt package

| What to use? | What for? | Purpose |
| ------------ | --------- | ------- |
| %v | general | For printing vlaue of default type |
| %T | general | For printing type of the varaible |
| %% | - | For printing ` % ` |
| %t | boolean | For printing booleans |
| %b | binary | For printing binary |
| %o | octal | For printing octal |
| %d | decimal | For printing decimal |
| %x, %X | hexdecimal | For printing hexadecimal (if ` X ` is used then hexadecimal would have capital letters) |
| %e | floating | For printing scientific notation |
| %f, %F | floating | For printing no exponent value |
| %g | floating | For printing floating with larger precision |
| %s | string | For printing string |
| %q | string | For printing strings with ` "" ` (double quotes)|
| %c | rune | For printing rune |

| What to use? | Width | Precision | Padding |
| ------------ | ----- | --------- | ------- |
| %f | default | default | None |
| %9f | 9 | default | None |
| %.2f | default | 2 | None |
| %9.2f | 9 | 2 | None |
| %9.f | 9 | 0 | None |
| %09d | 9 | None | 0 |
| %-4d | 4 | None | With space(`   `) |

## Syntax

```golang
var variableName string = fmt.Sprint("...", ...)

fmt.Printf("...", ...)
```

## Example

```golang
var someVariable string = fmt.Sprintf("%cNamaste%c my name is %s and I am %d years old", '🙏', '🙏', "Harshit", 24)

fmt.Printf("%v", someVariable)
```

## Output

```
🙏Namaste🙏 my name is Harshit and I am 22 years old
```