from playerManagement.Chars import Chars

class PlayerPy:
    nome = ""
    playerId = 0
    websocket = None
    personagens:list[Chars] = []
       
    def __init__(self,nome, websocket):
        self.nome = nome
        self.websocket = websocket
        
    def setId(self, id):
        self.playerId = id
        
    def getChar(self,id:int) -> Chars: 
        return self.personagens[id]
    
    def addChar(self,char:Chars):
        self.personagens.append(char)