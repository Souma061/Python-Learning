#order

snack = input("Enter your snack: ").lower()

print(f"You have ordered: {snack}")


if snack == "cookies" or snack == "samosa":
    print("Your order have been accepted.")
else:
    print("Sorry, we don't have that snack available.")
