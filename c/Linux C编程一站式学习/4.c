#include <stdio.h>

// 阶乘
// do...while
int factorial(int n)
{
    int result = 1;
    int i = 1;
    do {
        result = result * i;
        i = i + 1;
    } while (i <= n);

    return result;
}

int factorial1(int n)
{
    int result = 1;
    while (n > 0) {
        result = result * n;
        n = n - 1;
    }

    return result;
}

int factorial2(int n)
{
    int result = 1;
    int i;
    for (i = 1; i <= n; ++i) {
        result = result * i;
    }
/*
 * for (int i = 1; i <= n; ++i) {...}
 * c99 可在 for 的 表达式1 处定义变量
 * gcc编译需要加 -std=c99
 */

    return result;
}

int main(void)
{
    return 0;
}
