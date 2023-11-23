from pygame.math import Vector2
import pygame, math
from Models.Projectiles import projectilesDict
from Models.Characters.Mob import Mob
from Settings.Configuration import screen, cellSize, cellNumberX
from decimal import *


class Projectile(Mob):
    
    def __init__(self, x, y, type, target):
        super().__init__(x, y)
        self.health = 0
        self.mana = 0
        self.attack = 0
        self.ability = 0
        self.armor = 0
        self.MagicResistance = 0
        self.speed = 2
        self.sprite = pygame.image.load(projectilesDict[type]).convert_alpha()
        self.target = target
        if not self.isLeft():
            self.sprite = pygame.transform.flip(self.sprite, True, False) 
        
    def defineTarget(self, target):
        if target != None:
            self.target = target
        
    def update(self):
        return self.move()    
        
    def draw(self):
        self.rect = pygame.Rect(self.pos.x*cellSize, self.pos.y*cellSize, cellSize, cellSize)
        screen.blit(self.sprite, self.rect)  
        
    def move(self):
        if self.pos.x < self.target.x-1 or self.pos.x > self.target.x+1:
            self.walk(int(self.speed), int(1), self.target.y+0.500)
            return False
        else:
            self.vanish()
            return True
            
    def isLeft(self):
        if self.x < cellNumberX/2:
            return True
        return False
    
    def vanish(self):
        colorImage = pygame.Surface(self.sprite.get_size()).convert_alpha()
        colorImage.fill((255,255,255, 0))
        self.sprite.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        del self