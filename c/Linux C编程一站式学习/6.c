#include <stdio.h>
#include <math.h>

//复数的结构体函数练习

//复数运算
struct complex_struct{
    double r, A;
};

double real_part(struct complex_struct z)
{
    return z.r * cos(z.A);
}

double img_part(struct complex_struct z)
{
    return z.r * sin(z.A);
}

double magnitude(struct complex_struct z)
{
    return z.r;
}

double angle(struct complex_struct z)
{
    return z.A;
}

struct complex_struct make_from_real_img(double x, double y)
{
    struct complex_struct z;
    z.A = atan2(y, x);
    z.r = sqrt(x * x + y * y);
    return z;
}

struct complex_struct make_from_mag_ang(double r, double A)
{
    struct complex_struct z;
    z.r = r;
    z.A = A;
    return z;
}



//坐标运算
//struct complex_struct{
//    double x, y;
//};
//
//double real_part(struct complex_struct z)
//{
//    return z.x;
//}
//
//double img_part(struct complex_struct z)
//{
//    return z.y;
//}
//
//double magnitude(struct complex_struct z)
//{
//    return sqrt(z.x * z.x + z.y * z.y);
//}
//
//double angle(struct complex_struct z)
//{
//    return atan2(z.y, z.x);
//}
//
//struct complex_struct make_from_real_img(double x, double y)
//{
//    struct complex_struct z;
//    z.x = x;
//    z.y = y;
//    return z;
//}
//
//struct complex_struct make_from_mag_ang(double r, double A)
//{
//    struct complex_struct z;
//    z.x = r * cos(A);
//    z.y = r * sin(A);
//    return z;
//}
//
//struct complex_struct add_complex(struct complex_struct z1, struct complex_struct z2)
//{
//    return make_from_real_img(real_part(z1) + real_part(z2),
//                               img_part(z1) + img_part(z2));
//}
//
//struct complex_struct sub_complex(struct complex_struct z1, struct complex_struct z2)
//{
//    return make_from_real_img(real_part(z1) - real_part(z2),
//                               img_part(z1) + img_part(z2));
//}
//
//struct complex_struct mul_complex(struct complex_struct z1, struct complex_struct z2)
//{
//    return make_from_mag_ang(magnitude(z1) * magnitude(z2),
//                             angle(z1) + angle(z2));
//}
//
//struct complex_struct div_complex(struct complex_struct z1, struct complex_struct z2)
//{
//    return make_from_mag_ang(magnitude(z1) / magnitude(z2),
//                             angle(z1) - angle(z2));
//}
//
//int main()
//{
//    return 0;
//}
