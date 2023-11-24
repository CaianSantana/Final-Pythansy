import sys, random
from Settings.Configuration import screen, pygame
from Settings.InputBox import InputBox
from Models.Characters.Mob import Mob
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
        self.combat = Combat(self.player.chars, self.enemychars)
        self.combat.nextTurn()
        self.cont = 0
        self.scenario = Scenario("Dungeon")
        self.gameFont = pygame.font.Font('Game/Fonts/Pixeled.ttf', 15)
        self.HUD = HUD(self.player.chars, self.enemychars, self.gameFont)
        
        pass
    
    def update(self):
        for char in self.totalChars:
            char.update()
        self.HUD.update(self.combat.turn)
        pass
    def keyInput(self, event): 
        if self.combat.running == True:
            if self.combat.turn.state==States.ACTING and self.combat.turn in self.totalChars:
                print("Turno de "+ str(self.combat.turn)+" iniciado")
                if self.combat.turn in self.player.chars:
                    HUDReturn = self.HUD.handleEvent(event)
                    if isinstance(HUDReturn, Mob):
                        self.combat.turn.defineTarget(HUDReturn)
                    elif self.combat.turn.getInput(HUDReturn):
                        self.combat.turn.getInput(self.HUD.handleEvent(event))
                else:
                    self.combat.turn.defineTarget(self.player.chars[random.randint(0,2)])
                    self.combat.turn.getInput(random.randint(0,1))
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