import pygame
from pygame.math import Vector2
from Settings.Configuration import screen, cellSize
from Models.Damage import Damage

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
        
    def draw(self):
        pass
    
    
    def doBasicAttack(self, target):
        print("Atacando o alvo para causar "+str(self.attack)+" de dano fisico")
        target.receiveDamage(self.attack, Damage.PHYSICAL)
        pass
    
    
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
        
    
        
        