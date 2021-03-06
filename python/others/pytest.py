#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"http:/"/www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316399410395f704750ee9440228135925a6ca1dad8000
import sys
sys.path.append('lib')






# socket
'''
# TCP
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)
'''




# GUI
'''
from tkinter import *
import tkinter.messagebox as messagebo

class Application(Frame):
    def __init__(self, master=None):
        """docstring for __init__"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """docstring for createWidgets"""
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello',  command=self.hello)
        self.alertButton.pack()
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        """docstring for hello"""
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()
'''





# PIL
'''
from PIL import Image
im = Image.open('img/a.jpg')
w, h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))
im.save('img/thumbnail.jpg', 'jpeg')

from PIL import ImageFilter
# im = Image.open('img/a.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('img/blur.jpg', 'jpeg')

from PIL import ImageDraw, ImageFont, ImageFilter
import random
def rndChar():
    """random word"""
    return chr(random.randint(65, 90))
def rndColor():
    """random color"""
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def rndColor2():
    """random color"""
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('img/code.jpg', 'jpeg')
'''



# HTMLParser
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         """docstring for handle_starttag"""
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         """docstring for handle_endtag"""
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         """docstring for handle_startendtag"""
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         """docstring for handle_data"""
#         print(data)
#
#     def handle_comment(self, data):
#         """docstring for handle_comment"""
#         print('<--', data, '-->')
#
#     def handle_entityref(self, name):
#         """docstring for handle_entityref"""
#         print('&%s' % name)
#
#     def handle_charref(self, name):
#         """docstring for handle_charref"""
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')




# XML
## DOM
## SAX






'''
# itertools
import itertools
natuals = itertools.count(1)
for n in natuals:
    print(n)

cs = itertools.cycle('ABC')
ns = itertools.repeat('A', 3)

ns = itertools.takewhile(lambda x: x <= 10, natuals)
list(ns)

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
'''






'''
# hashlib
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()

def calc_md5(password):
    """The-Salt"""
    return get_md5(password + 'the-Salt')
'''


'''
# datetime
from datetime import datetime
now = datetime.now()
now.timestamp()
datetime.fromtimestamp(1429417200.0)
datetime.utcfromtimestamp(1429417200.0)
datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
now.strftime('%a, %b %d %H:%M')

from datetime import timedelta
now + timedelta(days=2, hours=12)

from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc_8)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
'''







# 多线程
'''
import time, threading

def loop():
    """新线程执行的代码"""
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name=('LoopThread'))
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
'''

# Lock
'''
lock = threading.Lock()
def run_thread(n):
    """lock"""
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
'''

# ThreadLocal
'''
import threading
local_school = threading.local()

def process_student():
    """获取当前线程关联的 student"""
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    """绑定 ThreadLocal 的 student"""
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
'''













# 多进程 multiprocessing
'''
import os
print('Process (%s) start...' % os.getpid())
pid = os.fork()
print(pid)
if pid==0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''

# Process 创建进程
'''
import os
from multiprocessing import Process

def run_proc(name):
    """docstring for run_proce"""
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join() # 等待子进程结束
    print('Child process end.')
'''


# Pool
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    """docstring for long_time_task"""
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
'''


'''
from multiprocessing import Process
import os

def run_proc(name):
        print("name=%s,PID=%s"%(name,os.getpid()))

print(os.getpid())
p=Process(target=run_proc,args=('aaaa',))
p.start()
p.join()
print('Child process end.')
if __name__=='__main__':
'''


'''
# 子进程
import subprocess

# print('$ nslookup www.baidu.com')
# r = subprocess.call(['nslookup', 'www.baidu.com'])
# print('Exit code: ', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nbaidu.com\nexit\n')
print(output.decode('utf-8'))
print('Exit code: ', p.returncode)
'''


'''
# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    """写数据进程执行的代码"""
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    """读数据进程执行的代码"""
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if '__main__'==__name__:
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate() # 强行终止死循环
'''













# 序列化
'''
# pickling unpickling
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

# loads() 将 bytes 反序列化为对象
# load() 直接操作 file-like Object
with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
print(d)
'''

