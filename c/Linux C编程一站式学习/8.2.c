#include <stdio.h>
#include <stdlib.h>
#define N 20 //使用 #define 定义一个常量，预处理阶段生成。 用 gcc -E 可看到 预处理之后、编译之前 的程序。

//生成并打印随机数

int a[N];

void gen_random(int upper_bound)
{
    int i;
    for (i = 0; i < N; i++) {
        a[i] = rand() % upper_bound; // %运算 将 rand() 转化为小于 upper_bound 的数
    }
}

void print_random()
{
    int i;
    for (i = 0; i < N; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

int main(void)
{
    int i, histogram[10] = {0}; //histogram 直方图 使用前必须初始化

    gen_random(10);
    print_random();

    // 统计各数岀现次数
    for (i = 0; i < N; i++) {
        histogram[a[i]]++;
    }

    return 0;
}
