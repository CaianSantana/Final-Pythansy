from playerManagement.PlayerPy import PlayerPy

class Game:
    playersPy :list[PlayerPy] = []
    
    def __init__(self) -> None:
        pass
    
    def __init__(self, playerPy:PlayerPy) -> None:
        self.playersPy.append(playerPy)
        playerPy.setId = len(self.playersPy)
        pass
    
    def join(self,playerPy:PlayerPy):
        playerPy.setId = len(self.playersPy) 
        self.playersPy.append(playerPy)
        
    def hit(self, message):
        playerId = int(message[7])
        playerTargetId = int(message[13])
        atacante = self.playersPy[playerId]
        atacado = self.playersPy[playerTargetId]
        atacante.causeDano(atacado,10)
        return
    
    def playerJaEstaEmPartida(self,websocket)-> bool:
        for player in self.playersPy:
            if(player.websocket == websocket):
                return True 
        return False
    
    def limiteDeJogadoresAtingido(self) -> bool:
        return len(self.playersPy)==2
        
        
    
    
        
    