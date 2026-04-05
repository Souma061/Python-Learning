def serve_chai():
    chai_type= "Normal" #local scope
    print(f"{chai_type}")


chai_type = "Milk"
serve_chai()
print(f"Outside: {chai_type}")



def chai_counter():
    chai_order = "Lemon" #enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)
    print_order()
    print("Outer: ", chai_order)

chai_order = "Tulsi"
chai_counter()
print("Global: ", chai_order)
