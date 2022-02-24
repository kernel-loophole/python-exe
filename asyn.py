import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
async def another_coroutine(what):
    await asyncio.sleep(2)
    print(what)
async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')
    await another_coroutine('hello')

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())