import threading
import time

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for i in range(100000):
        # counter += 1
        with lock:
            counter += 1


threads = [threading.Thread(target=increment_counter) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Final counter value: {counter}")

#NOTE: Lock is used to ensure that only one thread can access the critical section of code that modifies the shared resource (counter) at a time. This prevents race conditions and ensures that the final value of counter is correct.
