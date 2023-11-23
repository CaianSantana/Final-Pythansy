#from game.Game import Game
from ResponseStrategy.Response import Response
from ResponseStrategy.HitResponse import HitResponse
from websockets.server import serve



class MessageHandler:
    game = None
    websocket = None

    def __init__(self, game) -> None:
        self.game = game
        game.setMessageHandler(self)
        pass
    
    def setWebSocket(self,websocket):
        self.websocket = websocket
        
    def handleMessage(self, websocket,message):
        
        
        pass
    
    async def sendResponse(self, response:Response):
        
        pass
    
    def hit(self,message):
        self.game.hit(message)
        response:Response = HitResponse(1,1) #TODO pegar dinamicamente
        return response