import asyncio

async def hello():
    print('hello')
    await asyncio.sleep(2)
    await asyncio.sleep(3)
    print('world')
    
asyncio.run(hello())

import time
async def hello():
    print('hello')
    time.sleep(2)
    time.sleep(3)
    
    print('world')
    


