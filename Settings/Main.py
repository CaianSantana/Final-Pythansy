import sys
from Settings.Configuration import screen, pygame
from Settings.InputBox import InputBox
from Models.Mage import Mage
from Environments.Scenario import Scenario
from Environments.Combat import Combat

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        self.chars = [Mage(4, 5), Mage(11, 5)]
        self.combat = Combat(self.chars)
        self.chars[1].sprite = pygame.transform.flip(self.chars[1].sprite, True, False) 
        self.chars[1].armor = 2
        self.cont = 0
        
        self.scenario = Scenario("Forest")
        pass
    
    def update(self):
        for char in self.chars:
            char.update()
        pass
    def keyInput(self): 
        #for char in self.combat.order:
        pass
    def draw(self):
        self.scenario.draw()
        for char in self.chars:
            char.draw()
        #input.draw(screen)
        
    def gameOver(self):
        pygame.quit()
        sys.exit()