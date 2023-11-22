import sys
from Settings.Configuration import screen, pygame
from Settings.InputBox import InputBox
from Models.Mage import Mage
from Environments.Scenario import Scenario

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        
        self.char1 = Mage(4, 5)
        self.char2 = Mage(11, 5)
        self.chars = [self.char1, self.char2]
        self.char2.armor = 2
        self.cont = 0
        
        self.scenario = Scenario("Forest")
        pass
    
    def update(self):
        for char in self.chars:
            char.update()
        pass
    def keyInput(self): 
        self.char1.defineTarget(self.char2)
        pass
    def draw(self):
        self.scenario.draw()
        for char in self.chars:
            char.draw()
        #input.draw(screen)
        
    def gameOver(self):
        pygame.quit()
        sys.exit()