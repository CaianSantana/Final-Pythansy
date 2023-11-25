import asyncio 
import json
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
    client_host = websocket
    print("Requiscao de:",client_host.remote_address[0]) #sabendo o ip de quem se conectou
    if(game.limiteDeJogadoresAtingido()):
        return websocket.send("Refused\nConexao lotada")
    async for message in websocket:
        playerMessage = json.loads(message)
        await game.handleMessage(websocket,playerMessage)
    return
    
async def start():
    messageHandler = MessageHandler(game=game) 
    async with serve(echo, "localhost", 8080):
        print("Python ta on")
        await asyncio.Future()
        
#inicia o loop de execucao
asyncio.run(start())