#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316399410395f704750ee9440228135925a6ca1dad8000



# 迭代器
# Iterable
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance(100, Iterable))
# Iterator
from collections import Iterator
print(isinstance([], Iterator))
print(isinstance(100, Iterator))
print(isinstance((x for x in range(10)), Iterator))





'''
# 杨辉三角
def triangles():
    a = [1];
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
result = triangles()
i = 1
for a in result:
    i = i + 1
    print(a)
    if i > 10:
        break
'''

'''
# 生成器 generator
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10)) # This is a generator, 用来保存算法
print(g)
for n in g:
    print(n)

# fib function
def fib(max):
    """docstring for fib"""
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'
print(fib(6))
print('value value1 value3'.split())
'''
'''

# fib with generator
# use yield
def fibs(max):
    """docstring for fib"""
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
f = fibs(6)
print(f)
for n in f:
    print(n)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fibs(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# 调用 next() 时，遇到 yield 语句返回， 再次执行时从上次返回的 yield 处继续执行
def odd():
    """docstring for odd"""
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
print(next(o))
print(next(o))
print(next(o))

'''
'''
# 建议使用 for 循环
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # 超出索引
'''


'''
# 列表生成式
print(list(range(1, 11)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
# 两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')]) # os.listdir 列出文件和目录

# for同时使用两个甚至更多变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
print([k + '=' + v for k, v in d.items()])

# isinstance() 判断对象类型是否为指定值
x = 'abc'
y = 123
print(isinstance(x, int))
print(isinstance(y, int))

L1 = ['Hello', 'World', 18, 'Apple', None]
print([v.lower() for v in L1 if isinstance(v, str)])
'''


'''
# 判断对象是否为可迭代
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# enumerate() 将 list 变成 索引-元素对
# index 由 0 开始， list 内的元素变为 value
for i, value in enumerate(['A', 'b', 'C']):
    print(i, value)

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])

'''

'''
# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

print(L[0:3])
print(L[:3])
print(L[-2:])
print(L[-2:-1])
'''

'''
N = list(range(100))
# 前十个数，每两个取一个
print(N[:10:2])
# 所有数，每五个取一个
print(N[::5])
# 复制一个list
print(N[:])
# tuple
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串可看成一种 list ，但操作结果仍是字符串
print('ABCDEF'[:3])
print('ABCDEFG'[::2])
'''




'''
# 汉诺塔 (并不明白...)
def move(n, a, b, c):
    """docstring for move"""
    if n<1:
        return

    if n==1:
        print(a, '-->', c)

    if n!=1:
        move(n-1, a, c, b) # 将前n-1个盘子从a移动到b上
        move(1, a, b, c) # 将最底下的最后一个盘子从a移动到c上
        move(n-1, b, a, c) # 将b上的n-1个盘子移动到c上
n = input('pls input number:')
move(int(n), 'A', 'B', 'C')
'''




'''
# recursion
def fact(n):
    """docstring for fact"""
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(1))
print(fact(4))
print(fact(100))
# print(fact(1000)) # 将会 栈溢出

# 尾递归：函数返回时，调用自身，并且，return 不能包含表达式。
# 这种方式只占用一个栈帧，不会有栈溢出情况
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(25))
print(fact(1000))
# 尾递归 和 循环 等价
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题
'''




'''
# 参数组合：
# 参数定义顺序： 必选参数 默认参数 可变参数/命名关键字参数 关键字参数
def f1(a, b, c=0, *args, **kw):
    """docstring for f1"""
    print('a:', a, 'b:', b, 'c:', c, 'args:', args, 'kw:', kw)
def f2(a, b, c=0, *, d, **kw):
    """docstring for f2"""
    print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'kw:', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b') # **kw 将参数型的值转为 dict 显示，所以 'a' 'b' 在这里被视为是 args 的值。
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 通过 tuple dict 调用
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 99, 'x': '#'}
f2(*args, **kw)
'''




'''
# 命名关键字参数
# 下面例子的检查，显然并没有什么卵用
def person(name, age, **kw):
    """docstring for person"""
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack', 24, city='Beijing', addr='Chaoyang')

# * 为特使分隔符， * 后的参数被视为 命名关键字参数
def person(name, age, *, city='Beijing', job):
    """docstring for person"""
    print(name, age, city, job)
person('Jack', 25, city='Beijing', job='Engineer')
person('Jack', 25, job='Engineer')
# 该方式必须传入参数名
# 下面的会报错
# person('Jack', 25, 'Beijing', 'Engineer')
'''




