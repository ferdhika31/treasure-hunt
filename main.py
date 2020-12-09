import numpy as np
from itertools import product
from TreasureHunt import TreasureHunt

# init game
game = TreasureHunt()

# generate dumb rules
step_length = 10
rules = product(['NORTH', 'EAST', 'SOUTH'], repeat=step_length)

possibleRules = []
for rule in rules:
    # reset player location
    game.resetPlayerLocation()
    
    possibleStep = []
    founded = False
    for step in rule:
        # move step
        isMove = game.move(step)
        # check player founded treasure
        checkTreasure = game.checkPlayerGetTreasure()
        # if possible move?
        if isMove:
            possibleStep.append(step)
        # if founded treasure
        if checkTreasure:
            founded = True
            break

    # if founded treasure, append rules 
    if founded:        
        possibleRules.append(possibleStep)

# rule to tuple
rule_tuple = [tuple(x) for x in possibleRules]
# sorted position rules
uniquePossibleRules = sorted(set(rule_tuple), key=lambda x: rule_tuple.index(x))
print("Rules :")
for rule in uniquePossibleRules:
    print(rule)

# print board
game.displayBoard()