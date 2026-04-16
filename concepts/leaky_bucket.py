#NOTE: Leaking bucket algorithm
# The leaking bucket algorithm is similar to the token bucket except that requests are processed at a fixed rate. It is usually implemented with a first-in-first-out (FIFO) queue. The algorithm works as follows:

# When a request arrives, the system checks if the queue is full. If it is not full, the request is added to the queue.

# Otherwise, the request is dropped.

# Requests are pulled from the queue and processed at regular intervals.

import time
class Leakybucket:
    def __init__(self,bucket_size, leak_rate):
        self.bucket_size = bucket_size
        self.leak_rate = leak_rate
        self.queue = []
        self.last_leak_time = time.time()
    def leak(self):
        now = time.time()
        elapsed = now - self.last_leak_time
        leaks = int(elapsed * self.leak_rate)

        if leaks > 0:
            self.queue = self.queue[leaks:]
            self.last_leak_time += leaks / self.leak_rate
    def add_request(self, request):
        self.leak()
        if len(self.queue) < self.bucket_size:
            self.queue.append(request)
            return True
        else:
            return False


bucket = Leakybucket(bucket_size=5, leak_rate=2)

for i in range(40):
    if bucket.add_request(f"Request {i+1}"):
        print(f"Request {i+1} added. Queue size: {len(bucket.queue)}")
    else:
        print(f"Request {i+1} dropped!")

    time.sleep(0.1)
