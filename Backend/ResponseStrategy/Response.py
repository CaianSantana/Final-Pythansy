#Fazer outras classes herdarem e enviarem suas mensagens
import json

class Response:
    message:dict= None
    id:int = None
    
    def __init__(self, id:int) -> None:
        self.id = id
        pass
    
    async def messageSender(self, websocket):
        self.message = {"Response":"accepted",
                        "playerId":str(self.id)}
        await websocket.send(json.dumps(self.message))