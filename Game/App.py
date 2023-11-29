import threading
import asyncio
from Settings.Configuration import pygame, clock, SCREEN_UPDATE
from Run.Main import Main
#from API.MessageListener import MessageListener
pygame.init()
mainGame = Main()
#messageListener:MessageListener = MessageListener(mainGame)

"""def serverStart(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(messageListener.listen())"""

def start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame.gameOver()
            if event.type == SCREEN_UPDATE:
                mainGame.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mainGame.keyInput(event)
            mainGame.draw()  
            pygame.display.update()
            clock.tick(60)   

loop = asyncio.get_event_loop()
"""thread = threading.Thread(target=serverStart,args=(loop,))
thread.start()"""
start()
