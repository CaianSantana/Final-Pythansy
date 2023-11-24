from websockets.server import serve
from ResponseStrategy.HitResponse import HitResponse
from ResponseStrategy.Response import Response


class HitMessageHandler:
    game = None
    webSocket = None

    def __init__(self,game, webSocket) -> None:
        self.game = game
        self.webSocket = webSocket
        
    def setWebSocket(self,websocket):
        self.websocket = websocket
        
    async def canIawnser(self,message:str)-> bool:
        if(not message[0] == "H"):
            return False
        return True
    
    async def handleMessage(self, websocket,message:str):
        self.setWebSocket(websocket)
        if(await self.canIawnser(message)):
            self.game.hit(message)
            await self.sendResponse(HitResponse(int(message[7]),int(message[13])))
        pass
        
    async def sendResponse(self, response:Response):
        await response.messageSender(self.webSocket)
        