'''
# 可变参数
def calc(*numbers):
    """docstring for calc"""
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)
calc(1, 4)
calc(2, 6, 3)
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
# 在 list tuple 前加 '*'， 把两者元素变为可变参数传入
calc(*nums)

# 关键字参数
# 传入的关键字将在函数内部自动组装成为一个 dict
def person(name, age, **kw):
    """docstring for person"""
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Ben', 35, **extra) #
'''







'''
def add_end(L=[]):
    """docstring for add_end"""
    L.append('END')
    print(L)

add_end([1, 2, 3])
# L 指向的 '[]' 参数在附加 'END' ， L 最好还是指向 不变的对象
add_end()
add_end()
add_end()
# 修改后的函数
def add_end2(L=None):
    """docstring for add_end2"""
    if L is None:
        L = []
    L.append('END')
    print(L)
add_end2()
add_end2()
add_end2()
'''

'''
def enroll(name, age, city='Shanghai', country='China'):
    print('name:', name)
    print('age:', age)
    print('city:', city)
    print('country:', country)

enroll('Tiande', 14)

enroll('DS', 12, country='Xian')
'''





'''
def power(x):
   return x * x

print(power(4))

# n's default value is 2 ;)
def powers(x, n=2):
    """docstring for powers"""
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(powers(5, 2))
print(powers(16, 2))
print(powers(6))
'''



'''
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

print(math.sqrt(2))
'''


'''
def my_abs():
    pass
print('pass',my_abs())



def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-9))
print(my_abs(12))
'''


'''
print(abs(100))
print(max(2, 3, 1 ,-21))
print(int('123'))
print(float(12.2323))
print(str(1.23))
print(bool(1))
print(hex(567))
'''

'''
t1 = (1, 2, 3)
t2 = (1, [2, 3])
s = set(t1)
print(s)
# s = set(t2)
# print(s)
d = {t1: 20}
print(d)
print(d[t1])
# d = {t2}
# print(d)
'''


'''
# set()
s = set([1, 2, 3])
print(s)
s = set([1, 2, 3, 1, 3,  2, 3])
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
'''


'''
# dict{}
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])
d['adam'] = 67
print(d['adam'])
d['adam'] = 68
print(d['adam'])
d['99'] = 'hahaha'
print(d['99'])

if 'lambert' in d:
    print('true')
else:
    print('false')

print(d.get('adam'))
print(d.get('lambert'))
print(d.get('lambert', 'Don\'t have this value'))

print(d.pop('Bob'))
'''



# names = ['Bob', 'Jany', 'Lucy']
# for name in names:
# 	print(name)
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
# 	sum = sum + x
# 	print(sum)
'''
print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
    print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    print(sum)

L = ['a','b','c']
for l in L:
    print(l)
'''

# age = int(input('input your age here: '))
# if age >= 18:
#     print('Your age is: ', age)
#     print('adult')
# elif age <= 6:
#     print('Oh, baby')
# else:
#     print('teenager')


# tuple
# classmates = ('Michael', 'Bob', 'Tracy')
# t = (1) # t = 1
# print(t,'\n')
# t = (1,) #tuple
# print(t,'\n')
# t = ('a','b',['A', 'B'])
# print(t,'\n')
# t[2][0] = 'X'
# print(t,'\n')


# list
# classmates = ['Bob','Jessey','Tommy']
# print(classmates,'\n','The len of this list is:',len(classmates),'\n',classmates[0],'\n',classmates[1],'\n',classmates[-1])
# classmates.append('Adam')
# print(classmates,'\n')
# classmates.insert(1, 'Jack')
# print(classmates,'\n')
# classmates.pop()
# print(classmates,'\n')
# classmates.pop(2)
# print(classmates,'\n')
# classmates[1] = 'Sarah'
# print(classmates,'\n')
# L = ['Apple', 123, True]
# print(L,'\n')
# s = ['python', 'java', ['asp', 'php'], 'scheme']
# print(len(s),'\n')
# print(s[2][1])


# print('Hello, %s' % 'World')
# print('Hi, %s, you have $%d.' % ('Michael', 1000000),'\n')

# print(len(b'ABC'))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# print(len('中文'.encode('utf-8')),'\n')

# print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'),'\n')

# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'),'\n')

# print(ord('A'),'\n')

# print(chr(25991),'\n')

# if 15 >= 18:
	# print('True')
# else:
	# print('False','\n')

# print('''line1
# line2
# line3
# end''','\n')

# print('默认不转义方式： ',r'\\\\n\t ;)','\n')

# print('\t','<--This is a tab','\n')

# print('Test the \'Slash Single Quotes\'','\n')

# print('1024 * 768 = ',1024*768,'\n')

# a,b=0,1
# print(a+b+110,'\n')

# name = input('Type your name here: ')
# print('Your name is: ',name,'\n')

# print('Hello World','\n')


# ~/Practice/python/pytest.py
