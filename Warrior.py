import pygame
from Settings.Configuration import screen, cellSize, cellNumberX
from Models.Character import Character
from Models.States import States
from Models.Damage import Damage
from Models.Projectiles import projectilesDict
from pygame.math import Vector2
from Models.Projectile import Projectile

class Warrior(Character):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.armor = 2
        self.attack = 3
        self.speed = 2
        self.health = 25        
        self.projectile = None
        self.sprite = pygame.image.load("BlackMage.png").convert_alpha()#fonte: https://www.pngkey.com/maxpic/u2e6q8r5i1y3y3u2/
        if not self.isLeft():
            self.sprite = pygame.transform.flip(self.sprite, True, False)    

    def draw(self):
        self.rect = pygame.Rect(self.pos.x*cellSize, self.pos.y*cellSize, cellSize, cellSize)
        screen.blit(self.sprite, self.rect)
        
        if isinstance(self.projectile, Projectile):
            self.projectile.draw()
                
    def update(self):
        super().update()
        if self.projectile !=None:
            projectileHit = self.projectile.update()
            if projectileHit:
                self.projectile = True
    
        
    def act(self):
        self.resetStas()
        self.doBasicAttack()
    
    def block(self,atack,damageType):
        if self.state == States.DEFENDING:
            self.armor+=1
            print("Bloqueando ataque "+str(atack)+" de dano ")
            self.receiveDamage(atack, damageType)
        elif self.state == States.CONJURING and self.mana<=0:
            self.state = States.IDLE
        pass

    def powerAtack(self):
        if self.state == States.READY:
            self.state = States.MARCHING
        if self.state == States.MELEE:
            print("Dando ataque poderoso para causar "+str(self.attack+1)+" de dano fisico")
            self.target.receiveDamage(self.attack+1, Damage.PHYSICAL)
            self.state = States.RETREATING
            self.armor=-1
        pass

    def resetStas(self):
        self.armor=2
        pass