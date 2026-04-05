def update_order():
    chai_type = "Normal"
    def kitchen():
        nonlocal chai_type  #nonlocal allows us to modify the variable in the enclosing scope
        chai_type = "Milk"
    kitchen()
    print("After kitchen update",chai_type)

update_order()
