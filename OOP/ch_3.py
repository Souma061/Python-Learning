#Attribute Shadowing

class Chai:
    temperature = "hot"
    strength = "strong"
    cup = "glass"

cutting = Chai()
print(cutting.temperature)


cutting.temperature = "cold"
cutting.cup = "ceramic"
print(cutting.temperature)
print(cutting.cup)
print(Chai.temperature)


del cutting.temperature
print(cutting.temperature)
del cutting.cup
print(cutting.cup)



#Attribute shadowing means that when we assign a value to an attribute on an instance, it creates a new attribute on that instance that shadows the class attribute with the same name. This allows us to have different values for the same attribute on different instances of the class.
