#If the inheritance follows below then it will be diamond problem
#                  A
#                 / \
#                B   C
#                 \ /
#                  D
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        print("B")

class C(A):
    def greet(self):
        print("C")

class D(B, C):
    pass

d = D()
d.greet()
print(D.__mro__)