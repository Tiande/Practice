#include <stdio.h>

int main()
{
    int count[4] = { 3, 2, }, i;
    int count1[] = { 3, 2, 1, };
    int count2[4] = { [2] =3 };
    
    for (i = 0; i < 4; i++) {
        printf("count[%d]=%d\n", i, count[i]);
    }   
        //sizeof(count1) 求的是数组指针总长度， sizeof(count1[0]) 求的是指针长度
        printf("size of count is:%zu\n", sizeof(count1)/sizeof(count1[0]));
    return 0;
}
