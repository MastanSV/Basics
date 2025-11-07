import math

from decimal import Decimal
from fractions import Fraction
import sys
#Create three variable name, age and city and print them
'''
name = "Mastan"
age = 28
city = "Hyd"

print(name)
print(age)
print(city)
'''


#Swap two variables without using third variable.
'''
a = 10
b = 20

print('a, b values before swaping : ', a , ', ', b)

a = a + b
b = a - b
a = a - b
print('a, b values after swaping : ', a , ', ', b)
'''

#Reverse a string
'''
org = 'hello'
rev = ''
for i in range(len(org)):
    rev += org[len(org) - i - 1]

print(rev)


a = 10
b = 10
print(a is b)
print(id(a))
print(id(b))


c = 1000
d = 1000

print(c is d)
print(id(c))
print(id(d))


print(0.1 + 0.2 == 0.3)
print('using math.isclose() : ', math.isclose(0.1 + 0.2, 0.3))

print(f"Converting decimals using Decimal : {Decimal("0.1") + Decimal("0.2") == Decimal("0.3")}")

print(f"using Fraction 1/10 + 2/20 == 3/10:  {Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10)}")


print(issubclass(bool, int))


nums = [1, 3, 5, 1, 3, 7, 9]
print(list(set(nums)))

seen = set()
lst = []
for num in nums:
    if num not in seen: #Here seen lookup is O(1) - which is efficient
        lst.append(num)
    seen.add(num)
print(lst)
#space complexity: O(n) + O(n) = O(n)
#time complexity: O(n)

def tryHash(item):
    try:
        hash(item)
    except TypeError:
        return "Not able to generate hash"
    
    return "Hashable data."
    
print(tryHash((1, 3, 500)))
print(tryHash((1, 3, [5, 7, 9])))

(1, 3, 5)
a, b, c = (1, 3, 5)
print(a, b, c) 

a = 10
b = 20
c = 30
tu = (a, b, c)
print(tu)
print(type(tu))

tu = (10, 20, [30, 40, 50])
print(tu)
print(tu[2].append(70))
print(tu)
 
coord = (10.214545, 20.45678)
print(coord)

#size comparator
lst = [1, 2, 3, 4]
tup = (1, 2, 3, 4)

print(sys.getsizeof(lst))
print(sys.getsizeof(tup)) # tup is immutable it is memory efficient and suitable smaller data

s = {1, 20, 45, 60} # valid because all data is immutable and hashing is possible. 
#s = {1, 20, 45, 60, [1, 45, 75]} # invalid because set contains mutable data type for which hashing is not possible.
#s = {1, 2, 3, {4, 5, 6}}
s1 = {frozenset((1, 4, 5, 5, 7))}
print(s1)
print(tryHash({1, 2, 3}))
print(tryHash((1, 2, 3, (4, 5, 6))))


d = {'name' : 'Mastan', bool : 28, 2 : 'Hyderabad'}

for key in d.keys():
    print(key)
    print(d[key])


##be careful whenever using default fn args as default only created once at the function def, not
#every time you call the function.
def understanding_default_args(item, lst=[]):
    lst.append(item)
    return lst

print(understanding_default_args(10))
print(understanding_default_args(20))
print(understanding_default_args(30))


seen = set()
unique = []
input = [10, 10, 10, 20, 30, 40, 50]

for item in input:
    if item not in seen:
        unique.append(item)
    seen.add(item)

print(unique)

#Falsy values: None, 0, [], {}, ''
def CheckIfAndElse():
    if(None):
        print("checking if condition.")
    elif([]):
        print("Inside elif")
    else:
        print("Inside else.")

CheckIfAndElse()
#walrus operator:
#evaluate the expression and assigns value to it.
data = "ThisIsMyName"
if n := len(data) > 5:
    print("Word length is more than 5 letters.")



for i in range(5):
    print(i)
    if i == 4:
        break;
else:
    print('loop never broken')
#else will only execute if the loop executes fully. [means loops does not break.]

n = 3;
for i in range(2, int((n/2)+1)):
    if n % i == 0:
        print(f'{n} is not a prime number.')
        break
else:
    print(f'n is a prime number.')



print([i for i in range(1, 10) if i % 2 == 0])
print({i for i in range(1, 10) if i % 2 == 0})
d = {1 : 'one', 2 : 'two', 3 : 'three'}
print({k : f'{v} {v}' for k, v in d.items()})

gen = (x*x for x in range(10))
print(f'gen ----------------> {next(gen)}')
print(f'gen ----------------> {next(gen)}')
print(f'gen ----------------> {next(gen)}')
print(f'gen ----------------> {next(gen)}')

m = [[1, 2, 3], [4, 5, 6]]
print([x for row in m for x in row])

#Create a dictionary mapping words to their lengths in a sentence.
sentence = 'My name is mastan'
print({w : len(w) for w in sentence.split()})



print(sys.getsizeof((x*x for x in range(10**6))))
print(sys.getsizeof([x*x for x in range(10**6)]))

print(type((x*x for x in range(10**6))))
print(type([x*x for x in range(10**6)]))



def squares():
    for x in range(5):
        yield x*x

sq = squares()
for s in sq:
    print(s)
    break

print(next(sq))


def gen1():
    for n in range(10):
        yield n

def gen2():
    yield from gen1()

nums = gen2()
print(next(nums))
print(next(nums))


def gen1():
    x = yield 10
    print(f'inside loop : {x}')

va = gen1()

try:
    print(next(va))
    print(next(va))
except StopIteration:
    print('Generation exhausted. no values left to iterate.')


fs = [0, 1]
for i in range(2, 10):
    fs.append(fs[i-1] + fs[i-2]) 
print(fs)


import dis
dis.dis(lambda : [x for x in range(10)])

import timeit
print(timeit.timeit("[x**x for x in range(5)]"))
print(timeit.timeit("(x**x for x in range(5))"))


lst = [[1, 2, 3], [4, 5, 6]]
print([x for row in lst for x in row])


#Fibonacci series using for loop
lst = [0, 1]
for x in range(2, 10):
    lst.append(lst[x - 1] + lst[x - 2])

print(lst)

#Fibonacci series using while loop
lst = [0, 1]
n = 10
i = 2
while(i < (n - 2)):
    lst.append(lst[i - 1] + lst[i - 2])
    i += 1

print(lst)

#Fibonacci series using list comprehensions
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(10)]
print(fib)

#Fibonacci series using generators


def fibonacciSeries(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for x in fibonacciSeries(5):
    print(x)



inp = [1, 2, 3, 4, 5]

seen = set()

for num in inp:
    if num in seen:
        print(f'seen first duplicate : {num}')
        break;
    seen.add(num)
else:
    print('No duplicates found.')



def DummyFunction():
    print('This is my dummy function.')

print(type(DummyFunction))

def Dummy(a, b, c):
    print(a, b, c)

Dummy(1, 2, 3) #positional arguments

Dummy(a=1, b=2, c=3) #keyword arguments
Dummy(a=1, c=2, b=3)
#Dummy(a=1, 2, 3) #positional arguments can not appear after keyword arguments.
Dummy(1, 4, c=5) #its valid because positional arguments are not appearing after keyword arguments.
#Dummy(1, b=4, 5) #its not valid because positional arguments are appearing after keyword arguments

def defaultArgs(a, b=20, c=30):
    print(a, b, c)

defaultArgs(1)
defaultArgs(1, 40)
defaultArgs(1, 40, c=50)
defaultArgs(1, c=50)
#defaultArgs(1, b=20, 50) #not valid as positional arguments are appearing after keyword arguments



def trickyInterviewQs(a, lst=[]):
    lst.append(a)
    print(lst)

trickyInterviewQs(10)
trickyInterviewQs(20) #In python default parameters are initiated once and stored in memory
                        #so the same initiated lst will be reused.


def func(a, b, c):
    print(a, b, c)

lst = [1, 2, 3]
options = {"b" : 10, "c" : 20 }

func(100, **options)



def args(a, b, c=30, *args, **kwargs): # this order is imp. positional, keywords, defaults, arguments, kwargs
    print(f'a : {a}, b: {b}, c : {c}, args: {args}, kwargs: {kwargs}')

args(10,20,30,40,50,60,g=60, h=70)


len(b = "2")g

#scope resolution.
scope = "outer"
def outer():
    scope = "enclosing"
    def inner():
        scope = "inner"
        print(scope)
    inner()

outer()


#closure

def outer():
    msg = "outer"
    def inner():
        print(msg)
        #print(globals())
        #print(locals())
    return inner

inner = outer()
inner()
#print(inner.__closure__[0].cell_contents)

x = 10
def f():
    print(x)
    x = 20

f()


def outer():
    s = 10
    def inner():
        print(s)
    return inner

inner = outer()



sqr = lambda x : x * x
print(sqr(5))

#def Mul(a):
 #   return lambda x : x * a

def Mul(o):
    def byNum(i):
        return o * i
    return byNum

doub = Mul(2)
triple = Mul(3)

print(doub(10), triple(5))

class Dummy:
    pass

print(isinstance(Dummy, type))
print(object.__new__)
print(type.__call__)

class Sample:
    def __new__(cls):
        print(f'Before instanciating cls')
        instance = super().__new__(cls)
        print(f'after instanciating class')
        return instance
    def __init__(self):
        print(f'Object initializing')

sobj = Sample()


class singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print(f'Creating the new instance.')
            cls._instance = super().__new__(cls)
        else:
            print(f'Returning the existing instance.')

        return cls._instance
    def __init__(self):
        print(f'obj instanciated.')
    
sObj = singleton()
sObj = singleton()


class understandClass:
    _clsVariable = None

    def initializeClsVar(cls):
        cls._clsVariable = 'abc'
        print(cls._clsVariable)

csobj = understandClass()
csobj.initializeClsVar()
#understandClass.initializeClsVar() #as this is not a instance method it expects the object to passed
#inorder to make the above method as instance method we should mark it with decorator

class understandClassT:
    _clsVariable = None

    @classmethod
    def initializeClsVar(cls):
        cls._clsVariable = 'abc'
        print(cls._clsVariable)

csObjT = understandClassT()
csObjT.initializeClsVar()

understandClassT.initializeClsVar() #abc --> no error as clearly mentioned as class method

class Animal:
    def __init__(self):
        print(self)

class Dog(Animal):
    def __init__(self):
        super().__init__()


dog = Dog()

class Animal:
    def bark(self):
        print('Animal is barking')

class Dog(Animal):
    pass

animal = Dog()
animal.bark()

class Parent:
    def ask(self):
        print('inside parent asking.')

class Child(Parent):
    def ask(self):
        #super().ask()
        print('inside child ask.')

ch = Child()
ch.ask()

#single inheritance
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mdt(Employee):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email

mdtEmployee = Mdt('Mastan', 28, 'valis.mastan23@gmail.com')
print(mdtEmployee.age)
print(mdtEmployee.name)
print(mdtEmployee.email)

#multilevel inheritance 
class A:
    def __init__(self, a):
        self.a = a

    def printA(self):
        print(f'A is {self.a}')
        
class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def printB(self):
        print(f'B is {self.b}')

class C(B):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def printC(self):
        print(f'C is {self.c}')

c = C(10, 20, 30)
c.printA()
c.printB()
c.printC()


#Multiple Inheritance
class A:
    def __init__(self):
        pass

class B:
    def __init__(self):
        pass

class C(B, A):
    def __init__(self):
        pass

c = C()
print(c)


#Hirarchical Inheritance
class A:
    def __init__(self):
        pass
    def AisCommon(self):
        print('A is common')

class B(A):
    def __init__(self):
        pass

class C(A):
    def __init__(self):
        pass

c = C()
b = B()
c.AisCommon()
b.AisCommon()

'''

