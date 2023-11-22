import pygame
from pygame.math import Vector2
from Settings.Configuration import cellNumberX, cellSize
from Models.Damage import Damage
from Models.Side import Side

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
        self.speed = 1
        self.rect = self.pos
        self.target = None
        self.side = self.getSide()
        self.occupied = False
        
    def draw(self):
        pass
    
    def getInput(self):
        pass
    
    def defineTarget(self, target):
        if target != None:
            if target.side != self.side:
                self.target = target
        else:
            self.target = None
    
    def doBasicAttack(self):
        print("Atacando o alvo para causar "+str(self.attack)+" de dano fisico")
        self.target.receiveDamage(self.attack, Damage.PHYSICAL)
        pass
        
    def update(self):
        self.getInput()
        self.getSide()
        self.move()
        
    def doSomething(self):
        self.doBasicAttack()
    
    def isInOriginalPos(self):
        if self.pos.x == self.x and self.pos.y == self.y:
            self.occupied = False
            print(self.occupied)
        
    def move(self):
        if self.target != None:
            if self.pos.x < self.target.x-1 or self.pos.x > self.target.x+1:
                yRelation = self.pos.y - self.target.y
                if self.side == Side.LEFT:
                    self.pos.x+=1
                elif self.side == Side.RIGHT:
                    self.pos.x-=1
                if self.pos.x == cellNumberX/2:    
                    if yRelation>0:
                        self.pos.y-=1
                    elif yRelation<0:
                        self.pos.y+=1
            else:
                self.doSomething()
                self.defineTarget(None)
        else:
            
            if self.pos.x != self.x or self.pos.y != self.y:
                if self.side == Side.LEFT:
                    self.pos.x-=1
                elif self.side == Side.RIGHT:
                    self.pos.x+=1
                if self.pos.x == cellNumberX/2:
                    if self.pos.y < self.y:
                        self.pos.y+=1
                    elif self.pos.y > self.y:
                        self.pos.y-=1
                self.isInOriginalPos()
        
    def getSide(self):
        if self.x < cellNumberX/2:
            self.side = Side.LEFT
        else:
            self.side = Side.RIGHT
    
    def receiveDamage(self, damage, type):
        if type == Damage.PHYSICAL:
            damage -= self.armor
        else:
            damage -= self.MagicResistance
        self.health -= damage
        print(str(damage)+" de dano sofrido")
        print(str(self.health)+" de vida restante")
        if self.health <= 0:
            #Lógica de morte, provavelmente teremos de atribuir estado de vivo ou morto para o character
            pass