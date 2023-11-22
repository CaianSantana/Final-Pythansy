import random

class Combat:
    def __init__(self, playerChars, enemychars):
        self.playerChars = playerChars
        self.enemychars = enemychars
        self.listOfTotalChars = playerChars + enemychars
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
        if(len(self.order) <= len(self.listOfTotalChars)/2):
            if(len(self.playerChars) <1):
                print("Inimigo venceu.")
                self.running = False
                return -1
            elif(len(self.enemychars) <1):
                print("Jogador venceu.")
                self.running = False
                return -2

    def nextTurn(self):
        self.verifyLife()
        if self.running == True:
            self.turn = self.order.get(next(iter(self.order)))
            index = next(iter(self.order))
            self.order.pop(index)
            if self.turn.live == True:
                self.order[index] = self.turn
                self.turn.occupied = True
                return self.turn
            else:
                if self.turn in self.playerChars:
                    self.playerChars.remove(self.turn)
                else:
                    self.enemychars.remove(self.turn)
                return self.nextTurn()
        