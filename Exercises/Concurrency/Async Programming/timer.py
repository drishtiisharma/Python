import asyncio

async def task(name = 'task 1',delay = 3):
    print(name, 'started')
    await asyncio.sleep(delay)
    print(name, 'ended')

async def main():
    await task() # asyncio.gather() best for multiple tasks
asyncio.run(main())