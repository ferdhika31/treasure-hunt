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
            possibleStep.append(game.getPlayerLocation().toString())
        # if founded treasure
        if checkTreasure:
            founded = True
            break

    # if founded treasure, append rules 
    if founded:        
        possibleRules.append(possibleStep)

def checkDuplicates(arr):
    if len(arr) == len(set(arr)):
        return False
    else:
        return True

# rule to tuple
rule_tuple = [tuple(x) for x in possibleRules]
# sorted position rules
uniquePossibleRules = sorted(set(rule_tuple), key=lambda x: rule_tuple.index(x))

print("Player Position :", game.getPlayerLocation().toString())
print("Treasure Position :", [tloc.toString() for tloc in game.getTreasureLocation()])
print("Step Rules Coordinate :")
for rule in uniquePossibleRules:
    # handle back step position
    if not checkDuplicates(rule):
        print(rule)

# print board
game.displayBoard()