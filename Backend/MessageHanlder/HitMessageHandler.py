from websockets.server import serve
from ResponseStrategy.HitResponse import HitResponse
from ResponseStrategy.Response import Response
from MessageHanlder.CharMessageHandler import CharMessageHandler

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
            nextMessageHandler = CharMessageHandler(self.game,self.websocket)
            await nextMessageHandler.handleMessage(self.websocket,message)
            return False
        return True
    
    async def handleMessage(self, websocket,message:str):
        self.setWebSocket(websocket)
        if(await self.canIawnser(message)):
            self.parseMessage(message)
            await self.sendResponse(HitResponse(int(message[7]),int(message[13])))
        pass
        
    async def sendResponse(self, response:Response):
        await response.messageSender(self.webSocket)
        
    def parseMessage(self,message):
            print("how?")
            print(message)
            print("message?")
            self.game.hit(0,0,0,0,10)
        