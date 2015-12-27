#include <stdio.h>
#include <math.h>

void print_parity(int x)
{
    if (x % 2 == 0) {
        printf("%d is even.\n", x);
    }
    else{
        printf("%d is odd.\n", x);
    }
}

//get the unit and decade of integer
void print_unitdecade(int x)
{
    printf("the unit of %d is: %d\n", x, x%10);
    printf("the decade of %d is: %d\n", x, x/10%10);
}

void print_day(int day)
{
    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        case 4:
            printf("Thursday\n");
            break;
        case 5:
            printf("Friday\n");
            break;
        case 6:
            printf("Saturday\n");
            break;
        case 7:
            printf("Sunday\n");
            break;
        default:
            printf("Illegal day number: %d\n", day);
            break;
    }
}

void myround(double x)
{
    printf("ceil of %f is: %f\n", x, ceil(x));
    printf("floor of %g is: %g\n", x, floor(x));
}

int main(void)
{
    int x = 4;

    if (x != 0) {
        printf("x is nonzero.\n");
    }   
    else{
        printf("hhhh");
    }

    print_parity(17);
    print_parity(18);

    print_unitdecade(5);
    print_unitdecade(159);

    print_day(5);
    print_day(12);

    myround(-3.51);

    return 0;
}
