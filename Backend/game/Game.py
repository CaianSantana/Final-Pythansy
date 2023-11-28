from playerManagement.PlayerPy import PlayerPy
from MessageHanlder.MessageHandler import MessageHandler
from playerManagement.Chars import Chars

class Game:
    playersPy :list[PlayerPy] = []
    messageHandler:MessageHandler = None
    
    def __init__(self) -> None:
        pass
    
    def join(self,conexao, nome:str):
        if(self.playerJaEstaEmPartida(conexao)):    
            return    
        playerPy = PlayerPy(nome, conexao)
        playerPy.setId = len(self.playersPy) 
        self.playersPy.append(playerPy)
        print(len(self.playersPy))
        print(playerPy.nome)
        return playerPy.playerId
           
    def hit(self, atackerId:int,adversaryId:int,charId:int,targetId:int,dano:int):
        #print(len(self.playersPy))
        atacante = self.getPlayer(atackerId)
        atacado = self.getPlayer(adversaryId)
        charDoAtacante:Chars = atacante.getChar(charId)
        charDoAtacado:Chars = atacado.getChar(targetId)
        charDoAtacante.causeDano(charDoAtacado,dano)
        return
    
    def playerJaEstaEmPartida(self,websocket)-> bool:
        for player in self.playersPy:
            if(player.websocket == websocket):
                return True 
        return False
    
    def limiteDeJogadoresAtingido(self) -> bool:
        if(self.playersPy != None):
            return len(self.playersPy)==2
        return False
        
    def setMessageHandler(self, messageHandler):
        self.messageHandler = messageHandler
    
    async def handleMessage(self, websocket,message):
        await self.messageHandler.handleMessage(websocket,message)
        
    def getPlayer(self,id:int) -> PlayerPy:
        return self.playersPy[id]