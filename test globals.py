
__version__ = '0.1'
__author__ = 'Gaye Imaël'

from functools import wraps, partial
import time
import asyncio
from itertools import groupby
from datetime import date
import copy
from abc import ABC, abstractmethod
from collections import deque
from operator import itemgetter, methodcaller

#context manager
class DecoContext():
    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return decorated
    def __enter__(self):
        print("Hey")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
    def __iter__(self):
        self.x = 1
        return self
    def __next__(self):
        self.x *= 3
        if self.x < 100:
            return self.x
        else:
            raise StopIteration

class Timer():
    @property
    def timer(self):
        print("Getting")
        return self._timer
    @timer.setter
    def timer(self, value):
        print("Setting")
        self._timer = value
    def __call__(self, func):
        self.timer = time.time()
        @wraps(func)
        async def run(*args, **kwargs):
            global print1, print2
            print1 = asyncio.create_task(print1(self.timer))
            print2 = asyncio.create_task(print2(self.timer))

            await print1
            await print2
            return await func(*args, **kwargs)

        return run

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def frombirthdate(cls, name, birthdate):
        return cls(name, date.today().year - birthdate)
    def display(self):
        print("Prénom: {}\nAge: {}".format(self.name, self.age))

class Coords():
    __slots__ = ('name', 'x', 'y')

class MyABC(ABC):
    @abstractmethod
    def display(self):pass
    @property
    @abstractmethod
    def test(self):
        print('test parent')

class Child(MyABC):
    def display(self):
        print('Child')
    def test(self):
        print('test child')

def DecorateClass(decor_arg):
    class ClassWrap:
        def __init__(self, cls):
            self.other_class = cls

        def __call__(self, *cls_ars):
            other = self.other_class(*cls_ars)
            other.field += decor_arg
            return other

    return ClassWrap

@DecorateClass(' is decorated')
class ClassDecorated():
    def __init__(self, name):
        self.field = name
    def __repr__(self):
        return str(self.field)

async def print1(timer):
    print(str(round(time.time() - timer, 2)) + " //0")
    await asyncio.sleep(2)
    print(str(round(time.time() - timer, 2)) + " //3")
async def print2(timer):
    print(str(round(time.time() - timer, 2)) + " //1")
    await asyncio.sleep(1)
    print(str(round(time.time() - timer, 2)) + " //2")

@DecoContext()
def foo():
    print("Func")

def foo2():
    print("Func 2")

@Timer()
async def foo3():
    print("Func 3")

def mul(a, b):
    return a**b if a != 0 and b != 0 else None

print("==========================================")
foo()
print("==========================================")
with DecoContext():
    foo2()
print("==========================================")
print(vars(DecoContext))
print("==========================================")
test = DecoContext()
a = iter(test)
while True:
    try:
        print(next(a))
    except StopIteration:
        break
print("==========================================")
b = (c ** 2 for c in range(5))
while True:
    try:
        print(next(b))
    except StopIteration:
        break
print("==========================================")
mul_exp_3 = partial(mul, b=3)
print(mul_exp_3(2))

mul_3 = partial(mul, 3)
print(mul_3(2))
print("==========================================")
asyncio.run(foo3())
print("==========================================")
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x for x in lst if x %2 == 0])
print("==========================================")
char = "AAAAAAAAAAAABBBBBAAAAAAAAAADDDDDDDDHHDDDDDCDDDDDDDD"
print(''.join([x for x,_ in groupby(char)]))
print("==========================================")
c = Person("Corenting", 19)
c.display()

d = Person.frombirthdate("Fabieng", 1974)
d.display()
print("==========================================")
e = [1, 2, 3]
print(id(e))
f = e
print(id(f))
f.append(4)
print(e)
print(str(id(e)) +" / " + str(id(f)))
print("==========================================")
g = [1, 2, 3]
print(id(g))
h = copy.deepcopy(g)
print(id(h))
h.append(4)
print(g)
print(str(id(g)) + " / " + str(id(h)))
print("==========================================")
i = [[0]*3]*3
i[0][0] = 1
print(i)
j = [[0 for x in range(3)] for x in range(3)]
j[0][0] = 1
print(j)
print("==========================================")
k = Coords()
k.x, k.y, k.name = 0, 255, 'Coucou'
try:
    k.test = 'test'
except AttributeError:
    print('Can\'t assign test')
finally:
    print(k.name)
print("==========================================")
l = Child()
l.display()
l.test()
print("==========================================")
m = ClassDecorated('A')
print(m)
print("==========================================")
n = deque([1, 2, 3], 3)
n.appendleft(0)
print(list(n))
print("==========================================")
getter = itemgetter(1)
print(getter([0, 2, 4, 6]))
print("==========================================")
l_append = methodcaller('append', 3)
lst = [0, 1, 2]
l_append(lst)
print(lst)
print("==========================================")
max : int
print(max)
print("==========================================")
