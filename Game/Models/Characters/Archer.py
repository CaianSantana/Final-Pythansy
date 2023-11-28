import pygame
from Settings.Configuration import screen, cellSize
from Models.Characters.Mob import Mob
from Models.States import States
from CombatMechanics.Damage import Damage
from Models.Projectile import Projectile


class Archer(Mob):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.armor = 1
        self.attack = 3
        self.speed = 3
        self.health = 15  
        self.projectile = None
        self.prey=None
        self.className = "Archer"
        self.spriteNormal = pygame.image.load("Game/Graphics/Archer.png").convert_alpha()
        self.spriteDamaged = pygame.image.load("Game/Graphics/ArcherDamaged.png").convert_alpha()
        self.flipSprite()

    def draw(self):
        super().draw()
        self.rect = pygame.Rect(self.pos.x*cellSize, self.pos.y*cellSize, cellSize, cellSize)
        screen.blit(self.sprite, self.rect)
        if isinstance(self.projectile, Projectile):
            self.projectile.draw()
                
    def update(self):
        super().update()
        self.doBasicAttack()    
        if isinstance(self.projectile, Projectile):
            projectileHit = self.projectile.update()
            if projectileHit:
                self.projectile = True
        if isinstance(self.prey, Mob) and self.prey.state == States.DEAD:
            self.prey = None
    
    def getInput(self, command):
        match command:
            case 0: 
                self.state = States.RANGED
            case 1:
                self.firstSkill()
            case 2:
                self.secondSkill()
        pass
    
    
    def doBasicAttack(self): #ATIRAR FLECHA
        if self.state == States.RANGED:
            if self.projectile is None:
                if(self.target != self.prey and self.target != None):
                    self.projectile = Projectile(self.x, self.y+0.500, "Arrow", self.target)
                    print("Dar uma flechada no inimigo para causar "+str(self.attack)+" de dano Físico")
                elif(self.target == self.prey and self.target != None):
                    self.projectile = Projectile(self.x, self.y+0.500, "Arrow", self.target)
                    print("Dar uma flechada na sua presa para causar "+str(self.attack+2)+" de dano Físico")
            if self.projectile == True:
                    self.projectile = None
                    if self.target == self.prey:
                        self.target.receiveDamage(self.attack+2, Damage.PHYSICAL)
                    else:
                        self.target.receiveDamage(self.attack, Damage.PHYSICAL)
                    self.mana-=1
                    self.state = States.IDLE
        

        
    def firstSkill(self): #SNIPERfOCUS
        if self.prey==None:
            self.prey=self.target
            print("Marca um inimigo especifico como presa, aumentando o dano da próxima flecha contra o alvo")
            self.state = States.IDLE
        pass




    def resetStats(self):
        self.armor = 2
        self.attack = 3
        self.speed = 2
        pass