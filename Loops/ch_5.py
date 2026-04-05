customer_name = ["Alice", "Bob", "Charlie", "David", "Eve"]
total_bills = [250, 300, 150, 400, 350]




for name,bill in zip(customer_name,total_bills):
    print(f"Customer {name} has paid a bill of {bill} rupees.")
