import pygame
from pygame.math import Vector2
from Settings.Configuration import screen, cellSize

class Character():
    
    def __init__(self, x, y):
        """self.health = 10
        self.mana = 10
        self.attack = 2
        self.ability = 0
        self.armor = 1
        self.MagicResistance = 0"""
        self.x = x
        self.y = y
        self.pos = Vector2(self.x, self.y)
        self.sprite = pygame.image.load("Graphics/BlackMage.png").convert_alpha()
        #fonte: https://www.pngkey.com/maxpic/u2e6q8r5i1y3y3u2/
        
    def draw(self):
        
        charRect = pygame.Rect(self.pos.x*cellSize, self.pos.y*cellSize, cellSize, cellSize)
        screen.blit(self.sprite, charRect)
        #pygame.draw.rect(screen, (122, 122, 122), charRect)
        #print("to funfando")
        
    
        
        