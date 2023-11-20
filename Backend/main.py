import asyncio 
from websockets.server import serve
from playerManagement.PlayerPy import PlayerPy 

playersConections = set()
funcoes = {}

#Padrao de assinatura de toda funcao deve ser este a seguir {Negociavel de passar conexao algo a ser analisado}
def join(conexao, playerName):
    print("recebeu")
    return PlayerPy(playerName, 0,0, conexao)

async def echo(websocket):
    print(funcoes)
    
    if(len(playersConections) > 2):
        return "Refused\nConexao lotada"
    
    async for message in websocket:
        print(message)
        playersConections.add(websocket)
        funcoes[message[0]](websocket,message)
        await websocket.send(message)
    return
    
async def start():
    funcoes["J"] = join
    async with serve(echo, "localhost", 8080):
        print("Python ta on")
        await asyncio.Future()
        
asyncio.run(start())

