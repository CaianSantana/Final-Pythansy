import pygame
from pygame.math import Vector2
from Settings.Configuration import screen, cellSize

class Character():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = Vector2(self.x, self.y)
        self.health = 20
        self.mana = 0
        self.attack = 2
        self.ability = 0
        self.armor = 0
        self.MagicResistance = 0
        
    def draw(self):
        pass
        
    
        
        