import asyncio

async def func():
    print("starting...")
    await asyncio.sleep(2)
    print("finished...")

async def main():
    await asyncio.gather(func())
asyncio.run(main())