# integer
import sys
from fractions import Fraction
from decimal import Decimal
num1 = 10
num2 = 20

print(f"num1: {num1}, id: {id(num1)}")

num3 = num1 + num2
num4 = num1 - num2
print(f"num3: {num3}")
print(f"num4: {num4}")


num5 = 34
num6 = 4

num = num5 / num6
print(f"num: {num}")

new_num = 67.2
another_num = 12.4

result = new_num * another_num
print(f"result: {result}")


total_cardamom = 10
pods_per_cup = 3
leftover_pods = total_cardamom % pods_per_cup

print(f"Leftover cardamom pods: {leftover_pods}")

flvor = 2
scale = 3
scaled_factor = flvor ** scale
# ** = exponentiation operator, it raises the number to the power of the exponent 2 * 2 * 2 = 8
print(f"Scaled flavor factor: {scaled_factor}")

# boolean

is_raining = True
is_sunny = False
print(f"Is it raining? {is_raining}")
print(f"Is it sunny? {is_sunny}")

is_boiling = True
stri_count = 5

total_actions = stri_count + is_boiling #upcasting, True is treated as 1 and False is treated as 0
print(f"Total actions: {total_actions}")

milk_present = 0
print(f"is milk present? {bool(milk_present)}") # 0 is treated as False, any non-zero value is treated as True


# logical operators
# and, or, not


age = 30
is_teenager = age >= 10 and age <= 19
print(f"Is the person a teenager? {is_teenager}")

#leap year
year = 1900
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"Is {year} a leap year? {is_leap_year}")


# real numbers
pi = 3.14159
radius = 5
circumference = 2 * pi * radius
print(f"Circumference of the circle: {circumference}")
print(sys.float_info)
