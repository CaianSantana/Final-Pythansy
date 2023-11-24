import asyncio 
from websockets.server import serve
from playerManagement.PlayerPy import PlayerPy
from game.Game import Game

funcoes = {}
game:Game = Game()

#Padrao de assinatura de toda funcao deve ser este a seguir {Negociavel de passar conexao algo a ser analisado}
def join(conexao, playerName)-> PlayerPy:
    if(not game.playerJaEstaEmPartida(conexao)):    
        player = PlayerPy(playerName, conexao)
        game.join(player)
    return player

def hit(conexao,message):
    game.hit(message)

#A conexao é passada como parametro
async def echo(websocket):
    print(funcoes)    
    if(game.limiteDeJogadoresAtingido()):
        return "Refused\nConexao lotada"
    async for message in websocket:
        print(message)
        funcoes[message[0]](websocket,message)
        await websocket.send(message)
    return
    
async def start():
    funcoes["J"] = join
    funcoes["H"] = hit
    async with serve(echo, "localhost", 8080):
        print("Python ta on")
        await asyncio.Future()
        
#inicia o loop de execucao
asyncio.run(start())