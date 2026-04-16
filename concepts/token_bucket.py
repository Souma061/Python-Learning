# Rate limitting strategy for API calls

# 1 -> Token bucket algorithm
# 2 -> Leaky bucket algorithm
#3 -> Fixed window algorithm
# 4 -> Sliding window algorithm

#token bucket algorithm
import time
class TokenBucket:
    def __init__(self,Bucket_size, refill_rate):
        self.Bucket_size = Bucket_size
        self.refill_rate = refill_rate
        self.tokens = Bucket_size
        self.last_refill = time.time()
    def refill(self):
        # refill tokens at a constant rate
        # self.tokens = min(self.Bucket_size, self.tokens + self.refill_rate)
        now = time.time()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.refill_rate # calculate new tokens based on elapsed time and refill rate
        self.tokens = min(
            self.Bucket_size,
            self.tokens + new_tokens
        )
        self.last_refill = now
    def consume(self, tokens = 1):
        self.refill() # consume tokens for each API call
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        else:
            return False


bucket = TokenBucket(Bucket_size=5, refill_rate=1)

for i in range(40):
    if bucket.consume():
        print(f"API call {i+1} successful.")
    else:
        print(f"API call {i+1} rate limited.")

    time.sleep(0.1)
