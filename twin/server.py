#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
from . router import worker
from. import example
from quamash import QEventLoop, QThreadExecutor
from .qt_exapmple import Mystd
#async def time(websocket, path):
    #while True:
        #now = datetime.datetime.utcnow().isoformat() + 'Z'
        #await websocket.send(now)
        #await asyncio.sleep(random.random() * 3)



async def recieve(websocket, path):
    worker.setSocket(websocket)
    async for message in websocket:
        #data = json.loads(message)
        #loop = asyncio.get_event_loop()
        #def last_50():
            #loop.call_soon_threadsafe( worker.parse,message )
        #with QThreadExecutor(1) as exec:
            #await loop.run_in_executor(exec, last_50)
        
        #asyncio.get_event_loop().create_task( worker.parse(message) )
        await asyncio.ensure_future(worker.parse(message))
        
        #if rt:
            #await websocket.send( rt)


start_server = websockets.serve(recieve, '127.0.0.1', 5678)

if __name__ =='__main__':
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_until_complete(send())
    asyncio.get_event_loop().run_forever()
