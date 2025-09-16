import time
import asyncio

async def count():
    print("One")
    await asyncio.sleep(2)
    print("Two")

async def main():
    tasks = []
    for _ in range(120):
        tasks.append(count())
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