# json
'''
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age":20, "SCORE": 88, "NAME": "Bob"}'
print(json.loads(json_str))

# print(json.dumps(s, default=student2dict)) # 自定义对象的转换函数

# 把任意 class 实例变为 dict
# print(json.dumps(s, default=lambda obj: obj.__dict__))
'''














'''
# 操作文件和目录
import os
print(os.uname())
# print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))
print(os.path.join('/home/tiande/Practice/python', 'testdir'))
os.mkdir('/home/tiande/Practice/python/testdir')
os.rmdir('/home/tiande/Practice/python/testdir')

print(os.path.split('/home/tiande/Practice/python/testdir'))
print(os.path.splitext('/home/tiande/Practice/python/test.txt'))
with open('test.txt', 'w') as f:
    f.write('This is a test txt for test.\n')
os.rename('test.txt', 'test.py')
os.remove('test.py')
with open('test.py', 'w') as f:
    f.write('This is a test txt for test.\n')
os.rename('test.py', 'test.txt')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.splitext(x)[1]=='.py'])

os.system('dir -l --color=auto')
os.system('find . -name *%s*' % input('输入你要查询的关键字：\n'))
'''









# StringIO
'''
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.getvalue())

f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())
'''








# IO
'''
f = open('./test.txt', 'r')
print(f.read())
f.close()

with open('./test.txt', 'r') as f:
    print(f.read())

f = open('./test.txt', 'r')
for line in f.readlines():
    print(line.strip()) # 去掉末尾的 \n

# file-like Object

f = open('./img/a.jpg', 'rb') # 二进制读取
print(f.read())
f.close()
'''

# encoding
'''
with open('./test.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())
'''

'''
with open('./test.txt', 'w+') as f:
    f.write('Hello, world!')
with open('./test.txt', 'r') as f:
    print(f.read())
'''






# 单元测试
# 文档测试








# 调试
## 断言
## 启用解释器时可以用 -0 参数关闭 assert
'''
def foo(s):
    """docstring for foo"""
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    """docstring for main"""
    foo('0')

## logging
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
'''
# pdb
'''
import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)
'''



'''
# 错误 、 调试 、测试
try:
    print('try...')
    r = 10 / int('2') # 10 / 2
    print('result: ', r)
except ValueError as e:
    print('ValueError: ', e)
except ZeroDivisionError as e:
    print('except: ', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# 记录错误
import logging

def foo(s):
    """docstring for foo"""
    return 10 / int(s)

def bar(s):
    """docstring for bar"""
    return foo(s) * 2

def main():
    """docstring for main"""
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

# 抛出错误
class FooError(ValueError):
    pass
def foo(s):
    """docstring for foo"""
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo('0')
'''









# 使用元类
'''
## type()
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
'''

'''
"""use type() create a class"""
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # (类名， 继承类， 绑定方法名)
'''

# metaclass 跳过






# Enum
'''
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon, '\n', day1 == Weekday.Tue)
print(Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

print(type(Enum), '\n', type(Month))
print(isinstance(Month.Jan, Month), '\n', isinstance(Month.Jan, Enum))
'''





# 定制类
'''
class Student(object):
    def __init__(self, name):
        """__init__"""
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__ # 简单粗暴解决 直接显示变量 问题

print(Student('Michael'))
s = Student('Michael')
s # 此时在 IDE 中仍会返回 <__main__.Student object at 0x109afb310>, 因为直接显示变量调用的不是 __str__()， 而是 __repr__()
'''

'''
# Fib 虽能作用于 for 循环，但仍不能当作 list 使用.  Fib()[5] 会报错
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        """该方法返回一个迭代对象"""
        return self

    def __next__(self):
        """__next__"""
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration(); # 停止迭代
        return self.a

for n in Fib():
    print(n)
'''


'''
class Fib(object):
    def __getitem__(self, n):
        """需判断是否为切片参数"""
        a, b = 1, 1
        if isinstance(n, int):
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # 切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[10])
print(f[0:5])
# f[:10:2] 并没有对 step 参数作处理
# __setitem__() 把对象视作 list 或 dict 来对集合赋值
# __delitem__() 用于删除某个元素
'''


