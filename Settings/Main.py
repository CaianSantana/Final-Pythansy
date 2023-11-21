import sys
from .Configuration import screen, pygame
from .InputBox import InputBox
from Models.Mage import Mage
from Environments.Scenario import Scenario

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        self.char1 = Mage(3, 5)
        self.char2 = Mage(6, 5)
        self.char2.armor = 2
        self.char1.doBasicAttack(self.char2)
        self.scenario = Scenario("Forest")
        pass
    
    def update(self):
        pass
    def keyInput(self, event):
        #input.handle_event(event)
        pass
    def draw(self):
        self.scenario.draw()
        self.char1.draw()
        self.char2.draw()
        #input.draw(screen)
        
    def gameOver(self):
        pygame.quit()
        sys.exit()