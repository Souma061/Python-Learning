# Dictionaries
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
my_info = dict(name="Souma", age=30, city="Howrah")
print(my_info)

extras = {}
extras["hobby"] = "Coding"
extras["favorite_color"] = "Blue"
print(extras["favorite_color"])

del extras["hobby"]
print(extras)

print(f"Is 'name' a key in my_info? {'name' in my_info}")


print(f"Keys in my_info: {my_info.keys()}")
print(f"Values in my_info: {my_info.values()}")
print(f"Items in my_info: {my_info.items()}")
