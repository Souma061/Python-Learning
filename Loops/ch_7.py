flavours = ["Masala Chai", "Discontinued", "Cardamom Chai", "Out of stock", "Tulsi Chai"]



for flavour in flavours:
    if flavour == "Discontinued":
        # print(f"{flavour} is no longer available. Please choose another flavour.")
        continue
    elif flavour == "Out of stock":
        # print(f"{flavour} is currently out of stock. Please choose another flavour.")
        break
    else:
        print(f"Preparing {flavour} for you!")
