# # NOTE: GIL (Global Interpreter Lock) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. This means that even if you have multiple threads, only one thread can execute Python code at a time. This can limit the performance of CPU-bound tasks in multithreading, but it allows for concurrency in I/O-bound tasks where threads can be waiting for external resources.


# # import threading
# import time
# from multiprocessing import Process

# # def brew_chai():
# #     print(f"Brewing chai for {threading.current_thread().name}")
# #     count = 0
# #     for _ in range(10000):
# #         count += 1
# #     print(f"Chai for {threading.current_thread().name} is ready!")

# def brew_chai(name):
#     print(f"Brewing chai for {name}")
#     count = 0
#     for _ in range(10000):
#         count += 1
#     print(f"Chai for {name} is ready!")

# # worker1 = threading.Thread(target=brew_chai, name="Customer 1")
# # worker2 = threading.Thread(target=brew_chai, name="Customer 2")

# worker1 = Process(target=brew_chai, name="Customer 1")
# worker2 = Process(target=brew_chai, name="Customer 2")

# start = time.time()
# worker1.start()
# worker2.start()


# worker1.join()
# worker2.join()
# end = time.time()
# print(f"Total time taken: {end - start:.2f} seconds")


from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Brewing chai for {name}")
    count = 0
    for _ in range(10000):
        count += 1
    print(f"Chai for {name} is ready!")

# 👇 THIS IS THE FIX
if __name__ == "__main__":
    worker1 = Process(target=brew_chai, args=("Customer 1",))
    worker2 = Process(target=brew_chai, args=("Customer 2",))

    start = time.time()

    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()

    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")
