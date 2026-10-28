# ==========================================
# PHASE 13: CONCURRENCY DEMO
# ==========================================

import threading
import multiprocessing
import asyncio
import time


# 1. THREADING — suitable for I/O-bound tasks

def download_file(filename):
    print(f"Downloading {filename}...")
    time.sleep(2)  # Simulates waiting for a download
    print(f"{filename} downloaded")


def threading_demo():
    start = time.time()

    threads = []

    for filename in ["a.pdf", "b.pdf", "c.pdf"]:
        t = threading.Thread(
            target=download_file,
            args=(filename,)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Threading time: {time.time() - start:.2f}s\n")


# 2. MULTIPROCESSING — suitable for CPU-bound tasks

def calculate_square(number):
    return number * number


def multiprocessing_demo():
    if __name__ == "__main__":
        start = time.time()

        with multiprocessing.Pool(processes=3) as pool:
            results = pool.map(
                calculate_square,
                [10, 20, 30, 40]
            )

        print("Squares:", results)
        print(f"Multiprocessing time: {time.time() - start:.2f}s\n")


# 3. ASYNCIO — concurrent I/O without multiple threads

async def fetch_data(name):
    print(f"Fetching {name}...")
    await asyncio.sleep(2)  # Simulates asynchronous I/O
    print(f"{name} fetched")
    return name


async def asyncio_demo():
    start = time.time()

    results = await asyncio.gather(
        fetch_data("API 1"),
        fetch_data("API 2"),
        fetch_data("API 3")
    )

    print("Results:", results)
    print(f"Asyncio time: {time.time() - start:.2f}s\n")


# 4. RUN THE DEMOS

if __name__ == "__main__":
    threading_demo()
    multiprocessing_demo()
    asyncio.run(asyncio_demo())

