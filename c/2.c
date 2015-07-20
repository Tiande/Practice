#include <stdio.h>
#include <math.h>

/* gcc main.c -lm */

void newline(void); // 声明而未定义

void print_time(int hour, int minute){
    printf("%d:%d\n", hour, minute);
}

int main (void){
    double pi = 3.1416;

    printf("sin(pi/2)=%f\nln1=%f\n", sin(pi/2), log(1.0));

    newline();

    print_time(23, 59);

    return 0;
}

void newline(void){
    printf("\n");
}
