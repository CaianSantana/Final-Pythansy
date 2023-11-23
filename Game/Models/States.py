from enum import Enum

class States(Enum):
    DEAD = -1
    IDLE = 1
    ACTING = 2
    MARCHING = 3
    RETREATING = 4
    READY = 5
    MELEE = 6
    RANGED = 7
    CONJURING = 8
    