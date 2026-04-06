#Built in functions

def chai_flavor(flavor = "masala"):
    """Returns the flavor of chai."""
    return flavor


print(chai_flavor.__doc__)
print(chai_flavor.__name__)


# help(chai_flavor)

def generate_bill(chai=0,samosa=0,burger=0):
    """Calculates the total bill for the given quantities of items.
    :param chai: Quantity of chai ordered (default is 0)
    :param samosa: Quantity of samosas ordered (default is 0)
    :param burger: Quantity of burgers ordered (default is 0)
    """
    total = (chai * 10) + (samosa * 20) + (burger * 50)
    return total,"Thanks for ordering!"

print(generate_bill.__doc__)
print(generate_bill.__name__)
print(generate_bill(chai=2, samosa=3, burger=1))


