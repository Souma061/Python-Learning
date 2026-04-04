amount = 12
print(f"Amount: {amount}")
print(f"Amount id: {id(amount)}")
amount = 15
print(f"Amount: {amount}")
print(f"Amount id: {id(amount)}")



# in python, integers are immutable, so when we assign a new value to the variable 'amount', it creates a new object in memory, which is why the id changes.
