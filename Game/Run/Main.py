import sys, random
from Settings.Configuration import screen, pygame
from Models.Characters.Wizard import Wizard
from CombatMechanics.Combat import Combat
from Run.Menu import Menu
from Run.Player import Player

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        
        self.menu = Menu()

        """self.player = Player([Wizard(3, 4), Wizard(1, 4), Wizard(5, 4)])
        self.enemychars = [Wizard(10, 4), Wizard(12, 4), Wizard(14, 4)] 
        
        self.level = "Dungeon"
        self.combat = Combat(self.player.chars, self.enemychars, self.gameFont, self.level)"""
        pass
    
    def update(self):
        pass
        #self.combat.update()
        
    def keyInput(self, event): 
        pass
        #self.combat.doCombat(event)
       
    def draw(self):
        self.menu.draw()
        #self.combat.draw()
        
    def gameOver(self):
        pygame.quit()
        sys.exit()