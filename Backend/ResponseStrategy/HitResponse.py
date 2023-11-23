from ResponseStrategy.Response import Response

class HitResponse(Response):
    id:int = None
    idHitTaker:int = None
    
    def __init__(self, id: int, idHitTaker:int) -> None:
        super().__init__(id)
        self.id = id
        self.idHitTaker = idHitTaker
    
    async def messageSender(self, websocket):
        await websocket.send("U {self.id}")
    
    