#include <stdio.h>
#include <math.h>

/* 素数
 * 23:02 2015-10-21
 * m不必呗2~m-1之间的每一个整数去除，只需被2~√m之间的每一个整数去除就可以了。如果m不能被2~√m间任一整数整除，m必定是素数。
 */

int main()
{
    int m,i,k;
    printf("请输入一个整数：");
    scanf("%d", &m);
    k = (int)sqrt(m); //sqrt. Computes square root of arg. 
    for (i = 2; i <= k; i++) {
        if (0 == m%i) {
            break;
        }
    }
    if (i>k) {
        printf("%d是素数。\n",m);
    }
    else{
        printf("%d不是素数。\n",m);
    }
}
