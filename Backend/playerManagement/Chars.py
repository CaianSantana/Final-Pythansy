class Chars:    
    id = None
    myClass = ""
    hp = 0
    mana = 0
    attack = 0
    ability = 0
    armor = 0
    magicResistance = 0
    speed = 0

    def __init__(self,hp:int,mana:int,attack:int,ability:int,armor:int,magic:int,speed:int) -> None:
        self.hp = hp
        self.mana = mana
        self.attack = attack
        self.ability = ability
        self.armor = armor
        self.magicResistance = magic
        self.speed = speed
        pass
    
    def recebaDano(self, dano):
        self.hp = self.hp - dano
        print("hp restante", self.hp)
        
    def causeDano(self, char, dano:int):
        char.recebaDano(dano)
        pass
        
    def setId(self,id:int):
        self.id = id
        
    def getMyClass(self):
        return self.myClass