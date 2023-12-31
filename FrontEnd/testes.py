#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect
import json

async def hello():
    port = 8752
    with connect("ws://localhost:"+str(port)) as websocket:
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
        while(True):
            print(f"Received: {message}")
            print()
            hitMessage = {
                "action":"hit",
                "playerId":"0",
                "with":"0",
                "to":"0",
                "dano":"10"
            }
            websocket.send(json.dumps(hitMessage))
            message = websocket.recv()
            print(f"Received: {message}")
            await asyncio.sleep(1.5)
        
asyncio.get_event_loop().run_until_complete(hello())
        
        
#hello()