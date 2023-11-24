import pygame
from pygame.math import Vector2
from Settings.Configuration import cellNumberX, screen
from CombatMechanics.Damage import Damage
from Models.States import States

class Mob():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = Vector2(self.x, self.y)
        self.health = 2
        self.mana = 0
        self.attack = 2
        self.ability = 0
        self.armor = 0
        self.MagicResistance = 0
        self.speed = 1
        self.rect = self.pos
        self.target = None
        self.state = States.IDLE
        self.className = "Nulo"
        self.spriteNormal = pygame.surface.Surface((0,0))
        self.spriteDamaged = pygame.surface.Surface((0,0))
        self.sprite = self.spriteNormal
        self.flipSprite()
        self.countFlash = 20
        
        
    def draw(self):
        if self.sprite == self.spriteDamaged and self.countFlash>0:
            self.countFlash-=1
        elif self.state == States.DEAD:
            colorImage = pygame.Surface(self.sprite.get_size()).convert_alpha()
            colorImage.fill((0,0,0, 0))
            self.sprite.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
            del self
        else:
            self.sprite = self.spriteNormal
        pass
    
    def flipSprite(self):
        if not self.isLeft():
            self.spriteNormal = pygame.transform.flip(self.spriteNormal, True, False) 
            self.spriteDamaged = pygame.transform.flip(self.spriteDamaged, True, False) 
            self.sprite = pygame.transform.flip(self.sprite, True, False) 
    
    def getInput(self, command):
        match command:
            case 0: 
                self.state = States.MARCHING             
            case 1:
                self.state = States.CONJURING
                self.firstSkill()
            case 2:
                self.secondSkill()
        pass
    
    def defineTarget(self, target):
        if target != None:
            self.target = target
            
    def update(self):
        self.move()
        pass
    
    
    def doBasicAttack(self):
        print("Atacando o alvo para causar "+str(self.attack)+" de dano fisico")
        self.target.receiveDamage(self.attack, Damage.PHYSICAL)
        self.state = States.RETREATING
    
    def firstSkill(self):
        pass
    
    def secondSkill(self):
        pass
    
    def isInOriginalPos(self):
        if self.pos.x == self.x and self.pos.y == self.y:
            self.state = States.IDLE
        
    def move(self):
        if self.state == States.MARCHING:
            if self.pos.x < self.target.x-1 or self.pos.x > self.target.x+1:
               self.walk(self.speed, 1, self.target.y) 
            else:
                self.state = States.MELEE
                self.doBasicAttack()
                self.defineTarget(None)
        elif self.state == States.RETREATING:
            if self.pos.x != self.x or self.pos.y != self.y:
                self.walk(self.speed*-1, 1, self.y)
                self.isInOriginalPos()
        
    def walk(self, speedX, speedY, y):
        yRelation = self.pos.y - y
        if self.pos.x != self.x or speedX>0:
            if self.isLeft():
                self.pos.x+=speedX
            elif not self.isLeft():
                self.pos.x-=speedX
        if self.isLeft() and self.pos.x>cellNumberX/2 or not self.isLeft() and self.pos.x<cellNumberX/2:    
            if yRelation>0:
                self.pos.y-=speedY
            elif yRelation<0:
                self.pos.y+=speedY
    
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
        if self.health <= 0:
            print("Morreu.")
            self.die()
            pass
        else:
            self.blink()
           
       
        
    def blink(self):
        self.countFlash = 20
        self.sprite = self.spriteDamaged
        
    def die(self):
        self.state = States.DEAD
        if not self.isLeft():
            self.sprite = pygame.transform.rotate(self.sprite, -90) 
        else:
            self.sprite = pygame.transform.rotate(self.sprite, 90) 