import pygame
from Settings.Configuration import screen, cellSize, cellNumberX
from Models.Characters.Mob import Mob
from Models.States import States
from CombatMechanics.Damage import Damage
from Models.Projectiles import projectilesDict
from pygame.math import Vector2
from Models.Projectile import Projectile

class Wizard(Mob):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.mana = 5
        self.ability = 2
        self.MagicResistance = 1
        self.projectile = None
        self.spriteNormal = pygame.image.load("Game/Graphics/Wizard.png").convert_alpha()#fonte: https://www.pngkey.com/maxpic/u2e6q8r5i1y3y3u2/
        self.spriteDamaged = pygame.image.load("Game/Graphics/WizardDamaged.png").convert_alpha()
        self.flipSprite()

    def draw(self):
        super().draw()
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
        self.doBasicAttack()
        self.throwMagic()
    
    def throwMagic(self):
        if self.state == States.CONJURING and self.mana>=1:
            if self.projectile is None:
                self.projectile = Projectile(self.x, self.y+0.500, "Fireball", self.target)
                print("Lança uma bola de energia no alvo para causar "+str(self.ability)+" de dano mágico")
            if self.projectile == True:
                self.projectile = None
                self.target.receiveDamage(self.ability, Damage.MAGICAL)
                self.mana-=1
                self.state = States.IDLE
        elif self.state == States.CONJURING and self.mana<=0:
            print("Sem mana")
            self.state = States.IDLE
        pass