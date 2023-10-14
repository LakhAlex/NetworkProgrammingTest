import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)

async def stop_after(loop, when):
    await asyncio.sleep(when)
    loop.stop()

loop = asyncio.get_event_loop()
loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))
loop.create_task(say('third hello', 4))
loop.create_task(stop_after(loop, 3))

# loop.create_task(stop_after(loop, 3))로 인해서 4초 뒤에
# 출력되야 했던 loop가 실행되지 못 한 상태가 된다.

loop.run_forever()
loop.close()