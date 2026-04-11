from multiprocessing import Process,Queue

def prepare_chai(queue):
    queue.put("Chai is ready!")



if __name__ == "__main__":
    queue = Queue()
    process = Process(target=prepare_chai, args=(queue,))
    process.start()
    process.join()
    result = queue.get()
    print(result)
