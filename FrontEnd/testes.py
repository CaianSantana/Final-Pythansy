#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

async def hello():
    with connect("ws://localhost:8080") as websocket:
        websocket.send("J receba")
        message = websocket.recv()
        while(True):
            print(f"Received: {message}")
            print()
            websocket.send("H from:0\n to:0\n Dano:10\n")
            message = websocket.recv()
            print(f"Received: {message}")
            await asyncio.sleep(1)
        
asyncio.get_event_loop().run_until_complete(hello())
        
        
#hello()