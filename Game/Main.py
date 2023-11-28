import sys, random
from Settings.Configuration import screen, pygame
from CombatMechanics.Combat import Combat
from Models.States import States
from Models.Characters.Wizard import Wizard
from Models.Characters.Archer import Archer
import Models.Characters.Archer
import Models.Characters.Wizard
from Run.Player import Player

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        self.player = Player([Wizard(3, 4), Wizard(5, 4), Archer(1, 4)])
        self.enemychars = [Wizard(10, 4), Wizard(12, 4), Archer(14, 4)] 
        self.gameFont = pygame.font.Font('Game/Fonts/Pixeled.ttf', 15)
        self.level = "Dungeon"
        self.combat = Combat(self.player.chars, self.enemychars, self.gameFont, self.level)
        pass
    
    def update(self):
        self.combat.update()
        
    def keyInput(self, event): 
        self.combat.doCombat(event)
       
    def draw(self):
        self.combat.draw()
        
    def gameOver(self):
        pygame.quit()
        sys.exit()