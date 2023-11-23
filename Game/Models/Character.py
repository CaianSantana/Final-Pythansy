import pygame
from pygame.math import Vector2
from Settings.Configuration import cellNumberX
from Models.Damage import Damage
from Models.States import States

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
        self.state = States.IDLE
        self.sprite = None
        
    def draw(self):
        pass
    
    def getInput(self):
        pass
    
    def defineTarget(self, target):
        if target != None:
            self.target = target
            
    def update(self):
        self.getInput()
        self.move()
        self.act()
    
    def act(self):
        self.doBasicAttack()
    
    def doBasicAttack(self):
        if self.state == States.READY:
            self.state = States.MARCHING
        if self.state == States.MELEE:
            print("Atacando o alvo para causar "+str(self.attack)+" de dano fisico")
            self.target.receiveDamage(self.attack, Damage.PHYSICAL)
            self.state = States.RETREATING
        pass
    
    def isInOriginalPos(self):
        if self.pos.x == self.x and self.pos.y == self.y:
            self.state = States.IDLE
        
    def move(self):
        if self.state == States.MARCHING:
            if self.pos.x < self.target.x-1 or self.pos.x > self.target.x+1:
                yRelation = self.pos.y - self.target.y
                if self.isLeft():
                    self.pos.x+=1
                elif not self.isLeft():
                    self.pos.x-=1
                if self.pos.x == cellNumberX/2:    
                    if yRelation>0:
                        self.pos.y-=1
                    elif yRelation<0:
                        self.pos.y+=1
            else:
                self.state = States.MELEE
                self.defineTarget(None)
        elif self.state == States.RETREATING:
            if self.pos.x != self.x or self.pos.y != self.y:
                if self.isLeft():
                    self.pos.x-=1
                elif not self.isLeft():
                    self.pos.x+=1
                if self.pos.x == cellNumberX/2:
                    if self.pos.y < self.y:
                        self.pos.y+=1
                    elif self.pos.y > self.y:
                        self.pos.y-=1
                self.isInOriginalPos()
        
    
    def isLeft(self):
        if self.x < cellNumberX/2:
            return True
        return False
    
    def receiveDamage(self, damage, type):
        if type == Damage.PHYSICAL:
            damage -= self.armor
        else:
            damage -= self.MagicResistance
        self.health -= damage
        print(str(damage)+" de dano sofrido")
        print(str(self.health)+" de vida restante")
        if self.health <= 0:
            self.die()
            pass
        
    
    def die(self):
        print("Morreu.")
        self.state = States.DEAD
        colorImage = pygame.Surface(self.sprite.get_size()).convert_alpha()
        colorImage.fill((47,47,47))
        self.sprite.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        if not self.isLeft():
            self.sprite = pygame.transform.rotate(self.sprite, -90) 
        else:
            self.sprite = pygame.transform.rotate(self.sprite, 90) 