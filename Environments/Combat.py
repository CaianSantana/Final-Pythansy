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
        self.turn = next(iter(self.order))
        char = self.order.get(self.turn)
        self.order.pop(self.turn)
        self.order[self.turn] = char
        print(self.turn)
        print(next(iter(self.order)))
        