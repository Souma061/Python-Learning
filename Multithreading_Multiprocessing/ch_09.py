from multiprocessing import Process
import time

def cpu_bound_task():
    print("Starting CPU-bound task...")
    total = 0
    for i in range(10**9):
        total += i
    print(f"CPU-bound task completed with total: {total}")


if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_bound_task) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")
