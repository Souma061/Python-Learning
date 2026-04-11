def serve_chai(flavor):
    try:
        print(f"Serving {flavor} chai.")
        if flavor == "unknown":
            raise ValueError("Unknown flavor cannot be served.")
    except ValueError as e:
        print(f"Error: {e}")

    else:
        print(f"{flavor} chai served successfully.")
    finally:
        print("Thank you for visiting our chai shop!")


serve_chai("masala")
print("\n")
serve_chai("unknown")
