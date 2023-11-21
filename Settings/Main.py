import sys
from .Configuration import screen, pygame
from .InputBox import InputBox
from Models.Mage import Mage

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        self.char = Mage(3, 5)
        pass
    
    def update(self):
        pass
    def keyInput(self, event):
        #input.handle_event(event)
        pass
    def draw(self):
        self.char.draw()
        #input.draw(screen)
        
    def gameOver(self):
        pygame.quit()
        sys.exit()