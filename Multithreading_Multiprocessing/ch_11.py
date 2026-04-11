from multiprocessing import Process,Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock(): # Lock is used to ensure that only one process can access the critical section of code that modifies the shared resource (counter) at a time. This prevents race conditions and ensures that the final value of counter is correct.
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i',0) # 'i' stands for integer, 0 is the initial value
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    print(counter.value)

    print(f"Final counter value: {counter.value}")


# Usedases of processes:
# 1. CPU-bound tasks: Processes are ideal for CPU-bound tasks that require intensive computation, such as data processing, scientific simulations, and machine learning algorithms. By using multiple processes, you can take advantage of multiple CPU cores and improve performance.
# 2. Isolation: Processes run in separate memory spaces, which provides better isolation and security. If one process crashes, it does not affect the others. This is particularly useful for applications that require high reliability and stability, such as web servers and databases.
# 3. Parallelism: Processes can run in parallel on multiple CPU cores, allowing for true concurrent execution. This can significantly reduce the time taken for tasks that can be divided into smaller sub-tasks, such as image processing, video encoding, and large-scale data analysis.
