# Try-Catch Block

chai_menu = {
    "chai": 10,
    "masala chai": 15,
    "ginger chai": 12,
}

try:
    chai_menu["chai"]  # This will raise a KeyError since "lemon chai" is not in the menu
    print("Chai is available.")
except KeyError as e:
    print(f"Error: {e} - The item is not available in the menu.")


# print("This line will not be executed due to the error above.")
print("This line will be executed regardless of the error.")