'''
class Student(object):
    def __init__(self):
        """__init__"""
        self.name = 'Michael'
    def __getattr__(self, attr):
        """调用不存在的属性时，解释器调用此方法尝试获取属性,且此方法默认返回 None """
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age())
print(s.abc)
'''


'''
## 链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)


class Student(object):
    def __init__(self, name):
        """__init__"""
        self.name = name

    def __call__(self):
        """对实例进行调用的方法__call__"""
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

print('测试是否为 可调用 对象', '\n', callable(abs), '\n',callable([1, 2, 3]))
'''














'''
# 多重继承
## MixIn
class Dog(Mammal, RunnableMixIn, CarnivorusMixIn):
'''


# __slots__
'''
## 给实例绑定一个方法
class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    """set age"""
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
print(s.age)

def set_score(self, score):
    """set score"""
    self.score = score
Student.set_score = MethodType(set_score, Student) # 给 class 绑定方法
'''


'''
class Student(object):
    __slots__ = ('name', 'age')
s = Student()
s.name = 'Michael'
s.age = 25
# s.socre = 99 # no score attr

# __slots__ 对子类不起作用
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 9999
'''


'''
class Student(object):
    def get_score(self):
        """get score"""
        return self._score
    def set_score(self, value):
        """set score"""
        if not isinstance(value, int):
            raise ValueError('score must be an int!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100 !')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())
# s.set_score(9999)
'''

# @property 装饰器  将一个方法变成属性调用
'''
class Student(object):
    @property
    def score(self):
        """score"""
        return self._score
    @score.setter
    def score(self, value):
        """score"""
        if not isinstance(value, int):
            raise ValueError('score must be an int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100 !')
        self._score = value

s = Student()
s.score = 60
print(s.score)
# s.score = 9999

# 定义只读： 只定义 getter 方法， 不定义 setter 方法
class Student(object):
    @property
    def birth(self):
        """birth"""
        return self._birth
    @birth.setter
    def birth(self, value):
        """birth"""
        self._birth = value

    @property
    def age(self):
        """age"""
        return 2015 - self._birth
s = Student()
s.birth = 1995
print(s.age)
'''

'''
class Screen(object):
    @property
    def width(self):
        """width"""
        return self._width
    @width.setter
    def width(self, value):
        """set"""
        self._width = value

    @property
    def height(self):
        """height"""
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        """get"""
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
# assert s.resolution == 786431, '1024 * 768 = %d ?' % s.resolution # 断言
'''








'''
# 实例属性 和 类属性
class Student(object):
    def __init__(self, name):
        self.name = name
class Student(object):
    name = 'Student'
'''


# 获取对象信息
'''
print(type(123), ' ', type('123'), ' ', type(None), '\n', type(abs))
print(type(123)==type(456))
print(type(123)==int)
'''

## 判断对象是否为函数
'''
import types
def fn():
    """test"""
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

## 判断对象是否是某种类型 isinstance()
print(isinstance('a', str))
print(isinstance([1, 2, 3], (list, tuple)))

## dir() 获得对象所属性和方法
print(dir('ABC'))
print(len('ABC'), ' ', 'ABC'.__len__())

## len(XXX)==XXX.len()
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))
'''

'''
## 操作对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        """power"""
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'), '\n', hasattr(obj, 'y'), '\n', setattr(obj, 'y', 19), '\n',  hasattr(obj, 'y'), '\n', getattr(obj, 'y'))
print(obj.y)
## getattr(obj, 'z') 不存在会报错
print(getattr(obj, 'z', 404)) # 不存在，返回默认值
fn = getattr(obj, 'power') # 获取属性
print(fn)
print(fn())
'''







# OOP Object Oriented Programming
'''
class Student(object):
    def __init__(self, name, score):
        self.__name = name # 加 __ 变为私有变量 private 若要删改，需设定 get set 方法
        self.__score = score
    def print_score(self):
        """print"""
        print('%s: %s' % (self.__name, self.__score))
    def set_scoure(self, score):
        if 0 <= score <= 100:
            self.__scoure = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(bart._Student__name) # __name 可用 _Student__name 来访问
'''

