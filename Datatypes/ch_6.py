#List

Colors = ["Red", "Green", "Blue", "Yellow", "Pink"]



Colors2 = ["Cyan", "Magenta", "Black", "White"]

print(Colors)
print(Colors.append("Purple"))
print(Colors)
print(Colors[1])
print(Colors.pop(4))
Colors.sort()
print(Colors)

numbers = [5, 2, 9, 1, 5, 6]
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

joint_colors = Colors + Colors2
joint_colors.reverse()
print(joint_colors)



mix_array = [1, "Hello", 3.14, True]
for i in range(len(mix_array)):
    print(i,mix_array[i])


#operator overloading

strong_chai = ["water", "tea"] * 3
print(strong_chai)


#bytearray
raw_data = bytearray(b"MOM")
raw_data = raw_data.replace(b"M", b"S")
print(raw_data)
