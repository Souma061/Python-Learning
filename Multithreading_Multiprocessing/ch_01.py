#Concurrency & Parallelism is a way to achieve multitasking in programming.

import threading
import time

# def take_order():
#     for i in range(1,4):
#         print(f"Taking order {i}")
#         time.sleep(1)

# def brew_chai():
#     for i in range(1,4):
#         print(f"Brewing chai {i}")
#         time.sleep(3)

# people1 = threading.Thread(target=take_order)
# people2 = threading.Thread(target=brew_chai)

# people1.start()
# people2.start()

# # Wait for both threads to finish
# people1.join()
# people2.join()

# print("All tasks completed.")


def worker(calculation):
    for i in range(5):
        print(f"Worker {calculation} is working on task {i+1}")
        time.sleep(2)


def worker2(calculation):
    for i in range(5):
        print(f"Worker {calculation} is working on task {i+1}")
        time.sleep(4)



thread1 = threading.Thread(target=worker, args=(1,))
thread2 = threading.Thread(target=worker2, args=(2,))

thread1.start()
thread2.start()


thread1.join()
thread2.join()












# NOTE: Concurrency is when multiple tasks are making progress at the same time, but not necessarily executing simultaneously. It allows for interleaving of tasks, where one task can be paused while another task is running. This can be achieved through techniques like threading or asynchronous programming.

# NOTE: Parallelism, on the other hand, is when multiple tasks are executing simultaneously, typically on multiple processors or cores. This can be achieved through techniques like multiprocessing or distributed computing.

# NOTE: In Python, the Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. This means that even if you have multiple threads in a Python program, they may not be able to take full advantage of multiple CPU cores due to the GIL.
