import pygame
from Settings.Configuration import screen, screenHeight, screenWidth

class HUD:
    def __init__(self):
        self.surface = pygame.Surface((screenWidth, (screenHeight*2)/5))
        self.surface.fill("Blue")
        
    def draw(self):
        screen.blit(self.surface, (0, 432))