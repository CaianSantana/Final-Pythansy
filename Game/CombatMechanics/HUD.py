import pygame
from pygame.math import Vector2
from Settings.Configuration import screen, screenHeight, screenWidth, cellNumberX

class HUD:
    def __init__(self, playerChars, gameFont):
        self.height = screenHeight/4
        self.y = screenHeight - self.height
        self.surface = pygame.Surface((screenWidth, self.height))
        self.playerChars = playerChars
        self.gameFont = gameFont
        
        
    def draw(self):
        self.surface.fill("Blue")
        screen.blit(self.surface, (0, self.y))
        self.drawTeamStats()
        
        
    def drawTeamStats(self):
        self.distance = 20
        
        for i in range(3):
            self.score = "Batata"
            text = self.score
            textSurface = self.gameFont.render(text, False, (255, 255, 255))
            textPos = Vector2((screenWidth*3/4), self.y+self.distance)
            textRect = textSurface.get_rect(center = (textPos.x, textPos.y))
            screen.blit(textSurface, textRect)
            self.distance+=60