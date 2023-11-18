import asyncio 
from websockets.server import serve

playersConections = set()

async def echo(websocket):
    async for message in websocket:
        print(message)
        playersConections.add(websocket)
        print(len(playersConections))
        await websocket.send(message)
        
async def start():
    async with serve(echo, "localhost", 8080):
        print("Python ta on")
        await asyncio.Future()
        
asyncio.run(start())