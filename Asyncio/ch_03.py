import asyncio
import aiohttp

async def fetch_data(session,url):
    async with session.get(url) as response:
        print(f"Fetching data from {url} with status {response.status}")


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session,url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
