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