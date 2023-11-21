from Settings.Configuration import *
from Settings.Main import Main

pygame.init()

mainGame = Main()
scenarioRect = pygame.Rect(0, 0, screenWidth, screenHeight)
scenario = pygame.image.load("Final-Pythansy/Graphics/Scenario.png").convert_alpha()
#fonte: https://www.pixilart.com/art/traveled-path-8fb71335a1682f9?ft=staff-picks

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGame.gameOver()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        mainGame.keyInput(event)
        
    
    screen.blit(scenario, scenarioRect)
    mainGame.draw()  
    pygame.display.update()
    clock.tick(60)   
    