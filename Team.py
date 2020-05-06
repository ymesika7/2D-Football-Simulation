from Goalkeeper import Goalkeeper
from FieldPlayer import FieldPlayer


class Team:
    def __init__(self, color, teamSize, playersLocations):
        self._players = []
        self._numberOfPlayers = teamSize
        self._fileSize = playersLocations.__len__()

        # First player will be the Goalkeeper
        self._players.append(Goalkeeper(self.createPlayer(playersLocations, 0), color))
        for i in range(self._numberOfPlayers):
            if i > 0:
                self._players.append(FieldPlayer(self.createPlayer(playersLocations, i), color))

    def createPlayer(self, tempArr, index):
        """ Execute single player locations(by index) from the list playersLocations.
                    :param tempArr: List with all the data of all the players in the team.
                    :param index: Indicate index to the required player
                    :return frame : List with all the locations of the player[index].
                """
        reqArr = []
        for line in range(tempArr.__len__()):
            if line % self._numberOfPlayers == index:
                reqArr.append(tempArr[line])
        return reqArr

    def printObj(self, frame):
        """ Print all the current data of the team to the field sketch.
                    :param frame: (cv2.frame) copy of the field sketch
                    :return frame : the frame after all of the objects was printed
                """
        for i in range(self._numberOfPlayers):
            self._players[i].printObject(frame, self._players[i].getPlayerLocation())
            self._players[i].printObjectDirection(frame, self._players[i].getStartPoint(), self._players[i].getEndPoint())

        return frame

    def isNotEmpty(self):
        """ Check if the ball locations final reach to his end.
                :returns False : If reach to his end
                         True : Otherwise
            """
        if self._players[0].getCounter() >= self._fileSize / self._numberOfPlayers:
            return False
        return True

