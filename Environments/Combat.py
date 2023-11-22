import random

class Combat:
    def __init__(self, listOfChars):
        self.listOfChars = listOfChars
        self.running = True
        self.order = self.setOrder()
        #self.turn = self.order[0]
                
    def setOrder(self):
        order = {}
        inits = []
        for index, char in enumerate(self.listOfChars):
            inits.append(char.speed+random.randint(1, 20))
            print(inits[index])
        inits.sort()
        for index, init in enumerate(inits):
            order[init] = self.listOfChars[index]
        print(order.keys())
        print(order.items())
        #dict(sorted(order.keys(), key=lambda item: item[1]))
        
        return order
        