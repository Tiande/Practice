#include <stdio.h>

/*
 * stack LIFO
 */

char stack[512];
int top = 0;

void push(char c)
{
    stack[top++] = c;
}

char pop(void)
{
    return stack[--top];
}

int is_empty(void)
{
    return 0 == top;
}

int main(void)
{
    push('a');
    push('b');
    push('c');

    while (!is_empty()) {
        putchar(pop());
    }
    putchar('\n');

    return 0;
}
