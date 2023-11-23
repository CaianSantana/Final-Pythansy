from pygame.math import Vector2
import pygame
from Models.Projectiles import projectilesDict
from Settings.Configuration import screen, cellSize, cellNumberX
from Models.States import States

class Projectile:
    
    def __init__(self, x, y, type, target):
        self.x = x
        self.y = y
        self.pos = Vector2(self.x, self.y)
        self.sprite = pygame.image.load(projectilesDict[type]).convert_alpha()
        self.target = target
        self.state = States.MARCHING
        
    def defineTarget(self, target):
        if target != None:
            self.target = target
        
    def update(self):
        self.drawProjectile()
        self.moveProctile()    
        
    def drawProjectile(self):
        pass
    
    def moveProctile(self):
        pass