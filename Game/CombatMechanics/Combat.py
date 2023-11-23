import random
from Models.States import States


class Combat:
    def __init__(self, leftTeam, rightTeam):
        self.leftTeam = leftTeam
        self.rightTeam = rightTeam
        self.listOfTotalChars = leftTeam + rightTeam
        self.running = True
        self.order = self.setOrder()
        self.turn = 0
                
    def setOrder(self):
        order = {}
        inits = []
        for index, char in enumerate(self.listOfTotalChars):
            inits.append(char.speed+random.randint(1, 20))
        inits.sort()
        for index, init in enumerate(inits):
            order[init] = self.listOfTotalChars[index]
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