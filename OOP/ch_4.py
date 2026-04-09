class ChaiCup:
    size = 100

    def describe(self):
        return f"This is a chai cup of size {self.size} ml."



cup = ChaiCup()
# print(cup.describe())
print(ChaiCup.describe(cup))
