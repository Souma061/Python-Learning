class ChaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls,order_data):
        return cls(
          order_data["tea_type"],
          order_data["sweetness"],
          order_data["size"]
        )
    @classmethod
    def from_string(cls,order_string):
        tea_type, sweetness,size = order_string.split("-")
        return cls(tea_type,sweetness,size)


class ChaiUtils:
    @staticmethod
    def calculate_price(order):
        base_price = 100
        if order.tea_type == "Elaichi Chai":
            base_price += 20
        elif order.tea_type == "Ginger Chai":
            base_price += 30
        elif order.tea_type == "Masala Chai":
            base_price += 40

        if order.sweetness == "Medium":
            base_price += 10
        elif order.sweetness == "High":
            base_price += 20

        if order.size == "Medium":
            base_price += 15
        elif order.size == "Large":
            base_price += 25

        return base_price

order1 = ChaiOrder.from_dict({
    "tea_type":"Elaichi Chai",
    "sweetness":"Medium",
    "size":"Large"
})

order2 = ChaiOrder.from_string("Ginger Chai-High-Small")

order3 = ChaiOrder("Masala Chai","Low","Medium")

price = ChaiUtils.calculate_price(order1)
print(f"Price of order1: {price}")

price = ChaiUtils.calculate_price(order2)
print(f"Price of order2: {price}")

price = ChaiUtils.calculate_price(order3)
print(f"Price of order3: {price}")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)


# __dict__ is a special attribute in Python that stores an object's attributes and their corresponding values in a dictionary format. It allows you to access and manipulate the attributes of an object dynamically. When you print an object's __dict__, it shows you all the attributes and their current values for that object.


# class methods are methods that are bound to the class and not the instance of the class. They can be called on the class itself rather than on an instance of the class. Class methods take a reference to the class (cls) as their first parameter, which allows them to access and modify class-level attributes. They are often used for factory methods that create instances of the class or for methods that operate on class-level data.


# Staticmethod vs Classmethod:
# 1. Binding: Static methods are not bound to the class or instance, while class methods are bound to the class.

# 2. First Parameter: Static methods do not take any special first parameter, while class methods take a reference to the class (cls) as their first parameter.

# 3. Usage: Static methods are typically used for utility functions that perform a specific task related to the class but do not require access to instance or class data. Class methods are often used for factory methods that create instances of the class or for methods that operate on class-level data.
