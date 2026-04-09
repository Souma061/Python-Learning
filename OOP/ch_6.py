# #inheritence and Composition
# class Employee:
#     def __init__(self,type_):
#         self.type = type_


#     def summary(self):
#         print(f"This is a {self.type} employee.")


# class Manager(Employee):
#     def occupation(self):
#         print("This employee is a manager.")


# class Developer:
#     cls = Employee

#     def __init__(self):
#         self.emp = self.cls("New Developer")


#     def describe(self):
#         print(f"This is a developer who is a {self.emp.type} employee.")
#         self.emp.summary()



# class Company(Developer):
#     cls = Manager



# name = Developer()
# company = Company()
# name.describe()
# company.describe()


class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing a {self.type} chai.")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding spices to the chai.")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving a {self.chai.type} chai.")
        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()



