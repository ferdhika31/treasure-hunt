import random
import numpy as np
from Position import Position

class TreasureHunt:
    board = np.array([])
    playerLocation = Position(4, 1)
    treasures = ['$']

    def __init__(self):
        # init board
        self.board = np.array([
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", "#", ".", ".", "#"],
            ["#", ".", ".", ".", "#", ".", "#", "#"],
            ["#", ".", "#", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
        ])
        # init player location
        playerLocation = self.playerLocation
        self.board[playerLocation.x][playerLocation.y] = "X"

        # init treasure location
        self.randomTreasureLocation()

    def displayBoard(self):
        for b in self.board:
            for bc in b:
                print(bc,end = " ")
            print()
    
    def getPlayerLocation(self):
        return self.playerLocation

    def resetPlayerLocation(self):
        self.playerLocation = Position(4, 1)

    def randomTreasureLocation(self):
        treasures = self.treasures

        # find clear path
        clearPathLoc = np.argwhere(self.board == ".")
        # random shuffle clear path location
        np.random.shuffle(clearPathLoc)
        # At this time the treasure can only set one
        if len(treasures) > 1:
            print("At this time the treasure can only set one")
            exit()
        # Randomly locate the treasures in clear path
        for i in range(0, len(treasures)):
            # set treasure clearpath posistion
            treasureLocation = Position(clearPathLoc[i][0], clearPathLoc[i][1])
            # set treasure on board
            self.board[treasureLocation.x][treasureLocation.y] = treasures[i]

    def checkObstaclePath(self, location):
        # find obstacle path location
        obstaclePathLoc = np.argwhere(self.board == "#")
        # convert to object Position
        result = list(map(lambda x: Position(x[0], x[1]), obstaclePathLoc)) 
        # check obstacle
        for path in result:
            if path.isEqualTo(location):
                return True
                break

        return False

    def checkPlayerGetTreasure(self):
        location = self.playerLocation
        # find treasure location
        treasureLoc = np.argwhere(self.board == "$")
        # convert to object Position
        treasures = list(map(lambda x: Position(x[0], x[1]), treasureLoc)) 
        # check obstacle
        for treasure in treasures:
            if treasure.isEqualTo(location):
                # clear path and remove treasure
                # board[location.x][location.y] = "."
                # print("Treasure founded at coordinate %s." % (treasure.toString()))

                return True
                break

        return False

    def move(self, direction):
        playerLocation = self.playerLocation
        if direction == "NORTH":
            location = Position(playerLocation.x - 1, playerLocation.y)
            isObstacle = self.checkObstaclePath(location)
        elif direction == "EAST":
            location = Position(playerLocation.x, playerLocation.y + 1)
            isObstacle = self.checkObstaclePath(location)
        elif direction == "SOUTH":
            location = Position(playerLocation.x + 1, playerLocation.y)
            isObstacle = self.checkObstaclePath(location)

        if not isObstacle:
            # set new locatoin
            self.playerLocation = location
            return True
            
        return False
        