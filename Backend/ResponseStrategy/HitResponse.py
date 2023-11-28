import json
from ResponseStrategy.Response import Response

class HitResponse(Response):
    id:int = None
    idHitTaker:int = None
    dano:int = 0
    message:dict = None
    
    def __init__(self, id: int, idHitTaker:int,dano:int) -> None:
        super().__init__(id)
        self.id = id
        self.idHitTaker = idHitTaker
        self.dano = dano
    
    async def messageSender(self, websocket):
        self.message = {
       "Response":"update",
        "attacker":str(self.id),
        "target":str(self.idHitTaker),
        "dano":str(self.dano)
        }
        await websocket.send(json.dumps(self.message))
    
    