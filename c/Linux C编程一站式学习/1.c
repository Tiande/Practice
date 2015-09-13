#include <stdio.h>
/* main: generate some simple output 
 * 
 * gcc main.c -o main.h
 * gcc -Wall main.c
 *
 */
int main(void)
{
    printf("Hello, world!\n");

    printf("character: %c\ninteger: %d\nfloating point: %f\n", '}', 34, 3.14);

    printf("%c\n", 'a'+1); // ascii

    return 0;
}
