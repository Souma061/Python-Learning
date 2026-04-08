#send generators


def chai_customer():
    print("Customer: May I have a cup of tea?")
    order =  yield
    while True:
        print(f"Customer: I would like {order} tea, please.")
        order = yield



stall = chai_customer()
next(stall)  # Start the generator

stall.send("ginger")  # Customer orders ginger tea
stall.send("masala")  # Customer changes order to masala tea


#It is important to note that the generator will continue to run until it is explicitly closed or reaches a return statement. In this case, since there is no return statement, the generator will keep running indefinitely, allowing the customer to place multiple orders.


#if we remove order = yield from the while loop, the generator will not be able to receive new orders after the first one. The customer will only be able to place one order, and any subsequent calls to stall.send() will not have any effect.
#It will be a infinite loop that keeps printing the first order without allowing the customer to change it.



#Broke all the code in steps:
#1. The generator function chai_customer() is defined, which simulates a customer ordering tea.
#2. The generator is created by calling chai_customer() and assigned to the variable stall.
#3. The generator is started using next(stall), which runs the code up to the first yield statement, allowing the customer to place their first order.
#4. The customer places their first order by calling stall.send("ginger"), which sends the string "ginger" to the generator. The generator receives this value and prints the corresponding message.
#5. The customer changes their order by calling stall.send("masala"), which sends the string "masala" to the generator. The generator receives this new value and prints the updated message


# This is used in frameworks like Django, where you can use yield to create a generator that produces a sequence of values, such as database query results, without loading them all into memory at once. This allows for efficient handling of large datasets and improves performance.
