# Property Decorators - Getter, Setter, Deleter

class TeaLeaf:
    def __init__(self,age):
        self._age = age


    @property
    def age(self):
        return self._age + 1

    @age.setter
    def age(self,age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Age must be between 1 and 5")




leaf = TeaLeaf(7)
leaf.age = 7
print(leaf.age)


#Propoerty Decorators - Read Only
#the usecases of read only properties are when you want to calculate a value based on other attributes of the class, and you don't want to allow the user to set that value directly.


