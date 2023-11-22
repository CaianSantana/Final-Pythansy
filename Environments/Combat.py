import random

class Combat:
    def __init__(self, listOfChars):
        self.listOfChars = listOfChars
        self.running = True
        self.order = self.setOrder()
        self.turn = 0
                
    def setOrder(self):
        order = {}
        inits = []
        for index, char in enumerate(self.listOfChars):
            inits.append(char.speed+random.randint(1, 20))
        inits.sort()
        for index, init in enumerate(inits):
            order[init] = self.listOfChars[index]
        return order

    def nextTurn(self):
        self.turn = self.order.get(next(iter(self.order)))
        index = next(iter(self.order))
        self.order.pop(index)
        self.order[index] = self.turn
        self.turn.occupied = True
        return self.turn
        