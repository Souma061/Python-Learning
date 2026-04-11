def process_order(item,quantity):
    try:
        price = {"masala":20}[item]  # This will raise a KeyError if the item is not in the price dictionary
        cost = price * quantity
        print(f"The cost of {quantity} {item} chai is: {cost}")

    except KeyError as e:
        print(f"Error: {e} - The item '{item}' is not available in the price list.")
    except TypeError as e:
        print(f"Error: {e} - Quantity must be a number.")

process_order("ginger", 2) # This will raise a KeyError since "ginger" is not in the price dictionary
print("\n")
process_order("masala", "two")
# This will raise a TypeError
print("\n")
process_order("masala", 3)  # This will work correctly

