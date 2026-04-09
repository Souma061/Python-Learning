class Bird:
    def __init__(self, type_,color):
        self.type = type_
        self.color = color
    def summary(self):
        return f"This is a {self.color} {self.type}."



bird1 = Bird("Parrot","Green")
print(bird1.summary())


bird2 = Bird("Pigeon","Grey")
print(bird2.summary())
