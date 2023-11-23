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
        self.speed = 1.5
        self.sprite = pygame.image.load(projectilesDict[type]).convert_alpha()
        self.target = target
        if not self.isLeft():
            self.sprite = pygame.transform.flip(self.sprite, True, False) 
        
    def defineTarget(self, target):
        if target != None:
            self.target = target
        
    def update(self):
        return self.moveProctile()    
        
    def draw(self):
        self.rect = pygame.Rect(self.pos.x*cellSize, self.pos.y*cellSize, cellSize, cellSize)
        screen.blit(self.sprite, self.rect)  
        
    def moveProctile(self):
        if self.pos.x < self.target.x-self.speed or self.pos.x > self.target.x+self.speed:
            yRelation = self.pos.y - self.target.y
            if self.isLeft():
                self.pos.x+=self.speed
            elif not self.isLeft():
                self.pos.x-=self.speed
            if self.pos.x == cellNumberX/2: 
                if yRelation>0.5:
                    self.pos.y-=1
                elif yRelation<0.5:
                    self.pos.y+=1.5
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