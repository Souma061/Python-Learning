#MRO

class A:
    label = "A: Base class"


class B(A):
    label = "B: Another class"

class C(A):
    label = "C: Yet another class"

class D(C,B):
    pass


cup = D()
print(cup.label) # C: Yet another class
print(D.__mro__) # (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


#MRO is the method resolution order, which is the order in which Python looks for a method or attribute in a class hierarchy. In this example, when we create an instance of class D and access the label attribute, Python first looks in class D, then in class C, then in class B, and finally in class A. Since class C has the label attribute defined, it returns "C: Yet another class".
