#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316399410395f704750ee9440228135925a6ca1dad8000


Definition

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


~/Practice/python/pytest.py




