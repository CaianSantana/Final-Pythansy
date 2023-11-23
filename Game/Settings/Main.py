import sys
from Settings.Configuration import screen, pygame
from Settings.InputBox import InputBox
from Models.Mage import Mage
from Environments.Scenario import Scenario
from Environments.Combat import Combat
from Models.States import States

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        self.playerChars = [Mage(4, 6), Mage(2, 7)] #, Mage(2, 6)
        self.enemychars = [Mage(11, 6), Mage(13, 7)] #, Mage(13, 6)
        self.totalChars = self.playerChars + self.enemychars
        self.totalChars[0].health = 4
        self.totalChars[2].health = 4
        self.combat = Combat(self.playerChars, self.enemychars)
        self.combat.nextTurn()
        for char in self.enemychars:
            char.sprite = pygame.transform.flip(char.sprite, True, False) 
        self.cont = 0
        self.scenario = Scenario("Forest")
        pass
    
    def update(self):
        for char in self.totalChars:
            char.update()
            
        pass
    def keyInput(self): 
        if self.combat.running == True:
            if self.combat.turn.state==States.ACTING:
                print("Turno de "+ str(self.combat.turn)+" iniciado")
                nextItem = iter(self.combat.order)
                for i in enumerate(self.totalChars):
                    nextChar = self.combat.order.get(next(nextItem))
                    if self.combat.verifyTeam(self.combat.turn) and not self.combat.verifyTeam(nextChar) or not self.combat.verifyTeam(self.combat.turn) and self.combat.verifyTeam(nextChar):
                        self.combat.turn.defineTarget(nextChar)
                        self.combat.turn.state = States.CONJURING
                        break
            elif self.combat.turn.state == States.IDLE or self.combat.turn.state == States.DEAD:
                self.combat.nextTurn()
        else:
            print("Combate finalizado.")
       
       
    def draw(self):
        self.scenario.draw()
        for char in self.totalChars:
            char.draw()
        #input.draw(screen)
        
    def gameOver(self):
        pygame.quit()
        sys.exit()