'''
## 继承
class Animal(object):
    def run(self):
        """run"""
        print('Animal is running...')
class Dog(Animal):
    def run(self): # 覆写父类方法
        """run"""
        print('Dog is running...')
class Cat(Animal):
    pass
dog = Dog()
dog.run()
cat = Cat()
cat.run()
'''





# 安装第三方模块 pip

# 使用模块 Module




'''
# 偏函数 Partial function
print(int('12345'), ' ', int('12345', base=8), ' ',  int('12345', 16))
## def int2(x, base=2):
##     """int2"""
##     return int(x, base)
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
'''






'''
# 装饰器 Decorator
def now():
    """test"""
    print('2015-06-27')
f = now
f()

print(now.__name__)
print(f.__name__)

def log(func):
    """decorator"""
    def wrapper(*args, **kw):
        """wrapper"""
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    """print date"""
    print('2015-06-27 19:15')
now()
## now = log(now)
'''


'''
import functools # 导入 functools 模块
def log(text):
    """text log"""
    def decorator(func):
        """decorator"""
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    """date"""
    print('2015-06-27 19:22')

now()
print(now.__name__)
## now = log('execute')(now)
'''


'''
import functools
def logBoth(arg):
    """logBoth"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            """wrapper"""
            print('before call')
            res = func(*args, **kw)
            print('end call')
            return res
        return wrapper
    if isinstance(arg, str):
        print(arg)
        return decorator
    else:
        print('doesn\'t have str')
        return decorator(arg)

@logBoth
def now():
    """docstring for now"""
    print('2015-06-27 21:44')
now()
'''


'''
import functools

def log(ins):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            res = func(*args, **kw)
            print('end call')
            return res
        return wrapper

    if isinstance(ins, str):
        print(ins)
        return decorator
    else:
        return decorator(ins)

@log
def now():
    print('2015')

now()
'''



'''
# 匿名函数 lambda
print(list(map(lambda x: x * x, range(1, 10))))
## 返回 lambda
def build(x, y):
    """docstring for build"""
    return lambda: x * x + y * y
'''

'''
# 返回函数
def lazy_sum(*args):
    """return func"""
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f())
## 两次调用的非同一函数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)
'''

'''
# 闭包 Closure
## 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
'''

'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
'''






'''
# sorted()
print(sorted([36, 5, -12, 9, -21]))
## 绝对值大小
print(sorted([36, 5, -12, 9, -21], key=abs))
## ASCII 'Z' < 'a' ，故 Z 在 a 前
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

## 用一组tuple表示学生名字和成绩, 分别按名字排序,再按成绩从高到低排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda t: t[0]))
print(sorted(L, key=lambda t: t[1]))
print(sorted(L, key=lambda t: t[1], reverse=True))
'''






'''
# filter()
# 返回的是 Iterator
# 所以需要 list()
## 返回奇数
def is_odd(n):
    """docstring for is_odd"""
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

## 去空字符串
def not_empty(s):
    """docstring for not_empty"""
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))
'''





'''
## 埃氏筛法 求 素数
### 从 3 开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
### 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
### 定义生成器
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
for n in primes():
    if n < 100:
        print(n)
    else:
        break
'''

'''
# 回数
def is_palindrome(n):
    """docstring for is_palindrome"""
    string = str(n)
    return string == string[::-1]
print(list(filter(is_palindrome, range(1, 1000))))
'''







'''
# map()
def f(x):
    """map test"""
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

## 数字转字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce()
## reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
jdef add(x, y):
    """sum"""
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    """拼数字串"""
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

def fn(x, y):
    """to int"""
    return x * 10 + y

def char2num(s):
    """char2num"""
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(char2num('1'))
print(reduce(fn, map(char2num, '13579')))

def str2int(s):
    """str to int"""
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

## 使用 lambda 简化
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    """docstring for str2int"""
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(list('testlist'))
'''



'''
# map() 测试1： 规范英文名
## ['adam', 'LISA', 'barT']
## print([x for x in range(10)])
## print('qewr'.capitalize())
def normalize(name):
    """docstring for normalize"""
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习2
from functools import reduce
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)
print(prod([3, 5, 7, 9]))

