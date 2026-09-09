import asyncio

async def task(name):
    print(name,'started')
    await asyncio.sleep(3)
    print(name,'finished')

async def main():
    await asyncio.gather(
        task('task 1'),
        task('task 2'),
        task('task 3')
    )
asyncio.run(main())