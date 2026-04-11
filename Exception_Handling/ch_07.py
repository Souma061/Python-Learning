# # # File handling and exception handling

# # file = open("order.txt", "w")
# # try:
# #     file.write("Order details: 2 cups of masala chai\n")
# # finally:
# #     file.close()  # This will not be executed if an exception occurs before this line


# with open("order.txt","w") as file:
#     file.write("Order details: 5 cups of masala chai\n")


# #Behind the scenes, the with statement is doing something like this:
# # file = open("order.txt", "w")
# # try:
# #     file.write("Order details: 5 cups of masala chai\n")
# # finally:
# #     file.close()  # This ensures that the file is properly closed even if an error occurs during the write operation


# with open("order.txt","r") as file:
#     content = file.read()
#     print(content)


import os
import csv

# # Check if the file exists before trying to read it
file_exists = os.path.exists("data.csv")
with open("data.csv", "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["Name", "Age", "City"])  # Write header if file doesn't exist
        writer.writerow(["Alice", 30, "New York"])
    else:
        writer.writerow(["Bob", 25, "Los Angeles"])
