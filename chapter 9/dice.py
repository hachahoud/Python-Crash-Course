from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        n = randint(1,self.sides)
        print(n)

die = Die(6)
for i in range(10):
    die.roll_die()