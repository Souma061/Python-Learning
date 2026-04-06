def make_chai():
    return "Chai is ready!"

chai = make_chai()
print(chai)


#return statement is used to send a value back to the caller of the function. In this case, the function make_chai() returns the string "Chai is ready!" which is then stored in the variable chai and printed to the console.


def idle_chai():  #This function is defined but does not have any code inside it. The pass statement is used as a placeholder to indicate that the function does nothing. When idle_chai() is called, it will return None by default since there is no return statement in the function.
    pass

print(idle_chai())



def sold_cups():
    return 5

print(sold_cups())


def chai_status(cups_left):
    if cups_left > 0:
        return "Chai is ready!"
    # elif cups_left == 0:
    #     return "Chai is sold out!"
    # else:
    #     return "Invalid number of cups."

    return "Chai is sold out!" if cups_left == 0 else "Invalid number of cups." if cups_left < 0 else "Chai is ready!"


print(chai_status(3))
print(chai_status(0))


def chai_report():
    return 100,20,10 #sold, left



sold,left,_ = chai_report() #The underscore (_) is used as a placeholder for the third value returned by the chai_report() function, which is not needed in this case. The sold and left variables will be assigned the first two values returned by the function, which represent the number of cups sold and the number of cups left, respectively.
print("Sold: ", sold)
print("Left: ", left)
print("Total: ", sold + left)
