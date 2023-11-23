class Chars:    
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