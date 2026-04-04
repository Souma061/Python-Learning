# SET

essential_spices = {"salt", "pepper", "cumin", "turmeric"}
optional_spices = {"turmeric", "garlic powder", "cayenne pepper"}

# Union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# Intersection
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# Difference
unique_essential_spices = optional_spices - essential_spices
print(f"Unique essential spices: {unique_essential_spices}")

print(f"Is 'salt' an essential spice? {'salt' in essential_spices}")
print(f"Is 'salt' an optional spice? {'salt' in optional_spices}")
