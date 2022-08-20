package main

import "fmt"

func main() {
	var num1 int = 13
	var num2 int = 2

	fmt.Printf("%03d & %03d = %03d\n", num1, num2, (num1 & num2))
	fmt.Printf("%03d | %03d = %03d\n", num1, num2, (num1 | num2))
	fmt.Printf("%03d ^ %03d = %03d\n", num1, num2, (num1 ^ num2))
	fmt.Printf("%03d >> %03d = %03d\n", num1, num2, (num1 >> num2))
	fmt.Printf("%03d << %03d = %03d\n", num1, num2, (num1 << num2))
}
