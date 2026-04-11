from multiprocessing import Process
import time
# from tracemalloc import start

def worker(calculation):
    print(f"Worker {calculation} is working on task {calculation}")
    count = 0
    for _ in range(100000000):
        count += 1
    print(f"Worker {calculation} has completed the task!")



if __name__ == "__main__":
    start = time.time()
    worker1 = Process(target=worker, args=(1,))
    worker2 = Process(target=worker, args=(2,))
    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()

    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")
