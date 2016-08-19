#include <stdio.h>
#include "20.2.stack.h"

/* extern void push(char); */
/* extern char pop(void); */
/* extern int is_empty(void); */

int a, b = 1;

int main(void)
{
    /* void push(char); */
    /* char pop(void); */
    /* int is_empty(void); */
    /* extern int top; */

    push('a');
    push('b');
    push('c');
    /* printf("%d\n", top); */

    while(!is_empty())
        putchar(pop());
    putchar('\n');
    
    return 0;
}
