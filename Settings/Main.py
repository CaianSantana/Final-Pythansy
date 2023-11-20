import sys
from .Configuration import screen, pygame
from .InputBox import InputBox

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        pass
    
    def update(self):
        pass
    def keyInput(self, event):
        #input.handle_event(event)
        pass
    def draw(self):
        #input.draw(screen)
        pass
    def gameOver(self):
        pygame.quit()
        sys.exit()