import json
from ResponseStrategy.Response import Response

class CharResponse(Response):
    message:dict = None
    id:int = None
    
    def __init__(self, id:int) -> None:
        self.id = id
        pass
    
    async def messageSender(self, websocket):
        message = {"response":"confirmed",
                   "charId":str(self.id)
                   }
        await websocket.send(json.dumps(message))