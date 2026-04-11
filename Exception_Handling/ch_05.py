class OutOfIngredientsError(Exception):
    pass


def make_chai(milk,sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Cannot make chai - out of ingredients.")
    print("Chai is ready!")


make_chai(1, 1)  # This will work correctly
print("\n")
# make_chai(0, 1)  # This will raise an OutOfIngredientsError
