amount = set()
print(f"Amount: {amount}")
print(f"Amount id: {id(amount)}")
amount.add(12)
amount.add(15)
print(f"Amount: {amount}")
print(f"Amount id: {id(amount)}")


# Output:
# Amount: set()
# Amount id: 140353303441984
# in python, set is mutable, so the id of the set remains the same even after adding elements to it.
