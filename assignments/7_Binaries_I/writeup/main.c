/*
 * Name: Kenton Wong
 * Section: 0201
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Kenton Wong
 */

/* your code goes here */
#include <stdio.h>

int main() {
	int a = 0xfeedface;
	int b = 0x1ceb00da;
	printf("a = %d\n", a);
	printf("b = %d\n", b);
	b ^= a;
	a ^= b;
	b ^= a;
	printf("a = %d\n", a);
	printf("b = %d\n", b);
	return 0;
}
