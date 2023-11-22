from Settings.Configuration import *
from Settings.Main import Main

pygame.init()

mainGame = Main()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGame.gameOver()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        if event.type == pygame.KEYDOWN:
            mainGame.keyInput()
    mainGame.draw()  
    pygame.display.update()
    clock.tick(60)   
    