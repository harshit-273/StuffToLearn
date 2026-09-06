#include <stdio.h>
#include <stdbool.h> // for boolean types

int main() {
	int num; // declaration
	num = 5; // assignment

	float decim = 45.72; // declaration and assignment

	char c = 's'; // use single quotes for storing characters

	bool is_variable = true; // other value is "false"

	printf("int - %d\n", num);
	printf("float - %f\n", decim);
	printf("char - %c\n", c);
	printf("bool - %d\n", is_variable); // C does not have any format specifiers for printing booleans

	return(0);
}

/*
Output:
int - 5
float - 45.720001
char - s
bool - 1
*/