import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}...")
    time.sleep(2)  # Simulate time taken to check stock
    # print(f"{item} is in stock!")
    return f"{item} is in stock!"


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        task = [
            loop.run_in_executor(pool, check_stock, "Laptop"),
            loop.run_in_executor(pool, check_stock, "Smartphone"),
            loop.run_in_executor(pool, check_stock, "Headphones")
        ]
        result = await asyncio.gather(*task)
        for res in result:
            print(res)
        # result = await loop.run_in_executor(pool, check_stock, "Laptop")
        # print(result)


if __name__ == "__main__":
    asyncio.run(main())
