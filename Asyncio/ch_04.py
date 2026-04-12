import asyncio
import aiohttp

async def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(f"Title: {data['title']}")
            print(f"Body: {data['body']}")


asyncio.run(fetch_data())
