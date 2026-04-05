chai_type = "Milk"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Normal"
    kitchen()

front_desk()
print(f"Global:",chai_type)
