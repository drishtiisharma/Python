import asyncio

async def task1():
    print("task 1 started...")
    await asyncio.sleep(2)
    print("task 1 finished...")

async def task2():
    print("task 2 started...")
    await asyncio.sleep(3)
    print("task 2 finished...")

async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())

