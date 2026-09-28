import asyncio

async def greet(name):
    print("hello..."+name)
    await asyncio.sleep(3)
    print("how are you")

async def main():
    await asyncio.gather(greet('drishti'))
asyncio.run(main())
