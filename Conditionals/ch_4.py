device_status = input("Is the device on or off? (Active/Off): ").lower()
input_temp = input("Enter the current temperature: ")
input_temp = int(input_temp)



if device_status == "off":
    print("Device is off. Please turn it on to proceed.")
elif device_status == "active":
    if input_temp > 35:
        print("Temperature is too high. Please cool down the device.")
    else:
        print("Device is active and temperature is within the safe range.")
else:
    print("Invalid input. Please enter 'Active' or 'Off' for device status.")
