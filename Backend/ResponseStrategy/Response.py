#Fazer outras classes herdarem e enviarem suas mensagens

class Response:
    message:str = ""
    id:int = None
    
    def __init__(self, id:int) -> None:
        self.id = id
        pass
    
    async def messageSender(self, websocket):
        await websocket.send("A {self.id}")