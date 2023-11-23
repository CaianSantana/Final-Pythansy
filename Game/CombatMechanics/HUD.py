import pygame
from Settings.Configuration import screen, screenHeight, screenWidth

class HUD:
    def __init__(self):
        self.height = screenHeight/4
        self.surface = pygame.Surface((screenWidth, self.height))
        self.surface.fill("Blue")
        
    def draw(self):
        screen.blit(self.surface, (0, screenHeight - self.height))