#ternary operator

order_amount = input("Enter the order amount: ")




try:
    order_amount = float(order_amount)
except ValueError:
    print("Invalid input. Please enter a numeric value for the order amount.")
    exit()



result = "Free delivary" if order_amount > 300 else "Delivery charge applicable"
print(result)
