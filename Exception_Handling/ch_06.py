# Bill app with exception handling

class invalidChaiError(Exception):
    pass

def bill(flavor,cups):
    menu = {
        "chai": 10,
        "masala chai": 15,
        "ginger chai": 12,
        "lemon chai": 8
    }

    try:
        if flavor not in menu:
            raise invalidChaiError(f"Flavor '{flavor}' is not available.")
        if not isinstance(cups,int):
            raise TypeError("Number of cups must be an integer.")
        total_cost = menu[flavor] * cups
        print(f"The total cost for {cups} cups of {flavor} is: {total_cost}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting our chai shop!")


bill("masala chai", 3)  # This will work correctly
print("\n")
bill("lemon chai", 2)  # This will work correctly
print("\n")
bill("ginger", 2)  # This will raise an invalidChaiError since "ginger" is not in the menu
print("\n")
bill("chai", "two")  # This will raise a TypeError since the number of
