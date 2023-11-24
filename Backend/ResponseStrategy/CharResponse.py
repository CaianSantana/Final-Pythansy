from ResponseStrategy.Response import Response

class CharResponse(Response):
    message:str = ""
    id:int = None
    
    def __init__(self, id:int) -> None:
        self.id = id
        pass
    
    async def messageSender(self, websocket):
        await websocket.send("A " + str(self.id))