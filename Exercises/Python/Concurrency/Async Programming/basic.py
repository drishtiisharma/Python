# sequential working
# import time

# def task1():
#     print('task1 started...')
#     time.sleep(3)
#     print("task1 finished...")

# def task2():
#     print("task2 started...")
#     time.sleep(3)
#     print("task2 finished")

# task1()

# task2()

# async version
import asyncio

async def task1():
    print("task 1 started")
    await asyncio.sleep(4)
    print("task 1 done")

async def task2():
    print("task 2 started")
    await asyncio.sleep(2)
    print("task 2 done")

async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())