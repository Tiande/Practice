#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 20

//循环打印histogram

int a[N];

void gen_random(int upper_bound)
{
    int i;
    unsigned int seed;
    seed = time(NULL);
    srand(seed);
    for (i = 0; i < N; i++) {
        a[i] = rand() % upper_bound;
    }
}

int main(void)
{
    int i, j, max = 0, histogram[10] = {0};

    gen_random(10);
    for (i = 0; i < N; i++) {
        histogram[a[i]]++;
    }

    printf("水平方向打印: \n"); 
    for (i = 0; i < 10; i++) {
        printf("%d ", i);
        for (j = 0; j < histogram[i]; j++) {
            printf("* ");
        }
        printf("\n");
    }

    printf("\n\n垂直方向打印：\n");
    for (i = 0; i < 10; i++) {
        max = (max > histogram[i]) ? max : histogram[i]; //取最多的做基数
        printf("%d ", i);
    }   
    printf("\n\n");
    for (i = 0; i < max; i++) {
        for (j = 0; j < 10; j++) {
            if (histogram[j] > 0) {
                printf("* ");
                --histogram[j];
            }
            else{
                printf("  ");
            }
        }
        printf("\n");
    }   
    printf("\n");
    
    return 0;
}
