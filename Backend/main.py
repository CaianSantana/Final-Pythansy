import asyncio 
from websockets.server import serve
from playerManagement.PlayerPy import PlayerPy
from game.Game import Game
# from ResponseStrategy.Response import Response
# from ResponseStrategy.HitResponse import HitResponse
from MessageHanlder.MessageHandler import MessageHandler


funcoes = {}
game:Game = Game()

#A conexao é passada como parametro
async def echo(websocket):    
    if(game.limiteDeJogadoresAtingido()):
        return websocket.send("Refused\nConexao lotada")
    async for message in websocket:
        print(message)
        await game.handleMessage(websocket,message)
    return
    
async def start():
    messageHandler = MessageHandler(game=game) 
    async with serve(echo, "localhost", 8080):
        print("Python ta on")
        await asyncio.Future()
        
#inicia o loop de execucao
asyncio.run(start())