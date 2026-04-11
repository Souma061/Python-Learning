# NOTE: Process Vs Thread
# 1. Process: A process is an instance of a program that is being executed. It has its own memory space and resources. Each process runs independently and can have multiple threads within it. Processes are typically used for tasks that require heavy computation or need to run in isolation from other processes.
# 2. Thread: A thread is a smaller unit of execution within a process. Threads share the same memory space and resources of the process they belong to. They are used for tasks that can be performed concurrently within the same process, such as handling user input, performing background tasks, or managing multiple tasks simultaneously.

import threading
import time

def boil_water():
    print("Boiling water...")
    time.sleep(2)  # Simulate time taken to boil water
    print("Water boiled!")

def total_bun():
    print("Total bun is 10.")
    time.sleep(3)  # Simulate time taken to calculate total bun
    print("Total bun calculated!")


start = time.time()
# Create threads for boiling water and calculating total bun
thread1 = threading.Thread(target=boil_water)
thread2 = threading.Thread(target=total_bun)

# Start the threads
thread1.start()
thread2.start()
# Wait for both threads to finish
thread1.join()
thread2.join()
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")
