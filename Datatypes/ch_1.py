amount = 12
print(f"Amount: {amount}")
print(f"Amount id: {id(amount)}")
amount = 15
print(f"Amount: {amount}")
print(f"Amount id: {id(amount)}")



# in python, integers are immutable, so when we assign a new value to the variable 'amount', it creates a new object in memory, which is why the id changes.


# Mutable data types ion python include lists, dictionaries, and sets. When we modify a mutable object, it does not create a new object in memory, so the id remains the same.

# Immutable data types in python include integers, floats, strings, and tuples. When we modify an immutable object, it creates a new object in memory, so the id changes.
