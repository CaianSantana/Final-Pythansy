#from game.Game import Game
from ResponseStrategy.Response import Response
from ResponseStrategy.HitResponse import HitResponse
from websockets.server import serve
from MessageHanlder.HitMessageHandler import HitMessageHandler

class MessageHandler:
    game = None
    websocket = None

    def __init__(self, game) -> None:
        self.game = game
        game.setMessageHandler(self)
        pass
    
    def setWebSocket(self,websocket):
        self.websocket = websocket
        
    async def handleMessage(self, websocket,message:dict):
        self.setWebSocket(websocket)
        if((await self.canIawnser(message))):
            playerId = self.game.join(websocket, message.get("nome"))
            await self.sendResponse(Response(playerId))
    
    async def sendResponse(self, response:Response):
        await response.messageSender(self.websocket)
    
    async def canIawnser(self,message:dict)-> bool:
        if(not message.get("action") == "Join"):
            nextMessageHandler = HitMessageHandler(self.game,self.websocket)
            await nextMessageHandler.handleMessage(self.websocket,message)
            return False
        return True