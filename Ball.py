from DrawableObjects import DrawableObjects


class Ball(DrawableObjects):
    def __init__(self, color, ballLocations):
        DrawableObjects.__init__(self, color, size=8, arrow_color=(255, 255, 255))
        self._fileSize = ballLocations.__len__()
        self._locations = ballLocations
        self._counter = 0

    def getBallLocation(self):
        """ Check the current location of the ball.
                :returns tuple: (x, y) current location
            """
        self._counter += 1
        return self._locations[self._counter - 1]

    def printObj(self, frame):
        """ Print the current data to the field sketch.
                :param frame : (cv2.frame) copy of the field sketch
                :return frame : the frame after the ball location was printed
            """
        self.printObject(frame, self.getBallLocation())
        return frame


    def isNotEmpty(self):
        """ Check if the ball locations final reach to his end.
                :returns False : If reach to his end
                         True : Otherwise
            """
        if self._counter >= self._fileSize:
            return False
        return True


""" 
   def checkForSpecialEvent():
        if self._players[i].getRole() == "BALL":
            if 0 > getX(coors) or getX(coors) > int(frame.shape[1]):
                if 215 < getY(coors) < 515:
                    cv2.putText(frame, "GOAL!!!",
                                (int(frame.shape[1] / 2 - (SHIFTING.X_SHIFTING / 2)), int(frame.shape[0] / 2)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4, cv2.LINE_AA)
                else:
                    cv2.putText(frame, "OUT!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
"""