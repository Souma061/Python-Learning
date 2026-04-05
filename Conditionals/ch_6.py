seat_type = input("Enter your seat type (Sleeper/Ac/General/Luxury): ").lower()


match seat_type:
    case "sleeper":
        print("You have selected Sleeper class.")

    case "ac":
        print("You have selected AC class.")

    case "general":
        print("You have selected General class.")

    case "luxury":
        print("You have selected Luxury class.")

    case _:
        print("Invalid seat type. Please select from Sleeper, AC, General, or Luxury")
