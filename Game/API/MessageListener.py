import asyncio 
import json
from websockets.server import serve


class MessageListener:
    game = None

    def __init__(self,game) -> None:
        self.game = game
        pass

    async def listener(self,websocket):
        async for message in websocket:
            print(message)
            await websocket.send("resposta")
    
    async def listen(self):
        async with serve(self.listener, "localhost", 8752):
            print("Listener online")
            await asyncio.Future()
            