# 练习3
def str2float(s):
    def zheng(x,y):
        return x * 10 + y
    def xiao(x,y):
        return x/10 + y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9 }[s]
    i = s.find('.')
    return(reduce(zheng,map(char2num,s[:i])) + reduce(xiao,map(char2num,s[-1:i:-1]))/10)

print('str2float(\'123.456\') = ',str2float('123.456'))
'''













'''
# struct

## 准确地讲，Python没有专门处理字节的数据类型。但由于str既是字符串，又可以表示字节，所以，字节数组＝str。
## 而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
## 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
### >>> n = 10240099
### >>> b1 = (n & 0xff000000) >> 24
### >>> b2 = (n & 0xff0000) >> 16
### >>> b3 = (n & 0xff00) >> 8
### >>> b4 = n & 0xff
### >>> bs = bytes([b1, b2, b3, b4])
### >>> bs
### b'\x00\x9c@c'

import struct
## 转换任意数据为 bytes （字节）
### bits 字位
### 1bytes = 8bits
### 1B = 8b

print(struct.pack('>I', 10240099))

### pack的第一个参数是处理指令，'>I'的意思是：
### >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
### 后面的参数个数要和处理指令一致。

## unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
### 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

## 首先找一个bmp文件，没有的话用“画图”画一个。 读入前30个字节来分析：
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

### BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
###
### 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
### 一个4字节整数：表示位图大小；
### 一个4字节整数：保留位，始终为0；
### 一个4字节整数：实际图像的偏移量；
### 一个4字节整数：Header的字节数；
### 一个4字节整数：图像宽度；
### 一个4字节整数：图像高度；
### 一个2字节整数：始终为1；
### 一个2字节整数：颜色数。
###
### (共30个字节)
###
### 所以，组合起来用unpack读取：

print(struct.unpack('<ccIIIIIIHH', s))

# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。

import struct

with open('a.bmp','rb') as f:
    s = f.read(30)

print('a.bmp 的头 30 字节(bytes) 为： ', s)

s = struct.unpack('<ccIIIIIIHH', s)
if s[0] + s[1] == b'BM' or s[0] + s[1] == b'BA':
    print('This is a bmp')
    print(s)
'''




'''
# base64
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

## 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_:
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

## Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。 Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉

## 请写一个能处理去掉=的base64解码函数：
import base64
def safe_base64_decode(s):
    """docstring for safe_base64_decode"""
    x = (-len(s)) % 4 # 负数取模 -7 % 4 = -2 * 4 + 1
    s = s + b'=' * x
    return base64.b64encode(s)
print(safe_base64_decode(b'YWJjZA'))
print(safe_base64_decode(b'YWJjZA=='))
'''






'''
# collections 集合模块
## namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, ' ', p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))
### circle
Circle = namedtuple('Circle', ['x', 'y', 'r'])

## deque
## 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。 deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
### 除了支持 list 的 append() pop() 还支持 appendleft() popleft()
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

## defaultdict
## dict 出现 KeyError 时返回默认值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key2'] # 会返回默认值

## OrderedDict
## 保持 Key 的顺序
## OrderedDict 的 Key 按照插入的顺序排列，而非 Key 本身排序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

## OrderedDict 实现一个 FIFO (先进先出) 的 dict， 当容量超出限制，先删除最早添加的 Key
## 删除老的，插入新的
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

## Counter
## 计数器
## 实际上是 dict 的子类
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
'''



'''
# 高阶函数
## 变量指向函数
print(abs(-10))
print(abs)
x = abs(-10)
f = abs
print(f(-10))




## 函数名其实是指向函数的变量
abs = 10
print(abs)
# 注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10
## 传入函数
## 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    """docstring for add"""
    return f(x) + f(y)
print(-5, 6, abs)
'''




'''
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
# iter() 将 list dict str 等 iterable 变成 iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
## for 循环本质上就是通过不断调用 next() 实现的：
for x in [1, 2, 3, 4, 5]:
    pass

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
'''




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
<<<<<<< HEAD
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 实际上返回的是 tuple
r = move(100, 100, 60, math.pi / 6)
print(r)
'''



'''
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
