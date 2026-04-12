import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging from background thread: {threading.current_thread().name}")



async def fetch_orders():
    await asyncio.sleep(3)  # Simulate time taken to fetch orders
    print("Orders fetched!")


worker1 = threading.Thread(
    target=background_worker, name="Worker-1", daemon=True
)
worker1.start()

asyncio.run(fetch_orders())
