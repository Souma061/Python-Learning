# # Write a function that:

# Takes a list of numbers
# Returns a new list with only even numbers


# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def even_numbers(list):
#     even_numbers = []
#     for i in list:
#         if i % 2 == 0:
#             even_numbers.append(i)
#     return even_numbers

# print(even_numbers(num))


# #data = {"a": 10, "b": 20, "c": 30}

# 👉 Print keys and values like:

# a -> 10
# b -> 20
# c -> 30

# data = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }


# for key,values in data.items():
#     print(f"{key} -> {values}")


# # Write a program to:

# Count frequency of each character in a string


# string = "hello world"

# def count_frequency(str):
#     frequency = {}
#     for char in str:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     return frequency


# print(count_frequency(string))


# # Find:

# Maximum
# Minimum
# WITHOUT using max() or min()

# list = [5, 2, 9, 1, 5, 6]

# def find_max_min(lst):
#     max_num = lst[0]
#     min_num = lst[0]

#     for num in lst:
#         if num > max_num:
#             max_num = num
#         if num < min_num:
#             min_num = num
#     return max_num,min_num



# max_value, min_value = find_max_min(list)
# print(f"Maximum: {max_value}")
# print(f"Minimum: {min_value}")


data = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 60},
    {"name": "C", "marks": 90}
]

# 👉 Print the student with highest marks

top_student = data[0]
for student in data:
    if student["marks"] > top_student["marks"]:
        top_student = student

print(f"Top student: {top_student['name']} with marks {top_student['marks']}")
