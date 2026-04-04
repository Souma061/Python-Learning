cup_size = input("Enter your cup size(Small/Medium/Large): ").lower()


if cup_size == "small":
    print("Prize: 10")
elif cup_size == "medium":
    print("Prize: 20")
elif cup_size == "large":
    print("Prize: 30")
else:
    print("Invalid cup size. Please enter small, medium, or large.")
