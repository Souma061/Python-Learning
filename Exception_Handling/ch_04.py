def brew_chai(flavor):
    if flavor not in ["chai", "masala chai", "ginger chai"]:
        raise ValueError(f"Flavor '{flavor}' is not available.")
    print(f"Brewing {flavor}...")



brew_chai("masala chai")  # This will work correctly
print("\n")
# brew_chai("lemon chai")  # This will raise a ValueError since "lemon chai" is not in the available flavors
