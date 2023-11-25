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
        
    async def canIawnser(self,message:dict)-> bool:
        if(not message.get("action") == "hit"):
            nextMessageHandler = CharMessageHandler(self.game,self.websocket)
            await nextMessageHandler.handleMessage(self.websocket,message)
            return False
        return True
    
    async def handleMessage(self, websocket,message:dict):
        self.setWebSocket(websocket)
        if(await self.canIawnser(message)):
            self.parseMessage(message)
            await self.sendResponse(HitResponse(int(message.get("playerId")),int(message.get("playerId")),int(message.get("dano"))))
        pass
        
    async def sendResponse(self, response:Response):
        await response.messageSender(self.webSocket)
        
    def parseMessage(self,message:dict):
            print(message)
            playerId = int(message.get("playerId"))
            adversaryId = playerId #+ 1 %2 -> seguinte so tem dois jogadores ou seja maximo de 2 ids entao basta ciclar entre 0 e 1 pra saber qual é qual
            atackerId = int(message.get("with"))
            dano = int(message.get("dano"))
            targetId = int(message.get("to"))
            self.game.hit(playerId,adversaryId,atackerId,targetId,dano)
        