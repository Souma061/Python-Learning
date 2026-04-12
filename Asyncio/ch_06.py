import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def encripting_data(data):
    return f"Encrypted({data[::-1]})"  # Simulate encryption by reversing the string


async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,
                                              encripting_data,
                                              "password123")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
