import threading
import requests
import time

def download_image(url):
    print(f"Downloading {url}")
    response = requests.get(url)
    print(f"Downloaded {url} with status code {response.status_code}")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]


start = time.time()
threads = [

]

for url in urls:
    t = threading.Thread(target=download_image, args=(url,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")

