#include <stdio.h>

int main()
{
    int count[4] = { 3, 2, }, i;
    int count1[] = { 3, 2, 1, };
    int count2[4] = { [2] =3 };
    
    for (i = 0; i < 4; i++) {
        printf("count[%d]=%d\n", i, count[i]);
    }   
    return 0;
}
