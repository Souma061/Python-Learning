# walrus operator

# value = 13
# remainder = value % 5

# print(f"{value} divided by 5 has a remainder of {remainder}")



value = 13

if( remainder := value % 5): #walrus operator(:=)
    print(f"{value} divided by 5 has a remainder of {remainder}")


# walrus operator is used to assign a value to a variable as part of an expression. It allows you to both compute and assign a value in a single line of code, which can make your code more concise and readable.


names = ["Alice", "Bob", "Charlie", "David", "Eve"]

if(name := input("Enter a name:")) in names:
    print(f"{name} is in the list.")
else:
    print(f"{name} is not in the list.")
