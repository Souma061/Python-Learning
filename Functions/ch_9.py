# chai = "Ginger"

# def prepare_chai(order):
#     print(f"Preparing {order} chai")


# prepare_chai(chai)


chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 4

edit_chai(chai)
print(chai)


def make_chai(tea,milk,sugar):
    print(f"Making {tea} chai with {milk} and {sugar}")

make_chai("Ginger", "Milk", "Sugar") #positional arguments

make_chai(milk="Milk",tea="Normal",sugar="Sugar") #keyword arguments


def special_chai(*ingredients, **extras):
    print("ingredients:", ingredients)
    print("extras:", extras)

special_chai("Cinnamon", "Cardamom", "Normal",sweetener="Honey", milk_type="Almond", size="Large", temperature="Hot")  #positional arguments and keyword arguments


def chai_orders(order=None): #default argument is mutable
    if order is None:
        order = []
    order.append("Ginger")
    print(order)



chai_orders()
chai_orders()
