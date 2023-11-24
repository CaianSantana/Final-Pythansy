import sys
from Settings.Configuration import screen, pygame
from Settings.InputBox import InputBox
from Models.Characters.Wizard import Wizard
from Environments.Scenario import Scenario
from CombatMechanics.Combat import Combat
from Models.States import States
from CombatMechanics.HUD import HUD
from Run.Player import Player

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        self.player = Player([Wizard(3, 4), Wizard(1, 4), Wizard(5, 4)])
        self.enemychars = [Wizard(10, 4), Wizard(12, 4), Wizard(14, 4)] 
        self.totalChars = self.player.chars + self.enemychars
        self.totalChars[0].health = 4
        self.totalChars[2].health = 4
        self.combat = Combat(self.player.chars, self.enemychars)
        self.combat.nextTurn()
        self.cont = 0
        self.scenario = Scenario("Dungeon")
        self.gameFont = pygame.font.Font('Game/Fonts/Pixeled.ttf', 25)
        self.HUD = HUD(self.player.chars, self.gameFont)
        
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
                    try:
                        nextChar = self.combat.order.get(next(nextItem))
                    except:
                        if self.combat.verifyLife() !=0:
                            self.combat.running = False
                    if self.combat.verifyTeam(self.combat.turn) and not self.combat.verifyTeam(nextChar) and not nextChar.state == States.DEAD or not self.combat.verifyTeam(self.combat.turn) and self.combat.verifyTeam(nextChar) and not nextChar.state == States.DEAD:
                        self.combat.turn.defineTarget(nextChar)
                        self.combat.turn.state = States.READY
                        break
            elif self.combat.turn.state == States.IDLE or self.combat.turn.state == States.DEAD:
                self.combat.nextTurn()
        else:
            print("Combate finalizado.")
       
       
    def draw(self):
        self.scenario.draw()
        self.HUD.draw()
        for char in self.totalChars:
            char.draw()
        #input.draw(screen)
        
    def gameOver(self):
        pygame.quit()
        sys.exit()