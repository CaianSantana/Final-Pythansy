import pygame
from Environments.Levels import levelDict
from Settings.Configuration import screenHeight, screenWidth, screen

class Scenario:
    def __init__(self, level):
        self.x = 0
        self.y = 0
        self.level = levelDict[level]
        
    def draw(self):
        scenarioRect = pygame.Rect(0, 0, screenWidth, screenHeight)
        scenario = pygame.image.load(self.level).convert_alpha()
        screen.blit(scenario, scenarioRect)

