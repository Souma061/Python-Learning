#armstrong num

num = int(input("Enter a number: "))
power = len(str(num))

sum = 0
temp = num


while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10 #integer division

if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
