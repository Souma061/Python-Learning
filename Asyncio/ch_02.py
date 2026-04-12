import asyncio
import time
async def brew(name):
    print(f"Preparing {name}...")
    await asyncio.sleep(2) # Simulate time taken to brew
    # time.sleep(2)  # This will block the event loop, simulating a synchronous operation
    print(f"{name} is ready!")

async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Ginger Chai"),
        brew("Lemon Chai")
    )

if __name__ == "__main__":
    asyncio.run(main())
