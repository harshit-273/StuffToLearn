#include <stdio.h>

void main() {
	printf("%f:Normal Number with default precision\n", 3.1415926535); // default precision for float is 6 digits after the point
	printf("%3d:Number with 3 width(total spaces taken is atleast 3)\n", 7); // Number will take up atleast 3 spaces, so right justifying in case of less digits than 3
	printf("%03d:Number with 3 width(total spaces taken is atleast 3) and preceeded with 0\n", 7); //Number will take u atleast 3 spaces and if number has less digits than 3 then preceed the number with 0s.
	printf("%-3d:Number with 3 width(total spaces taken is atleast 3) and left justified\n", 7); // Left justified, taking atleast 3 spaces
	printf("%+d:Number preceeded with the sign of the number\n", 7); // Number is preceeded with the sign of the number
	printf("%3.3f:Number with 3 width(total spaces taken is atleast 3) and 3 digit precision after the point", 3.1415926535); // Number after the point will specify the precision value, so if number has more digits then the specified precision number then the number will be rounded off
}

/*
Output:
3.141593:Normal Number with default precision
  7:Number with 3 width(total spaces taken is atleast 3)
007:Number with 3 width(total spaces taken is atleast 3) and preceeded with 0
7  :Number with 3 width(total spaces taken is atleast 3) and left justified
+7:Number preceeded with the sign of the number
3.142:Number with 3 width(total spaces taken is atleast 3) and 3 digit precision after the point
*/