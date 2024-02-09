import random

# for i in range(3):
#     print (random.randint(0,10))

# for i in range(3):
#     print (random.random())

# members = ['mahi','zizi','hanna','sheida']
# print (random.choice(members))




# roling dice 
class Dice:
    def roll (self):
        first = random.randint (1,6)
        second = random.randint (1,6)
        return [first , second]


dice = Dice()
rolling = dice.roll()
print (rolling)