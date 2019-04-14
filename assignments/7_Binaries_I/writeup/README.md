# Writeup 7 - Binaries I

Name: Kenton Wong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Kenton Wong

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
printf("your code here");

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
```

### Part 2 (10 Pts)

This program performs a swap of two integers without using extra memory space.
