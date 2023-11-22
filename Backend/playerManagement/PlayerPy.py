class PlayerPy:
    nome = ""
    playerId = 0
    hp = 100
    websocket = None
       
    def __init__(self,nome, websocket):
        self.nome = nome
        self.websocket = websocket
        
    def recebaDano(self, dano):
        self.hp = self.hp - dano
        
    def causeDano(self, PlayerPy, dano):
        PlayerPy.recebaDano(dano)
        
    def setId(self, id):
        self.playerId = id
        