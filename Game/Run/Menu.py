import pygame
from Settings.Configuration import screen, screenHeight, screenWidth, cellSize
from Environments.Scenario import Scenario
from pygame.math import Vector2


class Menu:

    def __init__(self):
        self.gameFont = pygame.font.Font('Game/Fonts/Pixeled.ttf', 40)
        self.surface = pygame.Surface((screenWidth, screenHeight))
        self.gameFont = self.gameFont
        self.scenario = Scenario("Forest")
    

    def update(self):
        pass
    
    def draw(self):
        self.scenario.draw()
        self.drawStart()
        self.drawLogo()

    def drawLogo(self):
        text = "Final Pythansy"
        actionSuface = self.gameFont.render(text, False, (0,0,54))
        actionPos = Vector2((screenWidth/2),  screenHeight*2/5)
        self.attackRect = actionSuface.get_rect(center = (actionPos.x, actionPos.y))
        screen.blit(actionSuface, self.attackRect)


    def drawStart(self):
        text = "Start"
        actionSuface = self.gameFont.render(text, False, (192,192,192))
        actionPos = Vector2((screenWidth/2),  screenHeight*4/5)
        self.attackRect = actionSuface.get_rect(center = (actionPos.x, actionPos.y))
        screen.blit(actionSuface, self.attackRect)
