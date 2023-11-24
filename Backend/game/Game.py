from playerManagement.PlayerPy import PlayerPy

class Game:
    playersPy :list[PlayerPy] = []
    
    def __init__(self) -> None:
        pass
    
    def join(self,playerPy:PlayerPy):
        playerPy.setId = len(self.playersPy) 
        print("join")
        self.playersPy.append(playerPy)
        print(len(self.playersPy))
        
        
    def hit(self, message):
        playerId = int(message[7])
        playerTargetId = int(message[13])
        print(len(self.playersPy))
        atacante = self.playersPy[playerId]
        atacado = self.playersPy[playerTargetId]
        atacante.causeDano(atacado,10)
        print(atacado.hp)
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
        
        
    
    
        
    