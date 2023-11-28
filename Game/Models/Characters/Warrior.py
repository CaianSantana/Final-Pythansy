import pygame
from Settings.Configuration import screen, cellSize, cellNumberX
from Models.States import States
from CombatMechanics.Damage import Damage
from Models.Projectile import Projectile
from Models.Characters.Mob import Mob

class Warrior(Mob):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.armor = 2
        self.attack = 2
        self.speed = 2
        self.health = 20      
        self.projectile = None
        self.className = "Warrior"
        self.spriteNormal = pygame.image.load("Game/Graphics/Warrior.png").convert_alpha()
        self.spriteDamaged = pygame.image.load("Game/Graphics/WarriorDamaged.png").convert_alpha()   
        self.flipSprite()

    def draw(self):
        super().draw()
        self.rect = pygame.Rect(self.pos.x*cellSize, self.pos.y*cellSize, cellSize, cellSize)
        screen.blit(self.sprite, self.rect)
                
    def update(self):
        super().update()
        
    def getInput(self, command):
        match command:
            case 0: 
                self.state = States.MARCHING             
            case 1:
                self.firstSkill()
            case 2:
                self.secondSkill()
        pass
        
    
    def firstSkill(self):
        print("Erguendo escudo!")
        self.armor+=1
        self.state = States.IDLE
            

    def secondSkill(self):
        print("Dando ataque poderoso para causar "+str(self.attack+1)+" de dano fisico")
        self.attack = 4
        self.state = States.MARCHING
        self.armor=-1
        pass

    def receiveDamage(self, damage, type):
        super().receiveDamage(damage, type)
        self.resetStats()
    
    def resetStats(self):
        self.armor=2
        pass