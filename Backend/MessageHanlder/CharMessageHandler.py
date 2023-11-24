from ResponseStrategy.CharResponse import CharResponse
from ResponseStrategy.Response import Response
from playerManagement.PlayerPy import PlayerPy
from playerManagement.Chars import Chars

class CharMessageHandler:
    game = None
    webSocket = None

    def __init__(self,game, webSocket) -> None:
        self.game = game
        self.webSocket = webSocket
        
    def setWebSocket(self,websocket):
        self.websocket = websocket
        
    async def canIawnser(self,message:str)-> bool:
        if(not message[0] == "C"):
            return False
        return True
    
    async def handleMessage(self, websocket,message:str):
        self.setWebSocket(websocket)
        if(await self.canIawnser(message)):
            id = self.createChar(message)         
            await self.sendResponse(CharResponse(id))
        pass
        
    async def sendResponse(self, response:Response):
        await response.messageSender(self.webSocket)
        
    def createChar(self,message:str):
        print(message[5])
        print(message)
        print(message[10:12])
        id:int = int(message[5])
        hp:int = int(message[10:12])
        attack:int = int(message[20:22])
        ability:int = int(message[31:33])
        armor:int = int(message[40:42])
        magicRes:int = int(message[59:61])
        speed:int = int(message[68:70])
        mana:int = int(message[76:78])
        char:Chars = Chars(hp,mana,attack,ability,armor,magicRes,speed)
        self.addCharToPlayerGroup(id,char)
    
    def addCharToPlayerGroup(self,id:int,char:Chars):
        player:PlayerPy = self.game.getPlayer(id)
        player.addChar(char)