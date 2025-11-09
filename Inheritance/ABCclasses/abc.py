'''from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Implementation from abstarct method.')

d = Dog()
d.speak()

class A: pass
class B(A): pass
class C(A): pass

# D inherits from B first, then C
class D(B, C): pass  # ✅ Works fine
class E(C, B): pass
class F(D, E):  # ⚠️ Error here
    pass
'''

class Test:
    def __init__(self):
        self.x = 10

    def add(self, a, b):
        return a + b
    

t = Test()
print(Test.__dict__)
print(t.__dict__)
