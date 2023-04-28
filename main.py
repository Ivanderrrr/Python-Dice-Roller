# version 1.0.0


import random
# amount of dice
dice = random.randint(1, 6)
# amount rollOfDice from input user
while True:
    rollOfDice = (input('amount of rolls: '))
    if rollOfDice.isdecimal() > 0:
        print(dice)
        break
    else:
        print("The amount of rolls must be at least one and must be only numeric characters")
