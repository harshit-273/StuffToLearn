# How to run a `go` program

1. When `go` is installed on the system.
   1. Go to the directory where the `.go` file is stored from the shell/terminal.
   2. Run the command:
		```
		go run fileName.go
		```
	> This would run the program.

2. When `go` is not installed on the system.
   1. Go to the directory where the `.go` file is stored from the shell/terminal.
   2. Run the command:
		```
		go build fileName.go
		```
	> This will create a `.exe` file which can run on any other system without having the go installed.
	3. Open the `.exe` file i.e., double click it or type below in the terminal:
		```
		./fileName.exe
		```

# Hello World Program
```golang
package main

import "fmt"

func main() {
	fmt.Printf("🙏Namaste🙏, World!")
}
```