#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

async def hello():
    with connect("ws://localhost:8080") as websocket:
        while(True):
            websocket.send("Hello world!")
            message = websocket.recv()
            print(f"Received: {message}")
            await asyncio.sleep(1)
        
asyncio.get_event_loop().run_until_complete(hello())
        
        
#hello()