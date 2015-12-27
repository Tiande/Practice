/*
 * GCD: Greatest Common Divisor
 * 最大公因数
 * Euclid算法
 */
#include <stdio.h>

//其实 n m 的位置并不重要
int gcd(int n, int m)
{
    if (0 == n%m) {
        return(m);
    }
    return(gcd(m,n%m));
}

int main()
{
    int m,n,s;
    printf("请输入两个整数:\n");
    scanf("%d%d", &m, &n);
    printf("the GCD of %d & %d is:%d\n", m, n, gcd(n,m));
    return 0;
}
