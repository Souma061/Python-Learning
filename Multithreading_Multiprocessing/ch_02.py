#NOTE: Multiprocessing is a way to achieve parallelism in programming by using multiple processes. Each process has its own memory space and can run independently, allowing for true parallel execution on multiple CPU cores. This can be achieved through the multiprocessing module in Python.


from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Brewing chai for {name}")
    time.sleep(2)
    print(f"Chai for {name} is ready!")


if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai,args=(f"Customer {i+1}",)) for i in range(3)



    ]
    # Start all processes
    for maker in chai_makers:
        maker.start()


    # Wait for all processes to finish
    for maker in chai_makers:
        maker.join()

    print("All tasks completed.")
