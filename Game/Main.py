import sys, random
from Settings.Configuration import screen, pygame
from Settings.InputBox import InputBox
from Models.Characters.Mob import Mob
from Models.Characters.Wizard import Wizard
from CombatMechanics.Combat import Combat
from Models.States import States

from Run.Player import Player

#input = InputBox(570, 376, 140, 32)  -- Teste de inputbox

class Main:
    
    def __init__(self):
        self.player = Player([Wizard(3, 4), Wizard(1, 4), Wizard(5, 4)])
        self.enemychars = [Wizard(10, 4), Wizard(12, 4), Wizard(14, 4)] 
        self.totalChars = self.player.chars + self.enemychars
        self.gameFont = pygame.font.Font('Game/Fonts/Pixeled.ttf', 15)
        self.level = "Dungeon"
        self.combat = Combat(self.player.chars, self.enemychars, self.gameFont, self.level)
        self.combat.nextTurn()
        self.cont = 0
        pass
    
    def update(self):
        self.combat.update()
        
    def keyInput(self, event): 
        if self.combat.running == True:
            if self.combat.turn.state==States.ACTING and self.combat.turn in self.totalChars:
                print("Turno de "+ str(self.combat.turn)+" iniciado")
                if self.combat.turn in self.player.chars:
                    HUDReturn = self.combat.HUD.handleEvent(event)
                    if isinstance(HUDReturn, Mob):
                        self.combat.turn.defineTarget(HUDReturn)
                    elif self.combat.turn.getInput(HUDReturn):
                        self.combat.turn.getInput(self.combat.HUD.handleEvent(event))
                else:
                    self.combat.turn.defineTarget(self.player.chars[random.randint(0,2)])
                    self.combat.turn.getInput(random.randint(0,1))
            elif self.combat.turn.state == States.IDLE or self.combat.turn.state == States.DEAD:
                self.combat.nextTurn()
        else:
            print("Combate finalizado.")
       
       
    def draw(self):
        self.combat.draw()
        
    def gameOver(self):
        pygame.quit()
        sys.exit()