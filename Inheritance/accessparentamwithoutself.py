class Parent:
    def greet(self):
        print("Inside parent")

class Child(Parent):
    def greet(self):
        Parent.greet(self=self) #This is how you can call parent method without using self
        print("Inside Child")


child = Child()
child.greet()

#NOTE: You can access parent method/attributes as shown in above example, because of following reasons.
#1. Super() will do automatically methods/attributes as per MRO
#2. Super() will avoid using hardcoding of Classname in child classes.


