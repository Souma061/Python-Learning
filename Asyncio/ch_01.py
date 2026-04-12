#NOTE: Asyncio is a library to write concurrent code using the async/await syntax. It provides a way to handle asynchronous tasks and I/O operations without blocking the main thread.



import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(2)
    print("World")


# if __name__ == "__main__":
asyncio.run(main())
