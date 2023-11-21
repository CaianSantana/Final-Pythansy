import pygame
from Settings.Configuration import screen, cellSize
from Models.Character import Character


class Mage(Character):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.mana = 5
        self.ability = 2
        self.MagicResistance = 1
        self.sprite = pygame.image.load("Final-Pythansy/Graphics/BlackMage.png").convert_alpha()
        #fonte: https://www.pngkey.com/maxpic/u2e6q8r5i1y3y3u2/
        
    def draw(self):
        charRect = pygame.Rect(self.pos.x*cellSize, self.pos.y*cellSize, cellSize, cellSize)
        screen.blit(self.sprite, charRect)