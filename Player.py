from enum import Enum

from DrawableObjects import DrawableObjects
from TupleToInt import getX, getY

class directions(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    DIAG_UP_LEFT = 4
    DIAG_UP_RIGHT = 5
    DIAG_DOWN_LEFT = 6
    DIAG_DOWN_RIGHT = 7


class Player(DrawableObjects):
    def __init__(self, locations, color):
        DrawableObjects.__init__(self, color)
        self._locations = locations
        self._counter = 0
        self._direction = [0] * directions.__len__()
        self._startPoint = (0, 0)
        self._endPoint = (0, 0)
        self._lastDirection = directions.LEFT.value

    def getPlayerLocation(self):
        """ Get the current player location. Update his direction movment.
                    :return tuple : (x,y) current location
                """
        self._counter += 1
        x = getX(self._locations[self._counter - 1])
        y = getY(self._locations[self._counter - 1])
        self.checkDirection(getX(self._locations[self._counter - 2]), x,
                            getY(self._locations[self._counter - 2]), y)
        self.setDirection(x, y)
        return self._locations[self._counter - 1]

    def getCounter(self):
        """  Get the counter(how many frames we passed).
                   :return counter
               """
        return self._counter

    def checkDirection(self, x1, x2, y1, y2):
        """  Estimate the movement direction of the player.
                :param x1, y1 : last location of the player
                :param x2, y2 : current location of the player
                """
        if x1 > x2:
            if y1 == y2:  # left V
                self._direction[directions.LEFT.value] = self._direction[directions.LEFT.value] + 1
            elif y1 > y2:  # diag_up_left V
                self._direction[directions.DIAG_UP_LEFT.value] = self._direction[directions.DIAG_UP_LEFT.value] + 1
            else:  # diag_down_left V
                self._direction[directions.DIAG_DOWN_LEFT.value] = self._direction[directions.DIAG_DOWN_LEFT.value] + 1
        if x1 < x2:
            if y1 == y2:  # right V
                self._direction[directions.RIGHT.value] = self._direction[directions.RIGHT.value] + 1
            elif y1 > y2:  # diag_up_right V
                self._direction[directions.DIAG_UP_RIGHT.value] = self._direction[directions.DIAG_UP_RIGHT.value] + 1
            else:  # diag_down_right V
                self._direction[directions.DIAG_DOWN_RIGHT.value] = self._direction[
                                                                        directions.DIAG_DOWN_RIGHT.value] + 1
        if x1 == x2:
            if y1 < y2:  # down V
                self._direction[directions.DOWN.value] = self._direction[directions.DOWN.value] + 1
            elif y1 > y2:  # up V
                self._direction[directions.UP.value] = self._direction[directions.UP.value] + 1

    def setDirection(self, x, y):
        """  Set the movement direction of the player.
                :param x :  Current location.x of the player
                :param y : Current location.y of the player
            """
        num = self.findReqDirection()
        if num < 0:
            self.switchCase(x, y, self._lastDirection)
        else:
            self.switchCase(x, y, num)
            self._lastDirection = num
            self._direction = [0] * directions.__len__()

    def findReqDirection(self):
        """  Set the movement direction of the player.
                :return num: Indicate of the current player total direction movement
            """
        max_val = max(self._direction)
        sec_max = 0
        for i in range(self._direction.__len__()):
            if self._direction[i] > sec_max and self._direction[i] != max_val:
                sec_max = self._direction[i]

        if max_val - sec_max > 5:
            return self._direction.index(max_val)

        return -1

    def getStartPoint(self):
        """  Get the startPoint of the movement indicator direction.
                :return startPoint : Start location of the arrow
            """
        return self._startPoint

    def getEndPoint(self):
        """  Get the endPoint of the movement indicator direction.
                :returnendPoint : End location of the arrow
            """
        return self._endPoint

    def switchCase(self, x, y, num):
        """  Set the direction of the arrow that indicate the player movement by edit startPoint and endPoint.
                    :param x :  Current location.x of the player
                    :param y:  Current location.y of the player
                    :param num: The current direction
                """
        arrow_size = 1
        if num == directions.LEFT.value:
            self._startPoint = (x + arrow_size, y)
            self._endPoint = (x - arrow_size, y)
        elif num == directions.DIAG_UP_LEFT.value:  # diag_up_left V
            self._startPoint = (x + arrow_size, y + arrow_size)
            self._endPoint = (x - arrow_size, y - arrow_size)
        elif num == directions.DIAG_DOWN_LEFT.value:  # diag_down_left V
            self._startPoint = (x + arrow_size, y - arrow_size)
            self._endPoint = (x - arrow_size, y + arrow_size)
        elif num == directions.RIGHT.value:  # right V
            self._startPoint = (x - arrow_size, y)
            self._endPoint = (x + arrow_size, y)
        elif num == directions.DIAG_UP_RIGHT.value:  # diag_up_right V
            self._startPoint = (x - arrow_size, y + arrow_size)
            self._endPoint = (x + arrow_size, y - arrow_size)
        elif num == directions.DIAG_DOWN_RIGHT.value:  # diag_down_right V
            self._startPoint = (x - arrow_size, y - arrow_size)
            self._endPoint = (x + arrow_size, y + arrow_size)
        elif num == directions.DOWN.value:  # down V
            self._startPoint = (x, y - arrow_size)
            self._endPoint = (x, y + arrow_size)
        else:  # up V
            self._startPoint = (x, y + arrow_size)
            self._endPoint = (x, y - arrow_size)
