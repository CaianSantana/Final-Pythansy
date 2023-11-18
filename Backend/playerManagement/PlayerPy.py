class PlayerPy:
    nome = ""
    playerId = 0
    x = 0
    y = 0
    hp = 100
    websocket = None
       
    def __init__(self,nome, startXPos, startYPos, websocket):
        self.nome = nome
        self.x = startXPos
        self.y = startYPos
        self.websocket = websocket
        
    def recebaDano(self, dano):
        hp = hp - dano
        
    def causeDano(self, PlayerPy, dano):
        PlayerPy.recebaDano(dano)