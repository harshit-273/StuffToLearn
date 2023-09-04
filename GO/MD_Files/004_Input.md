# Input

## Syntax

```golang
scanner := bufio.NewScanner(os.Stdin) /************* Creating new Scanner object of input from keyboard *************/
scanner.Scan() /************* For scanning the input *************/
input := scanner.Text() /************* "Text()" method returns what has been scanned in scanner object *************/

fmt.Scanf("%s", &input) /************* Used for scanning inputs from keyboard, here string is taken as input *************/

fmt.Scan(&input)
```

---

### Example with ` Scanner `

```golang
scanner := bufio.NewScanner(os.Stdin)
fmt.Printf("Please enter something : ")
scanner.Scan()
var input string = scanner.Text()
fmt.Printf("You have typed %q\n\n", input)
```

### Output

```
Please enter something : one two
You have typed "one two"
```

---

### Example with ` Scanf `

```golang
fmt.Printf("Please enter some text: ")
fmt.Scanf("%s", &input)
fmt.Printf("you have entered %q\n\n", input)
```

### Output

```
Please enter some text: one two
you have entered "one"
```

---

### Example with ` Scan `

```golang
fmt.Print("Please enter something: ")
fmt.Scan(&input)
fmt.Printf("you have entered %q\n\n", input)
```

### Output

```
Please enter something: one
you have entered "one"
```