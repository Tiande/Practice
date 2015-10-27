#include <stdio.h>

/* Struct
 * 23:45 2015-10-21
 */

int main(void)
{
    struct complex_struct { double x, y; } z;
    double x = 3.0;
    z.x = x;
    z.y = 4.0;
    if (0 > z.y) {
        printf("z=%f%fi\n", z.x, z.y);
    }
    else{
        printf("z=%f+%fi\n", z.x, z.y);
    }
    return 0;
}

