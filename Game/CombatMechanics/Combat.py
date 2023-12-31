import random
from Models.States import States
from CombatMechanics.HUD import HUD
from Environments.Scenario import Scenario
from Models.Characters.Mob import Mob



class Combat:
    def __init__(self, leftTeam, rightTeam, gameFont, level):
        self.leftTeam = leftTeam
        self.rightTeam = rightTeam
        self.listOfTotalChars = leftTeam + rightTeam
        self.running = True
        self.order = self.setOrder()
        self.turn = self.nextTurn()
        self.HUD = HUD(self.leftTeam, self.rightTeam, gameFont)
        self.scenario = Scenario(level)
        
    def update(self):
        self.HUD.update(self.turn)
        for char in self.listOfTotalChars:
            char.update()
        
    def draw(self):
        self.scenario.draw()
        for char in self.listOfTotalChars:
            char.draw()
        self.HUD.draw()
    
    def doCombat(self, event):
        if self.running == True:
            if self.turn.state==States.ACTING and self.turn in self.listOfTotalChars:
                print("Turno de "+ str(self.turn)+" iniciado")
                if self.verifyTeam(self.turn):
                    HUDReturn = self.HUD.handleEvent(event)
                    if isinstance(HUDReturn, Mob):
                        self.turn.defineTarget(HUDReturn)
                    elif self.turn.getInput(HUDReturn):
                        self.turn.getInput(self.HUD.handleEvent(event))
                else:
                    self.turn.defineTarget(self.leftTeam[random.randint(0,2)])
                    self.turn.getInput(random.randint(0,1))
            elif self.turn.state == States.IDLE or self.turn.state == States.DEAD:
                self.nextTurn()
        else:
            print("Combate finalizado.")
                
    def setOrder(self):
        order = {}
        for index, char in enumerate(self.listOfTotalChars):
            order[char.speed+random.randint(1, 20)] = self.listOfTotalChars[index]
        order = dict(sorted(order.items(), reverse = True))
        return order

    def verifyLife(self):
        if(len(self.leftTeam) <1):
            print("Lado direito venceu.")
            self.running = False
            return -1
        elif(len(self.rightTeam) <1):
            print("Lado esquerdo venceu.")
            self.running = False
            return -2
        return 0

    def nextTurn(self):
        self.verifyLife()
        if self.running == True:
            self.turn = self.order.get(next(iter(self.order)))
            index = next(iter(self.order))
            self.order.pop(index)
            if self.turn.state != States.DEAD:
                self.order[index] = self.turn
                self.turn.state = States.ACTING
                return self.turn
            else:
                if self.verifyTeam(self.turn):
                    self.leftTeam.remove(self.turn)
                else:
                    self.rightTeam.remove(self.turn)
                return self.nextTurn()
        
    def verifyTeam(self, char):
        if char in self.leftTeam:
            return True
        else:
            return False