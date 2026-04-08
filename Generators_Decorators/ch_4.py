#Close generator

def local_chai():
    yield "Boiling water"
    yield "Steeping tea"

def imported_chai():
    yield "masala chai"
    yield "ginger chai"
    yield "lemon chai"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "What would you like to order?"
    except:
        print("Closing the stall. Goodbye!")


stall = chai_stall()
print(next(stall))  # Start the generator and get the initial prompt
stall.close()  # Close the generator, which will trigger the except block and print the closing message
