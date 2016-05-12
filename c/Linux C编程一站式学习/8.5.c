#include <stdio.h>

//多维数组
//
// \0 表示 ASCII 的 Null 字符

int main(void)
{
    int a[3][2] = { 1, 2, 3, 4, 5 };
    int b[][2] = {
        { 1, 2},
        { 3, 4},
        { 5, }
    };

    struct complex_struct{
        double x, y;
    } c[4] = { [0].x = 8.0 };

    struct {
        double x, y;
        int count[4];
    } s = { .count[2] = 9 };

    //如果是多维字符组，也可以嵌套使用字符串字面值做初始化
    char day[8][10] = {
        "",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    };

    return 0;
}
