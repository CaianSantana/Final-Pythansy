#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect
import json

async def hello():
    with connect("ws://localhost:8080") as websocket:
        joinMessage = {
                "action":"Join",
                "nome":"Yasmin yaz bollaz"
            }
        websocket.send((json.dumps(joinMessage)))
        message = websocket.recv()
        print(message)
        charMessage = {
                "action":"char",
                "class":"empty",
                "playerId":"0",
                "hp":"25",
                "attack":"30",
                "ability":"12",
                "armor":"10",
                "magicResistance":"15",
                "speed":"35",
                "mana":"20"
        }
        websocket.send(json.dumps(charMessage))
        message = websocket.recv()
        print(message)
        
        # while(True):
        #     print(f"Received: {message}")
        #     print()
        #     websocket.send("H from:0 with:0 to:0 Dano:+10")
        #     message = websocket.recv()
        #     print(f"Received: {message}")
        #     await asyncio.sleep(1.5)
        
asyncio.get_event_loop().run_until_complete(hello())
        
        
#hello()