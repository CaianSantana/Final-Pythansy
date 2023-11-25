import json
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
        if(not message == "char"):
            return False
        return True
    
    async def handleMessage(self, websocket,message:dict):
        self.setWebSocket(websocket)
        if(await self.canIawnser(message.get("action"))):
            id = self.createChar(message)         
            await self.sendResponse(CharResponse(id))
        pass
        
    async def sendResponse(self, response:Response):
        await response.messageSender(self.webSocket)
        
    def createChar(self,message:dict):
        id:int = int(message.get("playerId"))
        hp:int = int(message.get("hp"))
        attack:int = int(message.get("attack"))
        ability:int = int(message.get("ability"))
        armor:int = int(message.get("armor"))
        magicRes:int = int(message.get("magicResistance"))
        speed:int = int(message.get("speed"))
        mana:int = int(message.get("mana"))
        char:Chars = Chars(hp,mana,attack,ability,armor,magicRes,speed)
        self.addCharToPlayerGroup(id,char)
        return char.id
    
    def addCharToPlayerGroup(self,id:int,char:Chars):
        player:PlayerPy = self.game.getPlayer(id)
        player.addChar(char)